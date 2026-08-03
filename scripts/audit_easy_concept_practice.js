#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'easy-concept-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'bundle.cjs');
const expectedConcepts = ['While Loop', 'Boolean Logic', 'Built-in', 'Set', 'Comprehension', 'For Loop', 'Iterator'];

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
  `export { EASY_CONCEPT_PRACTICE_EXERCISES } from ${JSON.stringify(path.join(root, 'easyConceptPracticeExercises.ts'))};`,
  `export { EASY_CONCEPT_PRACTICE_GRADERS } from ${JSON.stringify(path.join(root, 'easyConceptPracticeGraders.ts'))};`,
  `export { EASY_CONCEPT_PRACTICE_FR } from ${JSON.stringify(path.join(root, 'services/easyConceptPracticeFr.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const {
    EXERCISES: allExercises,
    EASY_CONCEPT_PRACTICE_EXERCISES: exercises,
    EASY_CONCEPT_PRACTICE_GRADERS: graders,
    EASY_CONCEPT_PRACTICE_FR: french,
  } = require(bundle);
  const failures = [];

  if (exercises.length !== 350) failures.push(`expected 350 exercises, found ${exercises.length}`);
  const expectedIds = Array.from({ length: 350 }, (_, index) => 5708 + index);
  if (JSON.stringify(exercises.map(item => item.id)) !== JSON.stringify(expectedIds)) failures.push('IDs are not exactly 5708-6057');
  const allIds = allExercises.map(item => item.id);
  if (new Set(allIds).size !== allIds.length) failures.push('duplicate exercise IDs found in the complete curriculum');

  const normalizedPrompts = exercises.map(item => item.description.split('\n')[0].toLowerCase().replace(/`[^`]+`/g, '<callable>'));
  if (new Set(normalizedPrompts).size !== normalizedPrompts.length) failures.push('duplicate normalized English prompts found');
  const functionNames = exercises.map(item => graders[item.id]?.functionNames?.[0]);
  if (new Set(functionNames).size !== functionNames.length) failures.push('duplicate function names found');
  if (new Set(exercises.map(item => item.solution)).size !== exercises.length) failures.push('duplicate solution text found');

  for (const concept of expectedConcepts) {
    const conceptExercises = exercises.filter(item => item.category === `${concept} Easy`);
    if (conceptExercises.length !== 50) failures.push(`${concept}: expected 50 Easy exercises, found ${conceptExercises.length}`);
  }

  const pythonChecks = [];
  for (const exercise of exercises) {
    const grader = graders[exercise.id];
    const localized = french[exercise.id];
    if (exercise.category.endsWith(' Easy') === false) failures.push(`${exercise.id}: category is not Easy`);
    if (!/\nDifficulty: Easy\./.test(exercise.description)) failures.push(`${exercise.id}: English difficulty is not Easy`);
    if (!localized?.description || !localized?.hint || !localized?.breakdown) failures.push(`${exercise.id}: French content incomplete`);
    if (!/Difficulté\s*:\s*Facile\./.test(localized?.description || '')) failures.push(`${exercise.id}: French difficulty is not Easy`);
    if (!grader || grader.tests?.length !== 3) failures.push(`${exercise.id}: grader must contain exactly three tests`);
    if (!exercise.solution.includes('# Example 5: direct call')) failures.push(`${exercise.id}: five solution presentations are missing`);
    if (!/^def\s+[A-Za-z_]\w*\([^)]*\):\n\s+pass$/m.test(exercise.initialCode)) failures.push(`${exercise.id}: starter function is malformed`);

    const concept = exercise.category.replace(/ Easy$/, '');
    if (concept === 'While Loop' && !grader?.requiredNodePatterns?.some(item => item.nodeType === 'While')) failures.push(`${exercise.id}: while syntax is not required`);
    if (concept === 'For Loop' && !grader?.requiredNodePatterns?.some(item => item.nodeType === 'For')) failures.push(`${exercise.id}: for syntax is not required`);
    if (concept === 'Comprehension' && !grader?.requiredNodePatterns?.some(item => /Comp$/.test(item.nodeType))) failures.push(`${exercise.id}: comprehension syntax is not required`);
    if (concept === 'Iterator' && !grader?.requiredCallPatterns?.some(item => item.functionName === 'iter')) failures.push(`${exercise.id}: iter() is not required`);
    if (concept === 'Built-in' && !grader?.requiredCallPatterns?.length) failures.push(`${exercise.id}: built-in call is not required`);
    if (concept === 'Set' && !grader?.requiredCallPatterns?.length && !grader?.requiredNodePatterns?.some(item => item.nodeType === 'SetComp')) failures.push(`${exercise.id}: set syntax is not required`);

    const canonical = exercise.solution.split('\n\nprint(')[0].replace(/^# Example 1:[^\n]*\n/, '');
    pythonChecks.push(canonical);
    for (const test of grader?.tests || []) {
      const call = `${grader.functionNames[0]}(${test.args.map(py).join(', ')})`;
      pythonChecks.push(`assert ${call} == ${py(test.expected)}, ${py(`Problem ${exercise.id}: ${call}`)}`);
    }
  }

  const pythonFile = path.join(tempDir, 'canonical-solutions.py');
  fs.writeFileSync(pythonFile, pythonChecks.join('\n\n'));
  const python = spawnSync('python3', [pythonFile], { encoding: 'utf8', maxBuffer: 20 * 1024 * 1024 });
  if (python.status !== 0) {
    const detail = python.error?.message || python.stderr || python.stdout || `python exited with status ${python.status}`;
    failures.push(`canonical solution execution failed: ${String(detail).trim()}`);
  }

  console.log('Easy concept practice audit');
  console.log(`Exercises: ${exercises.length}`);
  console.log(`Counts: ${JSON.stringify(Object.fromEntries(expectedConcepts.map(concept => [concept, exercises.filter(item => item.category === `${concept} Easy`).length])))}`);
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
