const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const MIN_FUNCTION_TESTS = 2;

function loadTsExports(fileName) {
  const source = fs.readFileSync(path.join(root, fileName), 'utf8');
  const compiled = ts.transpileModule(source, {
    compilerOptions: {
      module: ts.ModuleKind.CommonJS,
      target: ts.ScriptTarget.ES2020,
      esModuleInterop: true,
    },
    fileName,
  }).outputText;
  const sandbox = {
    exports: {},
    module: { exports: {} },
    require: () => ({}),
  };
  sandbox.exports = sandbox.module.exports;
  vm.runInNewContext(compiled, sandbox, { filename: fileName });
  return sandbox.module.exports;
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');

const exerciseById = new Map(EXERCISES.map(exercise => [exercise.id, exercise]));
const distribution = new Map();
const weakFunctionGraders = [];
const singleCaseScriptGraders = [];
const emptyGraders = [];

for (const [rawId, grader] of Object.entries(AUTO_GRADERS)) {
  const id = Number(rawId);
  const tests = Array.isArray(grader.tests) ? grader.tests : [];
  const testCount = tests.length;
  distribution.set(testCount, (distribution.get(testCount) || 0) + 1);

  if (testCount === 0) {
    emptyGraders.push(id);
    continue;
  }

  if (grader.mode === 'script') {
    if (testCount === 1) singleCaseScriptGraders.push(id);
    continue;
  }

  if (testCount < MIN_FUNCTION_TESTS) {
    weakFunctionGraders.push({
      id,
      title: exerciseById.get(id)?.title || `Problem ${id}`,
      functionNames: grader.functionNames || [],
    });
  }
}

const sortedDistribution = [...distribution.entries()].sort((a, b) => a[0] - b[0]);
const weakIds = weakFunctionGraders.map(item => item.id);
const showAll = process.argv.includes('--all');
const shownWeakIds = showAll ? weakIds : weakIds.slice(0, 100);

console.log('Grader quality audit');
console.log(`Exercises: ${EXERCISES.length}`);
console.log(`Graders: ${Object.keys(AUTO_GRADERS).length}`);
console.log(`Test-count distribution: ${sortedDistribution.map(([count, total]) => `${count}:${total}`).join(', ')}`);
console.log(`Function graders below ${MIN_FUNCTION_TESTS} tests: ${weakFunctionGraders.length}`);
console.log(`Single-case script graders: ${singleCaseScriptGraders.length}`);
console.log(`Empty graders: ${emptyGraders.length}`);

if (weakFunctionGraders.length) {
  console.log(`Weak function grader IDs${showAll ? '' : ' (first 100)'}: ${shownWeakIds.join(', ')}`);
  if (!showAll && weakIds.length > shownWeakIds.length) {
    console.log(`Run npm run audit:graders -- --all to print all ${weakIds.length} weak function grader IDs.`);
  }
  console.log('First weak function graders:');
  for (const item of weakFunctionGraders.slice(0, 25)) {
    console.log(`${item.id}: ${item.title} [${item.functionNames.join(', ')}]`);
  }
}

if (emptyGraders.length) {
  process.exitCode = 1;
}
