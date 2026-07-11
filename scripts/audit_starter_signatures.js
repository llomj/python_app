const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const shouldFix = process.argv.includes('--fix');

function loadTsExports(fileName) {
  const source = fs.readFileSync(path.join(root, fileName), 'utf8');
  const compiled = ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2020 },
    fileName,
  }).outputText;
  const sandbox = {
    exports: {}, module: { exports: {} }, console,
    require: request => {
      if (request === './atomicBeginnerExercises') return loadTsExports('atomicBeginnerExercises.ts');
      if (request === './atomicBeginnerGraders') return loadTsExports('atomicBeginnerGraders.ts');
      return {};
    },
  };
  sandbox.exports = sandbox.module.exports;
  vm.runInNewContext(compiled, sandbox, { filename: fileName });
  return sandbox.module.exports;
}

function splitTopLevel(value) {
  const parts = [];
  let current = '';
  let depth = 0;
  let quote = '';
  for (let index = 0; index < value.length; index += 1) {
    const char = value[index];
    if (quote) {
      current += char;
      if (char === quote && value[index - 1] !== '\\') quote = '';
      continue;
    }
    if (char === '"' || char === "'") quote = char;
    if ('([{'.includes(char)) depth += 1;
    if (')]}'.includes(char)) depth -= 1;
    if (char === ',' && depth === 0) {
      parts.push(current.trim());
      current = '';
    } else current += char;
  }
  if (current.trim()) parts.push(current.trim());
  return parts;
}

function parseFirstFunction(code) {
  const match = String(code || '').match(/(?:^|\n)\s*(?:async\s+)?def\s+([A-Za-z_]\w*)\s*\(([^\n]*)\)\s*(?:->[^:]*)?:/);
  if (!match) return null;
  const params = splitTopLevel(match[2]);
  const positional = params.filter(param => param !== '/' && param !== '*' && !param.startsWith('**'));
  const required = positional.filter(param => !param.startsWith('*') && !param.includes('=')).length;
  const variadic = positional.some(param => param.startsWith('*'));
  return { name: match[1], rawParams: match[2], required, maximum: variadic ? Infinity : positional.length };
}

function testArity(test) {
  return (test.args || []).length
    + (test.argExpressions || []).length
    + (test.argFunctionNames || []).length
    + (test.functionListArgNames ? 1 : 0);
}

function accepts(signature, arity) {
  return signature && arity >= signature.required && arity <= signature.maximum;
}

function solutionSignature(exercise, names, arity) {
  const definitions = [...String(exercise.solution || '').matchAll(/(?:^|\n)\s*(?:async\s+)?def\s+([A-Za-z_]\w*)\s*\(([^\n]*)\)\s*(?:->[^:]*)?:/g)];
  for (const name of names) {
    for (const definition of definitions) {
      if (definition[1] !== name) continue;
      const parsed = parseFirstFunction(`def ${definition[1]}(${definition[2]}):\n    pass`);
      if (accepts(parsed, arity)) return { name: definition[1], params: definition[2] };
    }
  }
  return null;
}

function inferredParams(test) {
  const values = [...(test.args || [])];
  for (let index = 0; index < (test.argExpressions || []).length; index += 1) values.push(() => {});
  for (let index = 0; index < (test.argFunctionNames || []).length; index += 1) values.push(() => {});
  if (test.functionListArgNames) values.unshift([() => {}]);
  const used = new Map();
  return values.map(value => {
    let base = Array.isArray(value) ? 'items'
      : value !== null && typeof value === 'object' ? 'dictionary'
        : typeof value === 'string' ? 'text'
          : typeof value === 'number' ? 'number'
            : typeof value === 'function' ? 'function'
              : 'value';
    const count = (used.get(base) || 0) + 1;
    used.set(base, count);
    if (count > 1) base += count;
    return base;
  }).join(', ');
}

function replaceInitialCode(source, id, previous, next) {
  const marker = new RegExp(`\\"id\\"\\s*:\\s*${id}\\b`);
  const start = source.search(marker);
  if (start < 0) throw new Error(`Exercise ${id} was not found in source.`);
  const end = source.indexOf('\n    },', start);
  const blockEnd = end >= 0 ? end : source.length;
  const block = source.slice(start, blockEnd);
  const oldLiteral = JSON.stringify(previous);
  const newLiteral = JSON.stringify(next);
  if (!block.includes(`"initialCode": ${oldLiteral}`)) throw new Error(`Exercise ${id} initialCode was not found.`);
  return source.slice(0, start) + block.replace(`"initialCode": ${oldLiteral}`, `"initialCode": ${newLiteral}`) + source.slice(blockEnd);
}

const { EXERCISES } = loadTsExports('exercises.ts');
const { AUTO_GRADERS } = loadTsExports('graders.ts');
const issues = [];
for (const exercise of EXERCISES) {
  const grader = AUTO_GRADERS[exercise.id];
  if (!grader || grader.mode === 'script' || !grader.tests?.length) continue;
  const starter = parseFirstFunction(exercise.initialCode);
  if (!starter) continue;
  const arity = testArity(grader.tests[0]);
  const names = grader.functionNames || [];
  const preferredName = names.find(name => new RegExp(`(?:called\\s+|define\\s+(?:a\\s+)?function\\s+|^|\\n\\s*)[\\x60']?${name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}[\\x60']?\\s*\\(`, 'i').test(exercise.description)) || names[0] || starter.name;
  if (starter.name === preferredName && accepts(starter, arity)) continue;
  const prioritizedNames = [preferredName, ...names.filter(name => name !== preferredName)];
  const solution = solutionSignature(exercise, prioritizedNames, arity);
  const targetName = preferredName;
  const targetParams = solution?.params || (accepts(starter, arity) ? starter.rawParams : inferredParams(grader.tests[0]));
  const nextCode = String(exercise.initialCode).replace(
    /((?:^|\n)\s*(?:async\s+)?def\s+)[A-Za-z_]\w*\s*\([^\n]*\)(\s*(?:->[^:]*)?:)/,
    `$1${targetName}(${targetParams})$2`,
  );
  issues.push({ id: exercise.id, starter: `${starter.name}(${starter.rawParams})`, expected: `${targetName}(${targetParams})`, previous: exercise.initialCode, next: nextCode });
}

console.log(`Starter signature issues: ${issues.length}`);
issues.forEach(issue => console.log(`${issue.id}: ${issue.starter} -> ${issue.expected}`));
if (shouldFix && issues.length) {
  let source = fs.readFileSync(path.join(root, 'exercises.ts'), 'utf8');
  for (const issue of issues) source = replaceInitialCode(source, issue.id, issue.previous, issue.next);
  fs.writeFileSync(path.join(root, 'exercises.ts'), source);
  console.log(`Fixed ${issues.length} starter signatures.`);
}

if (!shouldFix && issues.length) process.exitCode = 1;
