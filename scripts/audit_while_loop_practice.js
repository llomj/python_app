#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'while-loop-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'bundle.cjs');
fs.writeFileSync(entry, [
  `export { WHILE_LOOP_PRACTICE_EXERCISES } from ${JSON.stringify(path.join(root, 'whileLoopPracticeExercises.ts'))};`,
  `export { WHILE_LOOP_PRACTICE_GRADERS } from ${JSON.stringify(path.join(root, 'whileLoopPracticeGraders.ts'))};`,
  `export { WHILE_LOOP_PRACTICE_FR } from ${JSON.stringify(path.join(root, 'services/whileLoopPracticeFr.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const { WHILE_LOOP_PRACTICE_EXERCISES: exercises, WHILE_LOOP_PRACTICE_GRADERS: graders, WHILE_LOOP_PRACTICE_FR: french } = require(bundle);
  const failures = [];
  if (exercises.length !== 100) failures.push(`expected 100 exercises, found ${exercises.length}`);
  const expectedIds = Array.from({ length: 100 }, (_, index) => 2381 + index);
  if (JSON.stringify(exercises.map(item => item.id)) !== JSON.stringify(expectedIds)) failures.push('IDs are not exactly 2381-2480');
  const normalizedPrompts = exercises.map(item => item.description.split('\n')[0].toLowerCase().replace(/`[^`]+`/g, '<name>'));
  if (new Set(normalizedPrompts).size !== exercises.length) failures.push('duplicate normalized English prompts found');
  for (const exercise of exercises) {
    const grader = graders[exercise.id];
    const localized = french[exercise.id];
    if (!/\bwhile\b/.test(exercise.solution)) failures.push(`${exercise.id}: solution has no while loop`);
    if (!/^def\s+[A-Za-z_]\w*\([^)]*\):/m.test(exercise.solution)) failures.push(`${exercise.id}: solution has no function`);
    if (!exercise.solution.includes('# Script approach') || !exercise.solution.includes('# Direct approach')) failures.push(`${exercise.id}: solution approaches incomplete`);
    if (!grader || grader.tests?.length < 3) failures.push(`${exercise.id}: missing three grader cases`);
    if (!grader?.requiredNodePatterns?.some(item => item.nodeType === 'While')) failures.push(`${exercise.id}: grader does not require while syntax`);
    if (!localized?.description || !localized?.hint || !localized?.breakdown) failures.push(`${exercise.id}: French content incomplete`);
    if (!/boucle while/i.test(localized?.description || '')) failures.push(`${exercise.id}: French prompt does not require while`);
  }
  const levels = Object.fromEntries(['Easy', 'Intermediate', 'Difficult'].map(level => [level, exercises.filter(item => item.category === `While Loop ${level}`).length]));
  console.log('While-loop practice audit');
  console.log(`Exercises: ${exercises.length}`);
  console.log(`Levels: ${JSON.stringify(levels)}`);
  console.log(`Graders: ${Object.keys(graders).length}`);
  console.log(`French records: ${Object.keys(french).length}`);
  if (failures.length) {
    failures.slice(0, 100).forEach(failure => console.error(`- ${failure}`));
    process.exitCode = 1;
  } else console.log('Result: passed');
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
