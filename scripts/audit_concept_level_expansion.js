#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'concept-level-expansion-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'bundle.cjs');
const expectedCounts = {
  'While Loop Easy': 50,
  'While Loop Intermediate': 50,
  'While Loop Expert': 50,
  'Dictionary Easy': 100,
  'Comprehension Easy': 50,
  'Comprehension Intermediate': 50,
  'Closure Easy': 50,
  'Lambda Easy': 100,
  'Lambda Intermediate': 50,
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
  `export { CONCEPT_LEVEL_EXPANSION_EXERCISES } from ${JSON.stringify(path.join(root, 'conceptLevelExpansionExercises.ts'))};`,
  `export { CONCEPT_LEVEL_EXPANSION_GRADERS } from ${JSON.stringify(path.join(root, 'conceptLevelExpansionGraders.ts'))};`,
  `export { CONCEPT_LEVEL_EXPANSION_FR } from ${JSON.stringify(path.join(root, 'services/conceptLevelExpansionFr.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const {
    EXERCISES: allExercises,
    CONCEPT_LEVEL_EXPANSION_EXERCISES: exercises,
    CONCEPT_LEVEL_EXPANSION_GRADERS: graders,
    CONCEPT_LEVEL_EXPANSION_FR: french,
  } = require(bundle);
  const failures = [];

  if (exercises.length !== 550) failures.push(`expected 550 exercises, found ${exercises.length}`);
  const expectedIds = Array.from({ length: 550 }, (_, index) => 6058 + index);
  if (JSON.stringify(exercises.map(item => item.id)) !== JSON.stringify(expectedIds)) failures.push('IDs are not exactly 6058-6607');
  if (Object.keys(graders).length !== 550) failures.push(`expected 550 graders, found ${Object.keys(graders).length}`);
  if (Object.keys(french).length !== 550) failures.push(`expected 550 French records, found ${Object.keys(french).length}`);

  const allIds = allExercises.map(item => item.id);
  if (new Set(allIds).size !== allIds.length) failures.push('duplicate exercise IDs found in the complete curriculum');

  const promptLines = exercises.map(item => item.description.split('\n')[0].trim().toLowerCase());
  if (new Set(promptLines).size !== promptLines.length) failures.push('duplicate English task prompts found');
  const priorPromptLines = new Set(allExercises.filter(item => item.id < 6058 || item.id > 6607).map(item => item.description.split('\n')[0].trim().toLowerCase()));
  if (promptLines.some(prompt => priorPromptLines.has(prompt))) failures.push('a new task prompt duplicates a pre-existing curriculum prompt');
  const functionNames = exercises.map(item => graders[item.id]?.functionNames?.[0]);
  if (new Set(functionNames).size !== functionNames.length) failures.push('duplicate function names found');
  if (new Set(exercises.map(item => item.solution)).size !== exercises.length) failures.push('duplicate solution text found');

  for (const [category, expected] of Object.entries(expectedCounts)) {
    const actual = exercises.filter(item => item.category === category).length;
    if (actual !== expected) failures.push(`${category}: expected ${expected}, found ${actual}`);
  }

  const pythonChecks = [];
  for (const exercise of exercises) {
    const grader = graders[exercise.id];
    const localized = french[exercise.id];
    const level = exercise.category.split(' ').at(-1);
    const frenchLevel = { Easy: 'Facile', Intermediate: 'Intermédiaire', Expert: 'Expert' }[level];
    if (!expectedCounts[exercise.category]) failures.push(`${exercise.id}: unexpected category ${exercise.category}`);
    if (!exercise.description.includes(`\nDifficulty: ${level}.`)) failures.push(`${exercise.id}: English difficulty does not match category`);
    if (!localized?.description || !localized?.hint || !localized?.breakdown) failures.push(`${exercise.id}: French content incomplete`);
    if (!localized?.description?.includes(`Difficulté : ${frenchLevel}.`)) failures.push(`${exercise.id}: French difficulty does not match category`);
    if (!grader || grader.tests?.length !== 3) failures.push(`${exercise.id}: grader must contain exactly three tests`);
    if (!exercise.solution.includes('# Example 5: direct call')) failures.push(`${exercise.id}: five solution presentations are missing`);
    if (!/^def\s+[A-Za-z_]\w*\([^)]*\):\n\s+pass$/m.test(exercise.initialCode)) failures.push(`${exercise.id}: starter function is malformed`);

    const concept = exercise.category.replace(/ (Easy|Intermediate|Expert)$/, '');
    const nodes = grader?.requiredNodePatterns || [];
    if (concept === 'While Loop' && !nodes.some(item => item.nodeType === 'While')) failures.push(`${exercise.id}: while syntax is not required`);
    if (concept === 'Comprehension' && !nodes.some(item => /Comp$/.test(item.nodeType))) failures.push(`${exercise.id}: comprehension syntax is not required`);
    if (concept === 'Closure' && !nodes.some(item => item.nodeType === 'FunctionDef' && item.minCount >= 2)) failures.push(`${exercise.id}: nested functions are not required`);
    if (concept === 'Lambda' && !nodes.some(item => item.nodeType === 'Lambda')) failures.push(`${exercise.id}: lambda syntax is not required`);

    const canonical = exercise.solution.split('\n\nprint(')[0].replace(/^# Example 1:[^\n]*\n/, '');
    pythonChecks.push(canonical);
    for (const test of grader?.tests || []) {
      let call = `${grader.functionNames[0]}(${test.args.map(py).join(', ')})`;
      if (test.callReturnedWith) call += `(${test.callReturnedWith.map(py).join(', ')})`;
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

  console.log('Concept-level expansion audit');
  console.log(`Exercises: ${exercises.length}`);
  console.log(`Counts: ${JSON.stringify(Object.fromEntries(Object.keys(expectedCounts).map(category => [category, exercises.filter(item => item.category === category).length])))}`);
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
