#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { spawnSync } = require('child_process');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'foundation-intermediate-audit-'));
const entry = path.join(tempDir, 'entry.ts');
const bundle = path.join(tempDir, 'bundle.cjs');
const expectedCounts = {
  Indexing: 100,
  'String Method': 100,
  'List Method': 100,
  'Dictionary Method': 100,
  'Print vs Return': 100,
  'Function Argument': 100,
  'Boolean Logic': 100,
  'Input Parsing': 100,
  'Range Practice': 100,
  'Basic Validation': 100,
  'Enumerate & Zip': 100,
  'Searching & Counting': 100,
  'Nested Collection': 100,
  'Sorting Key': 100,
  'String Parsing': 100,
  'Accumulation Pattern': 100,
  'Filtering & Transformation': 100,
  'Early Exit': 100,
  'Multiple Return Value': 100,
  'Data Cleaning': 100,
};

fs.writeFileSync(entry, [
  `export { FOUNDATION_INTERMEDIATE_EXERCISES } from ${JSON.stringify(path.join(root, 'foundationIntermediateExercises.ts'))};`,
  `export { FOUNDATION_INTERMEDIATE_GRADERS } from ${JSON.stringify(path.join(root, 'foundationIntermediateGraders.ts'))};`,
  `export { FOUNDATION_INTERMEDIATE_FR } from ${JSON.stringify(path.join(root, 'services/foundationIntermediateFr.ts'))};`,
].join('\n'));

try {
  buildSync({ entryPoints: [entry], outfile: bundle, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const {
    FOUNDATION_INTERMEDIATE_EXERCISES: exercises,
    FOUNDATION_INTERMEDIATE_GRADERS: graders,
    FOUNDATION_INTERMEDIATE_FR: french,
  } = require(bundle);
  const failures = [];
  const expectedIds = Array.from({ length: 2000 }, (_, index) => 3658 + index);
  if (exercises.length !== 2000) failures.push(`expected 2000 exercises, found ${exercises.length}`);
  if (JSON.stringify(exercises.map(item => item.id)) !== JSON.stringify(expectedIds)) failures.push('IDs are not exactly 3658-5657');

  const normalizedPrompts = exercises.map(item => item.description.split('\n')[0].toLowerCase().replace(/`[^`]+`/g, '<function>').replace(/\s+/g, ' ').trim());
  const promptOwners = new Map();
  normalizedPrompts.forEach((prompt, index) => {
    if (promptOwners.has(prompt)) failures.push(`duplicate normalized prompt: ${exercises[promptOwners.get(prompt)].id} and ${exercises[index].id}`);
    else promptOwners.set(prompt, index);
  });

  for (const [concept, count] of Object.entries(expectedCounts)) {
    const matching = exercises.filter(item => item.category.startsWith(`${concept} `));
    if (matching.length !== count) failures.push(`${concept}: expected ${count}, found ${matching.length}`);
    if (!matching.some(item => item.category.endsWith(' Easy'))) failures.push(`${concept}: missing Easy exercises`);
    if (!matching.some(item => item.category.endsWith(' Intermediate'))) failures.push(`${concept}: missing Intermediate exercises`);
    if (matching.some(item => item.category.endsWith(' Difficult'))) failures.push(`${concept}: unexpected Difficult exercise`);
  }

  const executionPayload = [];
  for (const exercise of exercises) {
    const grader = graders[exercise.id];
    const localized = french[exercise.id];
    if (!grader || grader.tests?.length !== 3) failures.push(`${exercise.id}: grader must have exactly three hidden tests`);
    if (!localized?.description || !localized?.hint || !localized?.breakdown) failures.push(`${exercise.id}: French content incomplete`);
    for (let example = 1; example <= 5; example += 1) {
      if (!exercise.solution.includes(`# Example ${example}:`)) failures.push(`${exercise.id}: Example ${example} missing`);
    }
    const sourceMatch = exercise.solution.match(/^(?:#.*\n)+(?<source>def\s+[A-Za-z_]\w*\([^)]*\):[\s\S]*?)(?=\n\nprint\()/);
    if (!sourceMatch?.groups?.source) failures.push(`${exercise.id}: canonical solution could not be extracted`);
    else if (grader) executionPayload.push({ id: exercise.id, source: sourceMatch.groups.source, name: grader.functionNames[0], tests: grader.tests });
  }

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
            actual = normalize(function(*test.get("args", []), **test.get("kwargs", {})))
            expected = normalize(test["expected"])
            if actual != expected:
                failures.append(f'{item["id"]} test {index + 1}: {actual!r} != {expected!r}')
    except Exception as exc:
        failures.append(f'{item["id"]}: {type(exc).__name__}: {exc}')
print(json.dumps(failures))
`;
  const run = spawnSync('python3', ['-c', pythonAudit], { input: JSON.stringify(executionPayload), encoding: 'utf8', maxBuffer: 100 * 1024 * 1024 });
  if (run.status !== 0) failures.push(`Python execution audit crashed: ${run.stderr.trim()}`);
  else failures.push(...JSON.parse(run.stdout || '[]'));

  console.log('Foundation/intermediate practice audit');
  console.log(`Exercises: ${exercises.length}`);
  console.log(`Counts: ${JSON.stringify(Object.fromEntries(Object.keys(expectedCounts).map(concept => [concept, exercises.filter(item => item.category.startsWith(`${concept} `)).length])))}`);
  console.log(`Graders: ${Object.keys(graders).length}`);
  console.log(`French records: ${Object.keys(french).length}`);
  console.log(`Canonical solutions executed: ${executionPayload.length * 3}`);
  if (failures.length) {
    failures.slice(0, 150).forEach(failure => console.error(`- ${failure}`));
    console.error(`Total failures: ${failures.length}`);
    process.exitCode = 1;
  } else {
    console.log('Result: passed');
  }
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
