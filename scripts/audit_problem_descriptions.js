#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'problem-description-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'entry.cjs');

fs.writeFileSync(entry, [
  `export { EXERCISES } from ${JSON.stringify(path.join(root, 'exercises.ts'))};`,
  `export { formatExerciseDescription } from ${JSON.stringify(path.join(root, 'services/exercisePresentation.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const { EXERCISES, formatExerciseDescription } = require(bundle);
  const failures = [];

  for (const exercise of EXERCISES) {
    const description = String(exercise.description || '');
    const firstLine = description.split('\n').find(line => line.trim()) || '';
    if (firstLine.length < 20) failures.push(`Problem ${exercise.id}: task statement is too short`);
    if (!description.split('\n')[0].trim()) failures.push(`Problem ${exercise.id}: task statement is missing`);
    if (/^description\\?\"\s*:/i.test(description.trim())) failures.push(`Problem ${exercise.id}: serialized field text leaked into task`);
    if (/\uFFFD|[\x00-\x08\x0B\x0C\x0E-\x1F]/.test(description)) failures.push(`Problem ${exercise.id}: invalid text character`);

    const exampleSection = description.split(/\n(?:Examples?|Exemples?)\s*:\s*\n/i).slice(1).join('\n');
    const counts = new Map();
    for (const line of exampleSection.split('\n').map(item => item.trim()).filter(Boolean)) {
      counts.set(line, (counts.get(line) || 0) + 1);
    }
    if ([...counts.values()].some(count => count > 1)) failures.push(`Problem ${exercise.id}: repeated example text`);

    const withoutDifficulty = description
      .split('\n')
      .filter(line => !/^\s*(?:Difficulty|Difficulté)\s*:/i.test(line))
      .join('\n');
    const english = formatExerciseDescription(withoutDifficulty, 'beginner', 'en');
    const french = formatExerciseDescription(withoutDifficulty, 'beginner', 'fr');
    if (!/^Difficulty:\s*Easy\./m.test(english)) failures.push(`Problem ${exercise.id}: English difficulty missing`);
    if (!/^Difficulté\s*:\s*Facile\./m.test(french)) failures.push(`Problem ${exercise.id}: French difficulty missing`);
    const englishExample = english.search(/^Examples?\s*:/m);
    const englishDifficulty = english.search(/^Difficulty\s*:/m);
    if (englishExample >= 0 && englishDifficulty > englishExample) failures.push(`Problem ${exercise.id}: difficulty appears after examples`);
  }

  const problem856 = EXERCISES.find(exercise => exercise.id === 856);
  if (!problem856 || !/input 30[^\n]*900\n961/.test(problem856.description)) {
    failures.push('Problem 856: clear loop examples are missing');
  }

  console.log('Problem description audit');
  console.log(`Exercises checked: ${EXERCISES.length}`);
  console.log(`Failures: ${failures.length}`);
  failures.slice(0, 80).forEach(failure => console.error(failure));
  if (failures.length) process.exit(1);
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
