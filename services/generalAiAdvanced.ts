import { extractGeneralAiPythonCode } from './generalAiRuntime';
import type { GeneralAiResponseMode } from './generalAiMode';
import type { TutorMasteryProfile } from './generalAiTutor';

export type AdvancedAiLanguage = 'en' | 'fr';

export interface GeneralAiQuizState {
  subject: string;
  expected: string[];
  explanation: string;
  prompt: string;
}

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

export const createAdaptiveQuiz = (subject: string, mode: GeneralAiResponseMode, language: AdvancedAiLanguage): GeneralAiQuizState => {
  const fr = language === 'fr';
  const key = pathKey(subject);
  const subjectLabel = fr ? ({ list: 'listes', dictionary: 'dictionnaires', function: 'fonctions', python: 'Python' } as Record<string, string>)[key] || key : key;
  const bank: Record<string, { code: string; expected: string[]; explanation: string }> = {
    list: { code: 'items = [1, 2]\nitems.append(3)\nprint(items[-1], len(items))', expected: ['3 3', '3, 3'], explanation: fr ? '`append()` ajoute 3, `[-1]` lit le dernier élément et `len()` renvoie trois.' : '`append()` adds 3, `[-1]` reads the final item, and `len()` returns three.' },
    dictionary: { code: 'data = {"a": 1}\ndata["b"] = data.get("a", 0) + 2\nprint(data["b"])', expected: ['3'], explanation: fr ? '`get("a", 0)` renvoie 1, puis 2 est ajouté et enregistré sous la clé `b`.' : '`get("a", 0)` returns 1, then 2 is added and stored under `b`.' },
    function: { code: 'def change(value):\n    value += 2\n    return value\n\nnumber = 5\nprint(change(number), number)', expected: ['7 5', '7, 5'], explanation: fr ? 'L’argument entier est réaffecté localement : la fonction renvoie 7, tandis que `number` reste égal à 5.' : 'The integer argument is rebound locally, so the returned value is 7 while `number` remains 5.' },
    python: { code: 'values = [1, 2, 3, 4]\nprint(sum(value for value in values if value % 2 == 0))', expected: ['6'], explanation: fr ? 'Le générateur conserve 2 et 4, puis `sum()` renvoie 6.' : 'The generator keeps 2 and 4, then `sum()` returns 6.' },
  };
  const item = bank[key] || bank.python;
  return {
    subject: key,
    expected: item.expected,
    explanation: item.explanation,
    prompt: [
      `**${fr ? 'Quiz adaptatif' : 'Adaptive quiz'}: ${subjectLabel} (${mode})**`,
      fr ? 'Prédisez exactement ce qui sera affiché, puis expliquez une étape.' : 'Predict the exact printed output, then explain one step.',
      `\`\`\`python\n${item.code}\n\`\`\``,
      fr ? 'Répondez sans exécuter le code. Je vérifierai la sortie et le raisonnement.' : 'Answer without running the code. I will check the output and reasoning.',
    ].join('\n\n'),
  };
};

export const evaluateAdaptiveQuiz = (answer: string, quiz: GeneralAiQuizState, language: AdvancedAiLanguage): { correct: boolean; text: string } => {
  const normalized = answer.toLowerCase().replace(/[\[\]()'"`]/g, '').replace(/\s+/g, ' ').trim();
  const correct = quiz.expected.some(expected => normalized.includes(expected.toLowerCase()));
  const fr = language === 'fr';
  return {
    correct,
    text: [
      `**${fr ? 'Résultat du quiz' : 'Quiz result'}: ${correct ? (fr ? 'correct' : 'correct') : (fr ? 'à revoir' : 'needs revision')}**`,
      correct ? (fr ? '✓ La sortie proposée correspond à l’exécution.' : '✓ Your predicted output matches execution.') : (fr ? `✗ La sortie attendue est \`${quiz.expected[0]}\`.` : `✗ The expected output is \`${quiz.expected[0]}\`.`),
      `**${fr ? 'Explication' : 'Explanation'}**\n${quiz.explanation}`,
      fr ? 'Demandez « autre quiz » pour continuer avec une variante.' : 'Ask “another quiz” to continue with a variation.',
    ].join('\n\n'),
  };
};
