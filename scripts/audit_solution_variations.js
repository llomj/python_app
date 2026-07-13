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
const { GENERATED_SIMPLE_SCRIPT_EXAMPLES } = loadTsExports('services/generatedSimpleScriptExamples.ts');

const records = [];
const failures = [];
const scriptRecords = Object.entries(GENERATED_SIMPLE_SCRIPT_EXAMPLES).map(([id, code]) => ({ id: Number(id), code }));

if (scriptRecords.length < 1500) {
  failures.push(`only ${scriptRecords.length} exercises have a validated simple script example`);
}

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
  '    sections = []',
  '    current = []',
  '    for source_line in record["code"].splitlines():',
  '        if source_line.startswith(("# Example ", "# Nested function approach", "# Callable class approach")):',
  '            if current: sections.append("\\n".join(current))',
  '            current = []',
  '        else:',
  '            current.append(source_line)',
  '    if current: sections.append("\\n".join(current))',
  '    for index, section in enumerate(sections, 1):',
  '        try:',
  '            compile(section, f"problem_{record[\"id\"]}_example_{index}", "exec")',
  '        except Exception as error:',
  '            print(f"{record[\'id\']} example {index}: {type(error).__name__}: {error}")',
].join('\n');
const python = spawnSync('python3', ['-c', checker], {
  input: records.map(record => JSON.stringify(record)).join('\n'),
  encoding: 'utf8',
  maxBuffer: 20 * 1024 * 1024,
});

if (python.error) failures.push(`Python syntax audit could not start: ${python.error.message}`);
if (python.status !== 0) failures.push(`Python syntax audit exited ${python.status}: ${python.stderr.trim()}`);
if (python.stdout.trim()) failures.push(...python.stdout.trim().split('\n'));

const scriptChecker = [
  'import ast, json, sys',
  'for line in sys.stdin:',
  '    record = json.loads(line)',
  '    try:',
  '        tree = ast.parse(record["code"])',
  '        blocked = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda))]',
  '        if blocked: raise ValueError(f"contains {type(blocked[0]).__name__}")',
  '        compile(tree, f"problem_{record[\"id\"]}_simple_script", "exec")',
  '    except Exception as error:',
  '        print(f"{record[\'id\']} simple script: {type(error).__name__}: {error}")',
].join('\n');
const scriptPython = spawnSync('python3', ['-c', scriptChecker], {
  input: scriptRecords.map(record => JSON.stringify(record)).join('\n'),
  encoding: 'utf8',
  maxBuffer: 20 * 1024 * 1024,
});
if (scriptPython.error) failures.push(`Simple-script audit could not start: ${scriptPython.error.message}`);
if (scriptPython.status !== 0) failures.push(`Simple-script audit exited ${scriptPython.status}: ${scriptPython.stderr.trim()}`);
if (scriptPython.stdout.trim()) failures.push(...scriptPython.stdout.trim().split('\n'));

console.log('Solution variation audit');
console.log(`Exercises: ${EXERCISES.length}`);
console.log(`Generated variations: ${records.length * 3}+`);
console.log(`Validated simple scripts: ${scriptRecords.length}`);
console.log(`Failures: ${failures.length}`);

if (failures.length) {
  failures.slice(0, 100).forEach(failure => console.error(failure));
  if (failures.length > 100) console.error(`...and ${failures.length - 100} more`);
  process.exit(1);
}
