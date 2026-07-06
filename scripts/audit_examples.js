const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(root, 'exercises.ts'), 'utf8');
const graderSrc = fs.readFileSync(path.join(root, 'graders.ts'), 'utf8');

const compiledTs = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2020, esModuleInterop: true } }).outputText;
const compiledGr = ts.transpileModule(graderSrc, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2020, esModuleInterop: true } }).outputText;
const sandbox = { exports: {}, module: { exports: {} }, require: () => ({}) };
sandbox.exports = sandbox.module.exports;
vm.runInNewContext(compiledGr, sandbox);
vm.runInNewContext(compiledTs, sandbox);

const { EXERCISES, AUTO_GRADERS } = sandbox.module.exports;

function splitArgs(argsStr) {
  const args = [];
  let current = '';
  let depth = 0;
  let inStr = false;
  let quoteCh = '';
  for (let i = 0; i < argsStr.length; i++) {
    const ch = argsStr[i];
    if (inStr) {
      current += ch;
      if (ch === quoteCh) inStr = false;
      continue;
    }
    if (ch === '"' || ch === "'") {
      current += ch;
      inStr = true;
      quoteCh = ch;
      continue;
    }
    if (ch === '[' || ch === '(' || ch === '{') depth++;
    if (ch === ']' || ch === ')' || ch === '}') depth--;
    if (ch === ',' && depth === 0) {
      args.push(current.trim());
      current = '';
      continue;
    }
    current += ch;
  }
  if (current.trim()) args.push(current.trim());
  return args.filter(Boolean);
}

const issues = [];
let totalExamples = 0;

for (const ex of EXERCISES) {
  const desc = ex.description || '';
  const code = ex.initialCode || '';
  const grader = AUTO_GRADERS[ex.id];
  const fnMatch = code.match(/def\s+(\w+)\s*\(([^)]*)\)/);
  const fnName = fnMatch ? fnMatch[1] : null;
  const params = fnMatch ? fnMatch[2].split(',').map(p => p.trim().split(':')[0].trim()).filter(Boolean) : [];

  const lines = desc.split('\n');
  const exampleLines = lines.filter(l => l.includes('\u2192') || l.includes('->'));
  totalExamples += exampleLines.length;

  for (const line of exampleLines) {
    const callMatch = line.match(/(\w+)\s*\(([^)]*)\)/);
    if (!callMatch) continue;
    const callFn = callMatch[1];
    const argsStr = callMatch[2];
    const args = splitArgs(argsStr);

    // Check 1: args count doesn't match params
    if (fnName && callFn === fnName && params.length > 0 && args.length !== params.length) {
      issues.push({ id: ex.id, type: 'arg_count', detail: `${params.length} params but ${args.length} args: (${argsStr})` });
      continue;
    }

    // Check 2: expected output is "?" (unknown)
    const expectedMatch = line.match(/\u2192\s*(.+)$/);
    const expected = expectedMatch ? expectedMatch[1].trim() : '';
    if (expected === '?') {
      issues.push({ id: ex.id, type: 'unknown_result', detail: `example result is '?': (${argsStr})` });
      continue;
    }

    // Check 3: description says list/array but example passes single literal (string or number)
    const descLower = desc.toLowerCase();
    const looksLikeList = /list|array/.test(descLower);
    if (looksLikeList && args.length === 1 && fnName) {
      const param = params[0] || '';
      const paramLooksList = /lst|list|arr|array|items|numbers|strings|elems/.test(param);
      const allStrings = args.every(a => (a.startsWith("'") && a.endsWith("'")) || (a.startsWith('"') && a.endsWith('"')));
      const singleNumber = /^\d+$/.test(args[0]);
      if (paramLooksList && (allStrings || singleNumber)) {
        issues.push({ id: ex.id, type: 'single_arg_for_list', detail: `passes '${args[0]}' to list param '${param}'` });
        continue;
      }
    }

    // Check 4: grader has test data - does example match ANY test case?
    if (grader && grader.tests && Array.isArray(grader.tests) && fnName) {
      const graderTests = grader.tests;
      const exampleNorm = args.join(',').replace(/'/g, '').replace(/"/g, '');
      let matchesGrader = false;
      for (const tc of graderTests) {
        const tcArgs = Array.isArray(tc.args) ? tc.args : [tc.args];
        const tcStr = tcArgs.map(a => String(a).replace(/'/g, '').replace(/"/g, '')).join(',');
        if (exampleNorm === tcStr) {
          matchesGrader = true;
          break;
        }
      }
      if (!matchesGrader && graderTests.length > 0) {
        // Not in grader, but might be a simplified example
        // Only flag if it's clearly wrong (like string for list)
      }
    }
  }

  // Check 5: known wrong patterns
  // Examples with "hello" → "your world" (nonsensical)
  const fullDesc = desc.replace(/examples?:?\s*/i, '').split('\n').slice(0, 1).join('');
  for (const line of exampleLines) {
    const expectedStr = line.split('\u2192')[1]?.trim() || '';
    // Check for clearly wrong expected values that are just placeholders
    const weirdOutputs = ['?', '...', 'output', 'result', 'answer'];
    if (weirdOutputs.includes(expectedStr.toLowerCase())) {
      issues.push({ id: ex.id, type: 'placeholder_output', detail: `expected is '${expectedStr}': ${line.trim()}` });
    }
  }
}

// Group by type
const byType = {};
for (const issue of issues) {
  if (!byType[issue.type]) byType[issue.type] = [];
  byType[issue.type].push({ id: issue.id, detail: issue.detail });
}

console.log('Total example lines:', totalExamples);
console.log('Total issues found:', issues.length);
console.log('');

for (const [type, items] of Object.entries(byType).sort((a, b) => b[1].length - a[1].length)) {
  console.log(`${type}: ${items.length}`);
  items.slice(0, 25).forEach(i => console.log(`  P${i.id}: ${i.detail}`));
  if (items.length > 25) console.log(`  ... and ${items.length - 25} more`);
  console.log('');
}
