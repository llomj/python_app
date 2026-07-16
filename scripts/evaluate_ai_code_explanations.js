#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'ai-code-explanation-eval-'));
const bundleFile = path.join(tempDir, 'ai-code-explanation-eval.cjs');
const entry = path.join(tempDir, 'entry.ts');

fs.writeFileSync(entry, [
  `export { EXERCISES } from ${JSON.stringify(path.join(root, 'exercises.ts'))};`,
  `export { buildDetailedCodeExplanation } from ${JSON.stringify(path.join(root, 'services/aiCodeExplanation.ts'))};`,
  `export { splitAiReviewSteps, stripAiReviewCodeExplanation } from ${JSON.stringify(path.join(root, 'services/aiReviewFormatting.ts'))};`,
].join('\n'));

try {
  buildSync({
    entryPoints: [entry],
    outfile: bundleFile,
    bundle: true,
    platform: 'node',
    format: 'cjs',
    logLevel: 'silent',
  });
  const { EXERCISES, buildDetailedCodeExplanation, splitAiReviewSteps, stripAiReviewCodeExplanation } = require(bundleFile);
  const failures = [];

  for (const exercise of EXERCISES) {
    const explanation = buildDetailedCodeExplanation('', exercise.solution, 'en');
    if (!explanation.includes('```python')) failures.push(`Problem ${exercise.id}: missing highlighted Python block`);
    if (!explanation.includes('So this function is doing these things:')) failures.push(`Problem ${exercise.id}: missing expanded final summary`);
    if (!/# (This|The|Python|print|return|pass|Example|Data|So)/.test(explanation)) failures.push(`Problem ${exercise.id}: missing line-specific comments`);
    if (explanation.split('\n').length > 200) failures.push(`Problem ${exercise.id}: explanation is unbounded`);
  }

  const problem975 = EXERCISES.find(exercise => exercise.id === 975);
  const explanation975 = buildDetailedCodeExplanation('', problem975.solution, 'en');
  for (const fragment of [
    'This function takes one string containing numbers separated by commas.',
    '# Example input:',
    '# "10,20,30,40"',
    'splits the one big string wherever it finds',
    '# into:',
    '# ["10", "20", "30", "40"]',
    'int("10") -> 10',
    'list(...) collects all the converted integers into one list.',
    'The full transformation looks like this:',
    '"10" is a string.',
    '"10" + "10" gives "1010"',
    'So this function is doing these things:',
  ]) {
    if (!explanation975.includes(fragment)) failures.push(`Problem 975 regression: missing ${JSON.stringify(fragment)}`);
  }

  const french975 = buildDetailedCodeExplanation('', problem975.solution, 'fr');
  for (const fragment of ['Explication du code', 'Cela transforme', 'Cette solution effectue les étapes suivantes']) {
    if (!french975.includes(fragment)) failures.push(`Problem 975 French regression: missing ${JSON.stringify(fragment)}`);
  }

  const formattedSections = splitAiReviewSteps([
    '1. Problem requirement: parse comma-separated integers.',
    '',
    explanation975,
    '',
    '5. Solution workflow: return the converted list.',
  ].join('\n'));
  const codePanels = formattedSections.filter(section => section.includes('```python'));
  if (codePanels.length !== 1) failures.push(`Formatting regression: expected one code panel, got ${codePanels.length}`);
  if (!codePanels[0]?.includes('# ["10", "20", "30", "40"]')) failures.push('Formatting regression: concrete walkthrough escaped the Code Explanation panel');
  if (formattedSections.some(section => ((section.match(/```/g) || []).length % 2) !== 0)) failures.push('Formatting regression: a Python fence was split across panels');

  const modelReview = [
    '1. Problem requirement: parse comma-separated integers.',
    '',
    '2. Code explanation: part 1: split handles text. part 2: map changes values.',
    '',
    '3. Output analysis: Correct.',
    '',
    '4. Local model notes: the answer passes.',
  ].join('\n');
  const strippedReview = stripAiReviewCodeExplanation(modelReview);
  if (strippedReview.includes('Code explanation')) failures.push('Dedicated panel regression: model Code Explanation heading was not removed');
  if (strippedReview.includes('part 1: split handles text')) failures.push('Dedicated panel regression: generic part 1 / part 2 content was not removed');
  if (!explanation975.includes('The full transformation looks like this:')) failures.push('Dedicated panel regression: detailed standalone explanation is incomplete');

  console.log('AI Review code-explanation evaluation');
  console.log(`Exercises evaluated: ${EXERCISES.length}`);
  console.log('Problem 975 concrete transformation: checked');
  console.log('French explanation: checked');
  console.log('Numbered panel formatting: checked');
  console.log('Authoritative Code Explanation panel: checked');
  if (failures.length) {
    console.error(`Failures (${failures.length}):`);
    failures.slice(0, 100).forEach(failure => console.error(`- ${failure}`));
    process.exitCode = 1;
  } else {
    console.log('Result: passed');
  }
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
