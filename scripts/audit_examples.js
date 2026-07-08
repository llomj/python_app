const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const showAll = process.argv.includes('--show') || process.argv.includes('--all');
const maxIssuesArg = process.argv.find(arg => arg.startsWith('--max-issues='));
const maxIssues = maxIssuesArg ? Number(maxIssuesArg.slice('--max-issues='.length)) : null;

function loadTsExports(fileName) {
  const source = fs.readFileSync(path.join(root, fileName), 'utf8');
  const compiled = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2020, esModuleInterop: true },
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

function formatArg(arg) {
  if (typeof arg === 'string') return `'${arg}'`;
  if (Array.isArray(arg)) return `[${arg.map(formatArg).join(', ')}]`;
  if (arg === null) return 'None';
  if (arg === true) return 'True';
  if (arg === false) return 'False';
  if (typeof arg === 'object') return JSON.stringify(arg).replace(/"/g, "'");
  return String(arg);
}

function formatExpected(value) {
  if (typeof value === 'string') return `'${value}'`;
  if (Array.isArray(value)) return `[${value.map(formatExpected).join(', ')}]`;
  if (value === null) return 'None';
  if (value === true) return 'True';
  if (value === false) return 'False';
  if (value && typeof value === 'object') return JSON.stringify(value).replace(/"/g, "'");
  return String(value);
}

function splitArgs(rawArgs) {
  const args = [];
  let current = '';
  let depth = 0;
  let quote = null;
  let escaped = false;
  for (const ch of rawArgs) {
    if (quote) {
      current += ch;
      if (escaped) escaped = false;
      else if (ch === '\\') escaped = true;
      else if (ch === quote) quote = null;
      continue;
    }
    if (ch === '"' || ch === "'") {
      quote = ch;
      current += ch;
      continue;
    }
    if ('([{'.includes(ch)) depth++;
    if (')]}'.includes(ch)) depth--;
    if (ch === ',' && depth === 0) {
      args.push(current.trim());
      current = '';
    } else {
      current += ch;
    }
  }
  if (current.trim()) args.push(current.trim());
  return args;
}

function normalizeText(value) {
  return String(value).replace(/\s+/g, ' ').trim();
}

function normalizeLine(line) {
  return normalizeText(line.replace(/->/g, '→'));
}

function exampleLines(description) {
  return String(description || '')
    .split('\n')
    .filter(line => /(?:→|->)/.test(line));
}

function parseExampleLine(line) {
  const match = line.match(/^\s*([A-Za-z_]\w*)\((.*)\)\s*(?:→|->)\s*(.+?)\s*$/);
  if (!match) return null;
  return {
    functionName: match[1],
    rawArgs: match[2].trim(),
    args: splitArgs(match[2].trim()),
    expected: match[3].trim(),
  };
}

function graderExampleMap(grader) {
  const map = new Map();
  if (!grader || !Array.isArray(grader.tests)) return map;
  for (const test of grader.tests) {
    const names = test.functionName ? [test.functionName] : (grader.functionNames || []);
    if (!Array.isArray(test.args) || test.expected === undefined) continue;
    const args = test.args.map(formatArg).join(', ');
    for (const name of names) {
      map.set(`${name}(${normalizeText(args)})`, formatExpected(test.expected));
    }
  }
  return map;
}

function descriptionMainFunction(description) {
  const backticked = String(description || '').match(/`([A-Za-z_]\w*)`/);
  if (backticked) return backticked[1];
  const called = String(description || '').match(/(?:function|program)\s+(?:called|named)\s+([A-Za-z_]\w*)/i);
  return called ? called[1] : null;
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');

const issues = [];
let withExamples = 0;
let duplicateCount = 0;
let placeholderCount = 0;
let contradictionCount = 0;

for (const exercise of EXERCISES) {
  const lines = exampleLines(exercise.description);
  const grader = AUTO_GRADERS[exercise.id];
  const graderMap = graderExampleMap(grader);
  const allowedNames = new Set(grader?.functionNames || []);
  const mainName = descriptionMainFunction(exercise.description);
  if (mainName) allowedNames.add(mainName);

  if (lines.length) withExamples++;
  if (!lines.length) {
    issues.push({ id: exercise.id, type: 'missing_examples', detail: 'No example lines found.' });
    continue;
  }

  const seenLines = new Set();
  const seenCalls = new Set();
  const lowerDescription = String(exercise.description || '').toLowerCase();
  const expectsNumericData = /\b(integer|integers|number|numbers|numeric|float|floats)\b/.test(lowerDescription);
  const expectsListData = /\blist\b/.test(lowerDescription);

  for (const line of lines) {
    const normalized = normalizeLine(line);
    if (seenLines.has(normalized)) {
      duplicateCount++;
      issues.push({ id: exercise.id, type: 'duplicate_example_line', detail: normalized });
    }
    seenLines.add(normalized);

    if (/(?:→|->)\s*\?/.test(line)) {
      placeholderCount++;
      issues.push({ id: exercise.id, type: 'placeholder_output', detail: normalized });
    }

    const parsed = parseExampleLine(line);
    if (!parsed) {
      issues.push({ id: exercise.id, type: 'unparseable_example', detail: normalized });
      continue;
    }

    const callKey = `${parsed.functionName}(${normalizeText(parsed.rawArgs)})`;
    if (seenCalls.has(callKey)) {
      duplicateCount++;
      issues.push({ id: exercise.id, type: 'duplicate_example_input', detail: callKey });
    }
    seenCalls.add(callKey);

    if (allowedNames.size > 0 && !allowedNames.has(parsed.functionName)) {
      issues.push({ id: exercise.id, type: 'function_name_mismatch', detail: `${parsed.functionName} is not one of ${[...allowedNames].join(', ')}` });
    }

    const genericArg = parsed.args.find(arg => /^['"]?(hello|world|python|test|example|sample)['"]?$/i.test(arg));
    if (genericArg && (expectsNumericData || expectsListData)) {
      issues.push({ id: exercise.id, type: 'generic_arg_mismatch', detail: `${genericArg} does not fit the problem type` });
    }

    const expectedFromGrader = graderMap.get(callKey);
    if (expectedFromGrader !== undefined && normalizeText(expectedFromGrader) !== normalizeText(parsed.expected)) {
      contradictionCount++;
      issues.push({ id: exercise.id, type: 'grader_contradiction', detail: `${callKey} shows ${parsed.expected}, grader expects ${expectedFromGrader}` });
    }
  }
}

console.log('Example audit');
console.log(`Exercises: ${EXERCISES.length}`);
console.log(`Exercises with examples: ${withExamples}`);
console.log(`Issues: ${issues.length}`);
console.log(`Duplicate issues: ${duplicateCount}`);
console.log(`Placeholder outputs: ${placeholderCount}`);
console.log(`Grader contradictions: ${contradictionCount}`);

if (showAll || issues.length) {
  for (const issue of issues.slice(0, showAll ? issues.length : 80)) {
    console.log(`${issue.id}: ${issue.type}: ${issue.detail}`);
  }
  if (!showAll && issues.length > 80) console.log(`... ${issues.length - 80} more`);
}

if (maxIssues !== null && issues.length > maxIssues) {
  console.error(`Example audit failed: issues ${issues.length} exceeds max ${maxIssues}`);
  process.exit(1);
}
