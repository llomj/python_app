const fs = require('fs');
const path = require('path');
const ts = require('typescript');
const vm = require('vm');

const root = path.resolve(__dirname, '..');

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

function isSolutionHeading(line) {
  return /^#\s*(Using|Script|Direct|Built|Manual|Alternative|Try|Another|Equivalent|Convert|Modify|Consider)\b/i.test(line.trim());
}

function getSections(solution) {
  const lines = String(solution || '').split('\n');
  const sections = [];
  let current = null;

  for (const line of lines) {
    if (isSolutionHeading(line)) {
      if (current) sections.push(current);
      current = { heading: line.trim(), body: [] };
      continue;
    }
    if (current) current.body.push(line);
  }

  if (current) sections.push(current);
  return sections;
}

function normalizeSolutionHeadings(solution) {
  const lines = String(solution || '').split('\n');
  const normalized = [...lines];
  let changed = false;

  for (let index = 0; index < lines.length; index += 1) {
    const heading = lines[index].trim();
    if (!/^#\s*Using function approach\b/i.test(heading)) continue;

    const body = [];
    for (let next = index + 1; next < lines.length; next += 1) {
      if (isSolutionHeading(lines[next])) break;
      body.push(lines[next]);
    }

    const bodyText = body.join('\n');
    const hasCallable = /\bdef\s+[A-Za-z_][A-Za-z0-9_]*\s*\(/.test(bodyText)
      || /\bclass\s+[A-Za-z_][A-Za-z0-9_]*\b/.test(bodyText);
    if (!hasCallable) {
      normalized[index] = lines[index].replace(/Using function approach/i, 'Using script approach');
      changed = true;
    }
  }

  return {
    changed,
    solution: normalized.join('\n'),
  };
}

function fixExerciseSource() {
  const filePath = path.join(root, 'exercises.ts');
  const source = fs.readFileSync(filePath, 'utf8');
  let changedCount = 0;
  const updated = source.replace(/"solution":\s*"((?:\\.|[^"\\])*)"/g, (match, rawSolution) => {
    const solution = JSON.parse(`"${rawSolution}"`);
    const normalized = normalizeSolutionHeadings(solution);
    if (!normalized.changed) return match;
    changedCount += 1;
    return `"solution": ${JSON.stringify(normalized.solution)}`;
  });

  if (changedCount > 0) fs.writeFileSync(filePath, updated);
  return changedCount;
}

if (process.argv.includes('--fix')) {
  const changedCount = fixExerciseSource();
  console.log(`Updated ${changedCount} exercise solution records.`);
}

const { EXERCISES } = loadTsExports('exercises.ts');
const mislabeledFunctionSections = [];

for (const exercise of EXERCISES) {
  for (const section of getSections(exercise.solution)) {
    if (!/^#\s*Using function approach\b/i.test(section.heading)) continue;
    const body = section.body.join('\n');
    const hasCallable = /\bdef\s+[A-Za-z_][A-Za-z0-9_]*\s*\(/.test(body)
      || /\bclass\s+[A-Za-z_][A-Za-z0-9_]*\b/.test(body);
    if (!hasCallable) {
      mislabeledFunctionSections.push({
        id: exercise.id,
        heading: section.heading,
        firstLine: section.body.find(line => line.trim())?.trim() || '',
      });
    }
  }
}

console.log('Solution section audit');
console.log(`Exercises: ${EXERCISES.length}`);
console.log(`Mislabeled function sections: ${mislabeledFunctionSections.length}`);

if (process.argv.includes('--show')) {
  for (const item of mislabeledFunctionSections.slice(0, 200)) {
    console.log(`${item.id}: ${item.heading} -> ${item.firstLine}`);
  }
  if (mislabeledFunctionSections.length > 200) {
    console.log(`...and ${mislabeledFunctionSections.length - 200} more`);
  }
}

const maxMislabeledArg = process.argv.find(arg => arg.startsWith('--max-mislabeled='));
if (maxMislabeledArg) {
  const max = Number(maxMislabeledArg.split('=')[1]);
  if (!Number.isFinite(max)) {
    console.error(`Invalid --max-mislabeled value: ${maxMislabeledArg}`);
    process.exit(1);
  }
  if (mislabeledFunctionSections.length > max) {
    console.error(`Solution section audit failed: ${mislabeledFunctionSections.length} mislabeled function sections exceeds max ${max}.`);
    process.exit(1);
  }
}
