const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const writeMode = process.argv.includes('--write');
const showAll = process.argv.includes('--all');

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
    require: (specifier) => {
      if (specifier === './atomicBeginnerExercises') return loadTsExports('atomicBeginnerExercises.ts');
      if (specifier === './atomicBeginnerGraders') return loadTsExports('atomicBeginnerGraders.ts');
      return {};
    },
  };
  sandbox.exports = sandbox.module.exports;
  vm.runInNewContext(compiled, sandbox, { filename: fileName });
  return sandbox.module.exports;
}

function hasSourceRequirement(grader) {
  return (
    (grader.requiredCallPatterns?.length || 0) > 0 ||
    (grader.requiredNodePatterns?.length || 0) > 0 ||
    (grader.requiredClassInheritance?.length || 0) > 0 ||
    (grader.requiredBoolOps?.length || 0) > 0 ||
    (grader.requiredAstOperators?.length || 0) > 0 ||
    (grader.requiredUnpackPatterns?.length || 0) > 0
  );
}

function isSingleCaseScript(grader) {
  const tests = Array.isArray(grader.tests) ? grader.tests : [];
  return (
    grader.mode === 'script' &&
    grader.compare !== 'sourceOnly' &&
    grader.compare !== 'sourceIntent' &&
    tests.length === 1 &&
    Array.isArray(tests[0]?.args) &&
    tests[0].args.length === 0 &&
    hasSourceRequirement(grader)
  );
}

function shouldStayExact(description) {
  const text = description.toLowerCase();
  return [
    /following pattern/,
    /\bpyramid\b/,
    /\btriangle\b/,
    /full time table/,
    /square pattern/,
    /multiplication table/,
    /fibonacci/,
    /\bcount ?down\b/,
    /count from \d+ down/,
    /print numbers? from/,
    /prints? numbers? from/,
    /print all (?:the )?numbers? from/,
    /print all even numbers/,
    /print all odd numbers/,
    /even numbers? between/,
    /odd numbers? between/,
    /sum (?:all )?(?:the )?(?:odd )?numbers? from/,
    /sum of numbers from/,
    /product of numbers from/,
    /keeps doubling/,
    /repeatedly squares/,
    /keeps adding 5/,
    /skipping multiples/,
    /count how many times it doubled/,
  ].some(pattern => pattern.test(text));
}

function shouldUseSourceIntent(exercise, grader) {
  const description = exercise.description || '';
  const text = description.toLowerCase();
  if (shouldStayExact(description)) return false;
  const callNames = new Set((grader.requiredCallPatterns || []).map(pattern => pattern.functionName));
  const nodeNames = new Set((grader.requiredNodePatterns || []).map(pattern => pattern.nodeType));
  if (nodeNames.has('Try') || nodeNames.has('Assert')) return true;
  if (nodeNames.has('ClassDef') && /dataclass|file-like|context/.test(text)) return true;
  if (nodeNames.has('Subscript') && /slice|extract|string|reverse/.test(text)) return true;
  if (nodeNames.has('Dict') && /dictionary|dict|key-value|keys|prices/.test(text)) return true;
  if (nodeNames.has('ListComp') && /separate|filter|list/.test(text)) return true;
  if (nodeNames.has('DictComp') && /dictionary|invert|dict/.test(text)) return true;
  if (nodeNames.has('BinOp') && /set|intersection|union/.test(text)) return true;
  const sourceIntentCalls = new Set([
    'findall',
    'finditer',
    'fullmatch',
    'match',
    'search',
    'sub',
    'split',
    'items',
    'get',
    'setdefault',
    'defaultdict',
    'field',
    'dataclass',
    'casefold',
    'encode',
    'decode',
    'hasattr',
    'callable',
    'Counter',
    'sorted',
    'max',
    'set',
    'len',
    'append',
    'add',
    'extend',
    'strip',
    'my_context',
  ]);
  for (const callName of callNames) {
    if (sourceIntentCalls.has(callName)) return true;
  }
  return /\buse\b|\busing\b|\bpython(ic)?\b|\bdemonstrate\b|\bvalidate\b|\bcheck if\b|\bhandle\b|\bcatch\b/.test(text);
}

function findGraderBlock(source, id) {
  const marker = `  ${id}: {`;
  const start = source.indexOf(marker);
  if (start < 0) throw new Error(`Could not find grader block for ${id}`);
  let depth = 0;
  let inString = false;
  let quote = '';
  let escape = false;
  for (let index = start; index < source.length; index += 1) {
    const char = source[index];
    if (inString) {
      if (escape) escape = false;
      else if (char === '\\') escape = true;
      else if (char === quote) inString = false;
      continue;
    }
    if (char === '"' || char === "'") {
      inString = true;
      quote = char;
      continue;
    }
    if (char === '{') depth += 1;
    if (char === '}') {
      depth -= 1;
      if (depth === 0) {
        let end = index + 1;
        if (source[end] === ',') end += 1;
        return { start, end, block: source.slice(start, end) };
      }
    }
  }
  throw new Error(`Unterminated grader block for ${id}`);
}

function sourceIntentBlock(block) {
  if (/compare:\s*['"]/.test(block)) {
    return block.replace(/compare:\s*['"][^'"]+['"]/, "compare: 'sourceIntent'");
  }
  return block.replace(/mode:\s*['"]script['"],?/, match => `${match}\n    compare: 'sourceIntent',`);
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const exerciseById = new Map(EXERCISES.map(exercise => [exercise.id, exercise]));
const candidates = [];
const keptExact = [];

for (const [rawId, grader] of Object.entries(AUTO_GRADERS)) {
  const id = Number(rawId);
  const exercise = exerciseById.get(id);
  if (!exercise || !isSingleCaseScript(grader)) continue;
  const row = {
    id,
    description: (exercise.description || '').split('\n')[0],
    calls: (grader.requiredCallPatterns || []).map(pattern => pattern.functionName).join(','),
    nodes: (grader.requiredNodePatterns || []).map(pattern => `${pattern.nodeType}:${pattern.minCount || 1}`).join(','),
  };
  if (shouldUseSourceIntent(exercise, grader)) candidates.push(row);
  else keptExact.push(row);
}

console.log(`Source-intent conversions available: ${candidates.length}`);
console.log(`Remaining exact-output script graders kept: ${keptExact.length}`);

if (showAll) {
  console.log('\nSource-intent conversions:');
  candidates.forEach(row => console.log(`${row.id}\t${row.calls}\t${row.nodes}\t${row.description}`));
  console.log('\nKept exact:');
  keptExact.forEach(row => console.log(`${row.id}\t${row.calls}\t${row.nodes}\t${row.description}`));
}

if (!writeMode) {
  console.log('\nDry run only. Re-run with --write to apply sourceIntent conversions.');
  process.exit(0);
}

let graderSource = fs.readFileSync(path.join(root, 'graders.ts'), 'utf8');
const changed = [];
for (const row of candidates) {
  const found = findGraderBlock(graderSource, row.id);
  const nextBlock = sourceIntentBlock(found.block);
  if (nextBlock !== found.block) {
    graderSource = graderSource.slice(0, found.start) + nextBlock + graderSource.slice(found.end);
    changed.push(row.id);
  }
}

fs.writeFileSync(path.join(root, 'graders.ts'), graderSource);
console.log(`Applied ${changed.length} sourceIntent conversions.`);
if (changed.length) console.log(changed.join(','));
