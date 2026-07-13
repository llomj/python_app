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
        owner = call_name(node.value)
        return f'{owner}.{node.attr}' if owner else node.attr
    return ''

def technique(code, names, category):
    try:
        tree = ast.parse(code)
        compile(tree, '<solution>', 'exec')
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
    class_details = []
    for class_node in (node for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and not node.name.startswith('Exercise')):
        decorators = tuple(call_name(item) for item in class_node.decorator_list)
        bases = tuple(call_name(item) for item in class_node.bases)
        methods = tuple(statement.name for statement in class_node.body if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)))
        class_assignments = sum(isinstance(statement, (ast.Assign, ast.AnnAssign)) for statement in class_node.body)
        class_details.append((class_node.name, decorators, bases, methods, class_assignments))
    return repr((calls, structures, sorted(operators), architecture, sorted(class_details)))

distribution = collections.Counter()
under_three = []
technique_counts = {}
gap_features = collections.Counter()
gap_features_by_id = {}
for line in sys.stdin:
    record = json.loads(line)
    signatures = {technique(section, set(record['names']), record['category']) for section in sections(record['code'])}
    distribution[len(signatures)] += 1
    technique_counts[record['id']] = len(signatures)
    if len(signatures) < 3:
        under_three.append(record['id'])
        record_features = set()
        try:
            first_tree = ast.parse(sections(record['code'])[0])
            for node in ast.walk(first_tree):
                if isinstance(node, ast.Call):
                    name = call_name(node.func)
                    if name and name not in {'print', *record['names']}:
                        gap_features[f'call:{name}'] += 1
                        record_features.add(f'call:{name}')
                elif isinstance(node, (ast.ClassDef, ast.For, ast.While, ast.If, ast.Try, ast.With, ast.Match, ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)):
                    gap_features[f'node:{type(node).__name__}'] += 1
                    record_features.add(f'node:{type(node).__name__}')
        except Exception:
            gap_features['INVALID'] += 1
            record_features.add('INVALID')
        gap_features_by_id[record['id']] = sorted(record_features)
print(json.dumps({'distribution': distribution, 'underThree': under_three, 'techniqueCounts': technique_counts, 'gapFeatures': gap_features.most_common(30), 'gapFeaturesById': gap_features_by_id}))
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
const inspectArg = process.argv.find(argument => argument.startsWith('--inspect='));
if (inspectArg) {
  const inspectIds = inspectArg.split('=')[1].split(',').map(Number);
  for (const inspectId of inspectIds) {
    const record = records.find(item => item.id === inspectId);
    if (!record) throw new Error(`Unknown exercise ${inspectId}`);
    console.log(`\nRendered solution for ${inspectId}:\n${record.code}\n`);
  }
}

console.log('Solution semantic-diversity audit');
console.log(`Exercises: ${records.length}`);
console.log(`Technique-count distribution: ${JSON.stringify(report.distribution)}`);
console.log(`Exercises below three semantic techniques: ${report.underThree.length}`);
const categoryGaps = records.reduce((counts, record) => {
  if ((report.techniqueCounts[record.id] ?? 0) < 3) counts[record.category] = (counts[record.category] ?? 0) + 1;
  return counts;
}, {});
console.log(`Coverage gaps by category: ${JSON.stringify(categoryGaps)}`);
console.log(`Top gap features: ${JSON.stringify(report.gapFeatures)}`);
if (process.argv.includes('--show')) console.log(report.underThree.join(', '));
if (process.argv.includes('--show-details')) {
  for (const id of report.underThree) {
    console.log(`${id}\t${report.techniqueCounts[id]}\t${(report.gapFeaturesById[id] ?? []).join(',')}`);
  }
}
if (maxUnderThree !== null && report.underThree.length > maxUnderThree) {
  console.error(`Semantic-diversity regression: ${report.underThree.length} exceeds ${maxUnderThree}.`);
  process.exit(1);
}
