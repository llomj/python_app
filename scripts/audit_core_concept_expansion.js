#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'core-concept-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'bundle.cjs');
const expectedConcepts = ['None & Truthiness', 'Equality & Identity', 'String Formatting', 'Numbers & Precision', 'Mutability & Copying', 'Stacks & Queues', 'Collections Module', 'Paths & Directories', 'CSV & JSON', 'Algorithms & Complexity'];

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
  `export { CORE_CONCEPT_EXPANSION_EXERCISES } from ${JSON.stringify(path.join(root, 'coreConceptExpansionExercises.ts'))};`,
  `export { CORE_CONCEPT_EXPANSION_GRADERS } from ${JSON.stringify(path.join(root, 'coreConceptExpansionGraders.ts'))};`,
  `export { CORE_CONCEPT_EXPANSION_FR } from ${JSON.stringify(path.join(root, 'services/coreConceptExpansionFr.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const {
    EXERCISES: allExercises,
    CORE_CONCEPT_EXPANSION_EXERCISES: exercises,
    CORE_CONCEPT_EXPANSION_GRADERS: graders,
    CORE_CONCEPT_EXPANSION_FR: french,
  } = require(bundle);
  const failures = [];

  if (exercises.length !== 500) failures.push(`expected 500 exercises, found ${exercises.length}`);
  const expectedIds = Array.from({ length: 500 }, (_, index) => 6608 + index);
  if (JSON.stringify(exercises.map(item => item.id)) !== JSON.stringify(expectedIds)) failures.push('IDs are not exactly 6608-7107');
  const allIds = allExercises.map(item => item.id);
  if (new Set(allIds).size !== allIds.length) failures.push('duplicate exercise IDs found in the complete curriculum');

  const normalizedPrompts = exercises.map(item => item.description.split('\n')[0].toLowerCase().replace(/`[^`]+`/g, '<callable>'));
  if (new Set(normalizedPrompts).size !== normalizedPrompts.length) failures.push('duplicate normalized English prompts found');
  const functionNames = exercises.map(item => graders[item.id]?.functionNames?.[0]);
  if (new Set(functionNames).size !== functionNames.length) failures.push('duplicate function names found');
  if (new Set(exercises.map(item => item.solution)).size !== exercises.length) failures.push('duplicate solution text found');

  for (const concept of expectedConcepts) {
    const conceptExercises = exercises.filter(item => item.category.startsWith(`${concept} `));
    if (conceptExercises.length !== 50) failures.push(`${concept}: expected 50 exercises, found ${conceptExercises.length}`);
    for (const [level, expected] of [['Easy', 20], ['Intermediate', 20], ['Difficult', 10]]) {
      const actual = conceptExercises.filter(item => item.category === `${concept} ${level}`).length;
      if (actual !== expected) failures.push(`${concept} ${level}: expected ${expected}, found ${actual}`);
    }
  }

  const app = fs.readFileSync(path.join(root, 'App.tsx'), 'utf8');
  const translations = fs.readFileSync(path.join(root, 'services/translations.ts'), 'utf8');
  const modeIds = ['noneTruthiness', 'equalityIdentity', 'stringFormatting', 'numbersPrecision', 'mutabilityCopying', 'stacksQueues', 'collectionsModule', 'pathsDirectories', 'csvJson', 'algorithmsComplexity'];
  for (const modeId of modeIds) {
    if (!app.includes(`id: 'concept:${modeId}'`)) failures.push(`${modeId}: concept selector registration missing`);
    if (!app.includes(`'concept:${modeId}': {`)) failures.push(`${modeId}: reference guide missing`);
    for (const suffix of ['', 'Desc']) {
      const key = `'concept.${modeId}${suffix}'`;
      const count = translations.split(key).length - 1;
      if (count !== 2) failures.push(`${key}: expected English and French translations, found ${count}`);
    }
  }

  const pythonChecks = [];
  for (const exercise of exercises) {
    const grader = graders[exercise.id];
    const localized = french[exercise.id];
    if (!localized?.description || !localized?.hint || !localized?.breakdown) failures.push(`${exercise.id}: French content incomplete`);
    if (!/Difficulté\s*:\s*(?:Facile|Intermédiaire|Expert)\./.test(localized?.description || '')) failures.push(`${exercise.id}: French difficulty missing`);
    if (!grader || grader.tests?.length !== 3) failures.push(`${exercise.id}: grader must contain exactly three tests`);
    if (!exercise.solution.includes('# Example 5: boundary case')) failures.push(`${exercise.id}: five solution presentations are missing`);
    if (!/^def\s+[A-Za-z_]\w*\([^)]*\):\n\s+pass$/m.test(exercise.initialCode)) failures.push(`${exercise.id}: starter function is malformed`);

    const canonical = exercise.solution.split('\n\nprint(')[0];
    pythonChecks.push(canonical);
    for (const test of grader?.tests || []) {
      const call = `${grader.functionNames[0]}(${test.args.map(py).join(', ')})`;
      pythonChecks.push(`assert ${call} == ${py(test.expected)}, ${py(`Problem ${exercise.id}: ${call}`)}`);
    }
  }

  const pythonFile = path.join(tempDir, 'canonical-solutions.py');
  fs.writeFileSync(pythonFile, pythonChecks.join('\n\n'));
  const python = spawnSync('python3', [pythonFile], { encoding: 'utf8', maxBuffer: 30 * 1024 * 1024 });
  if (python.status !== 0) {
    const detail = python.error?.message || python.stderr || python.stdout || `python exited with status ${python.status}`;
    failures.push(`canonical solution execution failed: ${String(detail).trim()}`);
  }

  console.log('Core concept expansion audit');
  console.log(`Exercises: ${exercises.length}`);
  console.log(`Concepts: ${expectedConcepts.length}`);
  console.log('Per concept: 20 Easy, 20 Intermediate, 10 Expert');
  console.log(`Graders: ${Object.keys(graders).length}`);
  console.log(`French records: ${Object.keys(french).length}`);
  console.log(`Canonical cases executed: ${pythonChecks.filter(line => line.startsWith('assert ')).length}`);
  if (failures.length) {
    failures.slice(0, 100).forEach(failure => console.error(`- ${failure}`));
    process.exitCode = 1;
  } else console.log('Result: passed');
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
