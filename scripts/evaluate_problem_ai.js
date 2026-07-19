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
  `export { FOUNDATION_INTERMEDIATE_FR } from ${JSON.stringify(path.join(root, 'services/foundationIntermediateFr.ts'))};`,
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
  const { EXERCISES, AUTO_GRADERS, EXERCISES_FR, FOUNDATION_INTERMEDIATE_FR, buildProblemAiTutorAnswer } = require(bundleFile);
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
  let foundationSpecific = 0;
  let foundationFrench = 0;

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

    if (exercise.id >= 3658 && exercise.id <= 5657) {
      const functionName = grader?.functionNames?.[0];
      const lineSection = answer.match(/\*\*8\. Line-by-line explanation\*\*\n([\s\S]*?)\n\n\*\*9\./)?.[1] || '';
      const executionSection = answer.match(/\*\*9\. Execution flow\*\*\n([\s\S]*?)\n\n\*\*10\./)?.[1] || '';
      if (!answer.includes('**Type**: function to write.')) failures.push(`Problem ${exercise.id}: generated function misclassified by Problem AI`);
      if (!functionName || !referenceCode.includes(`def ${functionName}(`)) failures.push(`Problem ${exercise.id}: canonical function is missing from reference code`);
      if (/solve_problem_|class Problem\d+Solution|# Example\s+2/i.test(referenceCode)) failures.push(`Problem ${exercise.id}: unrelated solution variation leaked into Problem AI`);
      if (/executes this statement in order|performs the operation|focus on the transformation described/i.test(answer)) failures.push(`Problem ${exercise.id}: generic explanation wording remains`);
      const canonicalBody = referenceCode.split('\n').map(line => line.trim()).filter(line => line && !line.startsWith('#') && !/^def\s+/.test(line) && !/^print\s*\(/.test(line));
      if (!canonicalBody.length || !canonicalBody.every(line => lineSection.includes(`\`${line}\``))) failures.push(`Problem ${exercise.id}: line-by-line section does not cover every canonical operation`);
      if (!canonicalBody.some(line => executionSection.includes(`\`${line}\``))) failures.push(`Problem ${exercise.id}: execution flow is not tied to canonical code`);
      for (const call of requiredCalls) {
        if (!answer.includes(`\`${call.functionName}`) && !answer.includes(`.${call.functionName}(`)) failures.push(`Problem ${exercise.id}: missing exact callable reference ${call.functionName}`);
      }
      const testCount = (answer.match(/^\- `.*` → `.*`$/gm) || []).length;
      if (testCount < 3) failures.push(`Problem ${exercise.id}: fewer than three concrete Problem AI tests (${testCount})`);
      else foundationSpecific += 1;

      const localized = FOUNDATION_INTERMEDIATE_FR[exercise.id];
      if (!localized) failures.push(`Problem ${exercise.id}: missing French Problem AI source`);
      else {
        const frenchExercise = { ...exercise, description: localized.description, hint: localized.hint, breakdown: localized.breakdown };
        const french = buildProblemAiTutorAnswer({ exercise: frenchExercise, description: localized.description, grader, language: 'fr', question: 'Explique ce problème.' });
        if (!french.includes('Ce que demande exactement le problème') || !french.includes('Explication ligne par ligne') || !french.includes('Cas de test concrets')) failures.push(`Problem ${exercise.id}: incomplete French Problem AI structure`);
        if (french.includes('What this problem asks') || french.includes('Line-by-line explanation') || french.includes('Common mistakes to avoid')) failures.push(`Problem ${exercise.id}: English heading leaked into French Problem AI`);
        if (!functionName || !french.includes(`\`${functionName}()`)) failures.push(`Problem ${exercise.id}: French answer is not grounded in its function contract`);
        else foundationFrench += 1;
      }
    }
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
  console.log(`New exercise-specific explanations: ${foundationSpecific}`);
  console.log(`New French explanations: ${foundationFrench}`);
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
