#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'problem-ai-eval-'));
const bundleFile = path.join(tempDir, 'problem-ai-eval.cjs');

const entry = path.join(tempDir, 'entry.ts');
fs.writeFileSync(entry, [
  `export { EXERCISES } from ${JSON.stringify(path.join(root, 'exercises.ts'))};`,
  `export { AUTO_GRADERS } from ${JSON.stringify(path.join(root, 'graders.ts'))};`,
  `export { EXERCISES_FR } from ${JSON.stringify(path.join(root, 'services/exercisesFr.ts'))};`,
  `export { buildProblemAiTutorAnswer } from ${JSON.stringify(path.join(root, 'services/problemAiTutor.ts'))};`,
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
  const { EXERCISES, AUTO_GRADERS, EXERCISES_FR, buildProblemAiTutorAnswer } = require(bundleFile);
  const failures = [];
  const requiredHeadings = [
    'What this problem asks', 'Inputs and result', 'Key words and concepts', 'Method and function reference',
    'Syntax the grader requires', 'Reference code pattern', 'Step-by-step plan', 'Line-by-line explanation',
    'Execution flow', 'Common mistakes to avoid', 'Concrete test cases', 'Other correct ways to write it',
  ];
  const banned = [
    /your_function/i,
    /carefully identify what the problem asks/i,
    /break the problem into input, operation/i,
    /not just copy the example output/i,
    /apply the operation described in the prompt/i,
  ];
  let grounded = 0;
  let structural = 0;
  let callableRequirements = 0;

  for (const exercise of EXERCISES) {
    const grader = AUTO_GRADERS[exercise.id] || null;
    const answer = buildProblemAiTutorAnswer({
      exercise,
      description: exercise.description,
      grader,
      language: 'en',
      question: 'Explain this problem.',
    });
    const missingHeading = requiredHeadings.find(heading => !answer.includes(heading));
    if (missingHeading) failures.push(`Problem ${exercise.id}: missing ${missingHeading}`);
    if (answer.length < 1100) failures.push(`Problem ${exercise.id}: explanation too short (${answer.length})`);
    const bannedPattern = banned.find(pattern => pattern.test(answer));
    if (bannedPattern) failures.push(`Problem ${exercise.id}: generic banned wording ${bannedPattern}`);
    const referenceCode = answer.match(/\*\*6\. Reference code pattern\*\*\n```python\n([\s\S]*?)```/)?.[1] || '';
    const topLevelDefinitions = [...referenceCode.matchAll(/^(?:def|class)\s+([A-Za-z_]\w*)/gm)].map(match => match[1]);
    if (new Set(topLevelDefinitions).size !== topLevelDefinitions.length) failures.push(`Problem ${exercise.id}: duplicate top-level definition leaked into reference code`);

    const promptLine = exercise.description.split('\n').find(line => line.trim()) || '';
    const promptWords = (promptLine.toLowerCase().match(/[a-z_]{5,}/g) || [])
      .filter(word => !['write', 'python', 'program', 'function', 'called', 'takes', 'input', 'returns'].includes(word));
    if (promptWords.some(word => answer.toLowerCase().includes(word))) grounded += 1;
    else failures.push(`Problem ${exercise.id}: answer is not grounded in prompt terminology`);

    const requiredNodes = grader?.requiredNodePatterns || [];
    if (!requiredNodes.length || requiredNodes.some(node => answer.includes(node.nodeType === 'Starred' ? '*values' : node.nodeType === 'Lambda' ? 'lambda' : '`'))) structural += 1;
    else failures.push(`Problem ${exercise.id}: structural grader requirement is not explained`);

    const requiredCalls = grader?.requiredCallPatterns || [];
    if (!requiredCalls.length || requiredCalls.slice(0, 6).every(call => answer.includes(call.functionName))) callableRequirements += 1;
    else failures.push(`Problem ${exercise.id}: required callable is not explained`);
  }

  const exercise898 = EXERCISES.find(exercise => exercise.id === 898);
  const answer898 = buildProblemAiTutorAnswer({
    exercise: exercise898,
    description: exercise898.description,
    grader: AUTO_GRADERS[898],
    language: 'en',
    question: 'Explain this problem.',
  });
  for (const fragment of ['three numbers', 'lambda a, b, c: a + b + c', '*values', 'separate positional arguments', 'Result type stated by the prompt: number']) {
    if (!answer898.includes(fragment)) failures.push(`Problem 898 regression: missing ${JSON.stringify(fragment)}`);
  }
  const reference898 = answer898.match(/\*\*6\. Reference code pattern\*\*\n```python\n([\s\S]*?)```/)?.[1] || '';
  if (!/\blambda\b/.test(reference898) || !/\*[A-Za-z_]\w*/.test(reference898)) failures.push('Problem 898 reference code does not satisfy its lambda and starred-unpacking requirements');
  if (/sum\(\)|solve\(\)|your_function/.test(answer898)) failures.push('Problem 898 regression: stale unrelated breakdown leaked into answer');

  const exercise1287 = EXERCISES.find(exercise => exercise.id === 1287);
  const answer1287 = buildProblemAiTutorAnswer({ exercise: exercise1287, description: exercise1287.description, grader: AUTO_GRADERS[1287], language: 'en' });
  for (const fragment of [
    '`text.isalpha()`', '`text.isdigit()`', 'must be a string (`str`)', 'Combine the two Booleans with `or`',
    '`or` short-circuits', '`text.isalnum()` is not equivalent', '`input value(s): "abc"` → `true`',
    '`input value(s): "abc123"` → `false`',
  ]) {
    if (!answer1287.includes(fragment)) failures.push(`Problem 1287 method regression: missing ${JSON.stringify(fragment)}`);
  }

  const exercise191 = EXERCISES.find(exercise => exercise.id === 191);
  const answer191 = buildProblemAiTutorAnswer({ exercise: exercise191, description: exercise191.description, grader: AUTO_GRADERS[191], language: 'en' });
  if (!answer191.includes('Result type stated by the prompt: number') || answer191.includes('Expected result type: string')) {
    failures.push('Prompt-declared output type did not override legacy grader serialization for Problem 191');
  }

  const french898 = { ...exercise898, description: EXERCISES_FR[898] || exercise898.description };
  const frenchAnswer = buildProblemAiTutorAnswer({
    exercise: french898,
    description: french898.description,
    grader: AUTO_GRADERS[898],
    language: 'fr',
    question: 'Explique ce problème.',
  });
  if (!frenchAnswer.includes('Ce que demande exactement le problème') || !frenchAnswer.includes('déballage étoilé') || !frenchAnswer.includes('Ordre d’exécution')) {
    failures.push('Problem 898 French tutoring regression failed');
  }
  if (frenchAnswer.includes('Votre objectif est de') || frenchAnswer.includes('évaleur')) failures.push('French Problem AI text was malformed');

  console.log('Problem AI catalog evaluation');
  console.log(`Exercises evaluated: ${EXERCISES.length}`);
  console.log(`Prompt-grounded explanations: ${grounded}`);
  console.log(`Structural requirements explained: ${structural}`);
  console.log(`Required callables explained: ${callableRequirements}`);
  console.log('Problem 898 lambda/unpacking regression: checked');
  console.log('Problem 1287 string-method/Boolean regression: checked');

  if (failures.length) {
    console.error(`\nFailures (${failures.length}):`);
    for (const failure of failures.slice(0, 100)) console.error(`- ${failure}`);
    if (failures.length > 100) console.error(`- ... ${failures.length - 100} more`);
    process.exitCode = 1;
  } else {
    console.log('Result: passed');
  }
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
