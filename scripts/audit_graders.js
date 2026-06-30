const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const MIN_FUNCTION_TESTS = 2;

function readNumberFlag(name) {
  const prefix = `--${name}=`;
  const inline = process.argv.find(arg => arg.startsWith(prefix));
  const flagIndex = process.argv.indexOf(`--${name}`);
  const rawValue = inline ? inline.slice(prefix.length) : flagIndex >= 0 ? process.argv[flagIndex + 1] : null;
  if (!rawValue || rawValue.startsWith('--')) return null;
  const value = Number(rawValue);
  if (!Number.isFinite(value)) {
    console.error(`Invalid --${name} value: ${rawValue}`);
    process.exit(1);
  }
  return value;
}

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
const singleCaseNoArgFunctionGraders = [];
const singleCaseScriptGraders = [];
const unguardedSingleCaseScriptGraders = [];
const hardcodeRiskScriptGraders = [];
const emptyGraders = [];
const invalidGraders = [];

function hasDynamicScriptSignal(grader, tests) {
  const callNames = new Set((grader.requiredCallPatterns || []).map(pattern => pattern.functionName));
  const nodeNames = new Set((grader.requiredNodePatterns || []).map(pattern => pattern.nodeType));
  const hasInputValues = tests.some(test => Array.isArray(test.inputValues) && test.inputValues.length > 0);
  const hasRandomValues = tests.some(test =>
    (Array.isArray(test.randomValues) && test.randomValues.length > 0) ||
    (Array.isArray(test.randomFloatValues) && test.randomFloatValues.length > 0) ||
    (Array.isArray(test.randomChoiceValues) && test.randomChoiceValues.length > 0) ||
    (Array.isArray(test.randomSampleValues) && test.randomSampleValues.length > 0) ||
    (Array.isArray(test.randomShuffleValues) && test.randomShuffleValues.length > 0)
  );
  const hasSetupOrFiles = tests.some(test =>
    (test.setupFiles && Object.keys(test.setupFiles).length > 0) ||
    (Array.isArray(test.setupDirs) && test.setupDirs.length > 0) ||
    (Array.isArray(test.setupRemove) && test.setupRemove.length > 0) ||
    (Array.isArray(test.getFiles) && test.getFiles.length > 0)
  );
  const hasRequiredCall = callNames.size > 0;
  const algorithmNodes = [
    'For', 'While', 'ListComp', 'DictComp', 'SetComp', 'GeneratorExp',
    'Lambda', 'Try', 'ExceptHandler', 'Raise', 'Assert', 'FunctionDef', 'ClassDef',
    'Subscript', 'Compare', 'BoolOp', 'IfExp', 'Tuple', 'Starred', 'Dict', 'Set',
    'BinOp', 'With', 'Assign', 'AnnAssign', 'AugAssign'
  ];
  return (
    hasInputValues ||
    hasRandomValues ||
    hasSetupOrFiles ||
    hasRequiredCall ||
    algorithmNodes.some(name => nodeNames.has(name))
  );
}

for (const [rawId, grader] of Object.entries(AUTO_GRADERS)) {
  const id = Number(rawId);
  const tests = Array.isArray(grader.tests) ? grader.tests : [];
  const testCount = tests.length;
  distribution.set(testCount, (distribution.get(testCount) || 0) + 1);

  if (!Array.isArray(grader.tests)) {
    invalidGraders.push(`${id}: tests must be an array`);
  }

  if (grader.mode !== 'script' && !Array.isArray(grader.functionNames)) {
    invalidGraders.push(`${id}: function graders must declare functionNames`);
  }

  if (grader.requiredCallPatterns !== undefined) {
    if (!Array.isArray(grader.requiredCallPatterns)) {
      invalidGraders.push(`${id}: requiredCallPatterns must be an array`);
    } else {
      grader.requiredCallPatterns.forEach((pattern, index) => {
        if (!pattern || typeof pattern.functionName !== 'string' || !pattern.functionName.trim()) {
          invalidGraders.push(`${id}: requiredCallPatterns ${index + 1} must declare functionName`);
        }
        if (pattern.keyword !== undefined && typeof pattern.keyword !== 'string') {
          invalidGraders.push(`${id}: requiredCallPatterns ${index + 1} keyword must be a string`);
        }
        if (pattern.minArgs !== undefined && (!Number.isInteger(pattern.minArgs) || pattern.minArgs < 0)) {
          invalidGraders.push(`${id}: requiredCallPatterns ${index + 1} minArgs must be a non-negative integer`);
        }
      });
    }
  }

  if (grader.requiredNodePatterns !== undefined) {
    if (!Array.isArray(grader.requiredNodePatterns)) {
      invalidGraders.push(`${id}: requiredNodePatterns must be an array`);
    } else {
      grader.requiredNodePatterns.forEach((pattern, index) => {
        if (!pattern || typeof pattern.nodeType !== 'string' || !pattern.nodeType.trim()) {
          invalidGraders.push(`${id}: requiredNodePatterns ${index + 1} must declare nodeType`);
        }
        if (pattern.minCount !== undefined && (!Number.isInteger(pattern.minCount) || pattern.minCount < 1)) {
          invalidGraders.push(`${id}: requiredNodePatterns ${index + 1} minCount must be a positive integer`);
        }
      });
    }
  }

  tests.forEach((test, index) => {
    if (!Object.prototype.hasOwnProperty.call(test, 'expected') && !Object.prototype.hasOwnProperty.call(test, 'expectedException')) {
      invalidGraders.push(`${id}: test ${index + 1} must declare expected or expectedException`);
    }
    if (!Object.prototype.hasOwnProperty.call(test, 'args')) {
      invalidGraders.push(`${id}: test ${index + 1} must declare args`);
    }
  });

  if (testCount === 0) {
    emptyGraders.push(id);
    continue;
  }

  if (grader.mode === 'script') {
    if (testCount === 1) {
      singleCaseScriptGraders.push(id);
      const hasSourceRequirements = (grader.requiredCallPatterns?.length || 0) > 0 || (grader.requiredNodePatterns?.length || 0) > 0;
      if (!hasSourceRequirements) unguardedSingleCaseScriptGraders.push(id);
      if (!hasDynamicScriptSignal(grader, tests)) {
        hardcodeRiskScriptGraders.push(id);
      }
    }
    continue;
  }

  if (testCount < MIN_FUNCTION_TESTS) {
    const firstArgs = Array.isArray(tests[0]?.args) ? tests[0].args : [];
    if (firstArgs.length === 0) {
      singleCaseNoArgFunctionGraders.push({
        id,
        title: exerciseById.get(id)?.title || `Problem ${id}`,
        functionNames: grader.functionNames || [],
      });
      continue;
    }
    weakFunctionGraders.push({
      id,
      title: exerciseById.get(id)?.title || `Problem ${id}`,
      functionNames: grader.functionNames || [],
    });
  }
}

const sortedDistribution = [...distribution.entries()].sort((a, b) => a[0] - b[0]);
const weakIds = weakFunctionGraders.map(item => item.id);
const showAll = process.argv.includes('--all') || process.argv.includes('--show');
const shownWeakIds = showAll ? weakIds : weakIds.slice(0, 100);
const maxWeakFunctions = readNumberFlag('max-weak-functions');
const maxSingleCaseScripts = readNumberFlag('max-single-case-scripts');
const maxUnguardedSingleCaseScripts = readNumberFlag('max-unguarded-single-case-scripts');
const maxHardcodeRiskScripts = readNumberFlag('max-hardcode-risk-scripts');
const maxEmptyGraders = readNumberFlag('max-empty-graders') ?? 0;

console.log('Grader quality audit');
console.log(`Exercises: ${EXERCISES.length}`);
console.log(`Graders: ${Object.keys(AUTO_GRADERS).length}`);
console.log(`Test-count distribution: ${sortedDistribution.map(([count, total]) => `${count}:${total}`).join(', ')}`);
console.log(`Parameterized function graders below ${MIN_FUNCTION_TESTS} tests: ${weakFunctionGraders.length}`);
console.log(`Single-case no-arg function graders: ${singleCaseNoArgFunctionGraders.length}`);
console.log(`Single-case script graders: ${singleCaseScriptGraders.length}`);
console.log(`Unguarded single-case script graders: ${unguardedSingleCaseScriptGraders.length}`);
console.log(`Hardcode-risk single-case script graders: ${hardcodeRiskScriptGraders.length}`);
console.log(`Empty graders: ${emptyGraders.length}`);
console.log(`Invalid grader definitions: ${invalidGraders.length}`);

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

if (singleCaseNoArgFunctionGraders.length && showAll) {
  console.log(`Single-case no-arg function grader IDs: ${singleCaseNoArgFunctionGraders.map(item => item.id).join(', ')}`);
  console.log('First single-case no-arg function graders:');
  for (const item of singleCaseNoArgFunctionGraders.slice(0, 25)) {
    console.log(`${item.id}: ${item.title} [${item.functionNames.join(', ')}]`);
  }
}

if (singleCaseScriptGraders.length && showAll) {
  console.log(`Single-case script grader IDs: ${singleCaseScriptGraders.join(', ')}`);
  console.log(`Unguarded single-case script grader IDs: ${unguardedSingleCaseScriptGraders.join(', ')}`);
  console.log(`Hardcode-risk single-case script grader IDs: ${hardcodeRiskScriptGraders.join(', ')}`);
  console.log('First single-case script graders:');
  for (const id of singleCaseScriptGraders.slice(0, 40)) {
    const exercise = exerciseById.get(id);
    const grader = AUTO_GRADERS[id];
    const expected = grader.tests?.[0]?.expected;
    const requiredCalls = (grader.requiredCallPatterns || []).map(pattern => pattern.functionName).join(', ');
    const requiredNodes = (grader.requiredNodePatterns || []).map(pattern => `${pattern.nodeType}:${pattern.minCount || 1}`).join(', ');
    console.log(`${id}: ${exercise?.title || `Problem ${id}`} expected=${JSON.stringify(expected)} calls=[${requiredCalls}] nodes=[${requiredNodes}]`);
  }
}

if (invalidGraders.length) {
  console.log('Invalid graders:');
  for (const issue of invalidGraders.slice(0, 80)) {
    console.log(issue);
  }
  if (invalidGraders.length > 80) {
    console.log(`...and ${invalidGraders.length - 80} more invalid grader issues.`);
  }
}

const gateFailures = [];
if (invalidGraders.length) {
  gateFailures.push(`${invalidGraders.length} invalid grader definitions`);
}
if (emptyGraders.length > maxEmptyGraders) {
  gateFailures.push(`${emptyGraders.length} empty graders exceeds max ${maxEmptyGraders}`);
}
if (maxWeakFunctions !== null && weakFunctionGraders.length > maxWeakFunctions) {
  gateFailures.push(`${weakFunctionGraders.length} weak function graders exceeds max ${maxWeakFunctions}`);
}
if (maxSingleCaseScripts !== null && singleCaseScriptGraders.length > maxSingleCaseScripts) {
  gateFailures.push(`${singleCaseScriptGraders.length} single-case script graders exceeds max ${maxSingleCaseScripts}`);
}
if (maxUnguardedSingleCaseScripts !== null && unguardedSingleCaseScriptGraders.length > maxUnguardedSingleCaseScripts) {
  gateFailures.push(`${unguardedSingleCaseScriptGraders.length} unguarded single-case script graders exceeds max ${maxUnguardedSingleCaseScripts}`);
}
if (maxHardcodeRiskScripts !== null && hardcodeRiskScriptGraders.length > maxHardcodeRiskScripts) {
  gateFailures.push(`${hardcodeRiskScriptGraders.length} hardcode-risk single-case script graders exceeds max ${maxHardcodeRiskScripts}`);
}

if (gateFailures.length) {
  console.error('Grader audit failed:');
  for (const failure of gateFailures) {
    console.error(`- ${failure}`);
  }
  process.exitCode = 1;
}
