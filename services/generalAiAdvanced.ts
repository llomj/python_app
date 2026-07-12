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
  string: ['string literals and quotes', 'indexing and slicing', 'immutability', 'methods (upper, split, join, replace)', 'f-strings', 'string formatting', 'regex basics', 'Unicode and encoding'],
  tuple: ['tuple literals', 'indexing and unpacking', 'immutability', 'namedtuple', 'tuple vs list', 'hashability', 'returning multiple values'],
  set: ['set literals', 'membership tests', 'union, intersection, difference', 'mutation methods', 'frozenset', 'set comprehensions', 'performance'],
  'exception-handling': ['try/except basics', 'catching specific exceptions', 'else and finally', 'raising exceptions', 'exception chaining', 'custom exceptions', 'context managers'],
  'file-io': ['open() and modes', 'reading (read, readline, readlines)', 'writing (write, writelines)', 'context managers (with)', 'encoding and binary mode', 'pathlib basics', 'CSV and JSON files'],
  'decorator-generator': ['iterators and iter()', 'generators and yield', 'generator expressions', 'decorator basics', 'decorators with arguments', 'generator-based pipelines', 'async generators'],
  'boolean': ['truth values (True/False)', 'truthiness protocol', 'comparison operators', 'and/or/not logic', 'short-circuit evaluation', 'boolean in conditions', 'De Morgan\'s laws'],
  'collections': ['list operations', 'dictionary operations', 'set operations', 'tuple usage', 'defaultdict for grouping', 'Counter for frequencies', 'namedtuple for records', 'deque for queues'],
  'type-hints': ['basic annotations', 'function signatures', 'Optional and Union', 'collections as types', 'type aliases', 'Protocol and structural typing', 'Generics'],
  'testing': ['test structure (arrange/act/assert)', 'pytest basics', 'fixtures', 'parameterized tests', 'mocking', 'property-based testing', 'test coverage'],
};

const PATHS_FR: Record<string, string[]> = {
  python: ['syntaxe et indentation', 'variables et types de données', 'conditions', 'boucles', 'fonctions', 'collections', 'fichiers et exceptions', 'modules', 'POO', 'tests'],
  list: ['littéraux de liste et indexation', 'découpage', 'méthodes de modification', 'itération', 'compréhensions de liste', 'tri et copie', 'listes imbriquées', 'complexité'],
  dictionary: ['paires clé-valeur', 'accès et get()', 'ajout et mise à jour', 'itération avec items()', 'compréhensions de dictionnaire', 'fusion', 'dictionnaires imbriqués', 'hachabilité'],
  function: ['paramètres et arguments', 'valeurs de retour', 'valeurs par défaut et mots-clés', '*args et **kwargs', 'portée et règle LEGB', 'fonctions d’ordre supérieur', 'fermetures', 'décorateurs'],
  oop: ['classes et objets', '__init__ et attributs', 'méthodes d’instance', 'méthodes de classe et statiques', 'héritage', 'composition', 'propriétés', 'protocoles et méthodes spéciales'],
  async: ['coroutines', 'await', 'tâches', 'gather()', 'délais d’attente', 'annulation', 'files', 'concurrence structurée'],
  string: ['littéraux de chaîne et guillemets', 'indexation et découpage', 'immutabilité', 'méthodes (upper, split, join, replace)', 'f-strings', 'formatage de chaîne', 'bases des regex', 'Unicode et encodage'],
  tuple: ['littéraux de tuple', 'indexation et déballage', 'immutabilité', 'namedtuple', 'tuple vs liste', 'hachabilité', 'renvoi de plusieurs valeurs'],
  set: ['littéraux d\'ensemble', 'tests d\'appartenance', 'union, intersection, différence', 'méthodes de modification', 'frozenset', 'compréhensions d\'ensemble', 'performances'],
  'exception-handling': ['bases try/except', 'capture d\'exceptions précises', 'else et finally', 'lever des exceptions', 'chaînage d\'exceptions', 'exceptions personnalisées', 'gestionnaires de contexte'],
  'file-io': ['open() et modes', 'lecture (read, readline, readlines)', 'écriture (write, writelines)', 'gestionnaires de contexte (with)', 'encodage et mode binaire', 'bases de pathlib', 'fichiers CSV et JSON'],
  'decorator-generator': ['itérateurs et iter()', 'générateurs et yield', 'expressions génératrices', 'bases des décorateurs', 'décorateurs avec arguments', 'pipelines basés sur générateurs', 'générateurs asynchrones'],
  'boolean': ['valeurs de vérité (True/False)', 'protocole de vérité', 'opérateurs de comparaison', 'logique and/or/not', 'évaluation court-circuit', 'booléens dans les conditions', 'lois de De Morgan'],
  'collections': ['opérations sur les listes', 'opérations sur les dictionnaires', 'opérations sur les ensembles', 'utilisation des tuples', 'defaultdict pour le groupement', 'Counter pour les fréquences', 'namedtuple pour les enregistrements', 'deque pour les files'],
  'type-hints': ['annotations de base', 'signatures de fonctions', 'Optional et Union', 'collections comme types', 'alias de types', 'Protocol et typage structurel', 'Generics'],
  'testing': ['structure de test (arranger/agir/affirmer)', 'bases de pytest', 'fixtures', 'tests paramétrés', 'mocking', 'tests basés sur les propriétés', 'couverture de test'],
};

const pathKey = (question: string): string => {
  const value = question.toLowerCase();
  if (/\b(?:dict|dictionary|dictionaries|dictionnaires?)\b/.test(value)) return 'dictionary';
  if (/\b(?:lists?|listes?)\b/.test(value)) return 'list';
  if (/\b(?:functions?|fonctions?)\b/.test(value)) return 'function';
  if (/\b(?:oop|poo|object.oriented|orient[eé]e objet|classes?)\b/.test(value)) return 'oop';
  if (/\b(?:async|asynchrone|await|asyncio)\b/.test(value)) return 'async';
  if (/\b(?:strings?|cha[îi]nes?|str|text)\b/.test(value)) return 'string';
  if (/\b(?:tuples?|tuples?)\b/.test(value)) return 'tuple';
  if (/\b(?:sets?|ensembles?)\b/.test(value) && !/\b(?:dict|dictionnary|dictionnaire)\b/.test(value)) return 'set';
  if (/\b(?:exception|error|erreur|try|except)\b/.test(value)) return 'exception-handling';
  if (/\b(?:file.?io|fichiers?|file operations?|lecture|write|read|open)\b/.test(value)) return 'file-io';
  if (/\b(?:generator|générateur|yield|itérateur|iterator)\b/.test(value)) return 'decorator-generator';
  if (/\b(?:boolean?|bool|truthy?|falsy?|vrai|faux|truth value)\b/.test(value) && !/set|dict/.test(value)) return 'boolean';
  if (/\b(?:defaultdict|counter|namedtuple|deque|ordereddict|collections)\b/.test(value)) return 'collections';
  if (/\b(?:type.?hint|annotation|typing|mypy)\b/.test(value)) return 'type-hints';
  if (/\b(?:test|pytest|unittest|testing|tests? unitaire)\b/.test(value)) return 'testing';
  if (/\b(?:integer|entier|int|number|nombre|numeric)\b/.test(value) && !/float|flottant/.test(value)) return 'integer';
  if (/\b(?:float|flottant|double|r[eé]el)\b/.test(value)) return 'float';
  if (/\b(?:method|m[eé]thode)\b/.test(value)) return 'method';
  if (/\b(?:slicing|slice|decoupage|d[eé]coupage|sous.?cha[îi]ne)\b/.test(value)) return 'slicing';
  if (/\b(?:comprehension|compr[eé]hension)\b/.test(value)) return 'comprehension';
  if (/\b(?:decorator|d[eé]corateur)\b/.test(value)) return 'decorator';
  if (/\b(?:recursion|r[eé]cursion|r[eé]cursif|recursive)\b/.test(value)) return 'recursion';
  if (/\b(?:module|modules?|paquets?|packages?)\b/.test(value) && !/import/.test(value)) return 'module';
  if (/\b(?:variable|variables?)\b/.test(value)) return 'variable';
  if (/\b(?:inheritance|h[eé]ritage|inherit|h[eé]riter)\b/.test(value)) return 'inheritance';
  if (/\blambda\b/.test(value)) return 'lambda';
  if (/\b(for|while)\s+loop/i.test(value)) return `${value.match(/\b(for|while)\b/i)![1].toLowerCase()}-loop`;
  if (/\bf[- ]?string\b/i.test(value)) return 'f-string';
  if (/\bunpack(?:ing)?\b/i.test(value)) return 'unpacking';
  if (/\bNone\b/.test(value)) return 'none';
  if (/\benumerate\b/i.test(value)) return 'enumerate';
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
  // Wildcard imports: `from module import *`
  if (/^\s*from\s+[\w.]+\s+import\s+\*/m.test(code)) findings.push({ severity: 'medium', text: fr ? '`import *` pollue l’espace de nommage et masque l’origine des noms. Importez des noms précis.' : '`import *` pollutes the namespace and hides where names come from. Import specific names.' });
  // `except: pass` — silently swallows every error
  if (/except\s*(?:\w+\s*)?:\s*\n\s*pass\s*(?:\n|$)/.test(code)) findings.push({ severity: 'high', text: fr ? 'Un bloc `except: pass` avale silencieusement toutes les erreurs. Au minimum, loggez l’exception.' : 'An `except: pass` block silently swallows every error. At minimum, log the exception.' });
  // `not x is y` style — should be `x is not y`
  if (/\bnot\s+\w+\s+is\b/.test(code)) findings.push({ severity: 'low', text: fr ? 'Préférez `x is not y` à `not x is y` (PEP 8).' : 'Prefer `x is not y` over `not x is y` (PEP 8).' });
  // `== True` / `== False` / `== None` — should use `is`
  const identityEquality = code.match(/(\w+)\s*==\s*(?:True|False|None)\b/);
  if (identityEquality) findings.push({ severity: 'medium', text: fr ? 'Utilisez `is` (pas `==`) avec `True`, `False` et `None`. Ex. : `if var is None`.' : 'Use `is` (not `==`) with `True`, `False`, and `None`. E.g. `if var is None`.' });
  // `assert` used for program validation (not testing) — disabled with `-O`
  if (/assert\s+\w+\s*(?:,|==|!=|is|in|\()/.test(code) && !code.includes('unittest') && !code.includes('pytest') && !code.includes('def test_')) findings.push({ severity: 'medium', text: fr ? '`assert` peut être désactivé avec `python -O`. Utilisez une vraie instruction `if` / `raise` pour la validation en production.' : '`assert` can be disabled with `python -O`. Use a real `if`/`raise` for production validation.' });
  // Bare `input()` without validation
  if (/input\([^)]*\)\s*==\s*['"]/.test(code) || /input\([^)]*\)\s*in\s*\[/.test(code)) findings.push({ severity: 'low', text: fr ? '`input()` renvoie `None` si l’utilisateur envoie EOF ou Ctrl+D. Utilisez `input(...).strip() or "default"` pour être robuste.' : '`input()` returns `None` on EOF/Ctrl+D. Use `input(...).strip() or "default"` for robustness.' });
  // Unnecessary `else` after `return` / `raise` / `continue` / `break`
  const elseAfterJump = code.match(/^\s*(?:return|raise|continue|break)\b.*\n\s*else\s*:/m);
  if (elseAfterJump) findings.push({ severity: 'low', text: fr ? '`else` après `return`/`raise`/`continue`/`break` est inutile. Déduentez le code de l\'`else`.' : '`else` after `return`/`raise`/`continue`/`break` is unnecessary. Unindent the `else` body.' });
  // PEP 8 naming: detect camelCase variables (should be snake_case)
  const camelVars = code.match(/\b[a-z][a-z]*[A-Z][a-zA-Z]*\s*=\s*[^=]/g);
  if (camelVars && camelVars.length > 1) findings.push({ severity: 'low', text: fr ? `Variables en camelCase détectées : utilisez snake_case (PEP 8). Ex. : ${camelVars[0].trim().split('=')[0].trim()}` : `camelCase variables detected: use snake_case (PEP 8). E.g.: ${camelVars[0].trim().split('=')[0].trim()}` });
  // Complex boolean expressions
  const boolCount = (code.match(/\b(?:and|or)\s/g) || []).length;
  if (boolCount >= 3) findings.push({ severity: 'low', text: fr ? `L'expression contient ${boolCount} opérateurs booléens. Envisagez de la décomposer.` : `The expression contains ${boolCount} boolean operators. Consider breaking it apart.` });
  // Deeply nested code
  const indentLevels = code.split('\n').map(line => line.search(/\S/)).filter(indent => indent > 0);
  const maxIndent = indentLevels.length ? Math.max(...indentLevels) : 0;
  if (maxIndent > 24) findings.push({ severity: 'medium', text: fr ? `Niveau d'indentation max : ${maxIndent / 4}. Envisagez d'extraire des fonctions.` : `Max indent level: ${maxIndent / 4}. Consider extracting functions.` });
  // String concatenation in loops: `result += chunk` is O(n²)
  if (/for\s+\w+\s+in\b[\s\S]*?result\s*\+=\s*\w+/ms.test(code) || /for\s+\w+\s+in\b[\s\S]*?\w+\s*\+=?\s*['"]/ms.test(code)) {
    findings.push({ severity: 'medium', text: fr ? 'Concaténation de chaînes dans une boucle — coût O(n²). Utilisez une liste et `"".join()`.' : 'String concatenation in a loop — O(n²) cost. Use a list and `"".join()`.' });
  }
  // Magic numbers: unexplained numeric literals
  const magicNumbers = code.match(/(?:^|[\s=,(+\-])(\d{3,})(?!\s*\%|\s*\*|\s*\/|\.\w)/gm);
  if (magicNumbers && magicNumbers.length >= 2) {
    findings.push({ severity: 'low', text: fr ? `Nombres magiques détectés : ${[...new Set(magicNumbers.map(m => m.trim()))].join(', ')}. Définissez des constantes nommées.` : `Magic numbers detected: ${[...new Set(magicNumbers.map(m => m.trim()))].join(', ')}. Define named constants.` });
  }
  // Missing docstrings on public functions
  const publicFunctions = [...code.matchAll(/^\s*def\s+(\w+)\s*\(/gm)].filter(([match]) => !match.includes('_')).map(m => m[1]);
  const documentedFunctions = [...code.matchAll(/^\s*def\s+\w+\s*\([^)]*\)\s*:\s*\n\s*"""/gm)].map(m => m[0].match(/def\s+(\w+)/)?.[1]);
  const missingDocs = publicFunctions.filter(name => !documentedFunctions?.includes(name));
  if (missingDocs.length > 1) findings.push({ severity: 'low', text: fr ? `Fonctions publiques sans docstring : ${missingDocs.join(', ')}.` : `Public functions without docstrings: ${missingDocs.join(', ')}.` });
  // Bare `raise` outside `except` block
  if (/^\s*raise\s(?!\w)/m.test(code)) findings.push({ severity: 'low', text: fr ? '`raise` nu (sans type d\'exception) ne fonctionne que dans un bloc `except`.' : 'A bare `raise` (without an exception type) only works inside an `except` block.' });
  // `except Exception` too broad
  if (/except\s+Exception\s*:/.test(code) && !/\bexcept\s+(?!Exception)\w+/.test(code)) findings.push({ severity: 'medium', text: fr ? '`except Exception:` attrape 99 % des erreurs Python. Capturez des exceptions précises.' : '`except Exception:` catches 99 % of Python errors. Catch specific exceptions instead.' });
  // `isinstance` chains
  const isinstanceCount = (code.match(/\bisinstance\s*\(/g) || []).length;
  if (isinstanceCount >= 3) findings.push({ severity: 'low', text: fr ? `${isinstanceCount} appels \`isinstance\` détectés. Envisagez le polymorphisme.` : `${isinstanceCount} \`isinstance\` calls detected. Consider polymorphism.` });
  // Unused variables (defined but never referenced after)
  const definedNames = [...code.matchAll(/\b([a-zA-Z_]\w*)\s*=\s*(?!.*for\s+\1)/g)].map(m => m[1]).filter(n => !['True', 'False', 'None'].includes(n));
  const usedNames = new Set([...code.matchAll(/\b([a-zA-Z_]\w*)\b/g)].map(m => m[1]));
  const unused = definedNames.filter(name => !usedNames.has(name) || code.match(new RegExp(`\\b${name}\\b`, 'g'))!.length <= 1);
  if (unused.length > 1) findings.push({ severity: 'low', text: fr ? `Variables potentiellement inutilisées : ${unused.join(', ')}` : `Potentially unused variables: ${unused.join(', ')}` });
  // — Security scan rules —
  // `subprocess.run(shell=True)` or `shell=True` anywhere
  if (/\bshell\s*=\s*True\b/i.test(code)) findings.push({ severity: 'high', text: fr ? '`shell=True` crée un risque d’injection de commande. Passez une liste d\'arguments plutôt qu\'une chaîne.' : '`shell=True` creates a command-injection risk. Pass an argument list instead of a single string.' });
  // `pickle.loads()` / `pickle.load()` — arbitrary code execution
  if (/pickle\.loads?\s*\(/.test(code)) findings.push({ severity: 'high', text: fr ? '`pickle.load()`/`loads()` exécute du code arbitraire lors de la désérialisation. Utilisez un format sécurisé (JSON) ou validez l\'origine.' : '`pickle.load()`/`loads()` executes arbitrary code on deserialization. Use a safe format (JSON) or verify the source.' });
  // `yaml.load()` without explicit Loader
  if (/yaml\.load\s*\(/.test(code) && !/yaml\.load\s*\([^)]*Loader/i.test(code)) findings.push({ severity: 'high', text: fr ? '`yaml.load()` sans `Loader` désactive toutes les protections. Utilisez `yaml.safe_load()` ou `Loader=yaml.SafeLoader`.' : '`yaml.load()` without `Loader` disables all protections. Use `yaml.safe_load()` or `Loader=yaml.SafeLoader`.' });
  // `requests.get()` / `requests.post()` without timeout
  if (/\brequests\.(?:get|post|put|delete|head)\s*\(/.test(code) && !/\btimeout\s*=/.test(code)) findings.push({ severity: 'medium', text: fr ? 'Appel `requests` sans `timeout` peut bloquer indéfiniment. Ajoutez `timeout=10` (ou une valeur adaptée).' : 'A `requests` call without `timeout` can hang forever. Add `timeout=10` (or an appropriate value).' });
  // `os.system()` or `os.popen()` — shell injection
  if (/\bos\.(?:system|popen)\s*\(/.test(code)) findings.push({ severity: 'high', text: fr ? '`os.system()`/`os.popen()` appelle un shell. Utilisez `subprocess.run()` avec une liste d\'arguments.' : '`os.system()`/`os.popen()` invokes a shell. Use `subprocess.run()` with an argument list.' });
  // SQL injection: f-string or `+` concatenation in a SQL query
  if (/(?:cursor\.execute|execute|executemany)\s*\(\s*f["']/.test(code) || /(?:cursor\.execute|execute)\s*\(\s*["'][^"']*\+(?:\s*["']|.*\bstr\b)/.test(code)) {
    findings.push({ severity: 'high', text: fr ? 'Concaténation dans une requête SQL — risque d\'injection SQL. Utilisez des paramètres (`?` ou `%s`) et passez les valeurs en second argument.' : 'String concatenation in a SQL query — SQL injection risk. Use parameterized queries (`?` or `%s`) and pass values as the second argument.' });
  }
  // Unsafe temp file: `tempfile.mktemp()`
  if (/tempfile\.mktemp\s*\(/.test(code)) findings.push({ severity: 'high', text: fr ? '`tempfile.mktemp()` est vulnérable aux attaques par course. Utilisez `tempfile.mkstemp()` ou `TemporaryFile()`.' : '`tempfile.mktemp()` is vulnerable to race-condition attacks. Use `tempfile.mkstemp()` or `TemporaryFile()`.' });
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
  string: [
    { id: 'string-upper', code: 'text = "hello"\nprint(text.upper())', expected: ['HELLO'], explanation: ['`.upper()` returns a new string with all characters converted to uppercase.', '`.upper()` renvoie une nouvelle chaîne avec tous les caractères convertis en majuscules.'], misconception: ['string method immutability', 'immutabilité des méthodes de chaîne'], hint: ['String methods always return new strings — the original is never modified.', 'Les méthodes de chaîne renvoient toujours de nouvelles chaînes — l\'originale n\'est jamais modifiée.'] },
    { id: 'string-split', code: 'data = "a,b,c"\nprint(data.split(","))', expected: ["['a', 'b', 'c']"], explanation: ['`.split(",")` splits the string at each comma and returns a list of substrings.', '`.split(",")` divise la chaîne à chaque virgule et renvoie une liste de sous-chaînes.'], misconception: ['split output type', 'type du résultat de split'], hint: ['`split()` always returns a list of strings, never a single string.', '`split()` renvoie toujours une liste de chaînes, jamais une seule chaîne.'] },
  ],
  tuple: [
    { id: 'tuple-index', code: 't = (10, 20, 30)\nprint(t[1])', expected: ['20'], explanation: ['Tuple indexing works like list indexing — `t[1]` returns the second element (index 1).', 'L\'indexation des tuples fonctionne comme celle des listes — `t[1]` renvoie le deuxième élément (indice 1).'], misconception: ['parentheses confusion with generator', 'confusion parenthèses avec générateur'], hint: ['`(x)` is just x; `(x,)` is a tuple with one element.', '`(x)` est simplement x ; `(x,)` est un tuple à un élément.'] },
  ],
  set: [
    { id: 'set-unique', code: 'values = {1, 2, 2, 3}\nprint(len(values))', expected: ['3'], explanation: ['Sets remove duplicates automatically, so `{1, 2, 2, 3}` contains only 1, 2, and 3.', 'Les ensembles suppriment automatiquement les doublons, donc `{1, 2, 2, 3}` ne contient que 1, 2 et 3.'], misconception: ['set deduplication', 'déduplication des ensembles'], hint: ['Sets only store unique elements — duplicates are silently discarded.', 'Les ensembles ne stockent que des éléments uniques — les doublons sont ignorés silencieusement.'] },
  ],
  boolean: [
    { id: 'boolean-not', code: 'print(not True)', expected: ['False'], explanation: ['`not True` evaluates to `False` — the negation of the boolean value.', '`not True` s\'évalue à `False` — la négation de la valeur booléenne.'], misconception: ['not operator as reversal', 'opérateur not comme inversion'], hint: ['`not` always returns a boolean. `not x` is True when x is falsy.', '`not` renvoie toujours un booléen. `not x` est True quand x est faux.'] },
  ],
  class: [
    { id: 'class-init', code: 'class Dog:\n    def __init__(self, name):\n        self.name = name\n\nd = Dog("Noll")\nprint(d.name)', expected: ['Noll'], explanation: ['`__init__` runs when the object is created, storing `"Noll"` in `self.name`.', '`__init__` s\'exécute à la création de l\'objet et stocke `"Noll"` dans `self.name`.'], misconception: ['self is passed automatically', 'self est passé automatiquement'], hint: ['`self` is the instance being created — Python passes it automatically.', '`self` est l\'instance en cours de création — Python le passe automatiquement.'] },
  ],
  generator: [
    { id: 'generator-next', code: 'def gen():\n    yield 1\n    yield 2\n\ng = gen()\nprint(next(g))\nprint(next(g))', expected: ['1\n2'], explanation: ['Each `next()` call resumes the generator and runs until the next `yield`.', 'Chaque appel `next()` reprend le générateur et s\'exécute jusqu\'au prochain `yield`.'], misconception: ['generator runs all at once', 'le générateur s\'exécute en une fois'], hint: ['Generators pause at each `yield` — they are lazy, not eager.', 'Les générateurs font une pause à chaque `yield` — ils sont paresseux, pas immédiats.'] },
  ],
  'exception-handling': [
    { id: 'exception-basic', code: 'try:\n    1 / 0\nexcept ZeroDivisionError:\n    print("caught")', expected: ['caught'], explanation: ['The `try` block raises `ZeroDivisionError`, which is caught by the matching `except` clause.', 'Le bloc `try` lève `ZeroDivisionError`, qui est attrapé par la clause `except` correspondante.'], misconception: ['exception breaks the program', 'l\'exception interrompt le programme'], hint: ['An `except` block handles the error — the program continues after it.', 'Un bloc `except` gère l\'erreur — le programme continue après.'] },
  ],
  integer: [
    { id: 'integer-division', code: 'print(3 / 2)\nprint(3 // 2)', expected: ['1.5\n1'], explanation: ['`/` always returns a float in Python 3; `//` performs floor (integer) division.', '`/` renvoie toujours un flottant en Python 3 ; `//` effectue la division entière.'], misconception: ['division operator behavior', 'comportement des opérateurs de division'], hint: ['`/` is true division; `//` is floor division. Try predicting both.', '`/` est la division exacte ; `//` est la division entière par défaut.'] },
  ],
  float: [
    { id: 'float-precision', code: 'print(0.1 + 0.2 == 0.3)\nprint(round(0.1 + 0.2, 1) == 0.3)', expected: ['False\nTrue'], explanation: ['`0.1 + 0.2` yields `0.30000000000000004`, so direct equality fails; rounding fixes the comparison.', '`0.1 + 0.2` donne `0.30000000000000004` ; l\'égalité directe échoue, l\'arrondi corrige la comparaison.'], misconception: ['floating-point precision is exact', 'la précision des flottants est exacte'], hint: ['Binary floating point cannot represent 0.1 or 0.2 exactly — a tiny rounding error exists.', 'Les flottants binaires ne peuvent pas représenter 0.1 ou 0.2 exactement — une petite erreur d\'arrondi existe.'] },
  ],
  method: [
    { id: 'method-return-none', code: 'items = [3, 1, 2]\nresult = items.sort()\nprint(items, result)', expected: ['[1, 2, 3] None'], explanation: ['.sort() mutates the list in-place and returns None; the variable `result` holds None.', '.sort() modifie la liste sur place et renvoie None ; la variable `result` contient None.'], misconception: ['mutating methods return the collection', 'les méthodes de modification renvoient la collection'], hint: ['`append()`, `sort()`, `reverse()` all modify in place and return None.', '`append()`, `sort()`, `reverse()` modifient sur place et renvoient None.'] },
  ],
  slicing: [
    { id: 'slicing-reverse', code: 'text = "python"\nprint(text[::-1])', expected: ['nohtyp'], explanation: ['A step of `-1` reverses the sequence: start at the end, move backward by one.', 'Un pas de `-1` inverse la séquence : commence à la fin, recule d\'un à chaque pas.'], misconception: ['reverse step direction', 'direction du pas inversé'], hint: ['A negative step means reverse traversal — `[::-1]` is the idiomatic reversal.', 'Un pas négatif signifie parcours inversé — `[::-1]` est l\'inversion idiomatique.'] },
  ],
  comprehension: [
    { id: 'comprehension-order', code: 'nums = [1, 2, 3, 4, 5]\nprint([n * 10 for n in nums if n % 2])', expected: ['[10, 30, 50]'], explanation: ['The `if` filters for truthy odd numbers, then the expression multiplies each by 10.', 'Le `if` filtre les nombres impairs (truthy), puis l\'expression multiplie chaque valeur par 10.'], misconception: ['comprehension expression runs before filter', 'l\'expression s\'exécute avant le filtre'], hint: ['The `if` clause comes after `for` and runs on each iteration before the expression.', 'La clause `if` vient après `for` et s\'exécute à chaque itération avant l\'expression.'] },
  ],
  decorator: [
    { id: 'decorator-wrapping', code: 'def decorator(func):\n    def wrapper():\n        print("before")\n        func()\n        print("after")\n    return wrapper\n\n@decorator\ndef say_hello():\n    print("hello")\n\nsay_hello()', expected: ['before\nhello\nafter'], explanation: ['The decorator replaces `say_hello` with `wrapper`, which calls the original between extra prints.', 'Le décorateur remplace `say_hello` par `wrapper`, qui appelle l\'original entre des prints supplémentaires.'], misconception: ['decorator only adds behavior after', 'le décorateur n\'ajoute qu\'après'], hint: ['Trace what `say_hello` actually points to after `@decorator` runs on the definition.', 'Suivez ce à quoi `say_hello` pointe après que `@decorator` s\'est exécuté sur la définition.'] },
  ],
  recursion: [
    { id: 'recursion-factorial', code: 'def factorial(n):\n    return 1 if n <= 1 else n * factorial(n - 1)\n\nprint(factorial(4))', expected: ['24'], explanation: ['`factorial(4)` unfolds as 4 × (3 × (2 × 1)) = 24, with each call stacking until the base case.', '`factorial(4)` se déplie comme 4 × (3 × (2 × 1)) = 24, chaque appel s\'empilant jusqu\'au cas de base.'], misconception: ['recursion result without understanding the stack', 'résultat de récursion sans comprendre la pile'], hint: ['Expand the expression: `factorial(4)` → `4 * factorial(3)` → `4 * (3 * factorial(2))` → etc.', 'Développez l\'expression : `factorial(4)` → `4 * factorial(3)` → `4 * (3 * factorial(2))` → etc.'] },
  ],
  module: [
    { id: 'module-import', code: 'from math import sqrt\nprint(sqrt(9))\nprint(sqrt)', expected: ['3.0\n<built-in function sqrt>'], explanation: ['`sqrt(9)` returns 3.0, and the bare name `sqrt` reveals a function object, not a number.', '`sqrt(9)` renvoie 3.0, et le nom `sqrt` seul révèle un objet fonction, pas un nombre.'], misconception: ['function objects vs call results', 'objet fonction vs résultat d\'appel'], hint: ['`print(sqrt)` prints the function itself; `print(sqrt(9)` prints the result of calling it.', '`print(sqrt)` affiche la fonction elle-même ; `print(sqrt(9))` affiche le résultat de son appel.'] },
  ],
  variable: [
    { id: 'variable-rebind', code: 'a = 1\nb = a\na = 2\nprint(a, b)', expected: ['2 1'], explanation: ['Integers are immutable. `b = a` copies the reference; reassigning `a` does not affect `b`.', 'Les entiers sont immuables. `b = a` copie la référence ; réaffecter `a` n\'affecte pas `b`.'], misconception: ['variables behave like pointers to shared state', 'les variables sont comme des pointeurs vers un état partagé'], hint: ['`b` holds the value it was assigned at that moment — later changes to `a` don\'t reach it.', '`b` contient la valeur qu\'il avait au moment de l\'affectation — les changements ultérieurs de `a` ne l\'atteignent pas.'] },
  ],
  inheritance: [
    { id: 'inheritance-super', code: 'class A:\n    def __init__(self):\n        self.v = 1\n\nclass B(A):\n    def __init__(self):\n        super().__init__()\n        self.v += 1\n\nb = B()\nprint(b.v)', expected: ['2'], explanation: ['`super().__init__()` calls `A.__init__`, setting `v = 1`. Then `B.__init__` increments it to 2.', '`super().__init__()` appelle `A.__init__`, qui définit `v = 1`. Puis `B.__init__` l\'incrémente à 2.'], misconception: ['overriding __init__ skips parent', 'surcharger __init__ saute le parent'], hint: ['Without `super()`, `v` would never be set. Trace the execution order.', 'Sans `super()`, `v` ne serait jamais défini. Suivez l\'ordre d\'exécution.'] },
  ],
  lambda: [
    { id: 'lambda-basic', code: 'f = lambda x, y: x + y\nprint(f(3, 4))', expected: ['7'], explanation: ['The lambda defines an anonymous function that adds two arguments then immediately returns the result.', 'Le lambda définit une fonction anonyme qui additionne deux arguments et renvoie immédiatement le résultat.'], misconception: ['lambda needs explicit return', 'lambda a besoin d\'un return explicite'], hint: ['A lambda body is a single expression — it is automatically returned.', 'Le corps d\'un lambda est une expression unique — elle est automatiquement renvoyée.'] },
  ],
  'for-loop': [
    { id: 'forloop-else', code: 'for n in [1, 2]:\n    print(n)\nelse:\n    print("done")', expected: ['1\n2\ndone'], explanation: ['The `else` clause runs after the loop finishes naturally (no `break`).', 'La clause `else` s\'exécute après la fin naturelle de la boucle (pas de `break`).'], misconception: ['else only runs with if', 'else ne s\'exécute qu\'avec if'], hint: ['A `for`\'s `else` runs when no `break` was hit — not when a condition is false.', 'Le `else` d\'un `for` s\'exécute quand aucun `break` n\'a été atteint — pas quand une condition est fausse.'] },
  ],
  'while-loop': [
    { id: 'while-break', code: 'n = 0\nwhile n < 10:\n    n += 3\n    if n > 5:\n        break\nprint(n)', expected: ['6'], explanation: ['`n` increments: 0→3→6. After the increment, `n > 5` is True, so `break` exits the loop.', '`n` s\'incrémente : 0→3→6. Après l\'incrément, `n > 5` est vrai, donc `break` quitte la boucle.'], misconception: ['break only ends the current iteration', 'break ne termine que l\'itération en cours'], hint: ['`break` exits the entire loop immediately, not just the current pass.', '`break` quitte la boucle entière immédiatement, pas seulement le passage en cours.'] },
  ],
  'file-io': [
    { id: 'fileio-read', code: 'with open("/tmp/demo.txt", "w") as f:\n    f.write("hello")\n\nwith open("/tmp/demo.txt") as f:\n    print(f.read())', expected: ['hello'], explanation: ['The first `with` block writes `"hello"`, then the second opens for reading and prints the content.', 'Le premier bloc `with` écrit `"hello"`, puis le second ouvre en lecture et affiche le contenu.'], misconception: ['file content exists without write', 'le contenu du fichier existe sans écriture'], hint: ['Trace the file state: empty → write "hello" → read → print.', 'Suivez l\'état du fichier : vide → écrire "hello" → lire → afficher.'] },
  ],
  none: [
    { id: 'none-is', code: 'def get_value(flag):\n    return None if flag else 42\n\nresult = get_value(True)\nprint(result is None)', expected: ['True'], explanation: ['`get_value(True)` returns `None`, and `None is None` is identity-true.', '`get_value(True)` renvoie `None`, et `None is None` est vrai par identité.'], misconception: ['None is checked with ==', 'None se vérifie avec =='], hint: ['Always use `is None` — None is a singleton, not just equal to itself.', 'Utilisez toujours `is None` — None est un singleton, pas seulement égal à lui-même.'] },
  ],
  'f-string': [
    { id: 'fstring-expression', code: 'x = 5\ny = 3\nprint(f"{x} + {y} = {x + y}")', expected: ['5 + 3 = 8'], explanation: ['Each `{expr}` in the f-string is evaluated and converted to a string inline.', 'Chaque `{expr}` dans la f-string est évalué et converti en chaîne en ligne.'], misconception: ['only variables work in f-string braces', 'seules les variables fonctionnent dans les accolades'], hint: ['Any valid Python expression can go inside `{}` in an f-string, not just variable names.', 'Toute expression Python valide peut aller dans les `{}` d\'une f-string, pas seulement des noms de variables.'] },
  ],
  unpacking: [
    { id: 'unpacking-list', code: 'pairs = [(1, "a"), (2, "b")]\nfor num, char in pairs:\n    print(num, char)', expected: ['1 a\n2 b'], explanation: ['Each tuple is unpacked into `num` and `char` directly in the `for` loop target.', 'Chaque tuple est déballé dans `num` et `char` directement dans la cible de la boucle `for`.'], misconception: ['iteration returns the whole tuple', 'l\'itération renvoie le tuple entier'], hint: ['`for num, char in pairs` unpacks each element — no indexing needed inside the loop.', '`for num, char in pairs` déballage de chaque élément — pas d\'indexation nécessaire dans la boucle.'] },
  ],
  async: [
    { id: 'async-coroutine', code: 'async def say():\n    return "hello"\n\nimport asyncio\nresult = asyncio.run(say())\nprint(result)', expected: ['hello'], explanation: ['`asyncio.run()` executes the coroutine and returns its value synchronously.', '`asyncio.run()` exécute la coroutine et renvoie sa valeur de manière synchrone.'], misconception: ['async functions return the value immediately', 'les fonctions async renvoient la valeur immédiatement'], hint: ['An `async def` returns a coroutine object — you need `await` or `asyncio.run()` to get the actual value.', 'Un `async def` renvoie un objet coroutine — vous avez besoin de `await` ou `asyncio.run()` pour obtenir la valeur réelle.'] },
  ],
  enumerate: [
    { id: 'enumerate-start', code: 'items = ["a", "b", "c"]\nfor i, v in enumerate(items, start=1):\n    print(i, v)', expected: ['1 a\n2 b\n3 c'], explanation: ['`enumerate()` yields (index, value) pairs starting from the specified `start` value.', '`enumerate()` produit des paires (indice, valeur) à partir de la valeur `start` spécifiée.'], misconception: ['enumerate always starts at 0', 'enumerate commence toujours à 0'], hint: ['`enumerate(items, start=1)` makes 1-based indices — useful for human-readable output.', '`enumerate(items, start=1)` produit des indices basés sur 1 — utile pour une sortie lisible.'] },
  ],
};

export const createAdaptiveQuiz = (subject: string, mode: GeneralAiResponseMode, language: AdvancedAiLanguage, variantIndex = 0, priorFocus = ''): GeneralAiQuizState => {
  const fr = language === 'fr';
  const key = pathKey(subject);
  const subjectLabel = fr ? ({ list: 'listes', dictionary: 'dictionnaires', function: 'fonctions', python: 'Python', string: 'chaînes', tuple: 'tuples', set: 'ensembles', boolean: 'booléens', class: 'classes', generator: 'générateurs', 'exception-handling': 'gestion des exceptions', integer: 'entiers', float: 'flottants', method: 'méthodes', slicing: 'découpage', comprehension: 'compréhensions', decorator: 'décorateurs', recursion: 'récursion', module: 'modules', variable: 'variables', inheritance: 'héritage', lambda: 'lambda', 'for-loop': 'boucles for', 'while-loop': 'boucles while', 'file-io': 'fichiers', none: 'None', 'f-string': 'f-strings', unpacking: 'déballage', async: 'async', enumerate: 'enumerate' } as Record<string, string>)[key] || key : key;
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

interface CodeMetrics {
  lines: number;
  loops: number;
  maxLoopDepth: number;
  comprehensions: number;
  sorts: number;
  collectionBuilds: number;
  branches: number;
  functions: number;
  recursive: boolean;
  mutations: number;
}

const extractPythonBlocks = (question: string): string[] => [...question.matchAll(/```(?:python)?\s*\n?([\s\S]*?)```/gi)]
  .map(match => match[1].trim())
  .filter(Boolean);

const codeMetrics = (code: string): CodeMetrics => {
  const sourceLines = code.split('\n').filter(line => line.trim() && !line.trim().startsWith('#'));
  let maxLoopDepth = 0;
  const loopIndents: number[] = [];
  for (const line of sourceLines) {
    const indent = line.match(/^\s*/)?.[0].replace(/\t/g, '    ').length || 0;
    while (loopIndents.length && indent <= loopIndents[loopIndents.length - 1]) loopIndents.pop();
    if (/^\s*(?:for|while)\b/.test(line)) {
      loopIndents.push(indent);
      maxLoopDepth = Math.max(maxLoopDepth, loopIndents.length);
    }
  }
  const functionNames = [...code.matchAll(/^\s*def\s+([A-Za-z_]\w*)\s*\(/gm)].map(match => match[1]);
  return {
    lines: sourceLines.length,
    loops: (code.match(/^\s*(?:for|while)\b/gm) || []).length,
    maxLoopDepth,
    comprehensions: (code.match(/[\[({][^\n\]}]*\bfor\s+\w+\s+in\b/g) || []).length,
    sorts: (code.match(/\b(?:sorted\s*\(|\.sort\s*\()/g) || []).length,
    collectionBuilds: (code.match(/\b(?:append|extend|add|update)\s*\(|(?:list|dict|set)\s*\(/g) || []).length,
    branches: (code.match(/^\s*(?:if|elif|match|case)\b/gm) || []).length,
    functions: functionNames.length,
    recursive: functionNames.some(name => new RegExp(`\\b${name}\\s*\\(`, 'g').test(code.replace(new RegExp(`def\\s+${name}\\s*\\(`), ''))),
    mutations: (code.match(/\.(?:append|extend|insert|remove|pop|clear|sort|reverse|add|discard|update)\s*\(/g) || []).length,
  };
};

const complexityEstimate = (metrics: CodeMetrics, fr: boolean): { time: string; space: string; evidence: string[]; caveat: string } => {
  let time = 'O(1)';
  const evidence: string[] = [];
  if (metrics.recursive) {
    time = fr ? 'dépend de la récurrence' : 'depends on the recurrence';
    evidence.push(fr ? 'Un appel récursif est détecté.' : 'A recursive call was detected.');
  } else if (metrics.maxLoopDepth >= 2) {
    time = `O(n^${metrics.maxLoopDepth})`;
    evidence.push(fr ? `${metrics.maxLoopDepth} boucles imbriquées ont été détectées.` : `${metrics.maxLoopDepth} nested loops were detected.`);
  } else if (metrics.sorts && (metrics.loops || metrics.comprehensions)) {
    time = 'O(n log n)';
    evidence.push(fr ? 'Un tri et un parcours de taille n ont été détectés.' : 'A sort and a size-n traversal were detected.');
  } else if (metrics.sorts) {
    time = 'O(n log n)';
    evidence.push(fr ? 'Un appel de tri domine généralement le coût.' : 'A sorting call normally dominates the cost.');
  } else if (metrics.loops || metrics.comprehensions) {
    time = 'O(n)';
    evidence.push(fr ? 'Un parcours simple ou une compréhension a été détecté.' : 'A single traversal or comprehension was detected.');
  } else {
    evidence.push(fr ? 'Aucune boucle, récursion ou opération de tri n’a été détectée.' : 'No loop, recursion, or sorting operation was detected.');
  }
  const growsCollection = metrics.comprehensions > 0 || metrics.collectionBuilds > 0 || metrics.sorts > 0;
  const space = growsCollection ? 'O(n)' : 'O(1)';
  if (growsCollection) evidence.push(fr ? 'Une collection proportionnelle à l’entrée peut être créée.' : 'A collection proportional to the input may be created.');
  else evidence.push(fr ? 'Seul un nombre constant de variables visibles est créé.' : 'Only a constant number of visible variables is created.');
  return {
    time,
    space,
    evidence,
    caveat: fr
      ? 'Estimation statique : `n` représente la taille de l’entrée. Les appels de bibliothèque, les tailles de plusieurs entrées et les chemins de branchement peuvent modifier le coût réel.'
      : 'Static estimate: `n` represents input size. Library calls, multiple input sizes, and branch paths can change the actual cost.',
  };
};

export const answerPythonComplexityRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:time complexity|space complexity|big[- ]?o|complexity|runtime cost|memory cost|complexit[eé]|notation grand o|co[uû]t temporel|co[uû]t m[eé]moire)(?=\s|[?:.,]|$)/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  if (!code || !/\n|def |for |while |sorted\(|\.sort\(/.test(code)) return null;
  const fr = language === 'fr';
  const metrics = codeMetrics(code);
  const estimate = complexityEstimate(metrics, fr);
  return [
    `**${fr ? 'Analyse de complexité' : 'Complexity analysis'}**`,
    `1. **${fr ? 'Temps estimé' : 'Estimated time'}: ${estimate.time}**`,
    `2. **${fr ? 'Espace auxiliaire estimé' : 'Estimated auxiliary space'}: ${estimate.space}**`,
    `3. **${fr ? 'Éléments détectés' : 'Detected evidence'}**\n${estimate.evidence.map(item => `- ${item}`).join('\n')}`,
    `4. **${fr ? 'Mesures structurelles' : 'Structural metrics'}**\n${fr ? 'lignes' : 'lines'}=${metrics.lines}, ${fr ? 'boucles' : 'loops'}=${metrics.loops}, ${fr ? 'profondeur' : 'depth'}=${metrics.maxLoopDepth}, ${fr ? 'compréhensions' : 'comprehensions'}=${metrics.comprehensions}, ${fr ? 'tris' : 'sorts'}=${metrics.sorts}.`,
    `5. **${fr ? 'Hypothèse et limite' : 'Assumption and limit'}**\n${estimate.caveat}`,
  ].join('\n\n');
};

export const answerPythonCodeComparison = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:compare|comparison|versus|vs\.?|which (?:code|solution|approach)|better solution|comparaison|compare|quelle solution|meilleure solution)\b/i.test(question)) return null;
  const blocks = extractPythonBlocks(question);
  if (blocks.length < 2) return null;
  const fr = language === 'fr';
  const first = codeMetrics(blocks[0]);
  const second = codeMetrics(blocks[1]);
  const firstEstimate = complexityEstimate(first, fr);
  const secondEstimate = complexityEstimate(second, fr);
  const complexityRank = (value: string) => value === 'O(1)' ? 1 : value === 'O(n)' ? 2 : value === 'O(n log n)' ? 3 : value.startsWith('O(n^') ? 4 : 5;
  const recommendation = firstEstimate.time === secondEstimate.time
    ? (first.lines <= second.lines
      ? (fr ? 'La solution A est plus concise, avec la même classe de complexité estimée.' : 'Solution A is more concise with the same estimated complexity class.')
      : (fr ? 'La solution B est plus concise, avec la même classe de complexité estimée.' : 'Solution B is more concise with the same estimated complexity class.'))
    : (complexityRank(firstEstimate.time) < complexityRank(secondEstimate.time)
      ? (fr ? 'La solution A présente la meilleure complexité asymptotique estimée.' : 'Solution A has the better estimated asymptotic complexity.')
      : (fr ? 'La solution B présente la meilleure complexité asymptotique estimée.' : 'Solution B has the better estimated asymptotic complexity.'));
  return [
    `**${fr ? 'Comparaison de deux solutions' : 'Two-solution code comparison'}**`,
    `| ${fr ? 'Critère' : 'Criterion'} | ${fr ? 'Solution A' : 'Solution A'} | ${fr ? 'Solution B' : 'Solution B'} |\n|---|---:|---:|\n| ${fr ? 'Temps estimé' : 'Estimated time'} | ${firstEstimate.time} | ${secondEstimate.time} |\n| ${fr ? 'Espace estimé' : 'Estimated space'} | ${firstEstimate.space} | ${secondEstimate.space} |\n| ${fr ? 'Lignes utiles' : 'Useful lines'} | ${first.lines} | ${second.lines} |\n| ${fr ? 'Boucles / profondeur' : 'Loops / depth'} | ${first.loops} / ${first.maxLoopDepth} | ${second.loops} / ${second.maxLoopDepth} |\n| ${fr ? 'Modifications visibles' : 'Visible mutations'} | ${first.mutations} | ${second.mutations} |`,
    `**${fr ? 'Recommandation' : 'Recommendation'}**\n${recommendation}`,
    `**${fr ? 'Pourquoi' : 'Why'}**\nA: ${firstEstimate.evidence.join(' ')}\n\nB: ${secondEstimate.evidence.join(' ')}`,
    `**${fr ? 'Vérification nécessaire' : 'Required verification'}**\n${fr ? 'Cette comparaison est structurelle. Exécutez les deux solutions avec les mêmes tests avant de conclure qu’elles produisent exactement le même comportement.' : 'This is a structural comparison. Run both solutions against the same tests before concluding that their behavior is identical.'}`,
  ].join('\n\n');
};

interface PythonProjectFile {
  path: string;
  module: string;
  code: string;
  imports: Array<{ module: string; names: string[]; relative: boolean }>;
  exports: Set<string>;
}

const projectFilesFromQuestion = (question: string): PythonProjectFile[] => {
  const blocks = [...question.matchAll(/```(?:python)?\s*\n?([\s\S]*?)```/gi)];
  return blocks.map((match, index) => {
    const raw = match[1].trim();
    const firstLine = raw.split('\n')[0]?.trim() || '';
    const commentName = firstLine.match(/^#\s*(?:file\s*:\s*)?([\w./-]+\.py)\s*$/i)?.[1];
    const prefix = question.slice(Math.max(0, (match.index || 0) - 100), match.index || 0);
    const labelName = prefix.match(/(?:^|\n)\s*([\w./-]+\.py)\s*:?[ \t]*$/i)?.[1];
    const path = commentName || labelName || `file${index + 1}.py`;
    const code = commentName ? raw.split('\n').slice(1).join('\n').trim() : raw;
    const module = path.replace(/\.py$/i, '').replace(/\/__init__$/, '').replace(/\//g, '.');
    const imports: PythonProjectFile['imports'] = [];
    for (const importMatch of code.matchAll(/^\s*import\s+([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)/gm)) {
      imports.push({ module: importMatch[1], names: [], relative: false });
    }
    for (const fromMatch of code.matchAll(/^\s*from\s+(\.*[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)\s+import\s+([^\n#]+)/gm)) {
      imports.push({
        module: fromMatch[1].replace(/^\.+/, ''),
        names: fromMatch[2].split(',').map(name => name.trim().split(/\s+as\s+/i)[0]).filter(Boolean),
        relative: fromMatch[1].startsWith('.'),
      });
    }
    const exports = new Set<string>();
    for (const exported of code.matchAll(/^(?:def|class)\s+([A-Za-z_]\w*)|^([A-Za-z_]\w*)\s*=/gm)) {
      exports.add(exported[1] || exported[2]);
    }
    return { path, module, code, imports, exports };
  });
};

export const answerPythonModuleProjectRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:modules?|imports?|packages?|multi[- ]?file|project structure|circular import|relative import|absolute import|__init__|__main__|fichiers? multiples?|structure (?:du |de )?projet|importation circulaire|importation relative|paquets?)\b/i.test(question)) return null;
  const fr = language === 'fr';
  const files = projectFilesFromQuestion(question);
  if (files.length < 2) {
    return [
      `**${fr ? 'Guide des modules et fichiers Python' : 'Python modules and files guide'}**`,
      `1. **${fr ? 'Module' : 'Module'}**\n${fr ? 'Chaque fichier `.py` est un module. Son nom importable vient de son chemin dans le projet.' : 'Each `.py` file is a module. Its importable name comes from its path in the project.'}`,
      `2. **${fr ? 'Paquet' : 'Package'}**\n${fr ? 'Un dossier de modules forme un paquet. `__init__.py` reste utile pour initialiser le paquet et exposer une API claire.' : 'A directory of modules forms a package. `__init__.py` remains useful for package initialization and a clear public API.'}`,
      `3. **${fr ? 'Import absolu' : 'Absolute import'}**\n\`from app.helpers import format_name\` — ${fr ? 'clair depuis la racine du paquet' : 'clear from the package root'}.`,
      `4. **${fr ? 'Import relatif' : 'Relative import'}**\n\`from .helpers import format_name\` — ${fr ? 'réservé au code exécuté dans un paquet' : 'for code running inside a package'}.`,
      `5. **${fr ? 'Point d’entrée' : 'Entry point'}**\n\`if __name__ == "__main__":\` ${fr ? 'sépare l’exécution directe du comportement lors d’un import' : 'separates direct execution from import behavior'}.`,
      `6. **${fr ? 'Structure recommandée' : 'Recommended structure'}**\n\`\`\`text\nproject/\n  app/\n    __init__.py\n    main.py\n    helpers.py\n  tests/\n    test_helpers.py\n\`\`\``,
      `7. **${fr ? 'Règle essentielle' : 'Core rule'}**\n${fr ? 'Placez la logique réutilisable dans des fonctions ou classes, gardez `main.py` léger et évitez les effets de bord au niveau du module.' : 'Put reusable logic in functions or classes, keep `main.py` thin, and avoid module-level side effects.'}`,
    ].join('\n\n');
  }

  const moduleMap = new Map(files.map(file => [file.module.split('.').at(-1) || file.module, file]));
  const edges: Array<{ from: string; to: string }> = [];
  const issues: string[] = [];
  for (const file of files) {
    for (const imported of file.imports) {
      const targetName = imported.module.split('.').at(-1) || imported.module;
      const target = moduleMap.get(targetName);
      if (!target) continue;
      edges.push({ from: file.module, to: target.module });
      for (const name of imported.names.filter(name => name !== '*')) {
        if (!target.exports.has(name)) {
          issues.push(fr
            ? `\`${file.path}\` importe \`${name}\` depuis \`${target.path}\`, mais aucune définition de niveau module portant ce nom n’est visible.`
            : `\`${file.path}\` imports \`${name}\` from \`${target.path}\`, but no module-level definition with that name is visible.`);
        }
      }
      if (imported.relative && !file.path.includes('/') && !files.some(candidate => candidate.path.endsWith('/__init__.py'))) {
        issues.push(fr
          ? `\`${file.path}\` utilise un import relatif sans contexte de paquet visible.`
          : `\`${file.path}\` uses a relative import without a visible package context.`);
      }
    }
  }
  for (const edge of edges) {
    if (edges.some(candidate => candidate.from === edge.to && candidate.to === edge.from)) {
      const cycle = [edge.from, edge.to].sort().join(' ↔ ');
      if (!issues.some(issue => issue.includes(cycle))) {
        issues.push(fr ? `Dépendance circulaire détectée : ${cycle}.` : `Circular dependency detected: ${cycle}.`);
      }
    }
  }
  const entryFiles = files.filter(file => /(?:^|\/)main\.py$/.test(file.path));
  for (const entry of entryFiles) {
    if (!/if\s+__name__\s*==\s*["']__main__["']\s*:/.test(entry.code) && /\bprint\s*\(|\binput\s*\(/.test(entry.code)) {
      issues.push(fr
        ? `\`${entry.path}\` exécute du code au niveau du module ; ajoutez une fonction \`main()\` et la garde \`if __name__ == "__main__":\`.`
        : `\`${entry.path}\` executes module-level code; add a \`main()\` function and an \`if __name__ == "__main__":\` guard.`);
    }
  }
  return [
    `**${fr ? 'Audit du projet Python multi-fichiers' : 'Multi-file Python project audit'}**`,
    `**${fr ? 'Fichiers détectés' : 'Detected files'} (${files.length})**\n${files.map((file, index) => `${index + 1}. \`${file.path}\` — ${file.exports.size} ${fr ? 'symboles exportés' : 'exported symbols'}`).join('\n')}`,
    `**${fr ? 'Graphe des imports locaux' : 'Local import graph'}**\n${edges.length ? edges.map(edge => `- \`${edge.from}\` → \`${edge.to}\``).join('\n') : (fr ? 'Aucun import entre les fichiers fournis.' : 'No imports between the supplied files.')}`,
    `**${fr ? 'Problèmes vérifiables' : 'Verifiable issues'}**\n${issues.length ? issues.map((issue, index) => `${index + 1}. ${issue}`).join('\n') : (fr ? 'Aucun nom importé manquant ni cycle direct n’a été détecté.' : 'No missing imported name or direct cycle was detected.')}`,
    `**${fr ? 'Limite de l’audit' : 'Audit limit'}**\n${fr ? 'Seuls les fichiers collés sont analysés. Les bibliothèques installées, les imports dynamiques et les chemins configurés à l’exécution ne sont pas vérifiés.' : 'Only pasted files are analyzed. Installed libraries, dynamic imports, and runtime path configuration are not verified.'}`,
  ].join('\n\n');
};

export const answerPythonMisconceptionRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:misconception|what am i misunderstanding|common mistake|why (?:is|does|do|am|are).*(?:none|wrong|change)|returns? none|unexpected behavior|conceptual error|malentendu|qu['’]est-ce que je comprends mal|erreur de compr[eé]hension|pourquoi.*(?:none|faux|change)|comportement inattendu)\b/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  const fr = language === 'fr';
  const findings: Array<{ title: string; explanation: string; correction: string }> = [];
  const inPlaceAssignment = code.match(/\b([A-Za-z_]\w*)\s*=\s*([A-Za-z_]\w*)\.(append|extend|insert|sort|reverse|remove|clear|update|add)\s*\(([^\n)]*)\)/);
  if (inPlaceAssignment) {
    findings.push({
      title: fr ? 'Modification sur place contre valeur de retour' : 'In-place mutation versus return value',
      explanation: fr ? 'La méthode modifie l’objet existant et renvoie `None`. Affecter son résultat remplace donc votre variable par `None`.' : 'The method changes the existing object and returns `None`. Assigning its result therefore stores `None` in your variable.',
      correction: `${inPlaceAssignment[2]}.${inPlaceAssignment[3]}(${inPlaceAssignment[4]})\n${inPlaceAssignment[1]} = ${inPlaceAssignment[2]}`,
    });
  }
  if (/\breturn\s+print\s*\(/.test(code)) {
    findings.push({
      title: fr ? '`print()` contre `return`' : '`print()` versus `return`',
      explanation: fr ? '`print()` affiche une valeur mais renvoie `None`. Une fonction doit utiliser `return valeur` si l’appelant a besoin du résultat.' : '`print()` displays a value but returns `None`. A function must use `return value` when its caller needs the result.',
      correction: 'def calculate(value):\n    return value * 2\n\nprint(calculate(4))',
    });
  } else if (/\bdef\s+\w+\([^)]*\):[\s\S]*?\bprint\s*\(/.test(code) && !/\breturn\b/.test(code)) {
    findings.push({
      title: fr ? 'Affichage sans résultat de fonction' : 'Display without a function result',
      explanation: fr ? 'La fonction affiche quelque chose, mais un appel comme `result = fonction()` reçoit `None` car aucun `return` n’est exécuté.' : 'The function displays something, but a call such as `result = function()` receives `None` because no `return` executes.',
      correction: 'def calculate(value):\n    return value * 2',
    });
  }
  const identityComparison = code.match(/\b([A-Za-z_]\w*)\s+is\s+((?:["'][^"']*["'])|[-+]?\d+(?:\.\d+)?)/);
  if (identityComparison) {
    findings.push({
      title: fr ? 'Identité contre égalité' : 'Identity versus equality',
      explanation: fr ? '`is` vérifie si deux références désignent le même objet. Utilisez `==` pour comparer des chaînes, nombres, listes ou autres valeurs.' : '`is` checks whether two references point to the same object. Use `==` to compare strings, numbers, lists, and other values.',
      correction: `if ${identityComparison[1]} == ${identityComparison[2]}:\n    print("equal value")`,
    });
  }
  if (/def\s+\w+\([^)]*=\s*(?:\[|\{|set\()/.test(code)) {
    findings.push({
      title: fr ? 'Argument par défaut mutable' : 'Mutable default argument',
      explanation: fr ? 'La même collection par défaut est réutilisée entre les appels, ce qui conserve un état inattendu.' : 'The same default collection is reused across calls, which preserves unexpected state.',
      correction: 'def collect(item, values=None):\n    if values is None:\n        values = []\n    values.append(item)\n    return values',
    });
  }
  if (/range\s*\(\s*len\s*\([^)]+\)\s*\+\s*1\s*\)/.test(code)) {
    findings.push({
      title: fr ? 'Limite supérieure hors plage' : 'Off-by-one upper bound',
      explanation: fr ? 'Le dernier indice valide vaut `len(sequence) - 1`. Inclure `len(sequence)` provoque un `IndexError`.' : 'The final valid index is `len(sequence) - 1`. Including `len(sequence)` causes an `IndexError`.',
      correction: 'for index in range(len(items)):\n    print(items[index])',
    });
  }
  const alias = code.match(/^\s*([A-Za-z_]\w*)\s*=\s*([A-Za-z_]\w*)\s*$/m);
  if (alias && new RegExp(`\\b${alias[1]}\\.(?:append|extend|sort|reverse|update|add)\\s*\\(`).test(code)) {
    findings.push({
      title: fr ? 'Alias contre copie' : 'Alias versus copy',
      explanation: fr ? `\`${alias[1]} = ${alias[2]}\` ne copie pas l’objet ; les deux noms désignent la même collection.` : `\`${alias[1]} = ${alias[2]}\` does not copy the object; both names refer to the same collection.`,
      correction: `${alias[1]} = ${alias[2]}.copy()`,
    });
  }
  // Late binding closure loop capture: `funcs = [lambda: i for i in range(5)]` or similar
  const loopLambda = code.match(/(?:for\s+(\w+)\s+in\s+.+:\s*)?\s*(?:funcs?|closures?|fns?)\s*=\s*\[.*(?:lambda|def\s+\w+).*\1/);
  if (loopLambda || /\[.*lambda\s*[:\w]*\s*:.*\b(\w+)\b.*\bfor\b.*\b\1\b/.test(code)) {
    findings.push({
      title: fr ? 'Fermeture à liaison tardive (boucle)' : 'Late-binding closure (loop capture)',
      explanation: fr ? 'Les fonctions créées dans la boucle capturent la variable de boucle (pas sa valeur au moment de la définition). Quand vous appelez la fonction, elle utilise la valeur finale de la boucle.' : 'Functions created in a loop capture the loop variable (not its value at definition time). When you call the function, it uses the final loop value.',
      correction: 'funcs = [lambda x=i: x for i in range(5)]  # capture current value\n# Or use functools.partial',
    });
  }
  // Generator exhaustion: using a generator twice
  if (/\bg\s*=\s*\(.*\)/.test(code) && /list\s*\(\s*g\s*\).*\n.*list\s*\(\s*g\s*\)/.test(code)) {
    findings.push({
      title: fr ? 'Épuisement du générateur' : 'Generator exhaustion',
      explanation: fr ? 'Un générateur se consomme une seule fois. Après l\'avoir parcouru entièrement, il est vide. Pour le réutiliser, créez-en un nouveau ou convertissez-le en liste.' : 'A generator can be iterated only once. After fully traversing it, it is empty. To reuse it, create a new one or convert it to a list.',
      correction: 'g = [x*2 for x in range(5)]   # list comprehension — reusable\ng = (x*2 for x in range(5))   # generator — one pass only\nprint(list(g))  # first pass: [0, 2, 4, 6, 8]\nprint(list(g))  # second pass: []',
    });
  }
  // Integer division: expecting `/` to floor in Python 3
  if (/print.*\d+\s*\/\s*\d+/.test(code) && !/\bfrom\s+__future__\s+import\s+division\b/.test(code)) {
    const divMatch = code.match(/(\d+)\s*\/\s*(\d+)/);
    if (divMatch && parseInt(divMatch[1]) % parseInt(divMatch[2]) !== 0) {
      findings.push({
        title: fr ? '`/` contre `//` en Python 3' : '`/` versus `//` in Python 3',
        explanation: fr ? 'Python 3 utilise la vraie division : `3 / 2` donne `1.5`. Utilisez `//` pour la division entière.' : 'Python 3 uses true division: `3 / 2` yields `1.5`. Use `//` for floor division.',
        correction: 'print(3 // 2)  # 1 — floor division\nprint(3 / 2)   # 1.5 — true division',
      });
    }
  }
  // String immutability: trying to assign to a string index
  if (/\[-?\d+\]\s*=\s*['"]/.test(code) && code.split('\n').some(line => /^\s*(?:str\s*=|[A-Za-z_]\w*\s*=\s*['"])/.test(line) && /\[-?\d+\]\s*=\s*['"]/.test(line))) {
    findings.push({
      title: fr ? 'Immutabilité des chaînes' : 'String immutability',
      explanation: fr ? 'Les chaînes Python sont immuables. Vous ne pouvez pas modifier un caractère par index ; créez une nouvelle chaîne.' : 'Python strings are immutable. You cannot change a character by index; create a new string instead.',
      correction: 'text = "hello"\ntext = text[:0] + "H" + text[1:]  # "Hello"\n# Or use text.replace("h", "H")',
    });
  }
  // Shadowing built-ins: using built-in names as variable names
  if (/^(?:list|dict|str|int|float|bool|set|tuple|type|input|print|len|range|zip|map|filter|sorted|enumerate)\s*=.*[{(\[]/.test(code.trim())) {
    findings.push({
      title: fr ? 'Masquage d\'un nom natif' : 'Shadowing a built-in name',
      explanation: fr ? `Réaffecter un nom natif comme \`${code.match(/^\w+/)[0]}\` empêche d'utiliser la fonction native dans la suite du programme.` : `Reassigning a built-in name like \`${code.match(/^\w+/)[0]}\` prevents using the native function later in the program.`,
      correction: 'original_list = [1, 2, 3]  # not "list ="\nitems_count = len(items)        # not "len = "',
    });
  }
  // `sorted()` vs `.sort()`: returning a new list vs mutating in-place
  if (/\.sort\s*\(\s*\)\s*$|\.sort\s*\(\s*\)\s*\n/.test(code)) {
    const sortReturn = code.match(/\b(\w+)\s*=\s*\w+\.sort\s*\(/);
    if (sortReturn) {
      findings.push({
        title: fr ? '`.sort()` contre `sorted()`' : '`.sort()` versus `sorted()`',
        explanation: fr ? '`list.sort()` modifie la liste sur place et renvoie `None`. Utilisez `sorted(list)` pour créer une nouvelle liste triée.' : '`list.sort()` mutates the list in place and returns `None`. Use `sorted(list)` to create a new sorted list.',
        correction: 'result = sorted(items)  # returns a new list\nitems.sort()             # returns None, items is sorted in-place',
      });
    }
  }
  // `isinstance()` vs `type()`: isinstance respects inheritance
  if (/\btype\s*\([^)]+\)\s*(?:==|is)\s*\w+\b/.test(code)) {
    findings.push({
      title: fr ? '`type()` contre `isinstance()`' : '`type()` versus `isinstance()`',
      explanation: fr ? '`type(x) == Class` ne fonctionne pas avec l\'héritage (sous-classes). Préférez `isinstance(x, Class)` qui respecte les hiérarchies.' : '`type(x) == Class` does not work with inheritance (subclasses). Prefer `isinstance(x, Class)` which respects class hierarchies.',
      correction: 'if isinstance(value, Class):  # correct: works with subclasses\nif type(value) == Class:    # fragile: fails on subclasses',
    });
  }
  // `__init__` is not a constructor
  if (/__init__.*construct/i.test(code) || /\b__new__\b/.test(code)) {
    findings.push({
      title: fr ? '`__init__` n\'est pas un constructeur' : '`__init__` is not a constructor',
      explanation: fr ? '`__init__` initialise une instance déjà créée. `__new__` est le vrai constructeur (crée l\'instance). Pour la plupart des classes, vous n\'avez besoin que de `__init__`.' : '`__init__` initialises an already-created instance. `__new__` is the actual constructor (creates the instance). For most classes, you only need `__init__`.',
      correction: 'class MyClass:\n    def __init__(self, value):   # initialiser — pas créer\n        self.value = value\n    def __new__(cls, value):      # constructeur — rarement nécessaire\n        return super().__new__(cls)',
    });
  }
  // Comprehension variable leaking (fixed in Python 3): list comps no longer leak
  if (/\[.*\bfor\s+\w+\s+in\b|\{.*\bfor\s+\w+\s+in\b|\(.*\bfor\s+\w+\s+in\b/.test(code)) {
    const loopVar = code.match(/for\s+(\w+)\s+in\b/);
    if (loopVar && new RegExp(`\\\\b${loopVar[1]}\\\\b`).test(code.replace(/\[[^\]]*\]/, ''))) {
      findings.push({
        title: fr ? 'Variable de compréhension (Python 3)' : 'Comprehension variable (Python 3)',
        explanation: fr ? 'En Python 3, les variables de compréhension de liste n\'affichent pas l\'espace de nommage englobant. Ce code fonctionne — aucun correctif nécessaire.' : 'In Python 3, list comprehension variables do not pollute the surrounding namespace. This code works — no fix needed.',
        correction: '# Python 3 guard: the loop variable stays inside the comprehension\nsquares = [x * x for x in range(5)]\n# "x" is NOT accessible here',
      });
    }
  }
  if (!findings.length) return null;
  return [
    `**${fr ? 'Diagnostic du malentendu Python' : 'Python misconception diagnosis'}**`,
    ...findings.map((finding, index) => `${index + 1}. **${finding.title}**\n${finding.explanation}\n\n\`\`\`python\n${finding.correction}\n\`\`\``),
    `**${fr ? 'Comment vérifier' : 'How to verify'}**\n${fr ? 'Affichez temporairement la valeur et son type avec `print(repr(value), type(value))`, puis testez au moins deux appels consécutifs.' : 'Temporarily inspect the value and type with `print(repr(value), type(value))`, then test at least two consecutive calls.'}`,
  ].join('\n\n');
};

export const answerGeneralAiProgressRequest = (
  question: string,
  mastery: TutorMasteryProfile,
  mistakes: GeneralAiMistakeProfile,
  language: AdvancedAiLanguage,
): string | null => {
  if (!/\b(?:my progress|learning progress|progress report|weak areas?|strengths?|what should i revise|mastery report|mes progr[eè]s|rapport de progression|points? faibles?|points? forts?|que dois-je r[eé]viser|bilan d['’]apprentissage)\b/i.test(question)) return null;
  const fr = language === 'fr';
  const masteryEntries = Object.entries(mastery).sort(([, left], [, right]) => right.views - left.views);
  const mistakeEntries = Object.entries(mistakes).sort(([, left], [, right]) => right.count - left.count || right.lastSeen - left.lastSeen);
  const totalInteractions = masteryEntries.reduce((sum, [, entry]) => sum + entry.views, 0);
  const totals = masteryEntries.reduce((sum, [, entry]) => ({
    beginner: sum.beginner + entry.beginner,
    intermediate: sum.intermediate + entry.intermediate,
    expert: sum.expert + entry.expert,
  }), { beginner: 0, intermediate: 0, expert: 0 });
  const nextFocus = mistakeEntries[0]?.[1].lastMistake || masteryEntries.at(-1)?.[0] || (fr ? 'fondamentaux Python' : 'Python fundamentals');
  return [
    `**${fr ? 'Bilan d’apprentissage Python' : 'Python learning progress report'}**`,
    `1. **${fr ? 'Activité enregistrée' : 'Recorded activity'}**\n${totalInteractions} ${fr ? 'interactions sur' : 'interactions across'} ${masteryEntries.length} ${fr ? 'sujets' : 'topics'}.`,
    `2. **${fr ? 'Niveaux d’explication utilisés' : 'Explanation levels used'}**\n${fr ? 'débutant' : 'beginner'}=${totals.beginner}, ${fr ? 'intermédiaire' : 'intermediate'}=${totals.intermediate}, expert=${totals.expert}.`,
    `3. **${fr ? 'Sujets les plus étudiés' : 'Most-studied topics'}**\n${masteryEntries.length ? masteryEntries.slice(0, 5).map(([subject, entry], index) => `${index + 1}. \`${subject}\` — ${entry.views}`).join('\n') : (fr ? 'Aucune activité enregistrée.' : 'No activity recorded yet.')}`,
    `4. **${fr ? 'Points faibles enregistrés' : 'Recorded weak points'}**\n${mistakeEntries.length ? mistakeEntries.slice(0, 5).map(([, entry], index) => `${index + 1}. ${entry.lastMistake} — ${entry.count}×`).join('\n') : (fr ? 'Aucune erreur de quiz enregistrée.' : 'No quiz mistakes recorded yet.')}`,
    `5. **${fr ? 'Prochaine priorité' : 'Next priority'}**\n${nextFocus}. ${fr ? 'Demandez une explication, un exemple, puis un quiz ciblé sur ce point.' : 'Ask for an explanation, one example, then a targeted quiz on this point.'}`,
    `**${fr ? 'Interprétation correcte' : 'Correct interpretation'}**\n${fr ? 'Les interactions mesurent l’exposition, pas une maîtrise prouvée. Les erreurs proviennent uniquement des quiz évalués dans cette application.' : 'Interactions measure exposure, not proven mastery. Mistakes come only from quizzes evaluated in this app.'}`,
  ].join('\n\n');
};

interface PythonVersionFeature {
  id: string;
  version: [number, number];
  label: [string, string];
  detect: RegExp;
  alternative: [string, string];
  source: string;
}

const PYTHON_VERSION_FEATURES: PythonVersionFeature[] = [
  { id: 'f-string', version: [3, 6], label: ['f-string syntax', 'syntaxe des f-strings'], detect: /(?:^|[^A-Za-z0-9_])f["'][^\n]*[{}]/m, alternative: ['Use `str.format()` on older Python.', 'Utilisez `str.format()` sur une version plus ancienne.'], source: 'https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals' },
  { id: 'dataclasses', version: [3, 7], label: ['the `dataclasses` standard-library module', 'le module standard `dataclasses`'], detect: /\b(?:from\s+dataclasses\s+import|import\s+dataclasses)\b/, alternative: ['Install the `dataclasses` backport for supported older releases.', 'Installez le rétroportage `dataclasses` pour les anciennes versions compatibles.'], source: 'https://docs.python.org/3/whatsnew/3.7.html#dataclasses' },
  { id: 'walrus', version: [3, 8], label: ['assignment expressions (`:=`)', 'les expressions d’affectation (`:=`)'], detect: /:=/, alternative: ['Assign the value on a separate line before the condition.', 'Affectez la valeur sur une ligne séparée avant la condition.'], source: 'https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions' },
  { id: 'zoneinfo', version: [3, 9], label: ['the `zoneinfo` standard-library module', 'le module standard `zoneinfo`'], detect: /\b(?:from\s+zoneinfo\s+import|import\s+zoneinfo)\b/, alternative: ['Use a maintained timezone dependency on older Python.', 'Utilisez une dépendance de fuseaux horaires maintenue sur une ancienne version.'], source: 'https://docs.python.org/3/whatsnew/3.9.html#zoneinfo' },
  { id: 'builtin-generics', version: [3, 9], label: ['built-in collection generics such as `list[str]`', 'les génériques intégrés comme `list[str]`'], detect: /\b(?:list|dict|set|tuple|type)\s*\[[^\]]+\]/, alternative: ['Use `typing.List`, `typing.Dict`, and related aliases.', 'Utilisez `typing.List`, `typing.Dict` et les alias associés.'], source: 'https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections' },
  { id: 'match', version: [3, 10], label: ['structural pattern matching (`match`/`case`)', 'le filtrage structurel (`match`/`case`)'], detect: /^\s*match\s+.+:|^\s*case\s+.+:/m, alternative: ['Rewrite simple cases with `if`/`elif`; complex patterns need explicit unpacking and guards.', 'Réécrivez les cas simples avec `if`/`elif` ; les motifs complexes exigent un déballage et des gardes explicites.'], source: 'https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching' },
  { id: 'union-operator', version: [3, 10], label: ['the `X | Y` union type syntax', 'la syntaxe de type union `X | Y`'], detect: /(?:^|[(:,]\s*)[A-Za-z_]\w*(?:\[[^\]]+\])?\s*\|\s*[A-Za-z_]\w*(?:\[[^\]]+\])?/m, alternative: ['Use `typing.Union[X, Y]`.', 'Utilisez `typing.Union[X, Y]`.'], source: 'https://docs.python.org/3/whatsnew/3.10.html#pep-604-new-type-union-operator' },
  { id: 'tomllib', version: [3, 11], label: ['the `tomllib` standard-library module', 'le module standard `tomllib`'], detect: /\b(?:from\s+tomllib\s+import|import\s+tomllib)\b/, alternative: ['Use the compatible `tomli` package on older Python.', 'Utilisez le paquet compatible `tomli` sur une ancienne version.'], source: 'https://docs.python.org/3/whatsnew/3.11.html#tomllib' },
  { id: 'taskgroup', version: [3, 11], label: ['`asyncio.TaskGroup`', '`asyncio.TaskGroup`'], detect: /\b(?:asyncio\.)?TaskGroup\s*\(/, alternative: ['Use carefully managed tasks with `asyncio.gather()` on older Python.', 'Gérez explicitement les tâches avec `asyncio.gather()` sur une ancienne version.'], source: 'https://docs.python.org/3/whatsnew/3.11.html#asyncio' },
  { id: 'exception-groups', version: [3, 11], label: ['exception groups and `except*`', 'les groupes d’exceptions et `except*`'], detect: /\bexcept\s*\*|\bExceptionGroup\s*\(/, alternative: ['Handle exceptions individually; there is no exact syntax-equivalent before 3.11.', 'Traitez les exceptions individuellement ; il n’existe pas d’équivalent syntaxique exact avant 3.11.'], source: 'https://docs.python.org/3/whatsnew/3.11.html#pep-654-exception-groups-and-except' },
  { id: 'type-statement', version: [3, 12], label: ['the `type` alias statement', 'l’instruction d’alias `type`'], detect: /^\s*type\s+[A-Za-z_]\w*(?:\[[^\]]+\])?\s*=/m, alternative: ['Use an assignment with `typing.TypeAlias`.', 'Utilisez une affectation avec `typing.TypeAlias`.'], source: 'https://docs.python.org/3/whatsnew/3.12.html#pep-695-type-parameter-syntax' },
  { id: 'removeprefix', version: [3, 9], label: ['`str.removeprefix()` / `str.removesuffix()`', '`str.removeprefix()` / `str.removesuffix()`'], detect: /\.removeprefix\s*\(|\.removesuffix\s*\(/, alternative: ['Use `.startswith()` + slicing for removeprefix; `.endswith()` + slicing for removesuffix.', 'Utilisez `.startswith()` + découpage pour removeprefix ; `.endswith()` + découpage pour removesuffix.'], source: 'https://docs.python.org/3/whatsnew/3.9.html#str' },
  { id: 'dict-merge', version: [3, 9], label: ['the `dict |` merge and `|=` update operators', 'les opérateurs de fusion `dict |` et de mise à jour `|=`'], detect: /[A-Za-z_]\w*\s*\|\s*=\s*\{/, alternative: ['Use `{**a, **b}` for merge or `.update()` for in-place update.', 'Utilisez `{**a, **b}` pour la fusion ou `.update()` pour la mise à jour sur place.'], source: 'https://docs.python.org/3/whatsnew/3.9.html#dictionary-merge-update-operators' },
  { id: 'batched', version: [3, 12], label: ['`itertools.batched()`', '`itertools.batched()`'], detect: /\bbatched\s*\(/, alternative: ['Implement a manual batching loop with `range(0, len(seq), n)`.', 'Implémentez une boucle de groupement manuelle avec `range(0, len(seq), n)`.'], source: 'https://docs.python.org/3/whatsnew/3.12.html#itertools' },
  { id: 'override', version: [3, 12], label: ['`typing.override` decorator', 'le décorateur `typing.override`'], detect: /\boverride\s*$|\boverride\s*\(/m, alternative: ['Use a comment or a consistent naming convention to mark overrides.', 'Utilisez un commentaire ou une convention de nommage cohérente pour signaler les surcharges.'], source: 'https://docs.python.org/3/whatsnew/3.12.html#typing' },
  { id: 'path-walk', version: [3, 12], label: ['`Path.walk()` method', 'la méthode `Path.walk()`'], detect: /\.walk\s*\(/, alternative: ['Use `os.walk()` on older Python (returns tuples, not a generator of `Path`).', 'Utilisez `os.walk()` sur une version plus ancienne (renvoie des tuples, pas un générateur de `Path`).'], source: 'https://docs.python.org/3/library/pathlib.html#pathlib.Path.walk' },
  { id: 'fstring-backslash', version: [3, 12], label: ['backslashes and quotes inside f-strings', 'antislash et guillemets dans les f-strings'], detect: /f["'][^\n]*?(?:\\[nrt'"\\]|["']\s*\{)/m, alternative: ['Pre-assign the escaped value to a variable outside the f-string.', 'Affectez la valeur échappée à une variable en dehors du f-string.'], source: 'https://docs.python.org/3/whatsnew/3.12.html#pep-701-fstring' },
  { id: 'deprecated-decorator', version: [3, 13], label: ['the `@warnings.deprecated()` decorator', 'le décorateur `@warnings.deprecated()`'], detect: /@(?:warnings\.)?deprecated/, alternative: ['Use a custom `@deprecated` decorator that calls `warnings.warn()`.', 'Utilisez un décorateur `@deprecated` personnalisé qui appelle `warnings.warn()`.'], source: 'https://docs.python.org/3/library/warnings.html#deprecated' },
  { id: 'copy-replace', version: [3, 13], label: ['`copy.replace()` for dataclasses', '`copy.replace()` pour les dataclasses'], detect: /\bcopy\.replace\s*\(/, alternative: ['Use `dataclasses.replace()` on older Python.', 'Utilisez `dataclasses.replace()` sur une version plus ancienne.'], source: 'https://docs.python.org/3/whatsnew/3.13.html#copy' },
  { id: 'parenthesized-context-managers', version: [3, 10], label: ['parenthesized context managers', 'gestionnaires de contexte parenthésés'], detect: /\bwith\s*\(\s*(?:open|mock|patch|contextlib\.)/s, alternative: ['Use separate `with` statements or `contextlib.ExitStack` on older Python.', 'Utilisez des instructions `with` séparées ou `contextlib.ExitStack` avec une version plus ancienne.'], source: 'https://docs.python.org/3/whatsnew/3.10.html#pep-634' },
  { id: 'match-case', version: [3, 10], label: ['`match`/`case` structural pattern matching', '`match`/`case` filtrage structurel'], detect: /\bmatch\s+\w+\s*:\s*\n\s*case\s/, alternative: ['Use `if`/`elif` chains with `isinstance()` checks on Python 3.9 and earlier.', 'Utilisez des chaînes `if`/`elif` avec des vérifications `isinstance()` avec Python 3.9 et antérieur.'], source: 'https://docs.python.org/3/whatsnew/3.10.html#pep-634' },
  { id: 'typing-self', version: [3, 11], label: ['`typing.Self` return type', 'le type de retour `typing.Self`'], detect: /\bSelf\b/, alternative: ['Use `from __future__ import annotations` or type the class name as a string literal on Python 3.10 and earlier.', 'Utilisez `from __future__ import annotations` ou tapez le nom de la classe en chaîne littérale avec Python 3.10 et antérieur.'], source: 'https://docs.python.org/3/whatsnew/3.11.html#pep-673' },
  { id: 'breakpoint', version: [3, 7], label: ['the `breakpoint()` built-in function', 'la fonction intégrée `breakpoint()`'], detect: /\bbreakpoint\s*\(/, alternative: ['Use `import pdb; pdb.set_trace()` on older Python.', 'Utilisez `import pdb; pdb.set_trace()` avec une version plus ancienne.'], source: 'https://docs.python.org/3/whatsnew/3.7.html#pep-553-breakpoint-built-in' },
  { id: 'positional-only', version: [3, 8], label: ['positional-only parameter syntax `/`', 'la syntaxe de paramètre positionnel seul `/`'], detect: /def\s+\w+[^)]*\/\s*[,)]/, alternative: ['Design around named parameters; there is no syntax-equivalent before 3.8.', 'Évitez de forcer le positionnel ; il n\'existe pas de syntaxe équivalente avant 3.8.'], source: 'https://docs.python.org/3/whatsnew/3.8.html#positional-only-parameters' },
  { id: 'fstring-equal', version: [3, 8], label: ['the `f"{x=}"` debug syntax', 'la syntaxe de débogage `f"{x=}"`'], detect: /f["'][^"']*=\s*(\{|\s*\{)/m, alternative: ['Print the name and value separately on older Python.', 'Affichez le nom et la valeur séparément avec une version antérieure.'], source: 'https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging' },
  { id: 'cached-property', version: [3, 8], label: ['the `@functools.cached_property` decorator', 'le décorateur `@functools.cached_property`'], detect: /\bcached_property\s*\(/, alternative: ['Store the computed value in `self.__dict__` manually on older Python.', 'Stockez la valeur calculée manuellement dans `self.__dict__` avec une version antérieure.'], source: 'https://docs.python.org/3/whatsnew/3.8.html#functools' },
];

const comparePythonVersions = (left: [number, number], right: [number, number]): number => left[0] - right[0] || left[1] - right[1];

export const answerPythonVersionCompatibilityRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:minimum python version|python version compatibility|will this (?:work|run)|compatible with python|requires? python|support python|version minimale de python|compatibilit[eé].*python|compatible (?:avec|sous) python|fonctionne(?:ra)? (?:avec|sous) python|n[eé]cessite python|prend en charge python)\b/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  if (!code || !/\n|import |def |class |match |type /.test(code)) return null;
  const fr = language === 'fr';
  const targetMatch = question.match(/python\s*(\d+)\.(\d+)/i);
  const target: [number, number] | null = targetMatch ? [Number(targetMatch[1]), Number(targetMatch[2])] : null;
  const detected = PYTHON_VERSION_FEATURES.filter(feature => feature.detect.test(code));
  const minimum = detected.reduce<[number, number]>((current, feature) => comparePythonVersions(feature.version, current) > 0 ? feature.version : current, [3, 0]);
  const compatible = target ? comparePythonVersions(target, minimum) >= 0 : null;
  return [
    `**${fr ? 'Vérification de compatibilité Python' : 'Python version compatibility check'}**`,
    `1. **${fr ? 'Version minimale détectée' : 'Detected minimum version'}: Python ${minimum[0]}.${minimum[1]}**`,
    target ? `2. **${fr ? 'Cible demandée' : 'Requested target'}: Python ${target[0]}.${target[1]} — ${compatible ? (fr ? 'compatible avec les fonctionnalités détectées' : 'compatible with the detected features') : (fr ? 'non compatible sans modification' : 'not compatible without changes')}**` : `2. **${fr ? 'Cible demandée' : 'Requested target'}**\n${fr ? 'Aucune version cible précise n’a été fournie.' : 'No exact target version was supplied.'}`,
    `3. **${fr ? 'Fonctionnalités déterminantes' : 'Version-determining features'}**\n${detected.length ? detected.map((feature, index) => `${index + 1}. Python ${feature.version[0]}.${feature.version[1]} — ${feature.label[fr ? 1 : 0]}\n${feature.alternative[fr ? 1 : 0]}`).join('\n\n') : (fr ? 'Aucune syntaxe postérieure à Python 3.0 n’a été reconnue dans cet extrait.' : 'No post-Python-3.0 syntax was recognized in this snippet.')}`,
    `4. **${fr ? 'Sources officielles' : 'Official sources'}**\n${detected.length ? [...new Set(detected.map(feature => feature.source))].map(url => `- ${url}`).join('\n') : '- https://docs.python.org/3/whatsnew/'}`,
    `**${fr ? 'Limite' : 'Limit'}**\n${fr ? 'Cette vérification couvre les fonctionnalités explicitement reconnues. Les versions des dépendances externes, les API supprimées et les branches non collées doivent être vérifiées séparément.' : 'This check covers explicitly recognized features. External dependency versions, removed APIs, and code paths not pasted here require separate verification.'}`,
  ].join('\n\n');
};

export const answerPythonFunctionContractRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:function contract|analy[sz]e (?:the )?contract|parameters?,? returns?|input.?output contract|preconditions?|postconditions?|contrat (?:de la )?fonction|analyse le contrat|param[eè]tres?,? retours?|pr[eé]conditions?|postconditions?)\b/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  const definition = code.match(/def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*(?:->\s*([^:\n]+))?\s*:/);
  if (!definition) return null;
  const fr = language === 'fr';
  const name = definition[1];
  const rawParameters = definition[2].split(',').map(value => value.trim()).filter(Boolean);
  const parameters = rawParameters.map(parameter => {
    const clean = parameter.replace(/^\*{1,2}/, '');
    const nameMatch = clean.match(/^([A-Za-z_]\w*)/);
    const typeMatch = clean.match(/:\s*([^=]+?)(?:\s*=|$)/);
    const defaultMatch = clean.match(/=\s*(.+)$/);
    return {
      name: nameMatch?.[1] || clean,
      type: typeMatch?.[1]?.trim() || (fr ? 'non annoté' : 'unannotated'),
      required: !defaultMatch && !parameter.startsWith('*'),
      defaultValue: defaultMatch?.[1]?.trim() || '',
      variadic: parameter.startsWith('*'),
    };
  });
  const parameterNames = new Set(parameters.map(parameter => parameter.name));
  const mutated = [...parameterNames].filter(parameter => (
    new RegExp(`\\b${parameter}\\.(?:append|extend|insert|remove|pop|clear|sort|reverse|add|discard|update)\\s*\\(`).test(code)
    || new RegExp(`\\b${parameter}\\s*\\[[^\\]]+\\]\\s*=`).test(code)
  ));
  const explicitRaises = [...code.matchAll(/\braise\s+([A-Za-z_]\w*)/g)].map(match => match[1]);
  const indexedParameters = parameters.filter(parameter => new RegExp(`\\b${parameter.name}\\s*\\[`).test(code));
  const indexedException = indexedParameters.some(parameter => /dict|mapping/.test(parameter.type.toLowerCase()))
    ? (fr ? '`KeyError` si la clé est absente' : '`KeyError` when the key is absent')
    : indexedParameters.length
      ? (fr ? '`IndexError` si l’indice est hors limites' : '`IndexError` when the index is out of range')
      : '';
  const inferredRaises = [
    indexedException,
    /\b(?:int|float)\s*\(/.test(code) ? (fr ? '`ValueError` pour une conversion invalide' : '`ValueError` for invalid conversion') : '',
    /\s\/\s|\/\//.test(code) ? (fr ? '`ZeroDivisionError` si le diviseur vaut zéro' : '`ZeroDivisionError` when the divisor is zero') : '',
  ].filter(Boolean);
  const returnExpressions = [...code.matchAll(/^\s*return(?:\s+(.+))?$/gm)].map(match => match[1]?.trim() || 'None');
  const returnType = definition[3]?.trim() || (returnExpressions.length ? (fr ? 'inféré depuis les chemins `return`' : 'inferred from `return` paths') : 'None');
  const definitionIndent = code.match(/^(\s*)def\s+[A-Za-z_]\w*/m)?.[1].replace(/\t/g, '    ').length || 0;
  const hasFunctionLevelReturn = [...code.matchAll(/^(\s*)return\b/gm)].some(match => match[1].replace(/\t/g, '    ').length === definitionIndent + 4);
  const missingReturnRisk = /\bif\b/.test(code) && returnExpressions.length > 0 && !hasFunctionLevelReturn && !/\belse\b/.test(code);
  const edgeCases = parameters.flatMap(parameter => {
    const type = parameter.type.toLowerCase();
    if (/list|sequence|iterable|dict|set|tuple/.test(type) || /items|values|numbers|data/.test(parameter.name)) return [fr ? `${parameter.name} vide` : `empty ${parameter.name}`];
    if (/str|string/.test(type) || /text|word|name/.test(parameter.name)) return [fr ? `${parameter.name} vide et Unicode` : `empty and Unicode ${parameter.name}`];
    if (/int|float|number/.test(type) || /count|number|value|size/.test(parameter.name)) return [fr ? `${parameter.name} égal à 0, négatif et très grand` : `${parameter.name} equal to 0, negative, and very large`];
    return [];
  });
  return [
    `**${fr ? 'Contrat de fonction analysé' : 'Analyzed function contract'}: ${name}()**`,
    `1. **${fr ? 'Signature' : 'Signature'}**\n\`${definition[0].replace(/:\s*$/, '')}\``,
    `2. **${fr ? 'Paramètres' : 'Parameters'}**\n${parameters.length ? parameters.map((parameter, index) => `${index + 1}. \`${parameter.name}\` — ${parameter.type}; ${parameter.variadic ? (fr ? 'variadique' : 'variadic') : parameter.required ? (fr ? 'obligatoire' : 'required') : `${fr ? 'facultatif, défaut' : 'optional, default'}=\`${parameter.defaultValue}\``}`).join('\n') : (fr ? 'Aucun paramètre.' : 'No parameters.')}`,
    `3. **${fr ? 'Retour' : 'Return contract'}**\n${fr ? 'Type' : 'Type'}: ${returnType}. ${fr ? 'Chemins visibles' : 'Visible paths'}: ${returnExpressions.length ? returnExpressions.map(value => `\`${value}\``).join(', ') : '`None`'}${missingReturnRisk ? (fr ? '. Attention : un chemin conditionnel peut atteindre la fin et renvoyer `None`.' : '. Warning: a conditional path may reach the end and return `None`.') : '.'}`,
    `4. **${fr ? 'Modification des entrées' : 'Input mutation'}**\n${mutated.length ? (fr ? `Modifie potentiellement : ${mutated.map(value => `\`${value}\``).join(', ')}.` : `Potentially mutates: ${mutated.map(value => `\`${value}\``).join(', ')}.`) : (fr ? 'Aucune modification visible des paramètres.' : 'No visible parameter mutation.')}`,
    `5. **${fr ? 'Exceptions' : 'Exceptions'}**\n${[...new Set([...explicitRaises.map(value => `\`${value}\` ${fr ? 'levée explicitement' : 'raised explicitly'}`), ...inferredRaises])].map((value, index) => `${index + 1}. ${value}`).join('\n') || (fr ? 'Aucune exception explicite ou opération risquée reconnue.' : 'No explicit exception or recognized risky operation.')}`,
    `6. **${fr ? 'Cas limites à tester' : 'Edge cases to test'}**\n${[...new Set(edgeCases)].map((value, index) => `${index + 1}. ${value}`).join('\n') || (fr ? 'Testez les valeurs limites définies par l’énoncé.' : 'Test the boundary values defined by the specification.')}`,
    `**${fr ? 'Limite de l’analyse' : 'Analysis limit'}**\n${fr ? 'Les annotations et opérations visibles sont analysées statiquement. Les appels externes et les exigences non écrites dans le code doivent être vérifiés séparément.' : 'Visible annotations and operations are analyzed statically. External calls and requirements not written in the code require separate verification.'}`,
  ].join('\n\n');
};

export const answerPythonTestExecutionRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:run|execute|check|verify|lance|ex[eé]cute|v[eé]rifie).{0,20}\b(?:tests?|assertions?)\b/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  const assertionCount = (code.match(/^\s*assert\s+/gm) || []).length;
  if (!assertionCount) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Exécution locale des tests demandée' : 'Local test execution requested'}**`,
    `${assertionCount} ${fr ? 'assertion(s) détectée(s). Chaque assertion sera exécutée séparément dans le moteur Python local borné.' : 'assertion(s) detected. Each assertion will run separately in the bounded local Python engine.'}`,
    fr ? 'Le rapport distinguera résultat attendu, résultat réel, réussite et exception.' : 'The report will separate expected value, actual value, pass status, and exceptions.',
  ].join('\n\n');
};

export const answerPythonDoctestExecutionRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/(?:doctests?|tests? de documentation|exemples? >>>)/i.test(question) || !/>>>/.test(question)) return null;
  const fr = language === 'fr';
  const examples = (question.match(/^\s*>>>\s+/gm) || []).length;
  return [
    `**${fr ? 'Exécution locale des doctests demandée' : 'Local doctest execution requested'}**`,
    fr
      ? `${examples} exemple(s) \`>>>\` détecté(s). Python comparera chaque résultat réel à la sortie écrite dans la docstring.`
      : `${examples} \`>>>\` example(s) detected. Python will compare each actual result with the output written in the docstring.`,
    fr
      ? 'Le rapport conservera les différences exactes produites par le module `doctest`.'
      : 'The report will preserve the exact differences produced by Python’s `doctest` module.',
  ].join('\n\n');
};
