const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const moduleCache = new Map();

function resolveLocalModule(fileName, specifier) {
  const base = path.normalize(path.join(path.dirname(fileName), specifier));
  return [base, `${base}.ts`, path.join(base, 'index.ts')]
    .find(candidate => fs.existsSync(path.join(root, candidate))) || null;
}

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
  const sandbox = { exports: module.exports, module, require: specifier => {
    const resolved = resolveLocalModule(fileName, specifier);
    return resolved ? loadTsExports(resolved) : {};
  } };
  vm.runInNewContext(compiled, sandbox, { filename: fileName });
  return module.exports;
}

function hasValue(value) {
  if (Array.isArray(value)) return value.length > 0;
  if (value && typeof value === 'object') return Object.keys(value).length > 0;
  return Boolean(value);
}

function scriptFallbackBlockedReason(testCase) {
  const blockedKeys = [];
  const key = blockedKeys.find(item => hasValue(testCase?.[item]));
  return key || null;
}

function fallbackKind(grader) {
  const tests = Array.isArray(grader.tests) ? grader.tests : [];
  if (grader.mode === 'script') return { kind: 'native-script-mode' };
  if (!Array.isArray(grader.functionNames) || grader.functionNames.length === 0) {
    return { kind: 'blocked', reason: 'missing functionNames' };
  }
  if (tests.length === 0) return { kind: 'blocked', reason: 'empty tests' };
  if (tests.every(test => hasValue(test.expectedException))) {
    return { kind: 'blocked', reason: 'expectedException' };
  }
  const blockedReasons = new Set();
  for (const test of tests) {
    const reason = scriptFallbackBlockedReason(test);
    if (reason) blockedReasons.add(reason);
  }
  if (blockedReasons.size > 0) {
    return { kind: 'blocked', reason: [...blockedReasons].sort().join(', ') };
  }
  const hasInput = tests.some(test => Array.isArray(test.inputValues) && test.inputValues.length > 0);
  const hasRandom = tests.some(test =>
    hasValue(test.randomValues) ||
    hasValue(test.randomFloatValues) ||
    hasValue(test.randomChoiceValues) ||
    hasValue(test.randomSampleValues) ||
    hasValue(test.randomShuffleValues)
  );
  const hasFileSetup = tests.some(test =>
    hasValue(test.setupRemove) ||
    hasValue(test.setupDirs) ||
    hasValue(test.setupFiles) ||
    hasValue(test.setupSymlinks) ||
    hasValue(test.permissionDeniedPaths)
  );
  const hasArgs = tests.some(test => Array.isArray(test.args) && test.args.length > 0);
  if (hasInput) return { kind: 'eligible-input' };
  if (hasRandom) return { kind: 'eligible-random' };
  if (hasFileSetup) return { kind: 'eligible-file-setup' };
  if (hasArgs) return { kind: 'eligible-argument-injection' };
  return { kind: 'eligible-no-arg' };
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const exerciseById = new Map(EXERCISES.map(exercise => [exercise.id, exercise]));
const showAll = process.argv.includes('--all') || process.argv.includes('--show');
const minEligible = readNumberFlag('min-eligible');
const maxBlocked = readNumberFlag('max-blocked');

const counts = new Map();
const eligible = [];
const blocked = [];

for (const [rawId, grader] of Object.entries(AUTO_GRADERS)) {
  const id = Number(rawId);
  const result = fallbackKind(grader);
  counts.set(result.kind, (counts.get(result.kind) || 0) + 1);
  if (result.kind.startsWith('eligible')) {
    eligible.push({ id, kind: result.kind, grader });
  } else if (result.kind === 'blocked') {
    blocked.push({ id, reason: result.reason, grader });
  }
}

console.log('Script fallback audit');
console.log(`Graders: ${Object.keys(AUTO_GRADERS).length}`);
console.log(`Eligible function graders: ${eligible.length}`);
console.log(`Blocked function graders: ${blocked.length}`);
console.log(`Native script-mode graders: ${counts.get('native-script-mode') || 0}`);
console.log(`Distribution: ${[...counts.entries()].sort((a, b) => a[0].localeCompare(b[0])).map(([kind, total]) => `${kind}:${total}`).join(', ')}`);

if (showAll) {
  console.log(`Eligible IDs: ${eligible.map(item => `${item.id}:${item.kind}`).join(', ')}`);
  console.log(`Blocked IDs: ${blocked.map(item => `${item.id}:${item.reason}`).join(', ')}`);
}

if (blocked.length) {
  console.log('First blocked function graders:');
  for (const item of blocked.slice(0, 40)) {
    const exercise = exerciseById.get(item.id);
    const names = Array.isArray(item.grader.functionNames) ? item.grader.functionNames.join(', ') : '';
    console.log(`${item.id}: ${exercise?.title || `Problem ${item.id}`} [${names}] reason=${item.reason}`);
  }
}

const failures = [];
if (minEligible !== null && eligible.length < minEligible) {
  failures.push(`eligible script fallback graders ${eligible.length} below min ${minEligible}`);
}
if (maxBlocked !== null && blocked.length > maxBlocked) {
  failures.push(`blocked script fallback graders ${blocked.length} exceeds max ${maxBlocked}`);
}
if (failures.length) {
  console.error(`Script fallback audit failed: ${failures.join('; ')}`);
  process.exit(1);
}
