const fs = require('fs');
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

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const { buildSolutionVariations } = loadTsExports('services/solutionVariations.ts');
const records = EXERCISES.map(exercise => ({
  id: exercise.id,
  category: exercise.category,
  names: AUTO_GRADERS[exercise.id]?.functionNames ?? [],
  code: buildSolutionVariations(exercise.solution, exercise.id, AUTO_GRADERS[exercise.id]),
}));

const auditor = String.raw`
import ast, collections, json, sys

def sections(code):
    headings = ('# Example ', '# Nested function approach', '# Callable class approach')
    result, current = [], []
    for line in code.splitlines():
        if line.startswith(headings):
            if current:
                result.append('\n'.join(current))
            current = []
        else:
            current.append(line)
    if current:
        result.append('\n'.join(current))
    return result

def call_name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return ''

def technique(code, names, category):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return 'INVALID'
    ignored = {'print', 'main', 'solve', 'run_solution', *names}
    calls = sorted(call_name(node.func) for node in ast.walk(tree)
                   if isinstance(node, ast.Call) and call_name(node.func) not in ignored)
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
        architecture = sorted(type(node).__name__ for node in tree.body if isinstance(node, (
            ast.FunctionDef, ast.ClassDef, ast.Assign, ast.Expr,
        )))
    return repr((calls, structures, sorted(operators), architecture))

distribution = collections.Counter()
under_three = []
for line in sys.stdin:
    record = json.loads(line)
    signatures = {technique(section, set(record['names']), record['category']) for section in sections(record['code'])}
    distribution[len(signatures)] += 1
    if len(signatures) < 3:
        under_three.append(record['id'])
print(json.dumps({'distribution': distribution, 'underThree': under_three}))
`;
const result = spawnSync('python3', ['-c', auditor], {
  input: records.map(record => JSON.stringify(record)).join('\n'),
  encoding: 'utf8',
  maxBuffer: 20 * 1024 * 1024,
});
if (result.error) throw result.error;
if (result.status !== 0) throw new Error(result.stderr || `Python exited ${result.status}`);
const report = JSON.parse(result.stdout);
const maxArg = process.argv.find(argument => argument.startsWith('--max-under3='));
const maxUnderThree = maxArg ? Number(maxArg.split('=')[1]) : null;

console.log('Solution semantic-diversity audit');
console.log(`Exercises: ${records.length}`);
console.log(`Technique-count distribution: ${JSON.stringify(report.distribution)}`);
console.log(`Exercises below three semantic techniques: ${report.underThree.length}`);
if (process.argv.includes('--show')) console.log(report.underThree.join(', '));
if (maxUnderThree !== null && report.underThree.length > maxUnderThree) {
  console.error(`Semantic-diversity regression: ${report.underThree.length} exceeds ${maxUnderThree}.`);
  process.exit(1);
}
