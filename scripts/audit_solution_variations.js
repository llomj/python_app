const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const moduleCache = new Map();

function resolveLocalModule(specifier) {
  const relative = specifier.replace(/^\.\//, '');
  const candidates = [relative, `${relative}.ts`, path.join(relative, 'index.ts')];
  return candidates.find(candidate => fs.existsSync(path.join(root, candidate))) || null;
}

function loadTsExports(fileName) {
  if (moduleCache.has(fileName)) return moduleCache.get(fileName).exports;
  const source = fs.readFileSync(path.join(root, fileName), 'utf8');
  const compiled = ts.transpileModule(source, {
    compilerOptions: {
      module: ts.ModuleKind.CommonJS,
      target: ts.ScriptTarget.ES2020,
      esModuleInterop: true,
    },
    fileName,
  }).outputText;
  const module = { exports: {} };
  moduleCache.set(fileName, module);
  const directory = path.dirname(fileName);
  vm.runInNewContext(compiled, {
    module,
    exports: module.exports,
    require: (specifier) => {
      const resolved = resolveLocalModule(path.normalize(path.join(directory, specifier)));
      return resolved ? loadTsExports(resolved) : {};
    },
  }, { filename: fileName });
  return module.exports;
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const { buildSolutionVariations, countDistinctSolutionVariations } = loadTsExports('services/solutionVariations.ts');

const records = [];
const failures = [];

for (const exercise of EXERCISES) {
  const rendered = buildSolutionVariations(exercise.solution, exercise.id, AUTO_GRADERS[exercise.id]);
  const headingCount = (rendered.match(/^# (?:Example \d+:|Nested function approach|Callable class approach)/gm) || []).length;
  const distinctCount = countDistinctSolutionVariations(rendered);
  if (headingCount < 3 || distinctCount < 3) {
    failures.push(`${exercise.id}: only ${headingCount} headings / ${distinctCount} distinct variations`);
  }
  records.push({ id: exercise.id, code: rendered });
}

const checker = [
  'import json, sys',
  'for line in sys.stdin:',
  '    record = json.loads(line)',
  '    try:',
  '        compile(record["code"], f"problem_{record[\"id\"]}", "exec")',
  '    except Exception as error:',
  '        print(f"{record[\'id\']}: {type(error).__name__}: {error}")',
].join('\n');
const python = spawnSync('python3', ['-c', checker], {
  input: records.map(record => JSON.stringify(record)).join('\n'),
  encoding: 'utf8',
  maxBuffer: 20 * 1024 * 1024,
});

if (python.error) failures.push(`Python syntax audit could not start: ${python.error.message}`);
if (python.status !== 0) failures.push(`Python syntax audit exited ${python.status}: ${python.stderr.trim()}`);
if (python.stdout.trim()) failures.push(...python.stdout.trim().split('\n'));

console.log('Solution variation audit');
console.log(`Exercises: ${EXERCISES.length}`);
console.log(`Generated variations: ${records.length * 3}+`);
console.log(`Failures: ${failures.length}`);

if (failures.length) {
  failures.slice(0, 100).forEach(failure => console.error(failure));
  if (failures.length > 100) console.error(`...and ${failures.length - 100} more`);
  process.exit(1);
}
