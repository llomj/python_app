#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'general-ai-eval-'));
const knowledgeBundle = path.join(tempDir, 'knowledge.cjs');
const conceptBundle = path.join(tempDir, 'concepts.cjs');
const localizationBundle = path.join(tempDir, 'localization.cjs');

const bundle = (entry, outfile) => buildSync({
  entryPoints: [path.join(root, entry)],
  outfile,
  bundle: true,
  platform: 'node',
  format: 'cjs',
  logLevel: 'silent',
});

try {
  bundle('services/pythonKnowledge.ts', knowledgeBundle);
  bundle('services/pythonConceptLibrary.ts', conceptBundle);
  bundle('services/aiLocalization.ts', localizationBundle);

  const knowledge = require(knowledgeBundle);
  const concepts = require(conceptBundle);
  const localization = require(localizationBundle);
  const failures = [];
  const terms = concepts.getAllConceptTerms();
  let structuredRecords = 0;
  let ambiguityResponses = 0;
  let definitionVariants = 0;

  for (const term of terms) {
    const resolution = knowledge.resolvePythonKnowledge(term);
    if (!resolution.record && resolution.alternatives.length === 0) {
      failures.push(`No structured record or ambiguity response for ${JSON.stringify(term)}`);
      continue;
    }
    if (resolution.record) {
      structuredRecords += 1;
      for (const field of ['canonicalName', 'kind', 'category', 'summary', 'details', 'signature', 'returns', 'raises', 'version', 'sourceUrl', 'confidence']) {
        if (!String(resolution.record[field] || '').trim()) failures.push(`Missing ${field} for ${JSON.stringify(term)}`);
      }
    } else {
      ambiguityResponses += 1;
    }

    if (/^[a-z][a-z0-9_. +\-/]*$/i.test(term)) {
      for (const prefix of ['what is', 'define', 'explain']) {
        const answer = knowledge.answerPythonKnowledgeQuestion(`${prefix} ${term}`, 'en')
          || knowledge.answerPythonKnowledgeComparison(`${prefix} ${term}`, 'en');
        if (!answer || answer.length < 40) failures.push(`${prefix} variant failed for ${JSON.stringify(term)}`);
        else definitionVariants += 1;
      }
    }
    if (failures.length >= 100) break;
  }

  const len = knowledge.resolvePythonKnowledge('len').record;
  if (!len || len.signature !== 'len(s)' || len.confidence !== 'authoritative' || !len.sourceUrl.includes('docs.python.org')) {
    failures.push('len did not resolve to an authoritative official API record');
  }

  const count = knowledge.resolvePythonKnowledge('count');
  if (count.alternatives.length !== 3) failures.push(`count ambiguity expected 3 alternatives, found ${count.alternatives.length}`);
  const countAnswer = knowledge.answerPythonKnowledgeQuestion('what is count', 'en') || '';
  if (!countAnswer.includes('Clarification needed') || !countAnswer.includes('list.count') || !countAnswer.includes('str.count')) {
    failures.push('count ambiguity did not produce a useful clarification');
  }

  const comparisonCases = [
    ['sort vs sorted', ['Sorts the list in place', 'Returns a new sorted list', 'Mutates object']],
    ['difference between list and tuple', ['list', 'tuple', 'Criterion']],
    ['compare reverse with reversed', ['Reverses the list in place', 'reverse iterator', 'Sources']],
    ['difference between dictionary and set', ['dict', 'set', 'Purpose']],
  ];
  for (const [question, fragments] of comparisonCases) {
    const answer = knowledge.answerPythonKnowledgeComparison(question, 'en') || '';
    for (const fragment of fragments) {
      if (!answer.toLowerCase().includes(fragment.toLowerCase())) failures.push(`Comparison ${JSON.stringify(question)} missing ${JSON.stringify(fragment)}`);
    }
  }

  const deepFollowUp = knowledge.resolveKnowledgeFollowUp('go deeper', 'what is len', 'normal');
  const exampleFollowUp = knowledge.resolveKnowledgeFollowUp('give another example', 'what is list', 'normal');
  const pronounFollowUp = knowledge.resolveKnowledgeFollowUp('why does it return None', 'what is list.sort', 'normal');
  const chainedContext = knowledge.selectKnowledgeContextQuestion(['give another example', 'go deeper', 'what is list.count']);
  if (deepFollowUp.mode !== 'deep' || deepFollowUp.question !== 'what is len') failures.push('Deep follow-up lost context');
  if (exampleFollowUp.mode !== 'examples' || exampleFollowUp.question !== 'what is list') failures.push('Example follow-up lost context');
  if (!pronounFollowUp.question.includes('list.sort')) failures.push('Pronoun follow-up did not restore the previous subject');
  if (chainedContext !== 'what is list.count') failures.push('Chained follow-ups lost the last substantive question');
  if (knowledge.isKnowledgeFollowUpQuestion('Explain this code:\n```python\nprint(1)\n```')) failures.push('Pasted code was incorrectly classified as a pronoun follow-up');
  const countDeep = knowledge.buildPythonKnowledgeDeepSupplement('what is list.count', 'en');
  const countExamples = knowledge.buildPythonKnowledgeExampleSupplement('what is list.count', 'en');
  if (!countDeep.includes('O(n)') || !countDeep.includes('list.count(x)')) failures.push('Deep list.count mechanics were not specific');
  if (!countExamples.includes('letters.count("a")') || !countExamples.includes('values.count(10)')) failures.push('Additional list.count examples were not specific');

  const codeAnswer = knowledge.answerPythonCodeQuestion([
    'Explain this code:',
    '```python',
    'items = ["a", "b", "c"]',
    'last = items[-1]',
    'print(last)',
    '```',
  ].join('\n'), 'en') || '';
  for (const fragment of ['Line-by-line code analysis', 'selects the last item', 'print()', 'Execution flow']) {
    if (!codeAnswer.includes(fragment)) failures.push(`Code analysis missing ${JSON.stringify(fragment)}`);
  }

  const versionAnswer = knowledge.answerPythonVersionQuestion('when was match statement added', 'en') || '';
  if (!versionAnswer.includes('Python 3.10') || !versionAnswer.includes('docs.python.org')) failures.push('Version-aware match answer failed');

  const frenchLookup = localization.normalizeAiQuestionForLookup("Qu'est-ce que len ?", 'fr');
  const frenchAnswer = knowledge.answerPythonKnowledgeQuestion(frenchLookup, 'fr') || '';
  for (const fragment of ['fonction intégrée', 'Type et syntaxe', 'Retour et modification', 'Source et confiance']) {
    if (!frenchAnswer.toLowerCase().includes(fragment.toLowerCase())) failures.push(`French structured answer missing ${JSON.stringify(fragment)}`);
  }

  console.log('General Python AI quality evaluation');
  console.log(`Catalog terms evaluated: ${terms.length}`);
  console.log(`Structured records: ${structuredRecords}`);
  console.log(`Ambiguity records: ${ambiguityResponses}`);
  console.log(`Definition query variants: ${definitionVariants}`);
  console.log(`Comparison cases: ${comparisonCases.length}`);
  console.log('Follow-up, code, version, source, and French checks: completed');

  if (failures.length) {
    console.error('\nFailures:');
    for (const failure of failures.slice(0, 100)) console.error(`- ${failure}`);
    process.exitCode = 1;
  } else {
    console.log('Result: passed');
  }
} finally {
  fs.rmSync(tempDir, { recursive: true, force: true });
}
