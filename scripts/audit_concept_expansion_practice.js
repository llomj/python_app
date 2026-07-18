#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'concept-expansion-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'bundle.cjs');
const expectedCounts = {
  Comprehension: 60,
  'For Loop': 50,
  Generator: 50,
  Recursion: 60,
  Closure: 42,
  Slicing: 50,
  Regex: 15,
};
const requiredNodes = {
  Comprehension: ['ListComp', 'DictComp'],
  'For Loop': ['For'],
  Generator: ['Yield'],
  Recursion: ['If'],
  Closure: ['FunctionDef'],
  Slicing: ['Slice'],
};

fs.writeFileSync(entry, [
  `export { CONCEPT_EXPANSION_EXERCISES } from ${JSON.stringify(path.join(root, 'conceptExpansionExercises.ts'))};`,
  `export { CONCEPT_EXPANSION_GRADERS } from ${JSON.stringify(path.join(root, 'conceptExpansionGraders.ts'))};`,
  `export { CONCEPT_EXPANSION_FR } from ${JSON.stringify(path.join(root, 'services/conceptExpansionFr.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const {
    CONCEPT_EXPANSION_EXERCISES: exercises,
    CONCEPT_EXPANSION_GRADERS: graders,
    CONCEPT_EXPANSION_FR: french,
  } = require(bundle);
  const failures = [];
  const expectedIds = Array.from({ length: 327 }, (_, index) => 2481 + index);
  if (exercises.length !== 327) failures.push(`expected 327 exercises, found ${exercises.length}`);
  if (JSON.stringify(exercises.map(item => item.id)) !== JSON.stringify(expectedIds)) failures.push('IDs are not exactly 2481-2807');
  const prompts = exercises.map(item => item.description.split('\n')[0].toLowerCase().replace(/`[^`]+`/g, '<function>'));
  if (new Set(prompts).size !== prompts.length) failures.push('duplicate normalized English prompts found');

  for (const [concept, count] of Object.entries(expectedCounts)) {
    const matching = exercises.filter(item => item.category.startsWith(`${concept} `));
    if (matching.length !== count) failures.push(`${concept}: expected ${count}, found ${matching.length}`);
    for (const level of ['Easy', 'Intermediate', 'Difficult']) {
      if (!matching.some(item => item.category === `${concept} ${level}`)) failures.push(`${concept}: missing ${level} exercises`);
    }
  }

  for (const exercise of exercises) {
    const concept = Object.keys(expectedCounts).find(name => exercise.category.startsWith(`${name} `));
    const grader = graders[exercise.id];
    const localized = french[exercise.id];
    if (!concept) failures.push(`${exercise.id}: unknown category ${exercise.category}`);
    if (!grader || grader.tests?.length !== 3) failures.push(`${exercise.id}: grader must contain exactly three hidden cases`);
    if (!localized?.description || !localized?.hint || !localized?.breakdown) failures.push(`${exercise.id}: incomplete French content`);
    if (!exercise.solution.includes('# Example 5: direct call')) failures.push(`${exercise.id}: five solution examples missing`);
    if (!/^def\s+[A-Za-z_]\w*\([^)]*\):/m.test(exercise.solution)) failures.push(`${exercise.id}: canonical function missing`);
    if (concept === 'Regex') {
      if (!grader?.requiredAnyCallPatterns?.length) failures.push(`${exercise.id}: regex call requirement missing`);
    } else if (concept === 'Recursion') {
      const name = grader?.functionNames?.[0];
      if (!grader?.requiredCallPatterns?.some(item => item.functionName === name)) failures.push(`${exercise.id}: recursive self-call requirement missing`);
    } else {
      const accepted = requiredNodes[concept] || [];
      if (!grader?.requiredNodePatterns?.some(item => accepted.includes(item.nodeType))) failures.push(`${exercise.id}: ${concept} AST requirement missing`);
    }
  }

  console.log('Concept expansion audit');
  console.log(`Exercises: ${exercises.length}`);
  console.log(`Counts: ${JSON.stringify(Object.fromEntries(Object.keys(expectedCounts).map(concept => [concept, exercises.filter(item => item.category.startsWith(`${concept} `)).length])))}`);
  console.log(`Graders: ${Object.keys(graders).length}`);
  console.log(`French records: ${Object.keys(french).length}`);
  if (failures.length) {
    failures.slice(0, 100).forEach(failure => console.error(`- ${failure}`));
    process.exitCode = 1;
  } else {
    console.log('Result: passed');
  }
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
