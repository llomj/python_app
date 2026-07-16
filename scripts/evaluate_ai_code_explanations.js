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
  `export { splitAiReviewSteps } from ${JSON.stringify(path.join(root, 'services/aiReviewFormatting.ts'))};`,
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
  const { EXERCISES, buildDetailedCodeExplanation, splitAiReviewSteps } = require(bundleFile);
  const failures = [];

  for (const exercise of EXERCISES) {
    const explanation = buildDetailedCodeExplanation('', exercise.solution, 'en');
    if (!explanation.includes('```python')) failures.push(`Problem ${exercise.id}: missing highlighted Python block`);
    if (!explanation.includes('Workflow summary:')) failures.push(`Problem ${exercise.id}: missing workflow summary`);
    if (!/# (This|The|Python|`|Workflow|Example|Data)/.test(explanation)) failures.push(`Problem ${exercise.id}: missing line-specific comments`);
    if (explanation.split('\n').length > 120) failures.push(`Problem ${exercise.id}: explanation is unbounded`);
  }

  const problem975 = EXERCISES.find(exercise => exercise.id === 975);
  const explanation975 = buildDetailedCodeExplanation('', problem975.solution, 'en');
  for (const fragment of [
    'splits one large string wherever it finds',
    'After split: ["10", "20", "30", "40"]',
    'int("10") -> 10',
    '`list(...)` collects the produced values',
    'The important difference: `"10"` is text, while `10` is an integer.',
  ]) {
    if (!explanation975.includes(fragment)) failures.push(`Problem 975 regression: missing ${JSON.stringify(fragment)}`);
  }

  const french975 = buildDetailedCodeExplanation('', problem975.solution, 'fr');
  for (const fragment of ['Explication du code', 'Après split', 'Résumé du déroulement']) {
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
  if (!codePanels[0]?.includes('After split: ["10", "20", "30", "40"]')) failures.push('Formatting regression: concrete walkthrough escaped the Code Explanation panel');
  if (formattedSections.some(section => ((section.match(/```/g) || []).length % 2) !== 0)) failures.push('Formatting regression: a Python fence was split across panels');

  console.log('AI Review code-explanation evaluation');
  console.log(`Exercises evaluated: ${EXERCISES.length}`);
  console.log('Problem 975 concrete transformation: checked');
  console.log('French explanation: checked');
  console.log('Numbered panel formatting: checked');
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
