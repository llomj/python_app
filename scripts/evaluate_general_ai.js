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
const intentBundle = path.join(tempDir, 'intent.cjs');
const tracebackBundle = path.join(tempDir, 'traceback.cjs');
const runtimeBundle = path.join(tempDir, 'runtime.cjs');
const verificationBundle = path.join(tempDir, 'verification.cjs');
const tutorBundle = path.join(tempDir, 'tutor.cjs');

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
  bundle('services/generalAiIntent.ts', intentBundle);
  bundle('services/generalAiTraceback.ts', tracebackBundle);
  bundle('services/generalAiRuntime.ts', runtimeBundle);
  bundle('services/generalAiVerification.ts', verificationBundle);
  bundle('services/generalAiTutor.ts', tutorBundle);

  const knowledge = require(knowledgeBundle);
  const concepts = require(conceptBundle);
  const localization = require(localizationBundle);
  const intent = require(intentBundle);
  const traceback = require(tracebackBundle);
  const runtime = require(runtimeBundle);
  const verification = require(verificationBundle);
  const tutor = require(tutorBundle);
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
    ['difference between dictionary and set', ['stores pairs of keys and values', 'unordered collection of unique items', 'Purpose']],
  ];
  for (const [question, fragments] of comparisonCases) {
    const answer = knowledge.answerPythonKnowledgeComparison(question, 'en') || '';
    for (const fragment of fragments) {
      if (!answer.toLowerCase().includes(fragment.toLowerCase())) failures.push(`Comparison ${JSON.stringify(question)} missing ${JSON.stringify(fragment)}`);
    }
  }

  const everydayAliases = [
    ['dictionary', 'dict'],
    ['array', 'list'],
    ['immutable list', 'tuple'],
    ['text', 'string'],
  ];
  for (const [alias, expectedCanonicalName] of everydayAliases) {
    const resolution = knowledge.resolvePythonKnowledge(alias);
    if (!resolution.record || resolution.record.canonicalName !== expectedCanonicalName || resolution.record.confidence === 'categorized') {
      failures.push(`Everyday alias ${JSON.stringify(alias)} did not resolve to curated ${JSON.stringify(expectedCanonicalName)}`);
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
  const typedMethodCode = knowledge.answerPythonCodeQuestion('Explain this code:\n```python\nnums = [1, 2]\nnums.pop()\n```', 'en') || '';
  if (!typedMethodCode.includes('nums.pop()') || typedMethodCode.includes('ambiguous name')) failures.push('Code analyzer did not infer method owner type');

  const versionAnswer = knowledge.answerPythonVersionQuestion('when was match statement added', 'en') || '';
  if (!versionAnswer.includes('Python 3.10') || !versionAnswer.includes('docs.python.org')) failures.push('Version-aware match answer failed');

  const frenchLookup = localization.normalizeAiQuestionForLookup("Qu'est-ce que len ?", 'fr');
  const frenchAnswer = knowledge.answerPythonKnowledgeQuestion(frenchLookup, 'fr') || '';
  for (const fragment of ['fonction intégrée', 'Type et syntaxe', 'Retour et modification', 'Source et confiance']) {
    if (!frenchAnswer.toLowerCase().includes(fragment.toLowerCase())) failures.push(`French structured answer missing ${JSON.stringify(fragment)}`);
  }

  const intentCases = [
    ['What is a list?', 'definition'],
    ['Define a closure', 'definition'],
    ['Qu’est-ce qu’un dictionnaire ?', 'definition'],
    ['difference between dictionary and set', 'comparison'],
    ['compare print with return', 'comparison'],
    ['Quelle est la différence entre liste et tuple ?', 'comparison'],
    ['How many built-in functions are there?', 'count'],
    ['Combien de méthodes existe-t-il ?', 'count'],
    ['How do I create a method?', 'creation'],
    ['Comment créer une classe ?', 'creation'],
    ['When was match added?', 'version'],
    ['Quelle version a ajouté les f-strings ?', 'version'],
    ['Quiz me on dictionaries', 'quiz'],
    ['Teste-moi sur les listes', 'quiz'],
    ['Give examples of lambda', 'examples'],
    ['Montre-moi des exemples de tuple', 'examples'],
    ['Show official docs for mapping keys and values', 'documentation'],
    ['Documentation officielle sur les ensembles uniques', 'documentation'],
    ['What should I use to remove duplicate values?', 'purpose'],
    ['Comment faire pour trier sans modifier la liste ?', 'purpose'],
    ['What concepts are related to generators?', 'relationships'],
    ['Que dois-je apprendre ensuite après les listes ?', 'relationships'],
    ['What is TypeError?', 'error_help'],
    ['Pourquoi cette erreur ValueError ?', 'error_help'],
    ['Explain this code:\n```python\nprint(1 + 2)\n```', 'code_explanation'],
    ['Analyse ce code :\nvalue = [1, 2][-1]', 'code_explanation'],
    ['Traceback (most recent call last):\n  File "main.py", line 2, in <module>\nNameError: name x is not defined', 'traceback'],
  ];
  for (const [question, expected] of intentCases) {
    const actual = intent.classifyGeneralAiIntent(question);
    if (actual.intent !== expected || actual.confidence < 0.7) {
      failures.push(`Intent ${JSON.stringify(question)} expected ${expected}, found ${actual.intent} (${actual.confidence})`);
    }
  }
  if (!intent.shouldClarifyGeneralAiQuestion('it?') || intent.shouldClarifyGeneralAiQuestion('What is a list?')) {
    failures.push('Clarification confidence gate failed');
  }

  const bareTerms = ['sys', 'len', 'list.append', 'TypeError', 'tuple', 'zip'];
  for (const term of bareTerms) {
    const answer = knowledge.answerPythonBareOrFuzzyQuestion(term, 'en') || '';
    if (answer.length < 80 || !answer.toLowerCase().includes(term.split('.')[0].toLowerCase())) failures.push(`Bare-term lookup failed for ${term}`);
  }
  const fuzzyLen = knowledge.answerPythonBareOrFuzzyQuestion('leng', 'en') || '';
  if (!fuzzyLen.includes('Likely correction') || !fuzzyLen.includes('len')) failures.push('Fuzzy bare-term correction failed');

  const beginnerList = knowledge.answerPythonAtLevel('list', 'en', 'beginner') || '';
  const intermediateList = knowledge.answerPythonAtLevel('list', 'en', 'intermediate') || '';
  const expertList = knowledge.answerPythonAtLevel('list', 'en', 'expert') || '';
  const progressiveList = knowledge.answerPythonProgressiveExamples('examples of list', 'en') || '';
  const progressiveSys = knowledge.answerPythonProgressiveExamples('examples of sys', 'en') || '';
  const contextualSys = knowledge.answerPythonAtLevel('Explain sys again', 'en', 'intermediate') || '';
  if (!beginnerList.includes('beginner level') || !beginnerList.includes('Tiny example')) failures.push('Beginner explanation contract failed');
  if (!intermediateList.includes('intermediate level') || !intermediateList.includes('Return and mutation')) failures.push('Intermediate explanation contract failed');
  if (!expertList.includes('expert level') || !expertList.includes('Version and source') || !expertList.includes('Deep mechanics')) failures.push('Expert explanation contract failed');
  if (!progressiveList.includes('Progressive examples: list') || !progressiveList.includes('Suggested progression')) failures.push('Progressive list examples failed');
  if (!progressiveSys.includes('Progressive examples: sys') || !progressiveSys.includes('import sys')) failures.push('Progressive sys examples failed');
  if (!contextualSys.includes('**sys — intermediate level**') || !contextualSys.includes('sys.argv') || contextualSys.includes('capsys')) failures.push('Contextual sys retrieval failed');

  let mastery = tutor.parseTutorMasteryProfile(null);
  const adaptiveFirst = tutor.inferTutorLevel('What is a closure?', mastery, 'normal', true);
  mastery = tutor.updateTutorMastery(mastery, 'closure', adaptiveFirst);
  const adaptiveSecond = tutor.inferTutorLevel('Explain closure again', mastery, 'normal', true);
  mastery = tutor.updateTutorMastery(mastery, 'closure', adaptiveSecond);
  mastery = tutor.updateTutorMastery(mastery, 'closure', 'normal');
  mastery = tutor.updateTutorMastery(mastery, 'closure', 'normal');
  const adaptiveExperienced = tutor.inferTutorLevel('Explain closure again', mastery, 'normal', true);
  const adaptiveExplicit = tutor.inferTutorLevel('Explain closure internals and bytecode', mastery, 'normal', true);
  if (adaptiveFirst !== 'simple' || adaptiveSecond !== 'normal' || adaptiveExperienced !== 'deep' || adaptiveExplicit !== 'deep') failures.push('Adaptive mastery levels failed');
  if (mastery.closure.views !== 4 || mastery.closure.beginner !== 1 || mastery.closure.intermediate !== 3) failures.push('Mastery persistence counters failed');

  const tutorModes = [
    ['socratic', 'list', 'Socratic mode'],
    ['quiz', 'list', 'Adaptive quiz'],
    ['practice', 'list', 'Targeted practice'],
    ['debug', 'Why is it broken?', 'Debug mode'],
    ['compare', 'Compare these', 'Compare mode'],
  ];
  for (const [mode, question, fragment] of tutorModes) {
    const answer = tutor.answerTutorMode(question, mode, 'normal', 'en') || '';
    if (!answer.includes(fragment)) failures.push(`${mode} tutor mode failed`);
  }

  const previousCodeAnswer = '**Example**\n```python\nitems = [1, 2]\nitems.append(3)\nprint(items)\n```';
  const runCommand = tutor.resolveTutorCodeCommand('run this', previousCodeAnswer, 'en');
  const lineCommand = tutor.resolveTutorCodeCommand('explain line 2', previousCodeAnswer, 'en');
  const changeCommand = tutor.resolveTutorCodeCommand('change the input to [8, 9]', previousCodeAnswer, 'en');
  if (!runCommand.effectiveQuestion?.includes('items.append(3)')) failures.push('Interactive run-this command failed');
  if (!lineCommand.directAnswer?.includes('items.append(3)')) failures.push('Interactive explain-line command failed');
  if (!changeCommand.effectiveQuestion?.includes('items = [8, 9]')) failures.push('Interactive change-input command failed');

  const purposeAnswer = knowledge.answerPythonPurposeQuestion('What should I use to remove duplicate values from a collection?', 'en') || '';
  const relationshipAnswer = knowledge.answerPythonRelationships('What concepts are related to list?', 'en') || '';
  if (!purposeAnswer.includes('Python tools matching the goal') || !purposeAnswer.includes('set')) failures.push('Purpose-based retrieval failed');
  if (tutor.getTutorSubject('What should I use to remove duplicate values from a collection?') !== 'set') failures.push('Purpose mastery subject did not match retrieval');
  if (!relationshipAnswer.includes('Concept map') || !relationshipAnswer.includes('Learn next')) failures.push('Concept relationship graph failed');

  const semanticStarted = Date.now();
  const semanticResults = knowledge.searchPythonKnowledge('unique unordered collection mathematical union', 3);
  const semanticElapsed = Date.now() - semanticStarted;
  if (semanticResults[0]?.record.canonicalName !== 'set') failures.push('Semantic retrieval did not rank set first');
  if (semanticElapsed > 1500) failures.push(`Lazy semantic index took too long to initialize: ${semanticElapsed}ms`);
  const docsAnswer = knowledge.answerPythonDocumentationQuestion('Show official docs for mapping keys and values', 'en') || '';
  if (!docsAnswer.includes('dict') || !docsAnswer.includes('docs.python.org')) failures.push('Semantic documentation answer did not retrieve dict documentation');
  const frenchDocs = knowledge.answerPythonDocumentationQuestion('Documentation officielle sur un ensemble unique', 'fr') || '';
  if (!frenchDocs.includes('Documentation Python correspondante') || !frenchDocs.includes('collection non ordonnée de valeurs uniques') || !frenchDocs.includes('docs.python.org') || frenchDocs.includes('is a Python concept')) failures.push('French documentation retrieval failed');
  const frenchComparison = knowledge.answerPythonKnowledgeComparison('difference between dict and set', 'fr') || '';
  if (!frenchComparison.includes('paires clé-valeur') || !frenchComparison.includes('valeurs uniques')) failures.push('French comparison summaries were not native');
  const frenchBeginner = knowledge.answerPythonAtLevel('list', 'fr', 'beginner') || '';
  const frenchIntermediate = knowledge.answerPythonAtLevel('list', 'fr', 'intermediate') || '';
  const frenchExpert = knowledge.answerPythonAtLevel('list', 'fr', 'expert') || '';
  const frenchSocratic = tutor.answerTutorMode('list', 'socratic', 'normal', 'fr') || '';
  const frenchPractice = tutor.answerTutorMode('list', 'practice', 'normal', 'fr') || '';
  if (!frenchBeginner.includes('niveau débutant') || !frenchIntermediate.includes('niveau intermédiaire') || !frenchExpert.includes('niveau expert')) failures.push('French explanation levels failed');
  if (!frenchSocratic.includes('Mode socratique') || !frenchPractice.includes('Exercice ciblé')) failures.push('French tutor modes failed');

  const tracebackText = [
    'Traceback (most recent call last):',
    '  File "main.py", line 8, in <module>',
    '    calculate()',
    '  File "helpers.py", line 3, in calculate',
    '    return values[5]',
    'IndexError: list index out of range',
  ].join('\n');
  const parsedTraceback = traceback.parsePythonTraceback(tracebackText);
  if (!parsedTraceback || parsedTraceback.frames.length !== 2 || parsedTraceback.failingFrame?.file !== 'helpers.py' || parsedTraceback.errorType !== 'IndexError') {
    failures.push('Frame-aware traceback parser failed');
  }
  const tracebackAnswer = traceback.answerPythonTraceback(tracebackText, 'en') || '';
  const frenchTracebackAnswer = traceback.answerPythonTraceback(tracebackText, 'fr') || '';
  for (const fragment of ['helpers.py:3', 'IndexError', 'Call stack', 'valid range']) {
    if (!tracebackAnswer.includes(fragment)) failures.push(`Traceback answer missing ${JSON.stringify(fragment)}`);
  }
  if (!frenchTracebackAnswer.includes('Pile d’appels') || !frenchTracebackAnswer.includes('hors des limites')) failures.push('Native French traceback explanation failed');

  const safeRuntime = runtime.assessGeneralAiRuntimeSafety('Explain this code:\n```python\nitems = [1, 2]\nitems.append(3)\nprint(items)\n```');
  const unsafeImport = runtime.assessGeneralAiRuntimeSafety('Explain:\n```python\nimport os\nprint(os.listdir())\n```');
  const unsafeLoop = runtime.assessGeneralAiRuntimeSafety('Explain:\n```python\nwhile True:\n    pass\n```');
  if (!safeRuntime.safe || unsafeImport.safe || unsafeLoop.safe) failures.push('Guarded runtime safety policy failed');
  const runtimeEvidence = runtime.formatGeneralAiRuntimeEvidence({ ok: true, stdout: '3\n', resultRepr: '', resultType: 'NoneType', errorType: '', errorMessage: '' }, 'en');
  const runtimeFailure = runtime.formatGeneralAiRuntimeEvidence({ ok: false, stdout: '', resultRepr: '', resultType: '', errorType: 'TypeError', errorMessage: 'bad type' }, 'fr');
  if (!runtimeEvidence.includes('Actual output') || !runtimeFailure.includes('TypeError') || !runtimeFailure.includes('déclenche')) failures.push('Runtime evidence formatting failed');

  const verifiedAnswer = verification.verifyGeneralAiAnswer('What is len?', '**Source and confidence**\nhttps://docs.python.org/3/library/functions.html#len');
  const badFence = verification.verifyGeneralAiAnswer('Explain code', '```python\nprint(1)');
  const badSource = verification.verifyGeneralAiAnswer('What is list?', 'See https://made-up-python-docs.example/list for details.');
  if (!verifiedAnswer.valid || badFence.valid || badSource.valid) failures.push('Answer verification gates failed');

  const frenchDirectExample = knowledge.resolveKnowledgeFollowUp('donne des exemples de dictionnaire', 'what is list', 'normal');
  const frenchDeepFollowUp = knowledge.resolveKnowledgeFollowUp('approfondis les tuples', 'what is list', 'normal');
  const switchedSubject = knowledge.resolveKnowledgeFollowUp('what about tuple?', 'what is list', 'normal');
  if (frenchDirectExample.mode !== 'examples' || !frenchDirectExample.question.includes('dictionnaire')) failures.push('French direct-example context failed');
  if (frenchDeepFollowUp.mode !== 'deep' || !frenchDeepFollowUp.question.includes('tuples')) failures.push('French deep context failed');
  if (switchedSubject.question !== 'what is tuple') failures.push('Conversation subject switching failed');

  console.log('General Python AI quality evaluation');
  console.log(`Catalog terms evaluated: ${terms.length}`);
  console.log(`Structured records: ${structuredRecords}`);
  console.log(`Ambiguity records: ${ambiguityResponses}`);
  console.log(`Definition query variants: ${definitionVariants}`);
  console.log(`Comparison cases: ${comparisonCases.length}`);
  console.log(`Intent variants: ${intentCases.length}`);
  console.log(`Bare-term checks: ${bareTerms.length}`);
  console.log(`Tutor modes: ${tutorModes.length}`);
  console.log(`Semantic index cold start: ${semanticElapsed}ms`);
  console.log('All 12 tutor gates: bare/fuzzy terms, levels, context, adaptation, relationships, ambiguity, purpose, progressive interaction, tutor modes, mastery, retrieval, and conversations completed');

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
