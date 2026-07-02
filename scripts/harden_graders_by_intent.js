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
    require: () => ({}),
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

function isSingleCaseScriptRisk(grader) {
  const tests = Array.isArray(grader.tests) ? grader.tests : [];
  return (
    grader.mode === 'script' &&
    grader.compare !== 'sourceOnly' &&
    tests.length === 1 &&
    Array.isArray(tests[0]?.args) &&
    tests[0].args.length === 0 &&
    hasSourceRequirement(grader)
  );
}

function classifyIntent(description) {
  const text = description.toLowerCase();
  if (/\bwhile loop\b/.test(text)) return 'while-loop';
  if (/\bslic/.test(text)) return 'slicing-demo';
  if (/\bunpack/.test(text)) return 'unpacking-demo';
  if (/\bcomprehension\b/.test(text)) return 'comprehension-demo';
  if (/\blambda\b/.test(text)) return 'lambda-demo';
  if (/\busing a (?:built-in )?method\b/.test(text)) return 'method-demo';
  if (/\bpythonic way\b/.test(text)) return 'pythonic-demo';
  if (/\bdemonstrate\b.*\bscope\b|\bscope\b/.test(text)) return 'scope-demo';
  if (/\btry\b|\bexcept\b|\bexception\b|\berror\b/.test(text)) return 'exception-demo';
  if (/\brandom\b|\brandint\b|\bshuffle\b|\bsample\b|\bchoice\b/.test(text)) return 'random-demo';
  if (/\bparse\b|\bextract\b|\bregex\b|\bjson\b|\bcsv\b|\bxml\b/.test(text)) return 'parser-demo';
  if (/\busing\b|\buse\b|\bwith\b|\bwithout\b/.test(text)) return 'demo';
  return 'other';
}

function sourceOnlySafeReason(exercise, grader, intent) {
  const nodeNames = new Set((grader.requiredNodePatterns || []).map(pattern => pattern.nodeType));
  const callNames = new Set((grader.requiredCallPatterns || []).map(pattern => pattern.functionName));

  if (['slicing-demo', 'unpacking-demo', 'comprehension-demo', 'lambda-demo', 'method-demo', 'pythonic-demo'].includes(intent)) {
    return 'demo prompt with source requirements';
  }
  if (intent === 'parser-demo' && callNames.size > 0) {
    return 'parser/extractor prompt with required parser call';
  }
  if (intent === 'exception-demo' && nodeNames.has('Try')) {
    return 'exception prompt with Try requirement';
  }
  if (intent === 'scope-demo' && nodeNames.has('FunctionDef')) {
    return 'scope demonstration with function/source requirement';
  }
  if (intent === 'random-demo' && callNames.size > 0) {
    return 'random API demonstration with required random call';
  }
  return null;
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

function sourceOnlyBlock(block) {
  let next = block.replace(/compare:\s*['"][^'"]+['"]/, "compare: 'sourceOnly'");
  next = next.replace(
    /expected:\s*(?:`[\s\S]*?`|'(?:\\.|[^'\\])*'|"(?:\\.|[^"\\])*"|\[[\s\S]*?\]|\{[\s\S]*?\}|\([^\n\r]*?\)|[^\n\r,}]+)/,
    'expected: null',
  );
  return next;
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const exerciseById = new Map(EXERCISES.map(exercise => [exercise.id, exercise]));
const risks = [];
const safeConversions = [];
const unsafeByIntent = new Map();

for (const [rawId, grader] of Object.entries(AUTO_GRADERS)) {
  const id = Number(rawId);
  const exercise = exerciseById.get(id);
  if (!exercise || !isSingleCaseScriptRisk(grader)) continue;
  const intent = classifyIntent(exercise.description || '');
  const reason = sourceOnlySafeReason(exercise, grader, intent);
  const row = {
    id,
    intent,
    reason,
    description: (exercise.description || '').split('\n')[0],
    calls: (grader.requiredCallPatterns || []).map(pattern => pattern.functionName).join(','),
    nodes: (grader.requiredNodePatterns || []).map(pattern => pattern.nodeType).join(','),
  };
  risks.push(row);
  if (reason) {
    safeConversions.push(row);
  } else {
    if (!unsafeByIntent.has(intent)) unsafeByIntent.set(intent, []);
    unsafeByIntent.get(intent).push(row);
  }
}

console.log(`Single-case script graders still tied to sample output: ${risks.length}`);
console.log(`Safe sourceOnly conversions available: ${safeConversions.length}`);

const intentCounts = risks.reduce((counts, row) => {
  counts[row.intent] = (counts[row.intent] || 0) + 1;
  return counts;
}, {});
console.log('Risk count by intent:');
Object.entries(intentCounts)
  .sort((left, right) => right[1] - left[1])
  .forEach(([intent, count]) => console.log(`  ${intent}: ${count}`));

if (showAll) {
  console.log('\nSafe conversions:');
  safeConversions.forEach(row => console.log(`${row.id}\t${row.intent}\t${row.calls}\t${row.nodes}\t${row.description}`));
  console.log('\nNeeds manual/higher-specificity rules:');
  [...unsafeByIntent.values()].flat().forEach(row => console.log(`${row.id}\t${row.intent}\t${row.calls}\t${row.nodes}\t${row.description}`));
}

if (!writeMode) {
  console.log('\nDry run only. Re-run with --write to apply safe sourceOnly conversions.');
  process.exit(0);
}

let graderSource = fs.readFileSync(path.join(root, 'graders.ts'), 'utf8');
const changed = [];
for (const row of safeConversions) {
  const found = findGraderBlock(graderSource, row.id);
  const nextBlock = sourceOnlyBlock(found.block);
  if (nextBlock !== found.block) {
    graderSource = graderSource.slice(0, found.start) + nextBlock + graderSource.slice(found.end);
    changed.push(row.id);
  }
}

fs.writeFileSync(path.join(root, 'graders.ts'), graderSource);
console.log(`Applied ${changed.length} safe sourceOnly conversions.`);
if (changed.length) console.log(changed.join(','));
