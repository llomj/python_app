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
const advancedBundle = path.join(tempDir, 'advanced.cjs');

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
  bundle('services/generalAiAdvanced.ts', advancedBundle);

  const knowledge = require(knowledgeBundle);
  const concepts = require(conceptBundle);
  const localization = require(localizationBundle);
  const intent = require(intentBundle);
  const traceback = require(tracebackBundle);
  const runtime = require(runtimeBundle);
  const verification = require(verificationBundle);
  const tutor = require(tutorBundle);
  const advanced = require(advancedBundle);
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

  const anySignature = knowledge.answerPythonCallableSignatureQuestion('how many arguments does any() take?', 'en') || '';
  const mapSignature = knowledge.answerPythonCallableSignatureQuestion('what is the order of arguments in map()?', 'en') || '';
  const countSignature = knowledge.answerPythonCallableSignatureQuestion('how many arguments does str.count take?', 'en') || '';
  const lambdaOrder = knowledge.answerPythonEvaluationAndScopeQuestion('what is the order of evaluation for lambda?', 'en') || '';
  const comprehensionOrder = knowledge.answerPythonEvaluationAndScopeQuestion('explain list comprehension order of operations', 'en') || '';
  const scopeOrder = knowledge.answerPythonEvaluationAndScopeQuestion('which local or global variable does Python use first?', 'en') || '';
  if (!anySignature.includes('exactly 1') || !anySignature.includes('any(iterable)')) failures.push('any() argument-count answer failed');
  if (!mapSignature.includes('at least 2') || !mapSignature.includes('function first')) failures.push('map() argument-order answer failed');
  if (!countSignature.includes('str.count(sub[, start[, end]])') || !countSignature.includes('1 required and 2 optional')) failures.push('str.count() optional-argument answer failed');
  if (!lambdaOrder.includes('single expression after `:`') || !lambdaOrder.includes('returned automatically')) failures.push('Lambda evaluation-order answer failed');
  if (!comprehensionOrder.includes('first `for` iterable') || !comprehensionOrder.includes('`if` filters')) failures.push('Comprehension evaluation-order answer failed');
  if (!scopeOrder.includes('LEGB') || !scopeOrder.includes('Enclosing') || !scopeOrder.includes('Built-ins')) failures.push('Variable-scope answer failed');

  const allMethodsCatalog = knowledge.answerPythonCatalogQuestion('list all methods', 'en') || '';
  const listMethodsCatalog = knowledge.answerPythonCatalogQuestion('list all list methods', 'en') || '';
  const builtinsCatalog = knowledge.answerPythonCatalogQuestion('list all built-in functions', 'en') || '';
  const builtinsCountCatalog = knowledge.answerPythonCatalogQuestion('how many built-in functions are there?', 'en') || '';
  const keywordCatalog = knowledge.answerPythonCatalogQuestion('show all Python keywords', 'en') || '';
  const typeCatalog = knowledge.answerPythonCatalogQuestion('list all built-in data types', 'en') || '';
  const operatorCatalog = knowledge.answerPythonCatalogQuestion('list all operators', 'en') || '';
  const comprehensionCatalog = knowledge.answerPythonCatalogQuestion('show all comprehension forms', 'en') || '';
  if (!allMethodsCatalog.includes('all core built-in-type methods') || !allMethodsCatalog.includes('str.capitalize()') || !allMethodsCatalog.includes('list.append(x)') || !allMethodsCatalog.includes('dict.get(key[, default])')) failures.push('Complete grouped method catalog failed');
  if (!listMethodsCatalog.includes('list methods') || !listMethodsCatalog.includes('list.extend(iterable)') || listMethodsCatalog.includes('str methods')) failures.push('Type-specific method catalog failed');
  if (!builtinsCatalog.includes('built-in functions') || !builtinsCatalog.includes('len(s)') || !builtinsCatalog.includes('map(function, iterable, ...)')) failures.push('Built-in function catalog failed');
  if (!builtinsCountCatalog.includes('built-in functions') || !builtinsCountCatalog.includes('`abs(x)`') || !builtinsCountCatalog.includes('71')) failures.push('Built-in count plus numbered catalog failed');
  if (!keywordCatalog.includes('keywords') || !keywordCatalog.includes('`for var in iterable:`')) failures.push('Keyword catalog failed');
  if (!typeCatalog.includes('built-in data types') || !typeCatalog.includes('`dict`')) failures.push('Data-type catalog failed');
  if (!operatorCatalog.includes('core operators') || !operatorCatalog.includes('`**`')) failures.push('Operator catalog failed');
  if (!comprehensionCatalog.includes('comprehension forms') || !comprehensionCatalog.includes('[expression for item in iterable]')) failures.push('Comprehension catalog failed');

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
    ['What does this print?\n```python\nprint(1 + 2)\n```', 'output_prediction'],
    ['Step through this code and show variable changes:\n```python\nfor n in range(2):\n    print(n)\n```', 'interactive_debug'],
    ['Generate test cases for this function:\n```python\ndef square(number):\n    return number ** 2\n```', 'test_generation'],
    ['What is the time complexity?\n```python\nfor item in values:\n    print(item)\n```', 'complexity_analysis'],
    ['Compare these solutions:\n```python\nfor a in values:\n    for b in values:\n        print(a, b)\n```\n```python\nfor value in values:\n    print(value)\n```', 'code_comparison'],
    ['How should I organize imports across multiple Python modules?', 'module_project'],
    ['Audit these files:\n```python\n# file: main.py\nfrom helpers import greet\nprint(greet("Noll"))\n```\n```python\n# file: helpers.py\ndef greet(name):\n    return f"Hi {name}"\n```', 'module_project'],
    ['Show my learning progress and weak areas', 'learning_progress'],
    ['What am I misunderstanding? This returns None:\n```python\nitems = [1, 2]\nresult = items.append(3)\n```', 'misconception'],
    ['Will this run on Python 3.9?\n```python\nmatch command:\n    case "go":\n        print("go")\n```', 'version_compatibility'],
    ['Review this code for readability:\n```python\nvalues = []\n```', 'code_quality'],
    ['Build me a learning path for OOP', 'learning_path'],
    ['Which list methods return None and mutate in place?', 'contract_search'],
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
  const safeFunctionLoop = runtime.assessGeneralAiRuntimeSafety('What does this print?\n```python\ndef total(values):\n    result = 0\n    for value in values:\n        result += value\n    return result\nprint(total([1, 2, 3]))\n```');
  const unsafeLargeRange = runtime.assessGeneralAiRuntimeSafety('Explain:\n```python\nfor item in range(9000):\n    print(item)\n```');
  if (!safeRuntime.safe || !safeFunctionLoop.safe || unsafeImport.safe || unsafeLoop.safe || unsafeLargeRange.safe) failures.push('Guarded runtime safety policy failed');
  const runtimeEvidence = runtime.formatGeneralAiRuntimeEvidence({ ok: true, stdout: '3\n', resultRepr: '', resultType: 'NoneType', errorType: '', errorMessage: '', variables: { total: '3' }, executionTrace: [{ line: 1, event: 'call', function: 'total', variables: {}, changedVariables: {} }, { line: 2, event: 'line', function: 'total', variables: { total: '3' }, changedVariables: { total: '3' } }, { line: 2, event: 'return', function: 'total', variables: { total: '3' }, changedVariables: {}, returnValue: '3' }] }, 'en');
  const runtimeFailure = runtime.formatGeneralAiRuntimeEvidence({ ok: false, stdout: '', resultRepr: '', resultType: '', errorType: 'TypeError', errorMessage: 'bad type', errorLine: 4, variables: { value: "'x'" }, executionTrace: [{ line: 4, event: 'line', function: 'change', variables: { value: "'x'" }, changedVariables: { value: "'x'" } }] }, 'fr');
  if (!runtimeEvidence.includes('Actual output') || !runtimeEvidence.includes('Final variable state') || !runtimeEvidence.includes('Verified step-by-step debugging') || !runtimeEvidence.includes('return `total()`') || !runtimeEvidence.includes('value=`3`') || !runtimeFailure.includes('TypeError') || !runtimeFailure.includes('Trace avant l’erreur')) failures.push('Runtime evidence formatting failed');

  const learningPath = advanced.answerPythonLearningPath('Build me a learning path for dictionaries', {}, 'en') || '';
  const frenchLearningPath = advanced.answerPythonLearningPath('Construis un parcours pour les dictionnaires', {}, 'fr') || '';
  const qualityReview = advanced.answerPythonCodeQuality('Review this code:\n```python\ndef add(item, values=[]):\n    try:\n        values.append(item)\n    except:\n        pass\n```', 'en') || '';
  const quiz = advanced.createAdaptiveQuiz('list', 'normal', 'en');
  const secondQuiz = advanced.createAdaptiveQuiz('list', 'normal', 'en', 1, 'negative indexing');
  const quizCorrect = advanced.evaluateAdaptiveQuiz('It prints 3 3 because append adds one item.', quiz, 'en');
  const quizWrong = advanced.evaluateAdaptiveQuiz('It prints 2.', quiz, 'en');
  const mistakeProfile = advanced.updateGeneralAiMistakes({}, quiz);
  const generatedTests = advanced.answerPythonTestCaseRequest('Generate test cases:\n```python\ndef total(values):\n    return sum(values)\n```', 'en') || '';
  const frenchGeneratedTests = advanced.answerPythonTestCaseRequest('Génère des cas de test :\n```python\ndef total(values):\n    return sum(values)\n```', 'fr') || '';
  const linearComplexity = advanced.answerPythonComplexityRequest('What is the complexity?\n```python\nresult = [value * 2 for value in values]\n```', 'en') || '';
  const nestedComplexity = advanced.answerPythonComplexityRequest('Analyse la complexité :\n```python\nfor left in values:\n    for right in values:\n        print(left, right)\n```', 'fr') || '';
  const sortedComplexity = advanced.answerPythonComplexityRequest('What is the Big O?\n```python\nresult = sorted(values)\n```', 'en') || '';
  const codeComparison = advanced.answerPythonCodeComparison('Compare these solutions:\n```python\nfor left in values:\n    for right in values:\n        if left == right:\n            return True\n```\n```python\nseen = set()\nfor value in values:\n    if value in seen:\n        return True\n    seen.add(value)\n```', 'en') || '';
  const frenchCodeComparison = advanced.answerPythonCodeComparison('Compare ces solutions :\n```python\nfor value in values:\n    print(value)\n```\n```python\nprint(*values)\n```', 'fr') || '';
  const moduleGuide = advanced.answerPythonModuleProjectRequest('How do modules, packages, and imports work?', 'en') || '';
  const projectAudit = advanced.answerPythonModuleProjectRequest('Audit these modules:\n```python\n# file: main.py\nfrom helpers import greet\nprint(greet("Noll"))\n```\n```python\n# file: helpers.py\ndef greet(name):\n    return f"Hi {name}"\n```', 'en') || '';
  const missingImportAudit = advanced.answerPythonModuleProjectRequest('Check imports:\n```python\n# file: main.py\nfrom helpers import missing_name\n```\n```python\n# file: helpers.py\ndef available():\n    return True\n```', 'en') || '';
  const circularAudit = advanced.answerPythonModuleProjectRequest('Analyse ces fichiers multiples :\n```python\n# file: first.py\nimport second\n```\n```python\n# file: second.py\nimport first\n```', 'fr') || '';
  const mutationMisconception = advanced.answerPythonMisconceptionRequest('Why does this return None?\n```python\nitems = [1, 2]\nresult = items.append(3)\n```', 'en') || '';
  const identityMisconception = advanced.answerPythonMisconceptionRequest('Quelle est mon erreur de compréhension ?\n```python\nvalue = 1000\nprint(value is 1000)\n```', 'fr') || '';
  const printMisconception = advanced.answerPythonMisconceptionRequest('What am I misunderstanding?\n```python\ndef double(value):\n    print(value * 2)\n```', 'en') || '';
  const progressReport = advanced.answerGeneralAiProgressRequest('Show my learning progress', {
    list: { views: 5, beginner: 1, intermediate: 2, expert: 2, lastSeen: 3 },
    dictionary: { views: 2, beginner: 1, intermediate: 1, expert: 0, lastSeen: 2 },
  }, {
    'list:slicing': { count: 2, lastSeen: 4, lastMistake: 'slice stop is excluded' },
  }, 'en') || '';
  const frenchProgress = advanced.answerGeneralAiProgressRequest('Montre mes progrès et mes points faibles', {}, {}, 'fr') || '';
  const matchCompatibility = advanced.answerPythonVersionCompatibilityRequest('Will this run on Python 3.9?\n```python\nmatch command:\n    case "go":\n        print("go")\n```', 'en') || '';
  const tomllibCompatibility = advanced.answerPythonVersionCompatibilityRequest('Is this compatible with Python 3.11?\n```python\nimport tomllib\n```', 'en') || '';
  const typeCompatibility = advanced.answerPythonVersionCompatibilityRequest('Minimum Python version?\n```python\ntype Point = tuple[float, float]\n```', 'en') || '';
  const frenchWalrusCompatibility = advanced.answerPythonVersionCompatibilityRequest('Fonctionnera sous Python 3.7 ?\n```python\nif (size := len(items)) > 2:\n    print(size)\n```', 'fr') || '';
  const frenchAdjectiveCompatibility = advanced.answerPythonVersionCompatibilityRequest('Est-ce compatible avec Python 3.9 ?\n```python\nmatch command:\n    case "go":\n        print("go")\n```', 'fr') || '';
  const unionCompatibility = advanced.answerPythonVersionCompatibilityRequest('What minimum Python version is required?\n```python\ndef parse(value: int | str) -> str:\n    return str(value)\n```', 'en') || '';
  if (!learningPath.includes('Adaptive learning path') || !learningPath.includes('key-value literals')) failures.push('Adaptive learning path failed');
  if (!frenchLearningPath.includes('Parcours d’apprentissage adaptatif') || !frenchLearningPath.includes('paires clé-valeur') || frenchLearningPath.includes('nested dictionaries')) failures.push('French adaptive learning path failed');
  if (!qualityReview.includes('mutable default') || !qualityReview.includes('bare `except:`')) failures.push('Code-quality review failed');
  if (!quiz.prompt.includes('Adaptive quiz') || secondQuiz.id === quiz.id || !secondQuiz.prompt.includes('negative indexing') || !quizCorrect.correct || quizWrong.correct || !quizWrong.text.includes('Misconception detected')) failures.push('Stateful adaptive quiz evaluation failed');
  if (Object.values(mistakeProfile)[0]?.count !== 1 || !Object.values(mistakeProfile)[0]?.lastMistake) failures.push('Mistake profile tracking failed');
  if (!generatedTests.includes('Generated test cases') || !generatedTests.includes('total([])') || !generatedTests.includes('Executable harness')) failures.push('Test-case generation failed');
  if (!frenchGeneratedTests.includes('Cas de test générés') || !frenchGeneratedTests.includes('Harnais exécutable')) failures.push('French test-case generation failed');
  if (!linearComplexity.includes('Estimated time: O(n)') || !linearComplexity.includes('Estimated auxiliary space: O(n)')) failures.push('Linear complexity analysis failed');
  if (!nestedComplexity.includes('Temps estimé: O(n^2)') || !nestedComplexity.includes('2 boucles imbriquées')) failures.push('French nested-loop complexity analysis failed');
  if (!sortedComplexity.includes('O(n log n)') || !sortedComplexity.includes('sorting call')) failures.push('Sorting complexity analysis failed');
  if (!codeComparison.includes('Two-solution code comparison') || !codeComparison.includes('Solution B has the better') || !codeComparison.includes('Required verification')) failures.push('Two-solution comparison failed');
  if (!frenchCodeComparison.includes('Comparaison de deux solutions') || !frenchCodeComparison.includes('Vérification nécessaire')) failures.push('French code comparison failed');
  if (!moduleGuide.includes('Python modules and files guide') || !moduleGuide.includes('__init__.py') || !moduleGuide.includes('__main__')) failures.push('Module and package guide failed');
  if (!projectAudit.includes('Multi-file Python project audit') || !projectAudit.includes('`main` → `helpers`') || !projectAudit.includes('add a `main()` function')) failures.push('Multi-file project audit failed');
  if (!missingImportAudit.includes('missing_name') || !missingImportAudit.includes('no module-level definition')) failures.push('Missing imported symbol audit failed');
  if (!circularAudit.includes('Audit du projet Python multi-fichiers') || !circularAudit.includes('Dépendance circulaire détectée')) failures.push('French circular-import audit failed');
  if (!mutationMisconception.includes('In-place mutation versus return value') || !mutationMisconception.includes('items.append(3)') || !mutationMisconception.includes('result = items')) failures.push('Mutation misconception diagnosis failed');
  if (!identityMisconception.includes('Identité contre égalité') || !identityMisconception.includes('value == 1000')) failures.push('French identity misconception diagnosis failed');
  if (!printMisconception.includes('Display without a function result') || !printMisconception.includes('return value * 2')) failures.push('Print-versus-return misconception diagnosis failed');
  if (!progressReport.includes('Python learning progress report') || !progressReport.includes('7 interactions') || !progressReport.includes('slice stop is excluded') || !progressReport.includes('exposure, not proven mastery')) failures.push('Learning-progress report failed');
  if (!frenchProgress.includes('Bilan d’apprentissage Python') || !frenchProgress.includes('Aucune activité enregistrée') || !frenchProgress.includes('pas une maîtrise prouvée')) failures.push('Empty French progress report failed');
  if (!matchCompatibility.includes('Python 3.10') || !matchCompatibility.includes('not compatible without changes') || !matchCompatibility.includes('docs.python.org/3/whatsnew/3.10')) failures.push('Pattern-matching compatibility failed');
  if (!tomllibCompatibility.includes('Python 3.11') || !tomllibCompatibility.includes('compatible with the detected features') || !tomllibCompatibility.includes('tomli')) failures.push('tomllib compatibility failed');
  if (!typeCompatibility.includes('Python 3.12') || !typeCompatibility.includes('typing.TypeAlias')) failures.push('Type-statement compatibility failed');
  if (!frenchWalrusCompatibility.includes('Python 3.8') || !frenchWalrusCompatibility.includes('non compatible sans modification') || !frenchWalrusCompatibility.includes('ligne séparée')) failures.push('French walrus compatibility failed');
  if (!frenchAdjectiveCompatibility.includes('Python 3.10') || !frenchAdjectiveCompatibility.includes('non compatible sans modification')) failures.push('French adjective compatibility phrasing failed');
  if (!unionCompatibility.includes('Python 3.10') || !unionCompatibility.includes('typing.Union')) failures.push('Union-type compatibility failed');

  const removeContracts = knowledge.answerPythonContractSearch('Which methods remove or delete items?', 'en') || '';
  const noneContracts = knowledge.answerPythonContractSearch('List methods that mutate in place and return None', 'en') || '';
  const iterableContracts = knowledge.answerPythonContractSearch('Which functions accept an iterable?', 'en') || '';
  if (!removeContracts.includes('Python contract search') || !removeContracts.includes('pop')) failures.push('Removal contract search failed');
  if (!noneContracts.includes('return `None`') || !noneContracts.includes('list.append')) failures.push('In-place contract search failed');
  if (!iterableContracts.includes('iterable') || !iterableContracts.includes('any(iterable)')) failures.push('Iterable contract search failed');

  const verifiedAnswer = verification.verifyGeneralAiAnswer('What is len?', '**Source and confidence**\nhttps://docs.python.org/3/library/functions.html#len');
  const badFence = verification.verifyGeneralAiAnswer('Explain code', '```python\nprint(1)');
  const badSource = verification.verifyGeneralAiAnswer('What is list?', 'See https://made-up-python-docs.example/list for details.');
  const offTopicAnswer = verification.verifyGeneralAiAnswer('What is a dictionary?', 'A tuple is an immutable ordered sequence of values.');
  const groundedAnswer = verification.verifyGeneralAiAnswer('What is a dictionary?', 'A dictionary stores key-value pairs and supports lookup by key.');
  if (!verifiedAnswer.valid || badFence.valid || badSource.valid || offTopicAnswer.valid || !groundedAnswer.valid) failures.push('Answer verification gates failed');

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
  console.log('Tutor gates include runtime traces, learning paths, code quality, stateful quizzes, contract search, bilingual retrieval, and durable conversation behavior');

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
