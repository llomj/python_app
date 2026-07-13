const fs = require('fs');
const os = require('os');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const cache = new Map();

function resolveLocalModule(specifier) {
  const candidates = [specifier, `${specifier}.ts`, path.join(specifier, 'index.ts')];
  return candidates.find(candidate => fs.existsSync(path.join(root, candidate))) || null;
}

function loadTsExports(fileName) {
  if (cache.has(fileName)) return cache.get(fileName).exports;
  const compiled = ts.transpileModule(fs.readFileSync(path.join(root, fileName), 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2020 },
    fileName,
  }).outputText;
  const module = { exports: {} };
  cache.set(fileName, module);
  vm.runInNewContext(compiled, {
    module,
    exports: module.exports,
    require: (specifier) => {
      const resolved = resolveLocalModule(path.normalize(path.join(path.dirname(fileName), specifier)));
      return resolved ? loadTsExports(resolved) : {};
    },
  }, { filename: fileName });
  return module.exports;
}

function renderedSections(code) {
  const result = [];
  let current = null;
  let heading = '';
  for (const line of code.split('\n')) {
    if (/^# (?:Example \d+:|Nested function approach|Callable class approach)/.test(line)) {
      if (current?.length) result.push({ heading, body: current.join('\n').trim() });
      heading = line.replace(/^#\s*/, '');
      current = [];
    } else if (current) current.push(line);
  }
  if (current?.length) result.push({ heading, body: current.join('\n').trim() });
  return result.filter(item => item.body && !/^(?:Nested function|Callable class)/.test(item.heading));
}

function sourceSections(code) {
  const headings = /^#\s*(?:[-=]+\s*)?(Using|Approach|Method|Version|Script|Direct|Built|Manual|Alternative|Try|Another|Equivalent|Convert|Modify|Consider|Nested|Advanced|Callable|Example|Reference)\b/i;
  const result = [];
  let current = null;
  let heading = 'Reference approach';
  for (const line of code.split('\n')) {
    if (headings.test(line)) {
      if (current?.length) result.push({ heading, body: current.join('\n').trim() });
      heading = line.replace(/^#\s*(?:[-=]+\s*)?/, '');
      current = [];
    } else if (current) current.push(line);
    else {
      current = [line];
    }
  }
  if (current?.length) result.push({ heading, body: current.join('\n').trim() });
  return result.filter(item => item.body);
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const { buildSolutionVariations } = loadTsExports('services/solutionVariations.ts');
const { SOLUTION_REFERENCE_OVERRIDES } = loadTsExports('services/solutionReferenceOverrides.ts');
const baseRecords = EXERCISES.map(exercise => ({
  id: exercise.id,
  category: exercise.category,
  description: exercise.description,
  names: AUTO_GRADERS[exercise.id]?.functionNames ?? [],
  sections: [
    ...renderedSections(buildSolutionVariations(exercise.solution, exercise.id, AUTO_GRADERS[exercise.id])),
    ...sourceSections(SOLUTION_REFERENCE_OVERRIDES[exercise.id] ?? exercise.solution),
  ],
}));

const transformer = String.raw`
import ast, copy, json, sys

BIN_OPS = {
    ast.Add: 'add', ast.Sub: 'sub', ast.Mult: 'mul', ast.MatMult: 'matmul',
    ast.Div: 'truediv', ast.FloorDiv: 'floordiv', ast.Mod: 'mod', ast.Pow: 'pow',
    ast.LShift: 'lshift', ast.RShift: 'rshift', ast.BitOr: 'or_', ast.BitXor: 'xor',
    ast.BitAnd: 'and_',
}
COMPARE_OPS = {
    ast.Eq: 'eq', ast.NotEq: 'ne', ast.Lt: 'lt', ast.LtE: 'le', ast.Gt: 'gt',
    ast.GtE: 'ge', ast.Is: 'is_', ast.IsNot: 'is_not', ast.In: 'contains',
}

def clone(tree):
    return copy.deepcopy(tree)

def operator_call(name, args):
    return ast.Call(ast.Attribute(ast.Name('operator', ast.Load()), name, ast.Load()), args, [])

class OperatorTransformer(ast.NodeTransformer):
    changed = False
    def visit_BinOp(self, node):
        node = self.generic_visit(node)
        name = BIN_OPS.get(type(node.op))
        if not name:
            return node
        self.changed = True
        return ast.copy_location(operator_call(name, [node.left, node.right]), node)
    def visit_Compare(self, node):
        node = self.generic_visit(node)
        if len(node.ops) != 1:
            return node
        name = COMPARE_OPS.get(type(node.ops[0]))
        if not name:
            return node
        args = [node.comparators[0], node.left] if name == 'contains' else [node.left, node.comparators[0]]
        self.changed = True
        return ast.copy_location(operator_call(name, args), node)

class EnumerateTransformer(ast.NodeTransformer):
    changed = False
    def visit_For(self, node):
        node = self.generic_visit(node)
        self.changed = True
        target = ast.Tuple([ast.Name('_index', ast.Store()), node.target], ast.Store())
        node.target = target
        node.iter = ast.Call(ast.Name('enumerate', ast.Load()), [node.iter], [])
        return node

class IndexLoopTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_For(self, node):
        node = self.generic_visit(node)
        if not isinstance(node.target, ast.Name) or node.orelse:
            return node
        self.counter += 1
        index_name = f'_index_{self.counter}'
        original_iter = node.iter
        assignment = ast.Assign(
            [node.target],
            ast.Subscript(copy.deepcopy(original_iter), ast.Name(index_name, ast.Load()), ast.Load()),
        )
        node.target = ast.Name(index_name, ast.Store())
        node.iter = ast.Call(ast.Name('range', ast.Load()), [ast.Call(ast.Name('len', ast.Load()), [original_iter], [])], [])
        node.body.insert(0, assignment)
        self.changed = True
        return node

class WhileTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_For(self, node):
        node = self.generic_visit(node)
        if node.orelse:
            return node
        self.counter += 1
        iterator = f'_iterator_{self.counter}'
        assign_iterator = ast.Assign([ast.Name(iterator, ast.Store())], ast.Call(ast.Name('iter', ast.Load()), [node.iter], []))
        assign_target = ast.Assign([node.target], ast.Call(ast.Name('next', ast.Load()), [ast.Name(iterator, ast.Load())], []))
        take_next = ast.Try(
            body=[assign_target],
            handlers=[ast.ExceptHandler(ast.Name('StopIteration', ast.Load()), None, [ast.Break()])],
            orelse=[], finalbody=[],
        )
        loop = ast.While(ast.Constant(True), [take_next, *node.body], [])
        self.changed = True
        return [assign_iterator, loop]

class ExpandConditionalTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) == 1 and isinstance(node.body[0], ast.Return) and isinstance(node.body[0].value, ast.IfExp):
            value = node.body[0].value
            node.body = [ast.If(value.test, [ast.Return(value.body)], [ast.Return(value.orelse)])]
            self.changed = True
        return node

class CollapseConditionalTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) == 1 and isinstance(node.body[0], ast.If):
            branch = node.body[0]
            if len(branch.body) == 1 and len(branch.orelse) == 1 and isinstance(branch.body[0], ast.Return) and isinstance(branch.orelse[0], ast.Return):
                node.body = [ast.Return(ast.IfExp(branch.test, branch.body[0].value, branch.orelse[0].value))]
                self.changed = True
        return node

class RegexCompileTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not isinstance(node.func, ast.Attribute) or not isinstance(node.func.value, ast.Name) or node.func.value.id != 're':
            return node
        if node.func.attr not in {'findall', 'search', 'match', 'fullmatch', 'split', 'sub'} or not node.args or node.keywords:
            return node
        pattern, rest = node.args[0], node.args[1:]
        compiled = ast.Call(ast.Attribute(ast.Name('re', ast.Load()), 'compile', ast.Load()), [pattern], [])
        self.changed = True
        return ast.copy_location(ast.Call(ast.Attribute(compiled, node.func.attr, ast.Load()), rest, []), node)

class LiteralPrintTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == 'print' and len(node.args) == 1 and isinstance(node.args[0], ast.Constant):
            value = node.args[0].value
            if isinstance(value, str):
                node.args[0] = ast.JoinedStr([ast.Constant(value)])
            elif isinstance(value, (int, float)) and not isinstance(value, bool):
                node.args[0] = ast.BinOp(ast.Constant(0), ast.Add(), ast.Constant(value))
            else:
                return node
            self.changed = True
        return node

class ConditionalPrintTransformer(ast.NodeTransformer):
    changed = False
    def visit_If(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 1 or len(node.orelse) != 1:
            return node
        left, right = node.body[0], node.orelse[0]
        if not (isinstance(left, ast.Expr) and isinstance(right, ast.Expr)):
            return node
        if not (isinstance(left.value, ast.Call) and isinstance(right.value, ast.Call)):
            return node
        if not (isinstance(left.value.func, ast.Name) and left.value.func.id == 'print' and isinstance(right.value.func, ast.Name) and right.value.func.id == 'print'):
            return node
        if len(left.value.args) != 1 or len(right.value.args) != 1:
            return node
        self.changed = True
        return ast.Expr(ast.Call(ast.Name('print', ast.Load()), [ast.IfExp(node.test, left.value.args[0], right.value.args[0])], []))

class ComprehensionTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        body = node.body
        if len(body) != 3 or not isinstance(body[0], ast.Assign) or not isinstance(body[1], ast.For) or not isinstance(body[2], ast.Return):
            return node
        assignment, loop, returned = body
        if len(assignment.targets) != 1 or not isinstance(assignment.targets[0], ast.Name) or not isinstance(returned.value, ast.Name):
            return node
        result_name = assignment.targets[0].id
        if returned.value.id != result_name:
            return node
        initial = assignment.value
        statements = loop.body
        conditions = []
        while len(statements) == 1 and isinstance(statements[0], ast.If) and not statements[0].orelse:
            conditions.append(statements[0].test)
            statements = statements[0].body
        if len(statements) != 1:
            return node
        statement = statements[0]
        generators = [ast.comprehension(loop.target, loop.iter, conditions, 0)]
        replacement = None
        if isinstance(initial, ast.List) and not initial.elts and isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
            call = statement.value
            if isinstance(call.func, ast.Attribute) and isinstance(call.func.value, ast.Name) and call.func.value.id == result_name and call.func.attr == 'append' and len(call.args) == 1:
                replacement = ast.ListComp(call.args[0], generators)
        elif isinstance(initial, ast.Set) and not initial.elts and isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call):
            call = statement.value
            if isinstance(call.func, ast.Attribute) and isinstance(call.func.value, ast.Name) and call.func.value.id == result_name and call.func.attr == 'add' and len(call.args) == 1:
                replacement = ast.SetComp(call.args[0], generators)
        elif isinstance(initial, ast.Dict) and not initial.keys and isinstance(statement, ast.Assign) and len(statement.targets) == 1 and isinstance(statement.targets[0], ast.Subscript):
            target = statement.targets[0]
            if isinstance(target.value, ast.Name) and target.value.id == result_name:
                replacement = ast.DictComp(target.slice, statement.value, generators)
        elif isinstance(initial, ast.Constant) and initial.value == 0 and isinstance(statement, ast.AugAssign) and isinstance(statement.target, ast.Name) and statement.target.id == result_name and isinstance(statement.op, ast.Add):
            replacement = ast.Call(ast.Name('sum', ast.Load()), [ast.GeneratorExp(statement.value, generators)], [])
        if replacement is None:
            return node
        node.body = [ast.Return(replacement)]
        self.changed = True
        return node

class ManualBuiltinTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 1 or not isinstance(node.body[0], ast.Return) or not isinstance(node.body[0].value, ast.Call):
            return node
        call = node.body[0].value
        name = call.func.id if isinstance(call.func, ast.Name) else ''
        if name not in {'sum', 'len', 'max', 'min'} or len(call.args) != 1 or call.keywords:
            return node
        iterable = call.args[0]
        self.counter += 1
        item = ast.Name(f'_item_{self.counter}', ast.Store())
        item_load = ast.Name(item.id, ast.Load())
        if name == 'sum':
            setup = ast.Assign([ast.Name('result', ast.Store())], ast.Constant(0))
            loop = ast.For(item, iterable, [ast.AugAssign(ast.Name('result', ast.Store()), ast.Add(), item_load)], [])
        elif name == 'len':
            setup = ast.Assign([ast.Name('result', ast.Store())], ast.Constant(0))
            loop = ast.For(item, iterable, [ast.AugAssign(ast.Name('result', ast.Store()), ast.Add(), ast.Constant(1))], [])
        else:
            iterator_name = f'_values_{self.counter}'
            iterator = ast.Assign([ast.Name(iterator_name, ast.Store())], ast.Call(ast.Name('iter', ast.Load()), [iterable], []))
            setup = ast.Assign([ast.Name('result', ast.Store())], ast.Call(ast.Name('next', ast.Load()), [ast.Name(iterator_name, ast.Load())], []))
            comparison = ast.Gt() if name == 'max' else ast.Lt()
            update = ast.If(ast.Compare(item_load, [comparison], [ast.Name('result', ast.Load())]), [ast.Assign([ast.Name('result', ast.Store())], item_load)], [])
            loop = ast.For(item, ast.Name(iterator_name, ast.Load()), [update], [])
            node.body = [iterator, setup, loop, ast.Return(ast.Name('result', ast.Load()))]
            self.changed = True
            return node
        node.body = [setup, loop, ast.Return(ast.Name('result', ast.Load()))]
        self.changed = True
        return node

class FunctionalToComprehensionTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Name) and node.func.id in {'list', 'tuple', 'set'} and len(node.args) == 1 and not node.keywords):
            return node
        inner = node.args[0]
        if not isinstance(inner, ast.Call) or not isinstance(inner.func, ast.Name) or inner.func.id not in {'map', 'filter'} or len(inner.args) != 2:
            return node
        self.counter += 1
        item_store = ast.Name(f'_item_{self.counter}', ast.Store())
        item_load = ast.Name(item_store.id, ast.Load())
        function, iterable = inner.args
        invocation = ast.Call(function, [item_load], [])
        if inner.func.id == 'map':
            comprehension = ast.ListComp(invocation, [ast.comprehension(item_store, iterable, [], 0)])
        else:
            comprehension = ast.ListComp(item_load, [ast.comprehension(item_store, iterable, [invocation], 0)])
        self.changed = True
        if node.func.id == 'list':
            return ast.copy_location(comprehension, node)
        return ast.copy_location(ast.Call(ast.Name(node.func.id, ast.Load()), [comprehension], []), node)

class GeneratorMaterializationTransformer(ast.NodeTransformer):
    changed = False
    def visit_GeneratorExp(self, node):
        node = self.generic_visit(node)
        self.changed = True
        return ast.copy_location(ast.ListComp(node.elt, node.generators), node)

class FStringFormatTransformer(ast.NodeTransformer):
    changed = False
    def visit_JoinedStr(self, node):
        node = self.generic_visit(node)
        template = ''
        arguments = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                template += value.value.replace('{', '{{').replace('}', '}}')
            elif isinstance(value, ast.FormattedValue) and value.conversion == -1 and value.format_spec is None:
                template += '{}'
                arguments.append(value.value)
            elif isinstance(value, ast.FormattedValue) and value.conversion == -1 and isinstance(value.format_spec, ast.JoinedStr) and all(isinstance(part, ast.Constant) for part in value.format_spec.values):
                specification = ''.join(str(part.value) for part in value.format_spec.values)
                template += '{:' + specification + '}'
                arguments.append(value.value)
            else:
                return node
        self.changed = True
        return ast.copy_location(ast.Call(ast.Attribute(ast.Constant(template), 'format', ast.Load()), arguments, []), node)

class DynamicAttributeTransformer(ast.NodeTransformer):
    changed = False
    def visit_Assign(self, node):
        node = self.generic_visit(node)
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Attribute) and isinstance(node.targets[0].value, ast.Name) and node.targets[0].value.id == 'self':
            target = node.targets[0]
            self.changed = True
            return ast.Expr(ast.Call(ast.Name('setattr', ast.Load()), [ast.Name('self', ast.Load()), ast.Constant(target.attr), node.value], []))
        return node

class ReflectiveReadTransformer(ast.NodeTransformer):
    changed = False
    def visit_Attribute(self, node):
        node = self.generic_visit(node)
        if isinstance(node.ctx, ast.Load) and isinstance(node.value, ast.Name) and node.value.id == 'self' and node.attr != '__class__':
            self.changed = True
            return ast.copy_location(ast.Call(ast.Name('getattr', ast.Load()), [ast.Name('self', ast.Load()), ast.Constant(node.attr)], []), node)
        return node

class CountToGeneratorTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Attribute) and node.func.attr == 'count' and len(node.args) == 1 and not node.keywords):
            return node
        self.counter += 1
        item = ast.Name(f'_item_{self.counter}', ast.Store())
        comparison = ast.Compare(ast.Name(item.id, ast.Load()), [ast.Eq()], [node.args[0]])
        generator = ast.GeneratorExp(ast.Constant(1), [ast.comprehension(item, node.func.value, [comparison], 0)])
        self.changed = True
        return ast.copy_location(ast.Call(ast.Name('sum', ast.Load()), [generator], []), node)

class ReverseSliceTransformer(ast.NodeTransformer):
    changed = False
    def visit_Subscript(self, node):
        node = self.generic_visit(node)
        slice_node = node.slice
        if not isinstance(slice_node, ast.Slice) or slice_node.lower is not None or slice_node.upper is not None:
            return node
        if not isinstance(slice_node.step, ast.UnaryOp) or not isinstance(slice_node.step.op, ast.USub) or not isinstance(slice_node.step.operand, ast.Constant) or slice_node.step.operand.value != 1:
            return node
        self.changed = True
        reversed_call = ast.Call(ast.Name('reversed', ast.Load()), [node.value], [])
        return ast.copy_location(ast.Call(ast.Attribute(ast.Constant(''), 'join', ast.Load()), [reversed_call], []), node)

class LibraryArithmeticTransformer(ast.NodeTransformer):
    changed = False
    needs_math = False
    def visit_BinOp(self, node):
        node = self.generic_visit(node)
        replacement = None
        if isinstance(node.op, ast.Mult):
            self.needs_math = True
            replacement = ast.Call(ast.Attribute(ast.Name('math', ast.Load()), 'prod', ast.Load()), [ast.Tuple([node.left, node.right], ast.Load())], [])
        elif isinstance(node.op, ast.Add):
            replacement = ast.Call(ast.Name('sum', ast.Load()), [ast.Tuple([node.left, node.right], ast.Load())], [])
        elif isinstance(node.op, ast.Mod):
            replacement = ast.Subscript(ast.Call(ast.Name('divmod', ast.Load()), [node.left, node.right], []), ast.Constant(1), ast.Load())
        elif isinstance(node.op, ast.Pow):
            replacement = ast.Call(ast.Name('pow', ast.Load()), [node.left, node.right], [])
        if replacement is None:
            return node
        self.changed = True
        return ast.copy_location(replacement, node)

def library_arithmetic(tree):
    instance = LibraryArithmeticTransformer()
    output = instance.visit(clone(tree))
    if not instance.changed:
        return None
    if instance.needs_math:
        output.body.insert(0, ast.Import([ast.alias('math')]))
    return ast.fix_missing_locations(output)

class DictBackedAttributeTransformer(ast.NodeTransformer):
    changed = False
    def dictionary(self):
        return ast.Attribute(ast.Name('self', ast.Load()), '__dict__', ast.Load())
    def visit_Assign(self, node):
        node = self.generic_visit(node)
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Attribute) and isinstance(node.targets[0].value, ast.Name) and node.targets[0].value.id == 'self':
            self.changed = True
            node.targets[0] = ast.Subscript(self.dictionary(), ast.Constant(node.targets[0].attr), ast.Store())
        return node
    def visit_Attribute(self, node):
        node = self.generic_visit(node)
        if isinstance(node.ctx, ast.Load) and isinstance(node.value, ast.Name) and node.value.id == 'self' and node.attr != '__dict__':
            self.changed = True
            return ast.copy_location(ast.Subscript(self.dictionary(), ast.Constant(node.attr), ast.Load()), node)
        return node

class AnagramCounterTransformer(ast.NodeTransformer):
    changed = False
    def visit_Compare(self, node):
        node = self.generic_visit(node)
        if len(node.ops) != 1 or not isinstance(node.ops[0], ast.Eq):
            return node
        left, right = node.left, node.comparators[0]
        def sorted_arg(value):
            return value.args[0] if isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id == 'sorted' and len(value.args) == 1 else None
        left_arg, right_arg = sorted_arg(left), sorted_arg(right)
        if left_arg is None or right_arg is None:
            return node
        self.changed = True
        module = ast.Call(ast.Name('__import__', ast.Load()), [ast.Constant('collections')], [])
        counter = lambda value: ast.Call(ast.Attribute(copy.deepcopy(module), 'Counter', ast.Load()), [value], [])
        return ast.copy_location(ast.Compare(counter(left_arg), [ast.Eq()], [counter(right_arg)]), node)

class SubsetAllTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Attribute) and node.func.attr == 'issubset' and len(node.args) == 1):
            return node
        self.counter += 1
        item = ast.Name(f'_item_{self.counter}', ast.Store())
        membership = ast.Compare(ast.Name(item.id, ast.Load()), [ast.In()], [node.args[0]])
        generator = ast.GeneratorExp(membership, [ast.comprehension(item, node.func.value, [], 0)])
        self.changed = True
        return ast.copy_location(ast.Call(ast.Name('all', ast.Load()), [generator], []), node)

class UnboundMethodTransformer(ast.NodeTransformer):
    changed = False
    METHODS = {
        'isdigit', 'isalpha', 'isalnum', 'isspace', 'islower', 'isupper', 'istitle',
        'lower', 'upper', 'title', 'capitalize', 'casefold', 'strip', 'lstrip', 'rstrip',
        'startswith', 'endswith', 'find', 'index', 'replace', 'split', 'rsplit', 'partition',
    }
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not isinstance(node.func, ast.Attribute) or node.func.attr not in self.METHODS:
            return node
        receiver = node.func.value
        self.changed = True
        function = ast.Attribute(ast.Name('str', ast.Load()), node.func.attr, ast.Load())
        return ast.copy_location(ast.Call(function, [receiver, *node.args], node.keywords), node)

class FindIterTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and node.func.value.id == 're' and node.func.attr == 'findall' and len(node.args) >= 2):
            return node
        pattern = node.args[0]
        if not isinstance(pattern, ast.Constant) or not isinstance(pattern.value, str):
            return node
        try:
            import re as regex
            groups = regex.compile(pattern.value).groups
        except Exception:
            return node
        self.counter += 1
        match = ast.Name(f'_match_{self.counter}', ast.Store())
        match_load = ast.Name(match.id, ast.Load())
        group_index = 1 if groups == 1 else 0
        value = ast.Call(ast.Attribute(match_load, 'group', ast.Load()), [ast.Constant(group_index)], [])
        iterator = ast.Call(ast.Attribute(ast.Name('re', ast.Load()), 'finditer', ast.Load()), node.args, node.keywords)
        self.changed = True
        return ast.copy_location(ast.ListComp(value, [ast.comprehension(match, iterator, [], 0)]), node)

class SortingStyleTransformer(ast.NodeTransformer):
    changed = False
    def visit_Assign(self, node):
        node = self.generic_visit(node)
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name) or not isinstance(node.value, ast.Call):
            return node
        call = node.value
        if not (isinstance(call.func, ast.Name) and call.func.id == 'sorted' and len(call.args) == 1):
            return node
        target = node.targets[0]
        copy_assignment = ast.Assign([copy.deepcopy(target)], ast.Call(ast.Name('list', ast.Load()), [call.args[0]], []))
        sort_call = ast.Expr(ast.Call(ast.Attribute(ast.Name(target.id, ast.Load()), 'sort', ast.Load()), [], call.keywords))
        self.changed = True
        return [copy_assignment, sort_call]

class MappingUpdateTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 2 or not isinstance(node.body[0], ast.Expr) or not isinstance(node.body[0].value, ast.Call) or not isinstance(node.body[1], ast.Return):
            return node
        call = node.body[0].value
        if not (isinstance(call.func, ast.Attribute) and call.func.attr == 'update' and len(call.args) == 1 and isinstance(node.body[1].value, ast.Name)):
            return node
        base = call.func.value
        if not isinstance(base, ast.Name) or node.body[1].value.id != base.id:
            return node
        node.body = [ast.Return(ast.Dict(keys=[None, None], values=[base, call.args[0]]))]
        self.changed = True
        return node

class MaxDefaultTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 2 or not isinstance(node.body[0], ast.If) or not isinstance(node.body[1], ast.Return):
            return node
        condition, final = node.body[0], node.body[1]
        if condition.orelse or len(condition.body) != 1 or not isinstance(condition.body[0], ast.Return):
            return node
        call = final.value
        if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id in {'max', 'min'} and len(call.args) == 1 and not call.keywords):
            return node
        default = condition.body[0].value
        node.body = [ast.Return(ast.Call(call.func, call.args, [ast.keyword('default', default)]))]
        self.changed = True
        return node

class KeyLambdaTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Name) and node.func.id == 'sorted'):
            return node
        for keyword in node.keywords:
            value = keyword.value
            if keyword.arg == 'key' and isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id == 'itemgetter' and len(value.args) == 1:
                keyword.value = ast.Lambda(
                    ast.arguments([], [ast.arg('_item')], None, [], [], None, []),
                    ast.Subscript(ast.Name('_item', ast.Load()), value.args[0], ast.Load()),
                )
                self.changed = True
        return node

class DictGetConditionalTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Attribute) and node.func.attr == 'get' and len(node.args) in {1, 2} and not node.keywords):
            return node
        default = node.args[1] if len(node.args) == 2 else ast.Constant(None)
        self.changed = True
        return ast.copy_location(ast.IfExp(
            ast.Compare(node.args[0], [ast.In()], [node.func.value]),
            ast.Subscript(node.func.value, node.args[0], ast.Load()),
            default,
        ), node)

class DictGetTryTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 1 or not isinstance(node.body[0], ast.Return) or not isinstance(node.body[0].value, ast.Call):
            return node
        call = node.body[0].value
        if not (isinstance(call.func, ast.Attribute) and call.func.attr == 'get' and len(call.args) in {1, 2}):
            return node
        default = call.args[1] if len(call.args) == 2 else ast.Constant(None)
        node.body = [ast.Try(
            [ast.Return(ast.Subscript(call.func.value, call.args[0], ast.Load()))],
            [ast.ExceptHandler(ast.Name('KeyError', ast.Load()), None, [ast.Return(default)])],
            [], [],
        )]
        self.changed = True
        return node

class MinMaxLoopTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 1 or not isinstance(node.body[0], ast.Return) or not isinstance(node.body[0].value, ast.Tuple):
            return node
        values = node.body[0].value.elts
        if len(values) != 2 or not all(isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and len(value.args) == 1 for value in values):
            return node
        if [value.func.id for value in values] != ['min', 'max'] or ast.dump(values[0].args[0]) != ast.dump(values[1].args[0]):
            return node
        iterable = values[0].args[0]
        node.body = [
            ast.Assign([ast.Name('_values', ast.Store())], ast.Call(ast.Name('iter', ast.Load()), [iterable], [])),
            ast.Assign([ast.Name('_minimum', ast.Store())], ast.Call(ast.Name('next', ast.Load()), [ast.Name('_values', ast.Load())], [])),
            ast.Assign([ast.Name('_maximum', ast.Store())], ast.Name('_minimum', ast.Load())),
            ast.For(ast.Name('_item', ast.Store()), ast.Name('_values', ast.Load()), [
                ast.If(ast.Compare(ast.Name('_item', ast.Load()), [ast.Lt()], [ast.Name('_minimum', ast.Load())]), [ast.Assign([ast.Name('_minimum', ast.Store())], ast.Name('_item', ast.Load()))], []),
                ast.If(ast.Compare(ast.Name('_item', ast.Load()), [ast.Gt()], [ast.Name('_maximum', ast.Load())]), [ast.Assign([ast.Name('_maximum', ast.Store())], ast.Name('_item', ast.Load()))], []),
            ], []),
            ast.Return(ast.Tuple([ast.Name('_minimum', ast.Load()), ast.Name('_maximum', ast.Load())], ast.Load())),
        ]
        self.changed = True
        return node

class MatchGuardTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 1 or not isinstance(node.body[0], ast.If):
            return node
        current = node.body[0]
        cases = []
        while isinstance(current, ast.If):
            if len(current.body) != 1 or not isinstance(current.body[0], ast.Return):
                return node
            cases.append(ast.match_case(ast.MatchAs(), current.test, [current.body[0]]))
            if len(current.orelse) == 1 and isinstance(current.orelse[0], ast.If):
                current = current.orelse[0]
            elif len(current.orelse) == 1 and isinstance(current.orelse[0], ast.Return):
                cases.append(ast.match_case(ast.MatchAs(), None, [current.orelse[0]]))
                break
            else:
                return node
        node.body = [ast.Match(ast.Constant(True), cases)]
        self.changed = True
        return node

class ReturnSortedTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 1 or not isinstance(node.body[0], ast.Return) or not isinstance(node.body[0].value, ast.Call):
            return node
        call = node.body[0].value
        if not (isinstance(call.func, ast.Name) and call.func.id == 'sorted' and len(call.args) == 1):
            return node
        self.counter += 1
        result = f'_sorted_{self.counter}'
        node.body = [
            ast.Assign([ast.Name(result, ast.Store())], ast.Call(ast.Name('list', ast.Load()), [call.args[0]], [])),
            ast.Expr(ast.Call(ast.Attribute(ast.Name(result, ast.Load()), 'sort', ast.Load()), [], call.keywords)),
            ast.Return(ast.Name(result, ast.Load())),
        ]
        self.changed = True
        return node

class HeapSortedTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Name) and node.func.id == 'sorted' and len(node.args) == 1):
            return node
        reverse = next((keyword.value for keyword in node.keywords if keyword.arg == 'reverse'), ast.Constant(False))
        if not isinstance(reverse, ast.Constant) or not isinstance(reverse.value, bool):
            return node
        key_keywords = [keyword for keyword in node.keywords if keyword.arg == 'key']
        function = 'nlargest' if reverse.value else 'nsmallest'
        self.changed = True
        return ast.copy_location(ast.Call(
            ast.Attribute(ast.Name('heapq', ast.Load()), function, ast.Load()),
            [ast.Call(ast.Name('len', ast.Load()), [node.args[0]], []), node.args[0]],
            key_keywords,
        ), node)

def heap_sorted(tree):
    instance = HeapSortedTransformer()
    output = instance.visit(clone(tree))
    if not instance.changed:
        return None
    output.body.insert(0, ast.Import([ast.alias('heapq')]))
    return ast.fix_missing_locations(output)

class LenGeneratorTransformer(ast.NodeTransformer):
    changed = False
    counter = 0
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Name) and node.func.id == 'len' and len(node.args) == 1 and not node.keywords):
            return node
        self.counter += 1
        item = ast.Name(f'_unused_{self.counter}', ast.Store())
        generator = ast.GeneratorExp(ast.Constant(1), [ast.comprehension(item, node.args[0], [], 0)])
        self.changed = True
        return ast.copy_location(ast.Call(ast.Name('sum', ast.Load()), [generator], []), node)

class ManualDataclassTransformer(ast.NodeTransformer):
    changed = False
    def visit_ClassDef(self, node):
        node = self.generic_visit(node)
        decorator_names = {decorator.id for decorator in node.decorator_list if isinstance(decorator, ast.Name)}
        if 'dataclass' not in decorator_names:
            return node
        fields = [statement for statement in node.body if isinstance(statement, ast.AnnAssign) and isinstance(statement.target, ast.Name)]
        if not fields:
            return node
        arguments = ast.arguments([], [ast.arg('self'), *[ast.arg(field.target.id, field.annotation) for field in fields]], None, [], [], None, [])
        assignments = [ast.Assign([ast.Attribute(ast.Name('self', ast.Load()), field.target.id, ast.Store())], ast.Name(field.target.id, ast.Load())) for field in fields]
        node.decorator_list = [decorator for decorator in node.decorator_list if not (isinstance(decorator, ast.Name) and decorator.id == 'dataclass')]
        node.body = [ast.FunctionDef('__init__', arguments, assignments or [ast.Pass()], [], None)]
        self.changed = True
        return node

class DataDrivenOverrideTransformer(ast.NodeTransformer):
    changed = False
    def visit_Module(self, node):
        node = self.generic_visit(node)
        classes = {statement.name: statement for statement in node.body if isinstance(statement, ast.ClassDef)}
        for child in classes.values():
            for base in child.bases:
                if not isinstance(base, ast.Name) or base.id not in classes:
                    continue
                parent = classes[base.id]
                parent_methods = {statement.name: statement for statement in parent.body if isinstance(statement, ast.FunctionDef)}
                for method in list(child.body):
                    original = parent_methods.get(method.name)
                    if not original or len(method.body) != 1 or len(original.body) != 1 or not isinstance(method.body[0], ast.Return) or not isinstance(original.body[0], ast.Return):
                        continue
                    if not isinstance(method.body[0].value, ast.Constant) or not isinstance(original.body[0].value, ast.Constant):
                        continue
                    attribute = f'_{method.name}_result'
                    parent_value = copy.deepcopy(original.body[0].value)
                    child_value = copy.deepcopy(method.body[0].value)
                    original.body[0].value = ast.Attribute(ast.Name('self', ast.Load()), attribute, ast.Load())
                    parent.body.insert(0, ast.Assign([ast.Name(attribute, ast.Store())], parent_value))
                    child.body.remove(method)
                    child.body.insert(0, ast.Assign([ast.Name(attribute, ast.Store())], child_value))
                    self.changed = True
        return node

class CollectionUnpackTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if len(node.args) != 1 or node.keywords or not isinstance(node.func, ast.Name):
            return node
        value = node.args[0]
        if node.func.id == 'list':
            replacement = ast.List([ast.Starred(value, ast.Load())], ast.Load())
        elif node.func.id == 'tuple':
            replacement = ast.Tuple([ast.Starred(value, ast.Load())], ast.Load())
        elif node.func.id == 'set':
            replacement = ast.Set([ast.Starred(value, ast.Load())])
        elif node.func.id == 'dict':
            replacement = ast.Dict([None], [value])
        else:
            return node
        self.changed = True
        return ast.copy_location(replacement, node)

class CopyUnpackTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Attribute) and node.func.attr == 'copy' and not node.args and not node.keywords):
            return node
        self.changed = True
        return ast.copy_location(ast.List([ast.Starred(node.func.value, ast.Load())], ast.Load()), node)

class ReduceLoopTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        helpers = {statement.name: statement for statement in node.body if isinstance(statement, ast.FunctionDef)}
        if not node.body or not isinstance(node.body[-1], ast.Return) or not isinstance(node.body[-1].value, ast.Call):
            return node
        call = node.body[-1].value
        if not (isinstance(call.func, ast.Name) and call.func.id == 'reduce' and len(call.args) == 3 and isinstance(call.args[0], ast.Name)):
            return node
        helper = helpers.get(call.args[0].id)
        if not helper or len(helper.args.args) != 2 or len(helper.body) != 1 or not isinstance(helper.body[0], ast.Return):
            return node
        replacements = {helper.args.args[0].arg: ast.Name('_result', ast.Load()), helper.args.args[1].arg: ast.Name('_item', ast.Load())}
        class Substitute(ast.NodeTransformer):
            def visit_Name(self, value):
                return copy.deepcopy(replacements[value.id]) if isinstance(value.ctx, ast.Load) and value.id in replacements else value
        expression = Substitute().visit(copy.deepcopy(helper.body[0].value))
        node.body = [
            ast.Assign([ast.Name('_result', ast.Store())], call.args[2]),
            ast.For(ast.Name('_item', ast.Store()), call.args[1], [ast.Assign([ast.Name('_result', ast.Store())], expression)], []),
            ast.Return(ast.Name('_result', ast.Load())),
        ]
        self.changed = True
        return node

class InsertionSortTransformer(ast.NodeTransformer):
    changed = False
    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if len(node.body) != 1 or not isinstance(node.body[0], ast.Return) or not isinstance(node.body[0].value, ast.Call):
            return node
        call = node.body[0].value
        if not (isinstance(call.func, ast.Name) and call.func.id == 'sorted' and len(call.args) == 1):
            return node
        key = next((keyword.value for keyword in call.keywords if keyword.arg == 'key'), None)
        reverse = next((keyword.value for keyword in call.keywords if keyword.arg == 'reverse'), ast.Constant(False))
        if not isinstance(reverse, ast.Constant) or not isinstance(reverse.value, bool):
            return node
        item_value = ast.Call(copy.deepcopy(key), [ast.Name('_item', ast.Load())], []) if key else ast.Name('_item', ast.Load())
        existing_value = ast.Call(copy.deepcopy(key), [ast.Subscript(ast.Name('_result', ast.Load()), ast.Name('_position', ast.Load()), ast.Load())], []) if key else ast.Subscript(ast.Name('_result', ast.Load()), ast.Name('_position', ast.Load()), ast.Load())
        comparison = ast.GtE() if reverse.value else ast.LtE()
        condition = ast.BoolOp(ast.And(), [
            ast.Compare(ast.Name('_position', ast.Load()), [ast.Lt()], [ast.Call(ast.Name('len', ast.Load()), [ast.Name('_result', ast.Load())], [])]),
            ast.Compare(existing_value, [comparison], [item_value]),
        ])
        node.body = [
            ast.Assign([ast.Name('_result', ast.Store())], ast.List([], ast.Load())),
            ast.For(ast.Name('_item', ast.Store()), call.args[0], [
                ast.Assign([ast.Name('_position', ast.Store())], ast.Constant(0)),
                ast.While(condition, [ast.AugAssign(ast.Name('_position', ast.Store()), ast.Add(), ast.Constant(1))], []),
                ast.Expr(ast.Call(ast.Attribute(ast.Name('_result', ast.Load()), 'insert', ast.Load()), [ast.Name('_position', ast.Load()), ast.Name('_item', ast.Load())], [])),
            ], []),
            ast.Return(ast.Name('_result', ast.Load())),
        ]
        self.changed = True
        return node

class AnySortedTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == 'sorted':
            node.func = ast.Name('_solution_sorted', ast.Load())
            self.changed = True
        return node

def any_sorted(tree):
    instance = AnySortedTransformer()
    output = instance.visit(clone(tree))
    if not instance.changed:
        return None
    helper = ast.parse('''
def _solution_sorted(iterable, *, key=None, reverse=False):
    result = []
    key_function = key or (lambda item: item)
    for item in iterable:
        position = 0
        while position < len(result):
            before = key_function(result[position])
            current = key_function(item)
            if (before < current if reverse else before > current):
                break
            position += 1
        result.insert(position, item)
    return result
''').body[0]
    output.body.insert(0, helper)
    return ast.fix_missing_locations(output)

class AnyReduceTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr if isinstance(node.func, ast.Attribute) else ''
        if name == 'reduce' and len(node.args) == 3 and not node.keywords:
            node.func = ast.Name('_solution_reduce', ast.Load())
            self.changed = True
        return node

def any_reduce(tree):
    instance = AnyReduceTransformer()
    output = instance.visit(clone(tree))
    if not instance.changed:
        return None
    helper = ast.parse('''
def _solution_reduce(function, iterable, initial):
    result = initial
    for item in iterable:
        result = function(result, item)
    return result
''').body[0]
    output.body.insert(0, helper)
    return ast.fix_missing_locations(output)

class DynamicTypeTransformer(ast.NodeTransformer):
    changed = False
    def visit_ClassDef(self, node):
        node = self.generic_visit(node)
        if node.decorator_list:
            return node
        if node.bases and isinstance(node.bases[0], ast.Name):
            base_name = node.bases[0].id
            class ExplicitSuper(ast.NodeTransformer):
                def visit_Call(self, call):
                    call = self.generic_visit(call)
                    if isinstance(call.func, ast.Attribute) and isinstance(call.func.value, ast.Call) and isinstance(call.func.value.func, ast.Name) and call.func.value.func.id == 'super' and not call.func.value.args:
                        call.func = ast.Attribute(ast.Name(base_name, ast.Load()), call.func.attr, ast.Load())
                        call.args.insert(0, ast.Name('self', ast.Load()))
                    return call
            node = ExplicitSuper().visit(node)
        namespace_keys = []
        namespace_values = []
        helper_definitions = []
        for statement in node.body:
            if isinstance(statement, ast.FunctionDef):
                helper = copy.deepcopy(statement)
                helper.name = f'_{node.name}_{statement.name}'
                helper_definitions.append(helper)
                namespace_keys.append(ast.Constant(statement.name))
                namespace_values.append(ast.Name(helper.name, ast.Load()))
            elif isinstance(statement, ast.Assign) and len(statement.targets) == 1 and isinstance(statement.targets[0], ast.Name):
                namespace_keys.append(ast.Constant(statement.targets[0].id))
                namespace_values.append(statement.value)
            elif isinstance(statement, ast.Pass):
                continue
            else:
                return node
        if not namespace_keys:
            return node
        bases = ast.Tuple(node.bases or [ast.Name('object', ast.Load())], ast.Load())
        assignment = ast.Assign(
            [ast.Name(node.name, ast.Store())],
            ast.Call(ast.Name('type', ast.Load()), [ast.Constant(node.name), bases, ast.Dict(namespace_keys, namespace_values)], []),
        )
        self.changed = True
        return [*helper_definitions, assignment]

class ComprehensionToFunctionalTransformer(ast.NodeTransformer):
    changed = False
    def lambda_for(self, target, expression):
        if not isinstance(target, ast.Name):
            return None
        return ast.Lambda(ast.arguments([], [ast.arg(target.id)], None, [], [], None, []), expression)
    def functional(self, element, generators, constructor):
        if len(generators) != 1 or generators[0].is_async:
            return None
        generator = generators[0]
        mapper = self.lambda_for(generator.target, element)
        if mapper is None:
            return None
        iterable = generator.iter
        if generator.ifs:
            condition = generator.ifs[0] if len(generator.ifs) == 1 else ast.BoolOp(ast.And(), generator.ifs)
            predicate = self.lambda_for(generator.target, condition)
            iterable = ast.Call(ast.Name('filter', ast.Load()), [predicate, iterable], [])
        mapped = ast.Call(ast.Name('map', ast.Load()), [mapper, iterable], [])
        self.changed = True
        return ast.Call(ast.Name(constructor, ast.Load()), [mapped], []) if constructor else mapped
    def visit_ListComp(self, node):
        node = self.generic_visit(node)
        return ast.copy_location(self.functional(node.elt, node.generators, 'list') or node, node)
    def visit_SetComp(self, node):
        node = self.generic_visit(node)
        return ast.copy_location(self.functional(node.elt, node.generators, 'set') or node, node)
    def visit_GeneratorExp(self, node):
        node = self.generic_visit(node)
        return ast.copy_location(self.functional(node.elt, node.generators, None) or node, node)
    def visit_DictComp(self, node):
        node = self.generic_visit(node)
        pair = ast.Tuple([node.key, node.value], ast.Load())
        return ast.copy_location(self.functional(pair, node.generators, 'dict') or node, node)

class AggregateAlternativeTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not isinstance(node.func, ast.Name) or len(node.args) != 1 or node.keywords:
            return node
        if node.func.id in {'max', 'min'}:
            index = ast.UnaryOp(ast.USub(), ast.Constant(1)) if node.func.id == 'max' else ast.Constant(0)
            self.changed = True
            return ast.copy_location(ast.Subscript(ast.Call(ast.Name('sorted', ast.Load()), node.args, []), index, ast.Load()), node)
        if node.func.id == 'sum':
            module = ast.Call(ast.Name('__import__', ast.Load()), [ast.Constant('functools')], [])
            operator_module = ast.Call(ast.Name('__import__', ast.Load()), [ast.Constant('operator')], [])
            self.changed = True
            return ast.copy_location(ast.Call(
                ast.Attribute(module, 'reduce', ast.Load()),
                [ast.Attribute(operator_module, 'add', ast.Load()), node.args[0], ast.Constant(0)],
                [],
            ), node)
        return node

class CopySliceTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if isinstance(node.func, ast.Attribute) and node.func.attr == 'copy' and not node.args and not node.keywords:
            self.changed = True
            return ast.copy_location(ast.Subscript(node.func.value, ast.Slice(None, None, None), ast.Load()), node)
        return node

class SubstringSplitCountTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Attribute) and node.func.attr == 'count' and len(node.args) == 1 and not node.keywords):
            return node
        pieces = ast.Call(ast.Attribute(node.func.value, 'split', ast.Load()), node.args, [])
        self.changed = True
        return ast.copy_location(ast.BinOp(ast.Call(ast.Name('len', ast.Load()), [pieces], []), ast.Sub(), ast.Constant(1)), node)

class LibraryBuiltinTransformer(ast.NodeTransformer):
    changed = False
    needs_heapq = False
    needs_math = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id in {'max', 'min'} and len(node.args) == 1 and not node.keywords:
            self.needs_heapq = True
            function = 'nlargest' if node.func.id == 'max' else 'nsmallest'
            values = ast.Call(ast.Attribute(ast.Name('heapq', ast.Load()), function, ast.Load()), [ast.Constant(1), node.args[0]], [])
            self.changed = True
            return ast.copy_location(ast.Subscript(values, ast.Constant(0), ast.Load()), node)
        if isinstance(node.func, ast.Name) and node.func.id == 'sum' and len(node.args) == 1 and not node.keywords:
            self.needs_math = True
            self.changed = True
            return ast.copy_location(ast.Call(ast.Attribute(ast.Name('math', ast.Load()), 'fsum', ast.Load()), node.args, []), node)
        if isinstance(node.func, ast.Name) and node.func.id == 'isinstance' and len(node.args) == 2 and not node.keywords:
            self.changed = True
            return ast.copy_location(ast.Call(ast.Name('issubclass', ast.Load()), [ast.Call(ast.Name('type', ast.Load()), [node.args[0]], []), node.args[1]], []), node)
        return node

def library_builtins(tree):
    instance = LibraryBuiltinTransformer()
    output = instance.visit(clone(tree))
    if not instance.changed:
        return None
    imports = []
    if instance.needs_heapq: imports.append(ast.alias('heapq'))
    if instance.needs_math: imports.append(ast.alias('math'))
    if imports: output.body.insert(0, ast.Import(imports))
    return ast.fix_missing_locations(output)

class SetDefaultConditionalTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.func, ast.Attribute) and node.func.attr == 'setdefault' and len(node.args) in {1, 2} and not node.keywords):
            return node
        mapping, key = node.func.value, node.args[0]
        default = node.args[1] if len(node.args) == 2 else ast.Constant(None)
        assign = ast.Call(ast.Attribute(mapping, '__setitem__', ast.Load()), [key, default], [])
        self.changed = True
        return ast.copy_location(ast.IfExp(
            ast.Compare(key, [ast.In()], [mapping]),
            ast.Subscript(mapping, key, ast.Load()),
            ast.BoolOp(ast.Or(), [assign, default]),
        ), node)

class AppendConcatenationTransformer(ast.NodeTransformer):
    changed = False
    def visit_Expr(self, node):
        node = self.generic_visit(node)
        call = node.value
        if isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute) and call.func.attr == 'append' and len(call.args) == 1 and not call.keywords:
            self.changed = True
            return ast.AugAssign(call.func.value, ast.Add(), ast.List([call.args[0]], ast.Load()))
        return node

class ItemsKeyIterationTransformer(ast.NodeTransformer):
    changed = False
    def visit_For(self, node):
        node = self.generic_visit(node)
        if not (isinstance(node.target, ast.Tuple) and len(node.target.elts) == 2 and isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Attribute) and node.iter.func.attr == 'items' and not node.iter.args):
            return node
        key, value = node.target.elts
        if not isinstance(key, ast.Name) or not isinstance(value, ast.Name):
            return node
        mapping = node.iter.func.value
        node.target = key
        node.iter = mapping
        node.body.insert(0, ast.Assign([value], ast.Subscript(copy.deepcopy(mapping), ast.Name(key.id, ast.Load()), ast.Load())))
        self.changed = True
        return node

class OpenToPathTransformer(ast.NodeTransformer):
    changed = False
    def visit_Call(self, node):
        node = self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == 'open' and node.args:
            path_object = ast.Call(ast.Attribute(ast.Name('pathlib', ast.Load()), 'Path', ast.Load()), [node.args[0]], [])
            self.changed = True
            return ast.copy_location(ast.Call(ast.Attribute(path_object, 'open', ast.Load()), node.args[1:], node.keywords), node)
        return node

def path_open(tree):
    instance = OpenToPathTransformer()
    output = instance.visit(clone(tree))
    if not instance.changed:
        return None
    output.body.insert(0, ast.Import([ast.alias('pathlib')]))
    return ast.fix_missing_locations(output)

class NewClassTransformer(ast.NodeTransformer):
    changed = False
    def visit_ClassDef(self, node):
        node = self.generic_visit(node)
        if node.decorator_list:
            return node
        if node.bases and isinstance(node.bases[0], ast.Name):
            base_name = node.bases[0].id
            class ExplicitSuper(ast.NodeTransformer):
                def visit_Call(self, call):
                    call = self.generic_visit(call)
                    if isinstance(call.func, ast.Attribute) and isinstance(call.func.value, ast.Call) and isinstance(call.func.value.func, ast.Name) and call.func.value.func.id == 'super' and not call.func.value.args:
                        call.func = ast.Attribute(ast.Name(base_name, ast.Load()), call.func.attr, ast.Load())
                        call.args.insert(0, ast.Name('self', ast.Load()))
                    return call
            node = ExplicitSuper().visit(node)
        keys, values, helpers = [], [], []
        for statement in node.body:
            if isinstance(statement, ast.FunctionDef):
                helper = copy.deepcopy(statement)
                helper.name = f'_{node.name}_{statement.name}'
                helpers.append(helper)
                keys.append(ast.Constant(statement.name))
                values.append(ast.Name(helper.name, ast.Load()))
            elif isinstance(statement, ast.Assign) and len(statement.targets) == 1 and isinstance(statement.targets[0], ast.Name):
                keys.append(ast.Constant(statement.targets[0].id))
                values.append(statement.value)
            elif isinstance(statement, ast.Pass):
                continue
            else:
                return node
        if not keys:
            return node
        bases = ast.Tuple(node.bases or [ast.Name('object', ast.Load())], ast.Load())
        namespace = ast.Dict(keys, values)
        callback = ast.Lambda(
            ast.arguments([], [ast.arg('namespace')], None, [], [], None, []),
            ast.Call(ast.Attribute(ast.Name('namespace', ast.Load()), 'update', ast.Load()), [namespace], []),
        )
        assignment = ast.Assign(
            [ast.Name(node.name, ast.Store())],
            ast.Call(ast.Attribute(ast.Name('types', ast.Load()), 'new_class', ast.Load()), [ast.Constant(node.name), bases, ast.Dict([], []), callback], []),
        )
        self.changed = True
        return [*helpers, assignment]

def new_class(tree):
    instance = NewClassTransformer()
    output = instance.visit(clone(tree))
    if not instance.changed:
        return None
    output.body.insert(0, ast.Import([ast.alias('types')]))
    return ast.fix_missing_locations(output)

def lambda_variant(tree):
    changed = False
    output = clone(tree)
    new_body = []
    for statement in output.body:
        if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)):
            arguments = statement.args
            if arguments.posonlyargs or arguments.kwonlyargs or arguments.vararg or arguments.kwarg or statement.decorator_list:
                new_body.append(statement)
                continue
            expression = None
            if len(statement.body) == 1 and isinstance(statement.body[0], ast.Return):
                expression = statement.body[0].value
            elif statement.body and isinstance(statement.body[-1], ast.Return):
                replacements = {}
                valid = True
                for setup in statement.body[:-1]:
                    if not isinstance(setup, ast.Assign) or len(setup.targets) != 1 or not isinstance(setup.targets[0], ast.Name):
                        valid = False
                        break
                    class Substitute(ast.NodeTransformer):
                        def visit_Name(self, node):
                            if isinstance(node.ctx, ast.Load) and node.id in replacements:
                                return copy.deepcopy(replacements[node.id])
                            return node
                    replacements[setup.targets[0].id] = Substitute().visit(copy.deepcopy(setup.value))
                if valid:
                    class FinalSubstitute(ast.NodeTransformer):
                        def visit_Name(self, node):
                            if isinstance(node.ctx, ast.Load) and node.id in replacements:
                                return copy.deepcopy(replacements[node.id])
                            return node
                    expression = FinalSubstitute().visit(copy.deepcopy(statement.body[-1].value))
            if expression is None:
                new_body.append(statement)
                continue
            target = ast.Name(statement.name, ast.Store())
            new_body.append(ast.Assign([target], ast.Lambda(arguments, expression)))
            changed = True
        else:
            new_body.append(statement)
    output.body = new_body
    return output if changed else None

def apply(tree, transformer, import_operator=False):
    instance = transformer()
    output = instance.visit(clone(tree))
    if not instance.changed:
        return None
    if import_operator:
        output.body.insert(0, ast.Import([ast.alias('operator')]))
    return ast.fix_missing_locations(output)

def technique(code, names, category):
    try:
        tree = ast.parse(code)
        compile(tree, '<candidate>', 'exec')
    except SyntaxError:
        return 'INVALID'
    def call_name(node):
        if isinstance(node, ast.Name): return node.id
        if isinstance(node, ast.Attribute):
            owner = call_name(node.value)
            return f'{owner}.{node.attr}' if owner else node.attr
        return ''
    ignored = {'print', 'main', 'solve', 'run_solution', *names}
    calls = sorted(call_name(node.func) for node in ast.walk(tree) if isinstance(node, ast.Call) and call_name(node.func) not in ignored)
    structures = sorted(type(node).__name__ for node in ast.walk(tree) if isinstance(node, (
        ast.For, ast.While, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp,
        ast.Lambda, ast.If, ast.IfExp, ast.Try, ast.With, ast.Match, ast.Yield,
        ast.YieldFrom, ast.Await, ast.Subscript, ast.JoinedStr,
    )))
    operators = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.BinOp, ast.BoolOp, ast.UnaryOp, ast.AugAssign)):
            operators.append(type(node.op).__name__)
        elif isinstance(node, ast.Compare):
            operators.extend(type(operator).__name__ for operator in node.ops)
    architecture = []
    if category == 'Atomic Beginner':
        architecture = sorted(type(node).__name__ for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr)))
    class_details = []
    for class_node in (node for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and not node.name.startswith('Exercise')):
        decorators = tuple(call_name(item) for item in class_node.decorator_list)
        bases = tuple(call_name(item) for item in class_node.bases)
        methods = tuple(statement.name for statement in class_node.body if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)))
        class_assignments = sum(isinstance(statement, (ast.Assign, ast.AnnAssign)) for statement in class_node.body)
        class_details.append((class_node.name, decorators, bases, methods, class_assignments))
    return repr((calls, structures, sorted(operators), architecture, sorted(class_details)))

TRANSFORMS = [
    ('operator module approach', lambda tree: apply(tree, OperatorTransformer, True)),
    ('enumerate loop approach', lambda tree: apply(tree, EnumerateTransformer)),
    ('index-based loop approach', lambda tree: apply(tree, IndexLoopTransformer)),
    ('iterator and while-loop approach', lambda tree: apply(tree, WhileTransformer)),
    ('expanded conditional approach', lambda tree: apply(tree, ExpandConditionalTransformer)),
    ('conditional-expression approach', lambda tree: apply(tree, CollapseConditionalTransformer)),
    ('compiled regular-expression approach', lambda tree: apply(tree, RegexCompileTransformer)),
    ('comprehension or generator approach', lambda tree: apply(tree, ComprehensionTransformer)),
    ('manual iteration approach', lambda tree: apply(tree, ManualBuiltinTransformer)),
    ('conditional expression approach', lambda tree: apply(tree, ConditionalPrintTransformer)),
    ('comprehension instead of map or filter', lambda tree: apply(tree, FunctionalToComprehensionTransformer)),
    ('eager comprehension approach', lambda tree: apply(tree, GeneratorMaterializationTransformer)),
    ('str.format approach', lambda tree: apply(tree, FStringFormatTransformer)),
    ('dynamic setattr approach', lambda tree: apply(tree, DynamicAttributeTransformer)),
    ('reflective getattr approach', lambda tree: apply(tree, ReflectiveReadTransformer)),
    ('generator counting approach', lambda tree: apply(tree, CountToGeneratorTransformer)),
    ('reversed and join approach', lambda tree: apply(tree, ReverseSliceTransformer)),
    ('standard-library arithmetic approach', lambda tree: library_arithmetic(tree)),
    ('dictionary-backed attribute approach', lambda tree: apply(tree, DictBackedAttributeTransformer)),
    ('Counter frequency approach', lambda tree: apply(tree, AnagramCounterTransformer, False)),
    ('all and generator subset approach', lambda tree: apply(tree, SubsetAllTransformer)),
    ('unbound string-method approach', lambda tree: apply(tree, UnboundMethodTransformer)),
    ('finditer comprehension approach', lambda tree: apply(tree, FindIterTransformer)),
    ('copied list and in-place sort approach', lambda tree: apply(tree, SortingStyleTransformer)),
    ('dictionary unpacking update approach', lambda tree: apply(tree, MappingUpdateTransformer)),
    ('built-in default argument approach', lambda tree: apply(tree, MaxDefaultTransformer)),
    ('lambda key-function approach', lambda tree: apply(tree, KeyLambdaTransformer)),
    ('conditional dictionary lookup approach', lambda tree: apply(tree, DictGetConditionalTransformer)),
    ('try-except dictionary lookup approach', lambda tree: apply(tree, DictGetTryTransformer)),
    ('single-pass min-max approach', lambda tree: apply(tree, MinMaxLoopTransformer)),
    ('match-case guard approach', lambda tree: apply(tree, MatchGuardTransformer)),
    ('copied list with in-place sorting', lambda tree: apply(tree, ReturnSortedTransformer)),
    ('heap-based sorting approach', lambda tree: heap_sorted(tree)),
    ('generator-based length approach', lambda tree: apply(tree, LenGeneratorTransformer)),
    ('manual class instead of dataclass', lambda tree: apply(tree, ManualDataclassTransformer)),
    ('data-driven method override approach', lambda tree: apply(tree, DataDrivenOverrideTransformer)),
    ('collection unpacking approach', lambda tree: apply(tree, CollectionUnpackTransformer)),
    ('unpacking copy approach', lambda tree: apply(tree, CopyUnpackTransformer)),
    ('explicit reduction loop approach', lambda tree: apply(tree, ReduceLoopTransformer)),
    ('stable insertion-sort approach', lambda tree: apply(tree, InsertionSortTransformer)),
    ('standalone insertion-sort helper', lambda tree: any_sorted(tree)),
    ('standalone reduction helper', lambda tree: any_reduce(tree)),
    ('dynamic class construction approach', lambda tree: apply(tree, DynamicTypeTransformer)),
    ('types.new_class construction approach', lambda tree: new_class(tree)),
    ('map and filter functional approach', lambda tree: apply(tree, ComprehensionToFunctionalTransformer)),
    ('sorting or reduction aggregate approach', lambda tree: apply(tree, AggregateAlternativeTransformer)),
    ('slice-copy approach', lambda tree: apply(tree, CopySliceTransformer)),
    ('split-based substring counting approach', lambda tree: apply(tree, SubstringSplitCountTransformer)),
    ('standard-library built-in alternative', lambda tree: library_builtins(tree)),
    ('conditional setdefault approach', lambda tree: apply(tree, SetDefaultConditionalTransformer)),
    ('list concatenation instead of append', lambda tree: apply(tree, AppendConcatenationTransformer)),
    ('dictionary key iteration approach', lambda tree: apply(tree, ItemsKeyIterationTransformer)),
    ('pathlib file-open approach', lambda tree: path_open(tree)),
    ('formatted literal approach', lambda tree: apply(tree, LiteralPrintTransformer)),
    ('lambda expression approach', lambda tree: lambda_variant(tree)),
]

for line in sys.stdin:
    record = json.loads(line)
    emitted = set()
    for section in record['sections']:
        code = section['body']
        signature = technique(code, record['names'], record['category'])
        key = (code, signature)
        if signature != 'INVALID' and key not in emitted:
            emitted.add(key)
            print(json.dumps({'id': record['id'], 'heading': section['heading'], 'solution': code, 'technique': signature}))
        try:
            tree = ast.parse(code)
        except SyntaxError:
            continue
        for heading, transform in TRANSFORMS:
            if heading == 'formatted literal approach' and record['category'] != 'Atomic Beginner':
                continue
            try:
                changed = transform(tree)
                if changed is None:
                    continue
                changed = ast.fix_missing_locations(changed)
                candidate = ast.unparse(changed)
                signature = technique(candidate, record['names'], record['category'])
                key = (candidate, signature)
                if signature != 'INVALID' and key not in emitted:
                    emitted.add(key)
                    print(json.dumps({'id': record['id'], 'heading': heading, 'solution': candidate, 'technique': signature}))
            except Exception:
                pass
`;

const transformed = spawnSync('python3', ['-c', transformer], {
  input: baseRecords.map(record => JSON.stringify(record)).join('\n'),
  cwd: root,
  encoding: 'utf8',
  maxBuffer: 100 * 1024 * 1024,
  timeout: 300000,
});
if (transformed.error) throw transformed.error;
if (transformed.status !== 0) throw new Error(transformed.stderr);
const candidates = transformed.stdout.trim().split('\n').filter(Boolean).map((line, candidateId) => ({
  ...JSON.parse(line),
  candidateId: String(candidateId),
  behaviorOnly: true,
}));

const temporaryDirectory = fs.mkdtempSync(path.join(os.tmpdir(), 'semantic-solutions-'));
const candidateFile = path.join(temporaryDirectory, 'candidates.json');
const resultsFile = path.join(temporaryDirectory, 'results.json');
fs.writeFileSync(candidateFile, JSON.stringify(candidates));
const validation = spawnSync(process.execPath, [
  path.join(root, 'scripts/validate_graders.js'),
  `--candidate-file=${candidateFile}`,
  `--results-file=${resultsFile}`,
  `--max-failures=${candidates.length}`,
], { cwd: root, encoding: 'utf8', maxBuffer: 100 * 1024 * 1024, timeout: 900000 });
if (validation.error) throw validation.error;
if (validation.status !== 0) throw new Error(validation.stderr || validation.stdout);
const results = JSON.parse(fs.readFileSync(resultsFile, 'utf8'));
const passedIds = new Set(results.filter(result => result.passed).map(result => result.candidateId));
const selected = {};
for (const candidate of candidates) {
  if (!passedIds.has(candidate.candidateId)) continue;
  const group = (selected[candidate.id] ??= []);
  if (group.some(item => item.technique === candidate.technique)) continue;
  group.push({ heading: candidate.heading, body: candidate.solution, technique: candidate.technique });
}
for (const [id, group] of Object.entries(selected)) {
  if (group.length < 3) delete selected[id];
  else selected[id] = group.slice(0, 4).map(({ heading, body }) => ({ heading, body }));
}
const output = [
  '// Generated by scripts/generate_semantic_solution_alternatives.js.',
  '// Every entry contains behavior-tested candidates with distinct AST technique signatures.',
  `export const GENERATED_SOLUTION_ALTERNATIVES: Readonly<Record<number, readonly { heading: string; body: string }[]>> = ${JSON.stringify(selected, null, 2)};`,
  '',
].join('\n');
fs.writeFileSync(path.join(root, 'services/generatedSolutionAlternatives.ts'), output);
fs.rmSync(temporaryDirectory, { recursive: true, force: true });
console.log(`Generated ${candidates.length} candidates; ${Object.keys(selected).length}/${EXERCISES.length} exercises have at least three passing techniques.`);
