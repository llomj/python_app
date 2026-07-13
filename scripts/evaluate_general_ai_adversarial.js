#!/usr/bin/env node

const fs = require('fs');
const os = require('os');
const path = require('path');
const { performance } = require('perf_hooks');
const { buildSync } = require('esbuild');

const root = path.resolve(__dirname, '..');
const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'general-ai-adversarial-'));
const bundleFile = path.join(tempDir, 'benchmark.cjs');
const entryFile = path.join(tempDir, 'entry.ts');

fs.writeFileSync(entryFile, [
  `export * as knowledge from ${JSON.stringify(path.join(root, 'services/pythonKnowledge.ts'))};`,
  `export * as intent from ${JSON.stringify(path.join(root, 'services/generalAiIntent.ts'))};`,
  `export * as verification from ${JSON.stringify(path.join(root, 'services/generalAiVerification.ts'))};`,
  `export * as localization from ${JSON.stringify(path.join(root, 'services/aiLocalization.ts'))};`,
].join('\n'));

const normalize = value => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
const includesAll = (answer, fragments) => fragments.every(fragment => normalize(answer).includes(normalize(fragment)));

try {
  buildSync({ entryPoints: [entryFile], outfile: bundleFile, bundle: true, platform: 'node', format: 'cjs', logLevel: 'silent' });
  const { knowledge, intent, verification, localization } = require(bundleFile);
  const failures = [];
  const timings = [];
  let checks = 0;

  const check = (condition, message) => {
    checks += 1;
    if (!condition) failures.push(message);
  };

  const timed = callback => {
    const started = performance.now();
    const result = callback();
    timings.push(performance.now() - started);
    return result || '';
  };

  const answerKnowledge = (question, language) => timed(() => {
    const normalizedQuestion = localization.normalizeAiQuestionForLookup(question, language);
    return knowledge.answerPythonCatalogQuestion(normalizedQuestion, language)
      || knowledge.answerPythonCallableSignatureQuestion(normalizedQuestion, language)
      || knowledge.answerPythonKnowledgeComparison(normalizedQuestion, language)
      || knowledge.answerPythonClassificationQuestion(normalizedQuestion, language)
      || knowledge.answerPythonEvaluationAndScopeQuestion(normalizedQuestion, language)
      || knowledge.answerPythonProtocolQuestion(normalizedQuestion, language)
      || knowledge.answerPythonSyntaxRoleQuestion(normalizedQuestion, language)
      || knowledge.answerPythonContractSearch(normalizedQuestion, language)
      || knowledge.answerPythonBareOrFuzzyQuestion(normalizedQuestion, language)
      || knowledge.answerPythonKnowledgeQuestion(normalizedQuestion, language);
  });

  const definitionSubjects = [
    ['list', 'list'], ['tuple', 'tuple'], ['dictionary', 'dict'], ['set', 'set'], ['string', 'str'],
    ['len', 'len'], ['range', 'range'], ['zip', 'zip'], ['enumerate', 'enumerate'], ['map', 'map'],
    ['filter', 'filter'], ['lambda', 'lambda'], ['closure', 'closure'], ['decorator', 'decorator'],
    ['generator', 'generator'], ['iterator', 'iterator'], ['iterable', 'iterable'], ['recursion', 'recursion'],
    ['inheritance', 'inheritance'], ['polymorphism', 'polymorphism'], ['encapsulation', 'encapsulation'],
    ['comprehension', 'comprehension'], ['exception', 'exception'], ['context manager', 'context manager'],
    ['asyncio', 'asyncio'], ['dataclass', 'dataclass'], ['descriptor', 'descriptor'], ['namespace', 'namespace'],
    ['scope', 'LEGB'], ['module', 'module'],
  ];
  const definitionTemplates = [
    ['What is {term}?', 'en'], ['Define {term}', 'en'], ['Explain {term} to me', 'en'],
    ['Qu’est-ce que {term} ?', 'fr'], ['Définis {term}', 'fr'], ['Explique {term}', 'fr'],
  ];
  for (const [term, expected] of definitionSubjects) {
    for (const [template, language] of definitionTemplates) {
      const question = template.replace('{term}', term);
      const answer = answerKnowledge(question, language);
      check(answer.length >= 80, `Definition too short: ${question}`);
      const localizedExpected = expected === 'decorator' && language === 'fr' ? 'decorat' : expected;
      check(normalize(answer).includes(normalize(localizedExpected.split(' ')[0])), `Definition lost subject: ${question}`);
      check((answer.match(/```/g) || []).length % 2 === 0, `Unclosed code fence: ${question}`);
    }
  }

  const comparisons = [
    ['list', 'tuple'], ['dict', 'set'], ['print', 'return'], ['sort', 'sorted'], ['is', '=='],
    ['iterator', 'iterable'], ['generator', 'list'], ['append', 'extend'], ['list.remove', 'list.pop'], ['str', 'bytes'],
  ];
  const comparisonTemplates = [
    ['What is the difference between {a} and {b}?', 'en'],
    ['Compare {a} versus {b}', 'en'],
    ['Quelle est la différence entre {a} et {b} ?', 'fr'],
    ['Compare {a} avec {b}', 'fr'],
  ];
  for (const [left, right] of comparisons) {
    for (const [template, language] of comparisonTemplates) {
      const question = template.replace('{a}', left).replace('{b}', right);
      const answer = answerKnowledge(question, language);
      check(answer.length >= 100, `Comparison too short: ${question}`);
      check(includesAll(answer, [left, right]), `Comparison omitted one side: ${question}`);
    }
  }

  const signatures = [
    ['any', 'any(iterable)'], ['all', 'all(iterable)'], ['len', 'len(s)'], ['map', 'map(function, iterable'],
    ['filter', 'filter(function, iterable)'], ['enumerate', 'enumerate(iterable'], ['zip', 'zip(*iterables'],
    ['str.count', 'str.count(sub'], ['list.index', 'list.index(x'], ['dict.get', 'dict.get(key'],
  ];
  const signatureTemplates = [
    ['How many arguments does {term} take?', 'en'], ['What is the argument order in {term}?', 'en'],
    ['Combien d’arguments accepte {term} ?', 'fr'], ['Quel est l’ordre des arguments de {term} ?', 'fr'],
  ];
  for (const [term, signature] of signatures) {
    for (const [template, language] of signatureTemplates) {
      const question = template.replace('{term}', term);
      const answer = answerKnowledge(question, language);
      check(answer.includes(signature), `Signature missing for ${question}`);
      check(/argument|param[eè]tre/i.test(answer), `Argument explanation missing for ${question}`);
    }
  }

  const classifications = [
    ['len', ['built-in function']], ['isalpha', ['str method']], ['yield', ['keyword', 'expression']],
    ['lambda', ['keyword', 'expression']], ['range', ['sequence type']], ['list', ['mutable sequence type']],
    ['dict', ['mapping type']], ['print', ['built-in function']],
  ];
  for (const [term, fragments] of classifications) {
    for (const question of [`Classify ${term}`, `What kind of Python thing is ${term}?`, `Classe ${term}`, `Quel type de construction est ${term} ?`]) {
      const language = /^(?:Classe|Quel)/.test(question) ? 'fr' : 'en';
      const answer = answerKnowledge(question, language);
      const expectedFragments = language === 'fr'
        ? fragments.map(fragment => fragment === 'built-in function' ? 'fonction intégrée' : fragment)
        : fragments;
      check(includesAll(answer, expectedFragments), `Classification failed: ${question}`);
    }
  }

  const protocols = [
    ['iterable', '__iter__'], ['iterator', '__next__'], ['generator', 'yield'], ['sequence', '__getitem__'],
    ['mapping', '__getitem__'], ['hashable', '__hash__'], ['callable', '__call__'], ['descriptor', '__get__'],
    ['context manager', '__enter__'], ['async iterator', '__anext__'], ['mutable', 'No universal mutable protocol'],
    ['immutable', 'No universal immutable protocol'],
  ];
  for (const [term, fragment] of protocols) {
    for (const [question, language] of [[`What is the ${term} protocol?`, 'en'], [`Explain ${term} in Python`, 'en']]) {
      const answer = answerKnowledge(question, language);
      check(answer.includes(fragment), `Protocol contract failed: ${question}`);
    }
  }

  const syntaxCases = [
    ['*', ['multiplication', 'unpacking']], ['**', ['exponentiation', 'mapping unpacking']],
    ['/', ['true division', 'positional-only']], ['//', ['floor division']], [':=', ['assignment expression']],
    ['->', ['return annotation']], ['@', ['decorator']], [':', ['indented suite', 'dictionaries']],
    ['.', ['attribute']], [',', ['tuple']], ['[]', ['subscription', 'slicing']], ['{}', ['dictionary', 'set']],
  ];
  for (const [token, fragments] of syntaxCases) {
    const answer = answerKnowledge(`What does \`${token}\` mean in Python?`, 'en');
    check(includesAll(answer, fragments), `Syntax roles failed for ${token}`);
  }

  const executionCases = [
    ['When are mutable default arguments evaluated?', ['once', 'def']],
    ['Explain decorator evaluation order', ['top to bottom', 'bottom to top']],
    ['Explain generator execution order', ['without running', 'next()']],
    ['What is the import execution order?', ['sys.modules', 'cached']],
    ['Explain short-circuit evaluation', ['left to right', 'operand']],
    ['What is the function call execution order?', ['arguments left to right', 'Bind values']],
    ['Explain list comprehension order of operations', ['first `for` iterable', '`if` filters']],
    ['Which local or global variable does Python use first?', ['LEGB', 'Enclosing']],
  ];
  for (const [question, fragments] of executionCases) {
    const answer = answerKnowledge(question, 'en');
    check(includesAll(answer, fragments), `Execution model failed: ${question}`);
  }

  const conversationSubjects = ['list', 'dict', 'tuple', 'generator', 'closure', 'lambda', 'decorator', 'iterator', 'set', 'recursion'];
  for (const subject of conversationSubjects) {
    const original = `What is ${subject}?`;
    for (const [followUp, expectedMode] of [['go deeper', 'deep'], ['give another example', 'examples'], ['explain more simply', 'simple']]) {
      const resolved = knowledge.resolveKnowledgeFollowUp(followUp, original, 'normal');
      check(resolved.usedContext && resolved.question === original && resolved.mode === expectedMode, `Follow-up lost ${subject}: ${followUp}`);
    }
    const switched = knowledge.resolveKnowledgeFollowUp('what about tuple?', original, 'normal');
    check(switched.question === 'what is tuple', `Subject switch failed after ${subject}`);
  }

  const misspellings = [
    ['leng', 'len'], ['dictonary', 'dict'], ['genrator', 'generator'], ['itterator', 'iterator'],
    ['decorater', 'decorator'], ['recurrsion', 'recursion'], ['comprehenshun', 'comprehension'], ['namepace', 'namespace'],
  ];
  for (const [query, correction] of misspellings) {
    const answer = answerKnowledge(query, 'en');
    check(answer.length >= 60 && normalize(answer).includes(correction), `Misspelling recovery failed: ${query}`);
  }

  const ambiguous = ['count', 'index', 'pop', 'remove', 'copy', 'clear', 'update'];
  for (const term of ambiguous) {
    const answer = answerKnowledge(`What is ${term}?`, 'en');
    check(/Clarification needed|Specify the owner|Python classification|Definition/i.test(answer), `Ambiguity handling failed: ${term}`);
  }

  const unclear = ['', 'it?', 'this', 'why', 'how?', 'cela', 'ça ?', 'pourquoi'];
  for (const question of unclear) check(intent.shouldClarifyGeneralAiQuestion(question), `Clarification gate failed: ${JSON.stringify(question)}`);
  for (const question of ['What is a list?', 'Compare list and tuple', 'Explain generator execution order']) {
    check(!intent.shouldClarifyGeneralAiQuestion(question), `Clear question was rejected: ${question}`);
  }

  const offTopic = ['best pizza nearby', 'weather tomorrow', 'who won the match'];
  for (const question of offTopic) check(intent.classifyGeneralAiIntent(question).intent === 'unknown', `Off-topic question misrouted: ${question}`);

  const verificationCases = [
    ['What is a list?', 'A list is a mutable ordered Python sequence.', true],
    ['What is a dictionary?', 'A tuple is an immutable sequence.', false],
    ['Explain code', '```python\nprint(1)', false],
    ['What is len?', '**Source and confidence**\nhttps://docs.python.org/3/library/functions.html#len', true],
  ];
  for (const [question, answer, valid] of verificationCases) check(verification.verifyGeneralAiAnswer(question, answer).valid === valid, `Verification gate failed: ${question}`);

  const sorted = timings.slice().sort((a, b) => a - b);
  const percentile = p => sorted[Math.min(sorted.length - 1, Math.floor(sorted.length * p))] || 0;
  const p95 = percentile(0.95);
  const maximum = sorted[sorted.length - 1] || 0;
  check(p95 < 25, `Knowledge response p95 too slow: ${p95.toFixed(2)}ms`);
  check(maximum < 150, `Single knowledge response too slow: ${maximum.toFixed(2)}ms`);

  console.log('General AI adversarial finalization benchmark');
  console.log(`Assertions: ${checks}`);
  console.log(`Timed local responses: ${timings.length}`);
  console.log(`Latency p50: ${percentile(0.5).toFixed(2)}ms`);
  console.log(`Latency p95: ${p95.toFixed(2)}ms`);
  console.log(`Latency max: ${maximum.toFixed(2)}ms`);
  console.log('Coverage: bilingual definitions, comparisons, signatures, classifications, protocols, syntax, execution order, conversations, misspellings, ambiguity, uncertainty, verification');

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
