import { extractGeneralAiPythonCode } from './generalAiRuntime';
import type { GeneralAiResponseMode } from './generalAiMode';
import type { TutorMasteryProfile } from './generalAiTutor';

export type AdvancedAiLanguage = 'en' | 'fr';

export interface GeneralAiQuizState {
  id?: string;
  subject: string;
  expected: string[];
  explanation: string;
  prompt: string;
  misconception?: string;
  hint?: string;
}

export interface GeneralAiMistakeEntry {
  count: number;
  lastSeen: number;
  lastMistake: string;
}

export type GeneralAiMistakeProfile = Record<string, GeneralAiMistakeEntry>;

const PATHS: Record<string, string[]> = {
  python: ['syntax and indentation', 'variables and data types', 'conditionals', 'loops', 'functions', 'collections', 'files and exceptions', 'modules', 'OOP', 'testing'],
  list: ['list literals and indexing', 'slicing', 'mutation methods', 'iteration', 'list comprehensions', 'sorting and copying', 'nested lists', 'complexity'],
  dictionary: ['key-value literals', 'lookup and get()', 'adding and updating', 'iteration with items()', 'dictionary comprehensions', 'merging', 'nested dictionaries', 'hashability'],
  function: ['parameters and arguments', 'return values', 'defaults and keywords', '*args and **kwargs', 'scope and LEGB', 'higher-order functions', 'closures', 'decorators'],
  oop: ['classes and objects', '__init__ and attributes', 'instance methods', 'class and static methods', 'inheritance', 'composition', 'properties', 'protocols and special methods'],
  async: ['coroutines', 'await', 'tasks', 'gather()', 'timeouts', 'cancellation', 'queues', 'structured concurrency'],
};

const PATHS_FR: Record<string, string[]> = {
  python: ['syntaxe et indentation', 'variables et types de données', 'conditions', 'boucles', 'fonctions', 'collections', 'fichiers et exceptions', 'modules', 'POO', 'tests'],
  list: ['littéraux de liste et indexation', 'découpage', 'méthodes de modification', 'itération', 'compréhensions de liste', 'tri et copie', 'listes imbriquées', 'complexité'],
  dictionary: ['paires clé-valeur', 'accès et get()', 'ajout et mise à jour', 'itération avec items()', 'compréhensions de dictionnaire', 'fusion', 'dictionnaires imbriqués', 'hachabilité'],
  function: ['paramètres et arguments', 'valeurs de retour', 'valeurs par défaut et mots-clés', '*args et **kwargs', 'portée et règle LEGB', 'fonctions d’ordre supérieur', 'fermetures', 'décorateurs'],
  oop: ['classes et objets', '__init__ et attributs', 'méthodes d’instance', 'méthodes de classe et statiques', 'héritage', 'composition', 'propriétés', 'protocoles et méthodes spéciales'],
  async: ['coroutines', 'await', 'tâches', 'gather()', 'délais d’attente', 'annulation', 'files', 'concurrence structurée'],
};

const pathKey = (question: string): string => {
  const value = question.toLowerCase();
  if (/\b(?:dict|dictionary|dictionaries|dictionnaires?)\b/.test(value)) return 'dictionary';
  if (/\b(?:lists?|listes?)\b/.test(value)) return 'list';
  if (/\b(?:functions?|fonctions?)\b/.test(value)) return 'function';
  if (/\b(?:oop|poo|object.oriented|orient[eé]e objet|classes?)\b/.test(value)) return 'oop';
  if (/\b(?:async|asynchrone|await|asyncio)\b/.test(value)) return 'async';
  return 'python';
};

export const answerPythonLearningPath = (
  question: string,
  profile: TutorMasteryProfile,
  language: AdvancedAiLanguage,
): string | null => {
  if (!/\b(?:learning path|roadmap|study plan|what should i learn|learn next|parcours|feuille de route|plan d['’][eé]tude|apprendre ensuite)\b/i.test(question)) return null;
  const key = pathKey(question);
  const fr = language === 'fr';
  const steps = (fr ? PATHS_FR : PATHS)[key] || (fr ? PATHS_FR.python : PATHS.python);
  const completed = new Set(Object.entries(profile).filter(([, entry]) => entry.views >= 3).map(([subject]) => subject.toLowerCase()));
  const completionSteps = PATHS[key] || PATHS.python;
  const isCompleted = (index: number) => [...completed].some(subject => completionSteps[index]?.includes(subject));
  const nextStep = Math.max(1, steps.findIndex((_, index) => !isCompleted(index)) + 1);
  return [
    `**${fr ? 'Parcours d’apprentissage adaptatif' : 'Adaptive learning path'}: ${key}**`,
    fr ? 'Chaque étape s’appuie sur la précédente. Les éléments déjà étudiés sont signalés.' : 'Each stage builds on the previous one. Previously studied subjects are marked.',
    ...steps.map((step, index) => {
      const done = isCompleted(index);
      return `${index + 1}. ${done ? '✓' : '○'} **${step}** — ${fr ? (done ? 'révision et exercice limite' : 'définition, exemple, exercice, vérification') : (done ? 'review and edge-case exercise' : 'definition, example, exercise, verification')}`;
    }),
    `**${fr ? 'Prochaine action' : 'Next action'}**\n${fr ? `Commencez par l’étape ${nextStep} et demandez « quiz-moi » après l’exemple.` : `Start at stage ${nextStep}, then ask “quiz me” after the example.`}`,
  ].join('\n\n');
};

const duplicateAssignments = (code: string): string[] => {
  const normalized = code.split('\n').map(line => line.trim()).filter(line => line && !line.startsWith('#'));
  return [...new Set(normalized.filter((line, index) => normalized.indexOf(line) !== index))];
};

export const answerPythonCodeQuality = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:review|quality|readability|pythonic|pep\s*8|performance|security|improve|refactor|analyse la qualit[eé]|lisibilit[eé]|am[eé]liore|refactorise)\b/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  if (!code || !/\n|=|def |class |print\(/.test(code)) return null;
  const fr = language === 'fr';
  const findings: Array<{ severity: string; text: string }> = [];
  if (/except\s*:/.test(code)) findings.push({ severity: 'high', text: fr ? 'Un `except:` nu masque toutes les erreurs. Capturez une exception précise.' : 'A bare `except:` hides every error. Catch a specific exception.' });
  if (/\b(?:eval|exec)\s*\(/.test(code)) findings.push({ severity: 'high', text: fr ? '`eval()`/`exec()` exécutent du texte comme du code et créent un risque de sécurité.' : '`eval()`/`exec()` execute text as code and create a security risk.' });
  if (/def\s+\w+\([^)]*=\s*(?:\[|\{|set\()/.test(code)) findings.push({ severity: 'high', text: fr ? 'Un argument par défaut mutable est partagé entre les appels. Utilisez `None` puis créez la collection dans la fonction.' : 'A mutable default argument is shared across calls. Use `None`, then create the collection inside the function.' });
  if (/\bfor\s+\w+\s+in\s+range\s*\(len\s*\(/.test(code)) findings.push({ severity: 'medium', text: fr ? 'Préférez l’itération directe ou `enumerate()` à `range(len(...))`.' : 'Prefer direct iteration or `enumerate()` over `range(len(...))`.' });
  if (/\b[A-Z][A-Z0-9_]*\s*=/.test(code) === false && /(?:password|api_key|secret)\s*=\s*['"][^'"]+/.test(code)) findings.push({ severity: 'high', text: fr ? 'Une valeur sensible semble codée en dur.' : 'A sensitive value appears to be hard-coded.' });
  const longLines = code.split('\n').map((line, index) => ({ line: index + 1, length: line.length })).filter(item => item.length > 100);
  if (longLines.length) findings.push({ severity: 'low', text: `${fr ? 'Lignes longues' : 'Long lines'}: ${longLines.map(item => item.line).join(', ')}.` });
  const duplicates = duplicateAssignments(code);
  if (duplicates.length) findings.push({ severity: 'medium', text: fr ? 'Des instructions identiques sont répétées ; extrayez une fonction ou une boucle.' : 'Identical statements are repeated; extract a function or loop.' });
  if (!/\bdef\b/.test(code) && code.split('\n').length > 12) findings.push({ severity: 'medium', text: fr ? 'Le script est assez long pour être découpé en fonctions testables.' : 'The script is long enough to split into testable functions.' });
  if (!findings.length) findings.push({ severity: 'pass', text: fr ? 'Aucun problème structurel évident détecté dans cet extrait.' : 'No obvious structural quality issue was detected in this snippet.' });
  return [
    `**${fr ? 'Revue de qualité du code' : 'Code-quality review'}**`,
    ...findings.map((finding, index) => `${index + 1}. **${finding.severity.toUpperCase()}** — ${finding.text}`),
    `**${fr ? 'Contrôles effectués' : 'Checks performed'}**\n${fr ? 'Exactitude visible, lisibilité, duplication, exceptions, sécurité, arguments par défaut, style d’itération et testabilité.' : 'Visible correctness, readability, duplication, exceptions, security, default arguments, iteration style, and testability.'}`,
    `**${fr ? 'Limite' : 'Limit'}**\n${fr ? 'Cette revue statique complète l’exécution locale ; elle ne remplace pas les tests du comportement attendu.' : 'This static review complements local execution; it does not replace behavioral tests.'}`,
  ].join('\n\n');
};

interface QuizTemplate {
  id: string;
  code: string;
  expected: string[];
  explanation: [string, string];
  misconception: [string, string];
  hint: [string, string];
}

const QUIZ_BANK: Record<string, QuizTemplate[]> = {
  list: [
    { id: 'list-mutation', code: 'items = [1, 2]\nitems.append(3)\nprint(items[-1], len(items))', expected: ['3 3', '3, 3'], explanation: ['`append()` adds 3, `[-1]` reads the final item, and `len()` returns three.', '`append()` ajoute 3, `[-1]` lit le dernier élément et `len()` renvoie trois.'], misconception: ['list mutation and negative indexing', 'modification de liste et indexation négative'], hint: ['Track the list after `append()` before reading `[-1]`.', 'Suivez la liste après `append()` avant de lire `[-1]`.'] },
    { id: 'list-slicing', code: 'values = [0, 1, 2, 3, 4]\nprint(values[1:4:2])', expected: ['[1, 3]'], explanation: ['The slice starts at index 1, stops before index 4, and advances by 2.', 'Le découpage commence à l’indice 1, s’arrête avant 4 et avance de 2.'], misconception: ['slice start, stop, and step rules', 'règles début, fin et pas du découpage'], hint: ['Read a slice as `start:stop:step`; the stop is excluded.', 'Lisez un découpage comme `début:fin:pas` ; la fin est exclue.'] },
    { id: 'list-comprehension', code: 'numbers = [1, 2, 3, 4]\nprint([n * 2 for n in numbers if n % 2 == 0])', expected: ['[4, 8]'], explanation: ['The filter keeps 2 and 4, then the expression doubles each retained value.', 'Le filtre conserve 2 et 4, puis l’expression double chaque valeur retenue.'], misconception: ['comprehension filter and expression order', 'ordre du filtre et de l’expression dans une compréhension'], hint: ['Apply the `if` test before calculating the output expression.', 'Appliquez le test `if` avant de calculer l’expression de sortie.'] },
  ],
  dictionary: [
    { id: 'dict-get', code: 'data = {"a": 1}\ndata["b"] = data.get("a", 0) + 2\nprint(data["b"])', expected: ['3'], explanation: ['`get("a", 0)` returns 1, then 2 is added and stored under `b`.', '`get("a", 0)` renvoie 1, puis 2 est ajouté et enregistré sous la clé `b`.'], misconception: ['dictionary lookup and assignment', 'recherche et affectation dans un dictionnaire'], hint: ['Resolve `get()` first, then follow the assignment to key `b`.', 'Résolvez d’abord `get()`, puis suivez l’affectation à la clé `b`.'] },
    { id: 'dict-default', code: 'scores = {"a": 2}\nprint(scores.get("b", 5), "b" in scores)', expected: ['5 False', '5, False'], explanation: ['`get()` returns the fallback 5 without inserting `b`, so membership is false.', '`get()` renvoie la valeur de secours 5 sans insérer `b` ; l’appartenance est donc fausse.'], misconception: ['the difference between get() and insertion', 'différence entre get() et insertion'], hint: ['A fallback returned by `get()` does not modify the dictionary.', 'Une valeur de secours renvoyée par `get()` ne modifie pas le dictionnaire.'] },
    { id: 'dict-comprehension', code: 'data = {n: n * n for n in range(3)}\nprint(data[2], len(data))', expected: ['4 3', '4, 3'], explanation: ['The keys are 0, 1, and 2; their values are their squares.', 'Les clés sont 0, 1 et 2 ; leurs valeurs sont leurs carrés.'], misconception: ['dictionary comprehension key-value construction', 'construction clé-valeur d’une compréhension de dictionnaire'], hint: ['Write the generated pairs for each value produced by `range(3)`.', 'Écrivez les paires générées pour chaque valeur produite par `range(3)`.'] },
  ],
  function: [
    { id: 'function-scope', code: 'def change(value):\n    value += 2\n    return value\n\nnumber = 5\nprint(change(number), number)', expected: ['7 5', '7, 5'], explanation: ['The integer argument is rebound locally, so the function returns 7 while `number` remains 5.', 'L’argument entier est réaffecté localement : la fonction renvoie 7, tandis que `number` reste égal à 5.'], misconception: ['local rebinding and immutable arguments', 'réaffectation locale et arguments immuables'], hint: ['Separate the local name `value` from the outer name `number`.', 'Distinguez le nom local `value` du nom externe `number`.'] },
    { id: 'function-return', code: 'def add(a, b=2):\n    return a + b\n\nprint(add(3), add(3, 4))', expected: ['5 7', '5, 7'], explanation: ['The first call uses the default value 2; the second overrides it with 4.', 'Le premier appel utilise la valeur par défaut 2 ; le second la remplace par 4.'], misconception: ['default and positional arguments', 'arguments positionnels et valeurs par défaut'], hint: ['Evaluate each call independently and check whether `b` was supplied.', 'Évaluez chaque appel séparément et vérifiez si `b` a été fourni.'] },
    { id: 'function-closure', code: 'def outer(x):\n    def inner(y):\n        return x + y\n    return inner\n\nadd_two = outer(2)\nprint(add_two(5))', expected: ['7'], explanation: ['`inner()` retains the enclosed value `x=2`, then adds the argument 5.', '`inner()` conserve la valeur englobante `x=2`, puis ajoute l’argument 5.'], misconception: ['closure state and returned functions', 'état d’une fermeture et fonction renvoyée'], hint: ['Follow what `outer(2)` returns before evaluating `add_two(5)`.', 'Suivez ce que renvoie `outer(2)` avant d’évaluer `add_two(5)`.'] },
  ],
  python: [
    { id: 'python-filter-sum', code: 'values = [1, 2, 3, 4]\nprint(sum(value for value in values if value % 2 == 0))', expected: ['6'], explanation: ['The generator keeps 2 and 4, then `sum()` returns 6.', 'Le générateur conserve 2 et 4, puis `sum()` renvoie 6.'], misconception: ['filtering before aggregation', 'filtrage avant agrégation'], hint: ['List the values that satisfy the condition before adding them.', 'Listez les valeurs qui satisfont la condition avant de les additionner.'] },
    { id: 'python-precedence', code: 'print(2 + 3 * 4 ** 2)', expected: ['50'], explanation: ['Exponentiation runs first, then multiplication, then addition: 16, 48, 50.', 'L’exponentiation s’exécute d’abord, puis la multiplication et l’addition : 16, 48, 50.'], misconception: ['operator precedence', 'priorité des opérateurs'], hint: ['Resolve `**`, then `*`, then `+`.', 'Résolvez `**`, puis `*`, puis `+`.'] },
    { id: 'python-boolean', code: 'value = 5\nprint(value > 2 and value < 5 or value == 5)', expected: ['True'], explanation: ['`and` is evaluated before `or`; the first group is false, but `value == 5` is true.', '`and` est évalué avant `or` ; le premier groupe est faux, mais `value == 5` est vrai.'], misconception: ['boolean operator precedence', 'priorité des opérateurs booléens'], hint: ['Evaluate both comparisons around `and`, then apply `or`.', 'Évaluez les comparaisons autour de `and`, puis appliquez `or`.'] },
  ],
};

export const createAdaptiveQuiz = (subject: string, mode: GeneralAiResponseMode, language: AdvancedAiLanguage, variantIndex = 0, priorFocus = ''): GeneralAiQuizState => {
  const fr = language === 'fr';
  const key = pathKey(subject);
  const subjectLabel = fr ? ({ list: 'listes', dictionary: 'dictionnaires', function: 'fonctions', python: 'Python' } as Record<string, string>)[key] || key : key;
  const subjectBank = QUIZ_BANK[key] || QUIZ_BANK.python;
  const item = subjectBank[Math.abs(variantIndex) % subjectBank.length];
  return {
    id: item.id,
    subject: key,
    expected: item.expected,
    explanation: item.explanation[fr ? 1 : 0],
    misconception: item.misconception[fr ? 1 : 0],
    hint: item.hint[fr ? 1 : 0],
    prompt: [
      `**${fr ? 'Quiz adaptatif' : 'Adaptive quiz'}: ${subjectLabel} (${mode})**`,
      fr ? 'Prédisez exactement ce qui sera affiché, puis expliquez une étape.' : 'Predict the exact printed output, then explain one step.',
      priorFocus ? `**${fr ? 'Point adapté à votre historique' : 'Adapted from your history'}**\n${priorFocus}` : '',
      `\`\`\`python\n${item.code}\n\`\`\``,
      fr ? 'Répondez sans exécuter le code. Je vérifierai la sortie et le raisonnement.' : 'Answer without running the code. I will check the output and reasoning.',
    ].filter(Boolean).join('\n\n'),
  };
};

export const evaluateAdaptiveQuiz = (answer: string, quiz: GeneralAiQuizState, language: AdvancedAiLanguage): { correct: boolean; text: string } => {
  const normalizeAnswer = (value: string) => value.toLowerCase().replace(/[\[\]()'"`,]/g, '').replace(/\s+/g, ' ').trim();
  const normalized = normalizeAnswer(answer);
  const correct = quiz.expected.some(expected => normalized.includes(normalizeAnswer(expected)));
  const fr = language === 'fr';
  return {
    correct,
    text: [
      `**${fr ? 'Résultat du quiz' : 'Quiz result'}: ${correct ? (fr ? 'correct' : 'correct') : (fr ? 'à revoir' : 'needs revision')}**`,
      correct ? (fr ? '✓ La sortie proposée correspond à l’exécution.' : '✓ Your predicted output matches execution.') : (fr ? `✗ La sortie attendue est \`${quiz.expected[0]}\`.` : `✗ The expected output is \`${quiz.expected[0]}\`.`),
      `**${fr ? 'Explication' : 'Explanation'}**\n${quiz.explanation}`,
      !correct && quiz.misconception ? `**${fr ? 'Point à revoir' : 'Misconception detected'}**\n${quiz.misconception}` : '',
      !correct && quiz.hint ? `**${fr ? 'Indice ciblé' : 'Targeted hint'}**\n${quiz.hint}` : '',
      fr ? 'Demandez « autre quiz » pour continuer avec une variante.' : 'Ask “another quiz” to continue with a variation.',
    ].filter(Boolean).join('\n\n'),
  };
};

export const updateGeneralAiMistakes = (profile: GeneralAiMistakeProfile, quiz: GeneralAiQuizState): GeneralAiMistakeProfile => {
  const key = `${quiz.subject}:${quiz.id || 'legacy'}`;
  const previous = profile[key];
  return {
    ...profile,
    [key]: {
      count: (previous?.count || 0) + 1,
      lastSeen: Date.now(),
      lastMistake: quiz.misconception || quiz.subject,
    },
  };
};

const testValueForParameter = (name: string, index: number): [string, string, string, string] => {
  if (/text|string|word|name|char|sentence/.test(name)) return ['"python"', '""', '"a"', '"naïve"'];
  if (/items|values|numbers|nums|list|sequence|data/.test(name)) return ['[1, 2, 3]', '[]', '[0]', '[-2, -2, 5]'];
  if (/dict|mapping|scores|record/.test(name)) return ['{"a": 1, "b": 2}', '{}', '{"a": 0}', '{"x": -1, "y": -1}'];
  if (/flag|enabled|valid/.test(name)) return ['True', 'False', 'True', 'False'];
  return index === 0 ? ['5', '0', '-1', '1'] : ['2', '0', '-3', '1'];
};

export const answerPythonTestCaseRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:generate|create|write|suggest|show|make|g[eé]n[eè]re|cr[eé]e|[eé]cris|propose|montre).{0,25}\b(?:tests?|test cases?|edge cases?|cas de test|cas limites?)\b/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  const definition = code.match(/def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)/);
  if (!definition) return null;
  const fr = language === 'fr';
  const functionName = definition[1];
  const parameters = definition[2].split(',').map(value => value.trim().split(/[=:]/)[0].trim()).filter(value => value && value !== 'self' && !value.startsWith('*'));
  const rows = ['normal', 'empty/boundary', 'negative/minimal', 'duplicates/unicode'].map((category, caseIndex) => {
    const args = parameters.map((parameter, index) => testValueForParameter(parameter.toLowerCase(), index)[caseIndex]);
    return { category, args };
  });
  const tuple = (args: string[]) => args.length === 1 ? `(${args[0]},)` : `(${args.join(', ')})`;
  return [
    `**${fr ? 'Cas de test générés' : 'Generated test cases'}: ${functionName}()**`,
    fr ? 'Ces cas couvrent le comportement normal, les limites et des entrées inhabituelles sans supposer une sortie qui n’est pas définie dans la question.' : 'These cases cover normal behavior, boundaries, and unusual inputs without inventing an expected result that the question does not define.',
    ...rows.map((row, index) => `${index + 1}. **${fr ? ({ 'normal': 'normal', 'empty/boundary': 'vide ou limite', 'negative/minimal': 'négatif ou minimal', 'duplicates/unicode': 'doublons ou Unicode' } as Record<string, string>)[row.category] : row.category}** — \`${functionName}(${row.args.join(', ')})\``),
    `**${fr ? 'Harnais exécutable' : 'Executable harness'}**\n\`\`\`python\ncases = [\n${rows.map(row => `    ${tuple(row.args)},`).join('\n')}\n]\n\nfor case in cases:\n    try:\n        print(case, "->", ${functionName}(*case))\n    except Exception as error:\n        print(case, "->", type(error).__name__, error)\n\`\`\``,
    `**${fr ? 'Étape suivante' : 'Next step'}**\n${fr ? 'Ajoutez les sorties attendues de l’énoncé, puis transformez chaque cas en assertion.' : 'Add the expected outputs from the specification, then convert each case into an assertion.'}`,
  ].join('\n\n');
};
