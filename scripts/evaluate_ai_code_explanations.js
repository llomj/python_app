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
    if (!explanation.includes('Complete value path for the shown example:')) failures.push(`Problem ${exercise.id}: missing complete value path`);
    if (!explanation.includes('# Operation:')) failures.push(`Problem ${exercise.id}: missing operation trace`);
    if (!explanation.includes('# Intermediate value and type:')) failures.push(`Problem ${exercise.id}: missing intermediate values and data types`);
    if (/\w+\s*\(/.test(exercise.solution) && !explanation.includes('Module, function, and method breakdown:')) failures.push(`Problem ${exercise.id}: missing callable semantics breakdown`);
    if (explanation.split('\n').some(line => line.trim() === '#')) failures.push(`Problem ${exercise.id}: contains a clutter-only hash line`);
    if (explanation.includes('\n\n\n')) failures.push(`Problem ${exercise.id}: contains excessive blank-line spacing`);
    if (explanation.split('\n').length > 280) failures.push(`Problem ${exercise.id}: explanation is unbounded`);

    const french = buildDetailedCodeExplanation('', exercise.solution, 'fr');
    if (!french.includes('Trajet complet des valeurs pour l’exemple affiché :')) failures.push(`Problem ${exercise.id}: missing French value path`);
    if (/\w+\s*\(/.test(exercise.solution) && !french.includes('Détail des modules, fonctions et méthodes :')) failures.push(`Problem ${exercise.id}: missing French callable semantics breakdown`);
    if (!french.includes('# Valeur intermédiaire et type :') && !french.includes('# Valeur intermédiaire et type:')) failures.push(`Problem ${exercise.id}: missing French value/type trace`);
    if (french.split('\n').some(line => line.trim() === '#')) failures.push(`Problem ${exercise.id}: French explanation contains a clutter-only hash line`);
    if (french.includes('\n\n\n')) failures.push(`Problem ${exercise.id}: French explanation contains excessive blank-line spacing`);
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

  const concreteCases = [
    [1, 'returned value = 10 (int)'],
    [8, 'returned value = 81 (int)'],
    [550, 'returned value = 1 (int)'],
    [869, 'first, second, third = [1, 2, 3] (list)'],
    [1006, 'returned value = "ab" (str)'],
    [1211, 'returned value = 60 (int)'],
    [1410, 'returned value = "Python is great" (str)'],
    [1725, 'returned value = True (bool)'],
    [1900, 'returned value = 25 (int)'],
  ];
  for (const [id, fragment] of concreteCases) {
    const exercise = EXERCISES.find(item => item.id === id);
    const explanation = buildDetailedCodeExplanation('', exercise.solution, 'en');
    if (!explanation.includes(fragment)) failures.push(`Problem ${id} concrete trace regression: missing ${JSON.stringify(fragment)}`);
  }

  const explanation1699 = buildDetailedCodeExplanation('', EXERCISES.find(item => item.id === 1699).solution, 'en');
  if (!explanation1699.includes('printed output = "True False" (display text)')) failures.push('Problem 1699 multi-call trace did not evaluate each argument independently');

  const explanation1179 = buildDetailedCodeExplanation('', EXERCISES.find(item => item.id === 1179).solution, 'en');
  for (const fragment of [
    '`datetime` is the imported module',
    '`datetime.datetime` is the `datetime` class stored inside that module',
    'the second `datetime` is not a method',
    '`now` is a class method of the `datetime` class',
    'Left-to-right resolution: find the `datetime` module',
    'Call order: Python resolves `datetime.datetime.now` first',
  ]) {
    if (!explanation1179.includes(fragment)) failures.push(`Problem 1179 callable semantics regression: missing ${JSON.stringify(fragment)}`);
  }

  const nestedCalls = buildDetailedCodeExplanation([
    'def convert_all(values):',
    '    return list(map(int, values))',
    '',
    'print(sum(convert_all(["1", "2", "3"])))',
  ].join('\n'), '', 'en');
  for (const fragment of [
    'Built-in function: map(function, iterable, ...)',
    'The first argument is the function to apply; the second is the iterable supplying items.',
    'Nested call:',
    'must finish before the outer call can begin.',
    'At the call, Python binds arguments to values',
  ]) {
    if (!nestedCalls.includes(fragment)) failures.push(`Nested-call semantics regression: missing ${JSON.stringify(fragment)}`);
  }

  const importedAlias = buildDetailedCodeExplanation([
    'from datetime import datetime as DateTime',
    'print(DateTime.now())',
  ].join('\n'), '', 'en');
  if (!importedAlias.includes('`DateTime` is the local name for `datetime`, imported from the `datetime` module')) failures.push('Imported-alias semantics regression: imported class was not identified');
  if (!importedAlias.includes('`DateTime` is the `datetime` class and `now` is its class method')) failures.push('Imported-alias semantics regression: class method was not identified');

  const nestedHelper = buildDetailedCodeExplanation([
    'def outer(value):',
    '    def helper(item):',
    '        return item * 2',
    '    return helper(value)',
    '',
    'print(outer(3))',
  ].join('\n'), '', 'en');
  if (!nestedHelper.includes('a nested helper created while outer is running')) failures.push('Nested-helper semantics regression: nested scope was not explained');

  const french1179 = buildDetailedCodeExplanation('', EXERCISES.find(item => item.id === 1179).solution, 'fr');
  if (!french1179.includes('le second `datetime` n’est pas une méthode')) failures.push('Problem 1179 French semantics regression: class/module distinction missing');

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
    '4. Expected solution workflow: step 1 def, step 2 return.',
    '',
    '5. Execution order: define, call, return.',
    '',
    '4. Local model notes: the answer passes.',
  ].join('\n');
  const strippedReview = stripAiReviewCodeExplanation(modelReview);
  if (strippedReview.includes('Code explanation')) failures.push('Dedicated panel regression: model Code Explanation heading was not removed');
  if (strippedReview.includes('part 1: split handles text')) failures.push('Dedicated panel regression: generic part 1 / part 2 content was not removed');
  if (strippedReview.includes('Expected solution workflow') || strippedReview.includes('Execution order')) failures.push('Dedicated panel regression: redundant two-line teaching cards were not removed');
  if (!explanation975.includes('The full transformation looks like this:')) failures.push('Dedicated panel regression: detailed standalone explanation is incomplete');

  console.log('AI Review code-explanation evaluation');
  console.log(`Exercises evaluated: ${EXERCISES.length}`);
  console.log('Problem 975 concrete transformation: checked');
  console.log('French explanation: checked');
  console.log('Universal value/type traces: checked');
  console.log('Numbered panel formatting: checked');
  console.log('Authoritative Code Explanation panel: checked');
  console.log('Callable/module/helper semantics: checked');
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
