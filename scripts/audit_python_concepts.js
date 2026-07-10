#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'python-concept-audit-'));
const conceptBundle = path.join(tempDir, 'concepts.cjs');
const referenceBundle = path.join(tempDir, 'reference.cjs');
const localizationBundle = path.join(tempDir, 'localization.cjs');
const modeBundle = path.join(tempDir, 'mode.cjs');

try {
  buildSync({
    entryPoints: [path.join(root, 'services/pythonConceptLibrary.ts')],
    outfile: conceptBundle,
    bundle: true,
    platform: 'node',
    format: 'cjs',
    logLevel: 'silent',
  });
  buildSync({
    entryPoints: [path.join(root, 'services/pythonReference.ts')],
    outfile: referenceBundle,
    bundle: true,
    platform: 'node',
    format: 'cjs',
    logLevel: 'silent',
  });
  buildSync({
    entryPoints: [path.join(root, 'services/aiLocalization.ts')],
    outfile: localizationBundle,
    bundle: true,
    platform: 'node',
    format: 'cjs',
    logLevel: 'silent',
  });
  buildSync({
    entryPoints: [path.join(root, 'services/generalAiMode.ts')],
    outfile: modeBundle,
    bundle: true,
    platform: 'node',
    format: 'cjs',
    logLevel: 'silent',
  });

  const concepts = require(conceptBundle);
  const reference = require(referenceBundle);
  const localization = require(localizationBundle);
  const modes = require(modeBundle);
  const coverage = concepts.getConceptCoverage();
  const terms = concepts.getAllConceptTerms();
  const failures = [];

  if (coverage.missing.length > 0) {
    failures.push(`Missing catalog lookups: ${coverage.missing.slice(0, 20).join(', ')}`);
  }

  for (const term of terms) {
    const bareAnswer = reference.answerGeneralPythonQuestion(term);
    if (!bareAnswer || bareAnswer.trim().length < 20) {
      failures.push(`Bare definition failed: ${JSON.stringify(term)}`);
    }

    if (/^[a-z][a-z0-9_. +\-/]*$/i.test(term)) {
      const questionAnswer = reference.answerGeneralPythonQuestion(`what is ${term}?`);
      if (!questionAnswer || questionAnswer.trim().length < 20) {
        failures.push(`Question definition failed: ${JSON.stringify(term)}`);
      }
    }

    if (failures.length >= 50) break;
  }

  const expectations = [
    ['what is len?', ['len(s)', 'number of items']],
    ['define append', ['list.append(x)', 'returns none']],
    ['what does list count method do?', ['list.count(x)', 'number of times']],
    ['what does string count method do?', ['str.count(', 'occurrences']],
    ['what is csv?', ['**csv**', 'comma-separated value']],
    ['what is threading?', ['**threading**', 'creating and coordinating threads']],
    ['what is xgboost?', ['**xgboost**', 'gradient-boosted decision trees']],
    ['what is is?', ['keyword', 'identity comparison']],
  ];

  for (const [question, fragments] of expectations) {
    const answer = (reference.answerGeneralPythonQuestion(question) || '').toLowerCase();
    for (const fragment of fragments) {
      if (!answer.includes(fragment.toLowerCase())) {
        failures.push(`${JSON.stringify(question)} is missing ${JSON.stringify(fragment)}`);
      }
    }
  }

  const frenchQueries = [
    ["Qu'est-ce que len ?", 'what is len ?'],
    ["Qu'est-ce que le len ?", 'what is len ?'],
    ["Qu'est-ce qu'une liste ?", 'what is a list data type ?'],
    ['Qu’est-ce que threading ?', 'what is threading ?'],
  ];
  for (const [question, expected] of frenchQueries) {
    const actual = localization.normalizeAiQuestionForLookup(question, 'fr');
    if (actual !== expected) failures.push(`French lookup normalization failed: ${JSON.stringify(question)} -> ${JSON.stringify(actual)}`);
  }

  const modeFixture = '**topic**\n\nA concise definition.\n\n**Deep context:** details that Simple mode must remove.\n\n```python\nprint("example")\n```';
  const simpleMode = modes.composeGeneralAiAnswer({ answer: modeFixture, topic: 'topic', mode: 'simple', language: 'en' });
  const deepMode = modes.composeGeneralAiAnswer({ answer: modeFixture, topic: 'topic', mode: 'deep', language: 'en' });
  if (simpleMode.includes('Deep context')) failures.push('Simple mode retained deep context');
  if (!simpleMode.includes('print("example")')) failures.push('Simple mode removed the first small example');
  if (!deepMode.includes('In-depth analysis')) failures.push('Deep mode did not add in-depth analysis');

  console.log('Python concept coverage audit');
  console.log(`Catalog terms: ${coverage.total}`);
  console.log(`Full hand-written entries or aliases: ${coverage.entries}`);
  console.log(`Term-specific categorized definitions: ${coverage.categoryFallbacks}`);
  console.log(`Missing lookups: ${coverage.missing.length}`);

  if (failures.length > 0) {
    console.error('\nFailures:');
    for (const failure of failures) console.error(`- ${failure}`);
    process.exitCode = 1;
  } else {
    console.log('Definition query variants: passed');
    console.log('Priority and parser regressions: passed');
    console.log('French query normalization: passed');
    console.log('Simple and deep mode contracts: passed');
  }
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
