#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'supplemental-concept-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'bundle.cjs');
const expected = {
  'Sorting Key': { total: 150, Easy: 70, Intermediate: 40, Difficult: 40 },
  'Testing & Debugging': { total: 50, Easy: 20, Intermediate: 20, Difficult: 10 },
  'Type Hint': { total: 50, Easy: 20, Intermediate: 20, Difficult: 10 },
  Exceptions: { total: 50, Easy: 20, Intermediate: 20, Difficult: 10 },
  'Equality & Identity': { total: 50, Easy: 20, Intermediate: 20, Difficult: 10 },
  'Enumerate & Zip': { total: 100, Easy: 40, Intermediate: 40, Difficult: 20 },
};
const py = value => {
  if (value === true) return 'True';
  if (value === false) return 'False';
  if (value === null) return 'None';
  if (typeof value === 'string') return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(py).join(', ')}]`;
  if (typeof value === 'object') return `{${Object.entries(value).map(([key, item]) => `${py(key)}: ${py(item)}`).join(', ')}}`;
  return String(value);
};

fs.writeFileSync(entry, [
  `export { EXERCISES } from ${JSON.stringify(path.join(root, 'exercises.ts'))};`,
  `export { SUPPLEMENTAL_CONCEPT_EXERCISES } from ${JSON.stringify(path.join(root, 'supplementalConceptExercises.ts'))};`,
  `export { SUPPLEMENTAL_CONCEPT_GRADERS } from ${JSON.stringify(path.join(root, 'supplementalConceptGraders.ts'))};`,
  `export { SUPPLEMENTAL_CONCEPT_FR } from ${JSON.stringify(path.join(root, 'services/supplementalConceptFr.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const data = require(bundle);
  const exercises = data.SUPPLEMENTAL_CONCEPT_EXERCISES;
  const graders = data.SUPPLEMENTAL_CONCEPT_GRADERS;
  const french = data.SUPPLEMENTAL_CONCEPT_FR;
  const failures = [];

  if (exercises.length !== 450) failures.push(`expected 450 exercises, found ${exercises.length}`);
  const expectedIds = Array.from({ length: 450 }, (_, index) => 7108 + index);
  if (JSON.stringify(exercises.map(item => item.id)) !== JSON.stringify(expectedIds)) failures.push('IDs are not exactly 7108-7557');
  const allIds = data.EXERCISES.map(item => item.id);
  if (new Set(allIds).size !== allIds.length) failures.push('duplicate IDs found in complete curriculum');
  const names = exercises.map(item => graders[item.id]?.functionNames?.[0]);
  if (new Set(names).size !== names.length) failures.push('duplicate function names found');
  const prompts = exercises.map(item => item.description.split('\n')[0].toLowerCase().replace(/`[^`]+`/g, '<callable>'));
  if (new Set(prompts).size !== prompts.length) failures.push('duplicate normalized prompts found');
  if (new Set(exercises.map(item => item.solution)).size !== exercises.length) failures.push('duplicate solutions found');

  for (const [concept, distribution] of Object.entries(expected)) {
    const conceptExercises = exercises.filter(item => item.category.startsWith(`${concept} `));
    if (conceptExercises.length !== distribution.total) failures.push(`${concept}: expected ${distribution.total}, found ${conceptExercises.length}`);
    for (const level of ['Easy', 'Intermediate', 'Difficult']) {
      const actual = conceptExercises.filter(item => item.category === `${concept} ${level}`).length;
      if (actual !== distribution[level]) failures.push(`${concept} ${level}: expected ${distribution[level]}, found ${actual}`);
    }
  }

  const pythonChecks = [];
  for (const exercise of exercises) {
    const grader = graders[exercise.id];
    const localized = french[exercise.id];
    if (!localized?.description || !localized?.hint || !localized?.breakdown) failures.push(`${exercise.id}: French content incomplete`);
    if (!grader || grader.tests?.length !== 3) failures.push(`${exercise.id}: expected three hidden cases`);
    if (!exercise.solution.includes('# Example 5: boundary case')) failures.push(`${exercise.id}: five solution presentations missing`);
    if (!/^def\s+[A-Za-z_]\w*\([^)]*\)(?:\s*->\s*[^:]+)?:\n\s+pass$/m.test(exercise.initialCode)) failures.push(`${exercise.id}: malformed starter`);
    const canonical = exercise.solution.split('\n\nprint(')[0];
    pythonChecks.push(canonical);
    for (const test of grader?.tests || []) {
      const call = `${grader.functionNames[0]}(${test.args.map(py).join(', ')})`;
      pythonChecks.push(`assert ${call} == ${py(test.expected)}, ${py(`Problem ${exercise.id}: ${call}`)}`);
    }
  }

  const pythonFile = path.join(tempDir, 'canonical.py');
  fs.writeFileSync(pythonFile, pythonChecks.join('\n\n'));
  const python = spawnSync('python3', [pythonFile], { encoding: 'utf8', maxBuffer: 30 * 1024 * 1024 });
  if (python.status !== 0) failures.push(`canonical execution failed: ${(python.stderr || python.stdout || python.error?.message).trim()}`);
  const solutionsFile = path.join(tempDir, 'complete-solutions.py');
  fs.writeFileSync(solutionsFile, exercises.map(item => item.solution).join('\n\n'));
  const solutions = spawnSync('python3', [solutionsFile], { encoding: 'utf8', maxBuffer: 30 * 1024 * 1024 });
  if (solutions.status !== 0) failures.push(`complete solution execution failed: ${(solutions.stderr || solutions.stdout || solutions.error?.message).trim()}`);

  console.log('Supplemental concept expansion audit');
  console.log(`Exercises: ${exercises.length}`);
  console.log('Sorting Keys: 70 Easy, 40 Intermediate, 40 Expert');
  console.log(`Graders: ${Object.keys(graders).length}`);
  console.log(`French records: ${Object.keys(french).length}`);
  console.log(`Canonical cases executed: ${exercises.length * 3}`);
  console.log(`Complete five-example solutions executed: ${exercises.length}`);
  if (failures.length) {
    failures.slice(0, 100).forEach(failure => console.error(`- ${failure}`));
    process.exitCode = 1;
  } else console.log('Result: passed');
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
