#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { spawnSync } = require('child_process');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'advanced-concept-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'bundle.cjs');
const expectedCounts = {
  Decorator: 50,
  Iterator: 50,
  'Context Manager': 50,
  Dataclass: 50,
  'Magic Method': 50,
  'Bitwise Operation': 50,
};

fs.writeFileSync(entry, [
  `export { ADVANCED_CONCEPT_EXERCISES } from ${JSON.stringify(path.join(root, 'advancedConceptExercises.ts'))};`,
  `export { ADVANCED_CONCEPT_GRADERS } from ${JSON.stringify(path.join(root, 'advancedConceptGraders.ts'))};`,
  `export { ADVANCED_CONCEPT_FR } from ${JSON.stringify(path.join(root, 'services/advancedConceptFr.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const {
    ADVANCED_CONCEPT_EXERCISES: exercises,
    ADVANCED_CONCEPT_GRADERS: graders,
    ADVANCED_CONCEPT_FR: french,
  } = require(bundle);
  const failures = [];
  const expectedIds = Array.from({ length: 300 }, (_, index) => 2808 + index);
  if (exercises.length !== 300) failures.push(`expected 300 exercises, found ${exercises.length}`);
  if (JSON.stringify(exercises.map(item => item.id)) !== JSON.stringify(expectedIds)) failures.push('IDs are not exactly 2808-3107');
  const prompts = exercises.map(item => item.description.split('\n')[0].toLowerCase());
  if (new Set(prompts).size !== prompts.length) failures.push('duplicate English prompts found');

  for (const [concept, count] of Object.entries(expectedCounts)) {
    const matching = exercises.filter(item => item.category.startsWith(`${concept} `));
    if (matching.length !== count) failures.push(`${concept}: expected ${count}, found ${matching.length}`);
    for (const level of ['Easy', 'Intermediate', 'Difficult']) {
      if (!matching.some(item => item.category === `${concept} ${level}`)) failures.push(`${concept}: missing ${level}`);
    }
  }

  const executionPayload = [];
  for (const exercise of exercises) {
    const grader = graders[exercise.id];
    const localized = french[exercise.id];
    if (!grader || grader.tests?.length !== 3) failures.push(`${exercise.id}: grader must have three tests`);
    if (!localized?.description || !localized?.hint || !localized?.breakdown) failures.push(`${exercise.id}: French content incomplete`);
    for (let example = 1; example <= 5; example += 1) {
      if (!exercise.solution.includes(`# Example ${example}:`)) failures.push(`${exercise.id}: Example ${example} missing`);
    }
    const sourceMatch = exercise.solution.match(/^(?:#.*\n)+(?<source>def\s+[A-Za-z_]\w*\([^)]*\):[\s\S]*?)(?=\n\nprint\()/);
    if (!sourceMatch?.groups?.source) {
      failures.push(`${exercise.id}: canonical solution could not be extracted`);
    } else if (grader) {
      executionPayload.push({ id: exercise.id, source: sourceMatch.groups.source, name: grader.functionNames[0], tests: grader.tests });
    }

    const concept = Object.keys(expectedCounts).find(name => exercise.category.startsWith(`${name} `));
    if (concept === 'Decorator' && !grader?.requiredDecorators?.length) failures.push(`${exercise.id}: decorator requirement missing`);
    if (concept === 'Iterator' && grader?.requiredCallPatterns?.length !== 2) failures.push(`${exercise.id}: iter()/next() requirements missing`);
    if (concept === 'Context Manager' && !grader?.requiredDefinedFunctions?.includes('__exit__')) failures.push(`${exercise.id}: context protocol requirement missing`);
    if (concept === 'Dataclass' && !grader?.requiredDecorators?.includes('dataclass')) failures.push(`${exercise.id}: dataclass requirement missing`);
    if (concept === 'Magic Method' && !grader?.requiredDefinedFunctions?.some(name => /^__.+__$/.test(name))) failures.push(`${exercise.id}: magic-method requirement missing`);
    if (concept === 'Bitwise Operation' && !grader?.requiredAstOperators?.length) failures.push(`${exercise.id}: bitwise operator requirement missing`);
  }

  if (executionPayload.length) {
    const pythonAudit = `
import json, sys

def normalize(value):
    if isinstance(value, tuple):
        return [normalize(item) for item in value]
    if isinstance(value, list):
        return [normalize(item) for item in value]
    if isinstance(value, dict):
        return {str(key): normalize(item) for key, item in value.items()}
    return value

payload = json.load(sys.stdin)
failures = []
for item in payload:
    try:
        namespace = {}
        exec(item["source"], namespace)
        function = namespace[item["name"]]
        for index, test in enumerate(item["tests"]):
            actual = normalize(function(*test["args"]))
            expected = normalize(test["expected"])
            if actual != expected:
                failures.append(f'{item["id"]} test {index + 1}: {actual!r} != {expected!r}')
    except Exception as exc:
        failures.append(f'{item["id"]}: {type(exc).__name__}: {exc}')
print(json.dumps(failures))
`;
    const run = spawnSync('python3', ['-c', pythonAudit], { input: JSON.stringify(executionPayload), encoding: 'utf8', maxBuffer: 20 * 1024 * 1024 });
    if (run.status !== 0) failures.push(`Python execution audit crashed: ${run.stderr.trim()}`);
    else failures.push(...JSON.parse(run.stdout || '[]'));
  }

  console.log('Advanced concept practice audit');
  console.log(`Exercises: ${exercises.length}`);
  console.log(`Counts: ${JSON.stringify(Object.fromEntries(Object.keys(expectedCounts).map(concept => [concept, exercises.filter(item => item.category.startsWith(`${concept} `)).length])))}`);
  console.log(`Graders: ${Object.keys(graders).length}`);
  console.log(`French records: ${Object.keys(french).length}`);
  console.log(`Canonical solutions executed: ${executionPayload.length * 3}`);
  if (failures.length) {
    failures.slice(0, 100).forEach(failure => console.error(`- ${failure}`));
    process.exitCode = 1;
  } else {
    console.log('Result: passed');
  }
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
