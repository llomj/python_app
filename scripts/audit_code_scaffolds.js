const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const moduleCache = new Map();

function loadTs(fileName) {
  const normalized = fileName.replace(/^\.\.\//, '').replace(/^\.\//, '');
  if (moduleCache.has(normalized)) return moduleCache.get(normalized);
  if (normalized === 'types' || normalized === 'types.ts') return {};

  const absolute = path.join(root, normalized.endsWith('.ts') ? normalized : `${normalized}.ts`);
  const source = fs.readFileSync(absolute, 'utf8');
  const compiled = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2020 },
    fileName: absolute,
  }).outputText;
  const module = { exports: {} };
  moduleCache.set(normalized, module.exports);
  const directory = path.dirname(normalized);
  const sandbox = {
    exports: module.exports,
    module,
    console,
    require: request => {
      if (!request.startsWith('.')) return require(request);
      const resolved = path.normalize(path.join(directory, request)).replace(/\\/g, '/');
      return loadTs(resolved);
    },
  };
  sandbox.exports = module.exports;
  vm.runInNewContext(compiled, sandbox, { filename: absolute });
  moduleCache.set(normalized, module.exports);
  return module.exports;
}

const { EXERCISES } = loadTs('exercises');
const { AUTO_GRADERS } = loadTs('graders');
const { buildExerciseCodeScaffold } = loadTs('services/codeScaffold');
const failures = [];
const generated = [];
let functionScaffolds = 0;
let scriptStarters = 0;
let generatedScriptScaffolds = 0;

const genericCommentPattern = /^#\s*(?:(?:write|enter|add|type|put)\b.*|(?:your|the)\s+(?:code|solution)\s+here\.?|todo\b.*)$/i;
const isGenericStarter = code => {
  const lines = code.trim().split('\n').map(line => line.trim()).filter(Boolean);
  return lines.length === 0 || lines.every(line => (
    /^(?:from\s+[A-Za-z_.]+\s+import\s+.+|import\s+[A-Za-z_., ]+)$/.test(line)
    || line === 'pass'
    || genericCommentPattern.test(line)
  ));
};

for (const exercise of EXERCISES) {
  const grader = AUTO_GRADERS[exercise.id];
  const scaffold = buildExerciseCodeScaffold(exercise, grader);
  generated.push({ id: exercise.id, code: scaffold });

  if (!grader || grader.mode === 'script' || !grader.tests?.length) {
    scriptStarters += 1;
    const hadGenericStarter = isGenericStarter(exercise.initialCode.trimEnd());
    if (hadGenericStarter && scaffold !== exercise.initialCode.trimEnd()) generatedScriptScaffolds += 1;
    if (isGenericStarter(scaffold)) failures.push(`Problem ${exercise.id}: script scaffold is still empty or generic`);
    if (hadGenericStarter && !/\b(?:def|class|result\s*=|print\s*\()/.test(scaffold)) failures.push(`Problem ${exercise.id}: generated script scaffold has no usable structure`);
    if (hadGenericStarter && !/# TODO:/.test(scaffold)) failures.push(`Problem ${exercise.id}: generated script scaffold does not identify the missing logic`);
    if (/Expected\s*:/i.test(scaffold)) failures.push(`Problem ${exercise.id}: script scaffold leaked an expected result`);
    continue;
  }

  functionScaffolds += 1;
  if (!/\b(?:print\s*\(|example\s*=)/.test(scaffold)) failures.push(`Problem ${exercise.id}: scaffold has no representative execution`);
  if (/Expected\s*:/i.test(scaffold.slice(exercise.initialCode.trimEnd().length))) failures.push(`Problem ${exercise.id}: scaffold leaked an expected result`);
}

const scaffoldById = new Map(generated.map(item => [item.id, item.code]));
const representativeChecks = [
  [1, 'print(add_numbers(2, 3))', 'positional arguments'],
  [550, 'print(count_digit(12345, 3))', 'multiple parameters'],
  [1380, 'print(greet(name="Bob", age=40))', 'keyword arguments'],
  [495, 'example = Dog()', 'class construction'],
  [495, 'print(example.speak())', 'class method call'],
  [598, 'print(compose(add_one, multiply_by_two)(5))', 'callable arguments and returned call'],
  [1597, 'def rsplit_string(s, delimiter, maxsplit):', 'script-mode function structure'],
  [1597, "print(rsplit_string('one.two.three.four', '.', 2))", 'script-mode representative call'],
];
for (const [id, expectedSnippet, label] of representativeChecks) {
  if (!scaffoldById.get(id)?.includes(expectedSnippet)) failures.push(`Problem ${id}: scaffold does not preserve ${label}`);
}

const pythonAudit = spawnSync('python3', ['-c', [
  'import ast, json, sys',
  'items = json.load(sys.stdin)',
  'failures = []',
  'for item in items:',
  '    try:',
  '        ast.parse(item["code"] or "# empty")',
  '    except SyntaxError as error:',
  '        failures.append({"id": item["id"], "line": error.lineno, "message": error.msg})',
  'print(json.dumps(failures))',
].join('\n')], { input: JSON.stringify(generated), encoding: 'utf8', maxBuffer: 20 * 1024 * 1024 });

if (pythonAudit.status !== 0) {
  failures.push(`Python syntax audit failed to run: ${pythonAudit.stderr.trim()}`);
} else {
  const syntaxFailures = JSON.parse(pythonAudit.stdout || '[]');
  for (const failure of syntaxFailures) failures.push(`Problem ${failure.id}: invalid scaffold syntax on line ${failure.line}: ${failure.message}`);
}

console.log('Code scaffold audit');
console.log(`Exercises checked: ${EXERCISES.length}`);
console.log(`Function/class scaffolds: ${functionScaffolds}`);
console.log(`Script-mode scaffolds: ${scriptStarters}`);
console.log(`Generated script scaffolds: ${generatedScriptScaffolds}`);
console.log(`Failures: ${failures.length}`);

if (failures.length) {
  failures.slice(0, 100).forEach(failure => console.error(`- ${failure}`));
  process.exitCode = 1;
}
