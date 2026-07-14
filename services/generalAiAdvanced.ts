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

export const answerPythonTraceRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  const code = extractGeneralAiPythonCode(question);
  if (!code) return null;
  const fr = language === 'fr';
  const lines = code.split('\n').filter(line => line.trim() && !/^\s*#/.test(line));
  if (lines.length < 2) return null;

  const state: Record<string, string> = {};
  const steps: string[] = [];
  let output = '';
  let loopGuard = 0;

  const substitute = (expr: string, depth = 0): string => {
    if (depth > 5) return expr;
    let result = expr;
    for (const [key, val] of Object.entries(state)) {
      result = result.replace(new RegExp(`\\b${key}\\b`, 'g'), val);
    }
    const simplify = (s: string): string => {
      const prev = s;
      s = s.replace(/(\d+)\s*\+\s*(\d+)/g, (_, a, b) => String(Number(a) + Number(b)));
      s = s.replace(/(\d+)\s*\*\s*(\d+)/g, (_, a, b) => String(Number(a) * Number(b)));
      s = s.replace(/(\d+)\s*-\s*(\d+)/g, (_, a, b) => String(Number(a) - Number(b)));
      return s === prev ? s : simplify(s);
    };
    const simplified = simplify(result);
    return simplified !== result ? substitute(simplified, depth + 1) : result;
  };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const indent = line.match(/^\s*/)?.[0] || '';
    const stripped = line.trim();
    const step = (text: string, stateUpdate: string, traceOut: string) => {
      steps.push([
        fr ? 'N' : 'S',
        i + 1,
        stripped.length > 60 ? stripped.slice(0, 57) + '...' : stripped,
        text,
        stateUpdate ? `${fr ? 'État' : 'State'}: {${stateUpdate}}` : '',
        traceOut ? `${fr ? 'Sortie' : 'Output'}: \`${traceOut}\`` : '',
      ].join(' | '));
    };

    if (/^\s*print\s*\(/.test(line)) {
      const content = stripped.match(/print\s*\((.+)\)/)?.[1] || '';
      const subbed = substitute(content);
      step(`${fr ? 'Affiche' : 'Prints'} \`${subbed}\``, '', subbed);
      output += (output ? '\n' : '') + subbed;
    } else if (/^\s*(?:return|yield)\s+(.+)/.test(line)) {
      const val = substitute(stripped.match(/^\s*(?:return|yield)\s+(.+)/)![1]);
      step(`${fr ? 'Renvoie' : 'Returns'} \`${val}\``, Object.entries(state).map(([k, v]) => `${k}: ${v}`).join(', '), '');
    } else if (/^\s*([A-Za-z_]\w*)\s*=\s*(.+)/.test(line)) {
      const [, name, expr] = stripped.match(/^\s*([A-Za-z_]\w*)\s*=\s*(.+)/)!;
      const subbed = substitute(expr);
      const displayVal = subbed;
      state[name] = displayVal;
      step(`${name} = ${displayVal}`, Object.entries(state).map(([k, v]) => `${k}: ${v}`).join(', '), '');
    } else if (new RegExp('^\\s*([A-Za-z_]\\w*)\\s*([+\\-*\\/%]|\\/\\/)\\s*=\\s*(.+)').test(line)) {
      const m = stripped.match(new RegExp('^\\s*([A-Za-z_]\\w*)\\s*([+\\-*\\/%]|\\/\\/)\\s*=\\s*(.+)'))!;
      const name = m[1], op = m[2], expr = m[3];
      const subbed = substitute(expr);
      const prev = state[name] || '?';
      const full = `${prev} ${op}= ${subbed}`;
      const resolved = substitute(`${prev} ${op} ${subbed}`);
      state[name] = resolved;
      step(`${full} → ${resolved}`, Object.entries(state).map(([k, v]) => `${k}: ${v}`).join(', '), '');
    } else if (/^\s*for\s+(\w+)\s+in\s+(.+):/.test(stripped)) {
      const [, loopVar, iterable] = stripped.match(/^\s*for\s+(\w+)\s+in\s+(.+):/)!;
      const raw = substitute(iterable);
      const items = raw.match(/\[([^\]]*)\]/)?.[1]?.split(',').map(s => s.trim()).filter(Boolean) || ['...'];
      if (loopGuard++ > 3) { steps.push(`⚠️ ${fr ? 'Boucle for limitée à 4 itérations' : 'For loop limited to 4 iterations'}`); break; }
      step(`${fr ? 'Boucle for sur' : 'For-loop over'} ${raw}`, '', '');
      for (let j = 0; j < items.length; j++) {
        state[loopVar] = items[j];
        const body = lines.slice(i + 1).find(l => l.trim() && /^\s*(?:print|[A-Za-z]|for|if|while)/.test(l)) || '';
        step(`  ${fr ? 'Itération' : 'Iter'} ${j + 1}: ${loopVar} = ${items[j]}${body ? ` → ${fr ? 'exécute' : 'runs'} \`${body.trim().slice(0, 30)}\`` : ''}`, Object.entries(state).map(([k, v]) => `${k}: ${v}`).join(', '), '');
      }
    } else if (/^\s*if\s+(.+):/.test(stripped)) {
      const cond = substitute(stripped.match(/^\s*if\s+(.+):/)![1]);
      const isTruthy = cond !== 'False' && !cond.startsWith('0') && cond !== 'None' && cond !== "''" && cond !== '""' && !cond.includes('==');
      step(`${fr ? 'Condition' : 'Condition'} \`${cond}\` ${isTruthy ? `${fr ? 'est vraie' : 'is truthy'}` : `${fr ? 'est fausse' : 'is falsy'}`}`, Object.entries(state).map(([k, v]) => `${k}: ${v}`).join(', '), '');
    } else if (/^\s*elif\s+(.+):/.test(stripped)) {
      const cond = substitute(stripped.match(/^\s*elif\s+(.+):/)![1]);
      step(`${fr ? 'Condition elif' : 'Elif condition'} \`${cond}\``, '', '');
    } else if (/^\s*else\s*:/.test(stripped)) {
      step(`${fr ? 'Branche else' : 'Else branch'}`, '', '');
    } else if (/^\s*while\s+(.+):/.test(stripped)) {
      if (loopGuard++ > 2) { steps.push(`⚠️ ${fr ? 'Boucle while limitée à 3 itérations' : 'While loop limited to 3 iterations'}`); break; }
      step(`${fr ? 'Boucle while' : 'While-loop'}`, '', '');
    } else if (/^\s*def\s+(\w+)/.test(stripped)) {
      const fnName = stripped.match(/^\s*def\s+(\w+)/)![1];
      step(`${fr ? 'Définit' : 'Defines'} \`${fnName}()\``, '', '');
    } else if (/^\s*class\s+(\w+)/.test(stripped)) {
      const clsName = stripped.match(/^\s*class\s+(\w+)/)![1];
      step(`${fr ? 'Définit' : 'Defines'} \`${clsName}\``, '', '');
    } else if (/\b(?:\.append\s*\(|\.extend\s*\()/.test(line)) {
      step(`${fr ? 'Modifie la liste' : 'Mutates list'}`, Object.entries(state).map(([k, v]) => `${k}: ${v}`).join(', '), '');
    } else {
      step(`${fr ? 'Exécute' : 'Executes'}`, Object.entries(state).map(([k, v]) => `${k}: ${v}`).join(', '), '');
    }
  }

  const finalState = Object.entries(state).filter(([k]) => !k.startsWith('_'));
  return [
    `**${fr ? 'Trace pas à pas' : 'Step-through trace'}**`,
    fr ? 'Voici comment ce code s\'exécute, ligne par ligne :' : 'Here is how this code runs, line by line:',
    ...steps.map((step, idx) => `${idx + 1}. ${step}`),
    finalState.length ? `**${fr ? 'État final' : 'Final state'}**\n\`${finalState.map(([k, v]) => `${k} = ${v}`).join(', ')}\`` : '',
    output ? `**${fr ? 'Sortie totale' : 'Total output'}**\n\`\`\`\n${output}\n\`\`\`` : '',
  ].filter(Boolean).join('\n\n');
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
  const lowerQ = question.toLowerCase();
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
  // `x += y` vs `x = x + y` for mutable types
  if (/\+=\s*\[/.test(code) || /\+=\s*\{/.test(code) || /\+=\s*set\(/.test(code)) {
    findings.push({
      title: fr ? '`+=` sur les listes/sets' : '`+=` on lists/sets',
      explanation: fr ? '`list += other` étend la liste sur place (appelle `__iadd__`). Pour les listes imbriquées ou dans des conteneurs, préférez `extend()` ou une nouvelle affectation.' : '`list += other` extends the list in-place (calls `__iadd__`). For nested lists or within containers, prefer `extend()` or a new assignment.',
      correction: '# In-place: modifies original\nitems += [4, 5]  # items is now [1, 2, 3, 4, 5]\n\n# Rebind: creates new list\nitems = items + [4, 5]',
    });
  }
  // Chained `==` or `!=` with non-transitive compares
  if (/==\s+\w+\s+==|!=\s+\w+\s+!=/.test(code)) {
    findings.push({
      title: fr ? 'Comparaisons chaînées' : 'Chained comparisons',
      explanation: fr ? '`a < b < c` se traduit par `a < b and b < c` (pas `(a < b) < c`). Python évalue b une seule fois. Cela fonctionne pour tous les opérateurs de comparaison.' : '`a < b < c` translates to `a < b and b < c` (not `(a < b) < c`). Python evaluates b only once. This works for all comparison operators.',
      correction: '# Chained comparison: a < b < c  →  a < b and b < c\nx, y, z = 1, 5, 10\nprint(x < y < z)  # True — chained correctly\nprint((x < y) < z)  # False — (True) < 10 → True < 10 → 1 < 10 → True',
    });
  }
  // Shared mutable initializer via `a = b = []`
  if (/\w+\s*=\s*\w+\s*=\s*\[\]|\w+\s*=\s*\w+\s*=\s*\{\}|\w+\s*=\s*\w+\s*=\s*set\(\)/.test(code)) {
    findings.push({
      title: fr ? 'Initialiseur mutable partagé' : 'Shared mutable initializer',
      explanation: fr ? '`a = b = []` crée une seule liste — `a` et `b` pointent vers le même objet. Les modifications via `b.append(x)` affectent aussi `a`.' : '`a = b = []` creates one list — both `a` and `b` point to the same object. Mutations via `b.append(x)` also affect `a`.',
      correction: 'a = []\nb = []   # separate lists\n\na.append(1)\nb.append(2)\nprint(a, b)  # [1] [2] — independent',
    });
  }
  // `except:` vs `except Exception:`
  if (/\bexcept\s*:/.test(code) && !/except\s+\w+/.test(code)) {
    findings.push({
      title: fr ? '`except:` nu attrape tout' : 'Bare `except:` catches everything',
      explanation: fr ? 'Un `except:` nu attrape `BaseException` — y compris `KeyboardInterrupt`, `SystemExit` et `GeneratorExit`. Utilisez `except Exception:` pour cibler les erreurs normales du programme.' : 'A bare `except:` catches `BaseException` — including `KeyboardInterrupt`, `SystemExit`, and `GeneratorExit`. Use `except Exception:` to target normal program errors.',
      correction: 'try:\n    risky_operation()\nexcept Exception:  # not bare except:\n    log_error()\n    raise',
    });
  }
  // Integer interning / small integer cache
  if (/\bis\b.*\d{3,}/.test(code) || /\d{3,}.*\bis\b/.test(code)) {
    findings.push({
      title: fr ? 'Mise en cache des petits entiers' : 'Small integer caching',
      explanation: fr ? 'Python met en cache les entiers de -5 à 256. `x is y` pour des entiers hors de cette plage peut être `False` même si les valeurs sont égales. Utilisez `==` pour comparer des valeurs.' : 'Python caches integers from -5 to 256. `x is y` for integers outside this range may be `False` even when values are equal. Use `==` to compare values.',
      correction: 'a, b = 257, 257\nprint(a is b)    # False (or True) — implementation-dependent\nprint(a == b)    # True — always correct',
    });
  }
  // `True == 1` and `False == 0` (bool is subclass of int)
  if (/True\s*==\s*1|False\s*==\s*0|sum\s*\([^)]*\[True/.test(code)) {
    findings.push({
      title: fr ? '`bool` est une sous-classe de `int`' : '`bool` is a subclass of `int`',
      explanation: fr ? '`True == 1` et `False == 0` sont vrais car `bool` hérite de `int`. `sum([True, False, True])` donne `2`. Utilisez `isinstance(x, bool)` avant `isinstance(x, int)` pour distinguer.' : '`True == 1` and `False == 0` are true because `bool` inherits from `int`. `sum([True, False, True])` yields `2`. Check `isinstance(x, bool)` before `isinstance(x, int)` to distinguish.',
      correction: 'total = sum([True, False, True])  # 2 — bools behave as ints\nprint(True + False)  # 1\n# Use explicit conversion if you need int:\ncount = sum(1 for x in items if condition(x))',
    });
  }
  // `copy.copy` vs `copy.deepcopy`
  if (/\.copy\s*\(\)/.test(code) && (/\blist\b|\bdict\b|nested/.test(code))) {
    findings.push({
      title: fr ? 'Copie superficielle contre copie profonde' : 'Shallow copy versus deep copy',
      explanation: fr ? '`list.copy()`, `dict.copy()` et `copy.copy()` créent une copie superficielle — la structure est copiée mais les objets imbriqués sont partagés. `copy.deepcopy()` copie récursivement tout.' : '`list.copy()`, `dict.copy()`, and `copy.copy()` create a shallow copy — the structure is copied but nested objects are shared. `copy.deepcopy()` recursively copies everything.',
      correction: 'import copy\n\noriginal = [[1, 2], [3, 4]]\nshallow = copy.copy(original)\ndeep = copy.deepcopy(original)\n\nshallow[0].append(99)  # affects original too\nprint(original)  # [[1, 2, 99], [3, 4]]\n\ndeep[0].append(99)  # does not affect original\nprint(original)  # [[1, 2, 99], [3, 4]]',
    });
  }
  // `re.match` vs `re.search`
  if (/\bre\.match\b/.test(code) || /regex.*match.*start|rechercher.*début/.test(lowerQ)) {
    findings.push({
      title: fr ? '`re.match()` contre `re.search()`' : '`re.match()` versus `re.search()`',
      explanation: fr ? '`re.match()` ne cherche une correspondance qu\'au début de la chaîne. `re.search()` cherche dans toute la chaîne. Beaucoup de développeurs utilisent `match` en pensant qu\'il cherche partout.' : '`re.match()` only checks the beginning of the string. `re.search()` searches the entire string. Many developers use `match` thinking it searches everywhere.',
      correction: 'import re\ntext = "hello world"\n\nprint(re.match("world", text))  # None — match at start only\nprint(re.search("world", text))  # <match> — search anywhere\n\n# For full-string match use fullmatch():\nprint(re.fullmatch("hello world", text))  # <match>',
    });
  }
  // `super().__init__()` call signature
  if (/\bsuper\(\).*\.__init__\(\)/.test(code) || /\bsuper\(\)\.__init__\([^)]*\)/.test(code)) {
    findings.push({
      title: fr ? 'Paramètres de `super().__init__()`' : '`super().__init__()` parameters',
      explanation: fr ? '`super().__init__()` appelle le constructeur de la classe parente. Vous devez passer *tous* les paramètres que le parent attend sauf `self` (le `self` est passé automatiquement).' : '`super().__init__()` calls the parent class constructor. You must pass *all* the parameters the parent expects except `self` (which is passed automatically).',
      correction: 'class Parent:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\nclass Child(Parent):\n    def __init__(self, name, age, extra):\n        super().__init__(name, age)  # passes self automatically\n        self.extra = extra',
    });
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
  { id: 'asyncio-run', version: [3, 7], label: ['the `asyncio.run()` entry point', 'le point d\'entrée `asyncio.run()`'], detect: /\basyncio\.run\s*\(/, alternative: ['Use `loop = asyncio.get_event_loop(); loop.run_until_complete(...)` on older Python.', 'Utilisez `loop = asyncio.get_event_loop(); loop.run_until_complete(...)` avec une version antérieure.'], source: 'https://docs.python.org/3/whatsnew/3.7.html#asyncio' },
  { id: 'dict-ordering', version: [3, 7], label: ['guaranteed dict insertion order', 'l\'ordre d\'insertion garanti des dictionnaires'], detect: /\b(?:dict|from collections import OrderedDict)\b(?!.*\bfrom __future__\b)/, alternative: ['On older Python, use `collections.OrderedDict` for guaranteed ordering.', 'Avec une version antérieure, utilisez `collections.OrderedDict` pour garantir l\'ordre.'], source: 'https://docs.python.org/3/whatsnew/3.7.html#python-3-7-data-model' },
  { id: 'functools-cache', version: [3, 9], label: ['`@functools.cache` decorator', 'le décorateur `@functools.cache`'], detect: /@functools\.cache|\bfunctools\.cache\b(?!\s*\()/, alternative: ['Use `@functools.lru_cache(maxsize=None)` on older Python.', 'Utilisez `@functools.lru_cache(maxsize=None)` avec une version antérieure.'], source: 'https://docs.python.org/3/library/functools.html#functools.cache' },
  { id: 'math-comb-perm', version: [3, 8], label: ['`math.comb()` and `math.perm()`', '`math.comb()` et `math.perm()`'], detect: /\bmath\.(?:comb|perm)\s*\(/, alternative: ['Implement manually using `math.factorial` or `scipy.special.comb` on older Python.', 'Implémentez manuellement avec `math.factorial` ou `scipy.special.comb` avec une version antérieure.'], source: 'https://docs.python.org/3/whatsnew/3.8.html#math' },
  { id: 'int-bitcount', version: [3, 8], label: ['`int.bit_count()` population count', 'le comptage de population `int.bit_count()`'], detect: /\.bit_count\s*\(/, alternative: ['Use `bin(x).count("1")` on older Python (slower but equivalent).', 'Utilisez `bin(x).count("1")` avec une version antérieure (plus lent mais équivalent).'], source: 'https://docs.python.org/3/whatsnew/3.8.html#int' },
  { id: 'math-prod', version: [3, 8], label: ['`math.prod()` product function', 'la fonction produit `math.prod()`'], detect: /\bmath\.prod\s*\(/, alternative: ['Use `functools.reduce(operator.mul, iterable, 1)` on older Python.', 'Utilisez `functools.reduce(operator.mul, iterable, 1)` avec une version antérieure.'], source: 'https://docs.python.org/3/whatsnew/3.8.html#math' },
  { id: 'typing-final', version: [3, 8], label: ['the `@typing.final` decorator', 'le décorateur `@typing.final`'], detect: /@(?:typing\.)?final\s*(?:\n|$)/m, alternative: ['Use a comment like `# final` and a custom metaclass on older Python.', 'Utilisez un commentaire `# final` et une métaclasse personnalisée avec une version antérieure.'], source: 'https://docs.python.org/3/whatsnew/3.8.html#typing' },
  { id: 'typing-literal', version: [3, 8], label: ['`typing.Literal` type', 'le type `typing.Literal`'], detect: /\bLiteral\b/, alternative: ['Use string compare or `enum.Enum` on older Python.', 'Utilisez la comparaison de chaînes ou `enum.Enum` avec une version antérieure.'], source: 'https://docs.python.org/3/whatsnew/3.8.html#typing' },
  { id: 'nullcontext', version: [3, 7], label: ['`contextlib.nullcontext`', '`contextlib.nullcontext`'], detect: /\bnullcontext\s*\(/, alternative: ['Create a dummy class that implements `__enter__`/`__exit__` on older Python.', 'Créez une classe factice qui implémente `__enter__`/`__exit__` avec une version antérieure.'], source: 'https://docs.python.org/3/library/contextlib.html#contextlib.nullcontext' },
  { id: 'typing-annotated', version: [3, 9], label: ['`typing.Annotated` type metadata', 'les métadonnées de type `typing.Annotated`'], detect: /\bAnnotated\b/, alternative: ['Use a comment or a custom `__metadata__` attribute on older Python.', 'Utilisez un commentaire ou un attribut personnalisé `__metadata__` avec une version antérieure.'], source: 'https://docs.python.org/3/whatsnew/3.9.html#typing' },
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

const pythonicFixups: Array<{ pattern: RegExp; fix: string; reasonEn: string; reasonFr: string }> = [
  { pattern: /\bfor\s+\w+\s+in\s+range\s*\(\s*len\s*\(/, fix: 'Use `enumerate()` or direct iteration', reasonEn: '`range(len(...))` is indirect and slower — iterate the collection directly', reasonFr: '`range(len(...))` est indirect et plus lent — itérez la collection directement' },
  { pattern: /\bnot\s+\w+\s+is\b/, fix: 'Use `x is not y` instead of `not x is y`', reasonEn: 'PEP 8 recommends `x is not y` as more readable', reasonFr: 'PEP 8 recommande `x is not y` pour une meilleure lisibilité' },
  { pattern: /^\s*(?:result|output)\s*=\s*""\s*\n[\s\S]*?for\s+\w+\s+in\b[\s\S]*?\1\s*\+=\s*\w+/m, fix: 'Use a list and `"".join()`', reasonEn: 'String concatenation in a loop is O(n²) — `"".join(list)` is O(n)', reasonFr: 'La concaténation de chaînes dans une boucle est O(n²) — `"".join(liste)` est O(n)' },
  { pattern: /if\s+\w+\s*==\s*True\b/, fix: 'Use `if x:` instead of `if x == True:`', reasonEn: '`== True` is redundant — `if x:` checks truthiness directly', reasonFr: '`== True` est redondant — `if x:` vérifie directement la vérité' },
  { pattern: /if\s+\w+\s*==\s*False\b/, fix: 'Use `if not x:` instead of `if x == False:`', reasonEn: '`== False` is redundant — `if not x:` is the idiomatic form', reasonFr: '`== False` est redondant — `if not x:` est la forme idiomatique' },
  { pattern: /except\s*:.*\n\s*pass/, fix: 'Catch a specific exception or at least log the error', reasonEn: 'A bare `except: pass` silently swallows every error including KeyboardInterrupt', reasonFr: 'Un `except: pass` nu avale silencieusement toutes les erreurs, y compris KeyboardInterrupt' },
  { pattern: /\bexec\s*\(|eval\s*\(/, fix: 'Avoid `exec()`/`eval()` — use safer alternatives', reasonEn: '`exec()`/`eval()` can execute arbitrary code and create security risks', reasonFr: '`exec()`/`eval()` peuvent exécuter du code arbitraire et créent des risques de sécurité' },
  { pattern: /=\s*\[\s*\]/, fix: 'Use `list()` or a literal directly', reasonEn: 'Prefer `[]` over `list()` for empty lists; use `list()` only when converting an iterable', reasonFr: 'Préférez `[]` à `list()` pour les listes vides ; utilisez `list()` seulement pour convertir un itérable' },
  { pattern: /\blambda\s+\w+\s*:\s*[^,)]+\s*\+\s*1\b/, fix: 'Inline the operation or define a named function', reasonEn: '`lambda x: x + 1` is better written as a named function if used more than once', reasonFr: '`lambda x: x + 1` est mieux écrit comme fonction nommée si utilisé plus d\'une fois' },
  { pattern: /\btry\s*:[\s\S]*?except\s*:\s*\n\s*pass/, fix: 'Never use bare `except: pass` — at minimum log the exception', reasonEn: 'Bare `except: pass` hides bugs and makes debugging impossible', reasonFr: 'Un `except: pass` nu cache les bugs et rend le débogage impossible' },
  { pattern: /while\s+True[\s\S]*?if\s+/, fix: 'Consider `for` with a break condition or a clear exit path', reasonEn: '`while True` with `break` works but should have a clearly bounded or documented exit path', reasonFr: '`while True` avec `break` fonctionne mais doit avoir un chemin de sortie clairement délimité ou documenté' },
  { pattern: /\bopen\s*\([^)]+\)[^.]*\n(?!\s*with\b)/, fix: 'Use `with open(...) as f:` for automatic cleanup', reasonEn: 'Files opened without `with` must be manually closed — `with` handles it automatically', reasonFr: 'Les fichiers ouverts sans `with` doivent être fermés manuellement — `with` le fait automatiquement' },
  { pattern: /\'[a-z]+(?:\s+[a-z]+){2,}\'/i, fix: 'Consider using a constant or variable', reasonEn: 'Repeated string literals should be stored in a named constant', reasonFr: 'Les chaînes littérales répétées doivent être stockées dans une constante nommée' },
];

export const answerPythonCodeRewriteRequest = (question: string, language: AdvancedAiLanguage): string | null => {
  const code = extractGeneralAiPythonCode(question);
  if (!code || code.split('\n').length < 2) return null;
  const fr = language === 'fr';
  const improvements: Array<{ line: number; before: string; after: string; reason: string }> = [];
  const lines = code.split('\n');
  let rewritten = code;
  for (const fixup of pythonicFixups) {
    if (fixup.pattern.test(code)) {
      const matchedLine = lines.findIndex(l => fixup.pattern.test(l));
      if (matchedLine >= 0) {
        improvements.push({
          line: matchedLine + 1,
          before: lines[matchedLine].trim(),
          after: fixup.fix,
          reason: fr ? fixup.reasonFr : fixup.reasonEn,
        });
      }
    }
  }
  if (!improvements.length) return null;
  return [
    `**${fr ? 'Réécriture de code' : 'Code rewrite'}**`,
    fr
      ? `${improvements.length} amélioration(s) détectée(s) :`
      : `${improvements.length} improvement(s) detected:`,
    '| # | Line | Before | After | Reason |',
    '|---|---|---|---|---|',
    ...improvements.map((imp, i) => `| ${i + 1} | ${imp.line} | \`${imp.before}\` | ${imp.after} | ${imp.reason} |`),
    '',
    `**${fr ? 'Résumé' : 'Summary'}**`,
    fr
      ? 'Ces modifications rendent le code plus lisible, plus performant et plus conforme à PEP 8.'
      : 'These changes make the code more readable, more performant, and more PEP 8 compliant.',
  ].join('\n');
};

export const answerPythonWhatIfQuestion = (question: string, _language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:what (?:if|happens?)|what about|suppose|imagine|scenario)\b/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  if (!code) return null;
  const fr = _language === 'fr';
  const lowerQ = question.toLowerCase();
  const scenarios: string[] = [];

  if (/\b(?:append|add|insert|extend)\b.*\b(?:while|for|loop|iterat)/i.test(lowerQ)) {
    scenarios.push(fr
      ? '**Scénario : modifier une liste pendant l\'itération**\nModifier une liste avec `append()`/`insert()` dans une boucle peut créer une boucle infinie car la liste grandit à chaque itération. Copiez d\'abord la liste ou itérez sur une copie : `for item in original[:]:`.'
      : '**Scenario: modifying a list while iterating**\nMutating a list with `append()`/`insert()` inside a loop can create an infinite loop because the list grows each iteration. Copy the list first or iterate over a copy: `for item in original[:]:`');
  }
  if (/\b(?:remove|pop|delete|del)\b.*\b(?:while|for|loop|iterat)/i.test(lowerQ)) {
    scenarios.push(fr
      ? '**Scénario : supprimer des éléments pendant l\'itération**\nSupprimer des éléments d\'une liste avec `remove()` ou `pop()` pendant l\'itération provoque un décalage des indices — des éléments sont sautés. Itérez sur une copie avec `for item in original[:]:` et filtrez.'
      : '**Scenario: removing items while iterating**\nRemoving elements from a list with `remove()` or `pop()` while iterating causes index shifting — elements are skipped. Iterate over a copy with `for item in original[:]:` and filter.');
  }
  if (/\b(?:defaultdict|default.?dict)\b|\bmissing\s+key\b/i.test(lowerQ)) {
    scenarios.push(fr
      ? '**Scénario : accéder à une clé manquante**\nSans `defaultdict`, `dict[key]` sur une clé inexistante lève `KeyError`. Utilisez `dict.get(key, default)` ou `defaultdict` pour gérer les clés manquantes automatiquement.'
      : '**Scenario: accessing a missing key**\nWithout `defaultdict`, `dict[key]` on a missing key raises `KeyError`. Use `dict.get(key, default)` or `defaultdict` to handle missing keys automatically.');
  }
  if (/\b(?:infinite|while\s+True|never.?end|never.?stop)\b/i.test(lowerQ)) {
    scenarios.push(fr
      ? '**Scénario : boucle infinie**\nUne boucle `while True` sans `break` ou une boucle `while` dont la condition ne devient jamais fausse s\'exécute indéfiniment. Assurez-vous que la condition progresse vers `False` ou utilisez `break` avec un compteur de sécurité.'
      : '**Scenario: infinite loop**\nA `while True` without `break` or a `while` whose condition never becomes false runs forever. Ensure the condition progresses toward `False` or use `break` with a safety counter.');
  }
  if (/\b(?:mutab|mutate|change|modif)\b.*\b(?:tuple|str(?:ing)?)\b|\b(?:tuple|str(?:ing)?)\b.*\b(?:mutab|mutate|change|modif)\b/i.test(lowerQ)) {
    scenarios.push(fr
      ? '**Scénario : modifier un tuple ou une chaîne**\nLes tuples et les chaînes sont immuables. `t[0] = x` lève `TypeError`. Créez un nouvel objet au lieu de modifier l\'original.'
      : '**Scenario: modifying a tuple or string**\nTuples and strings are immutable. `t[0] = x` raises `TypeError`. Create a new object instead of modifying the original.');
  }
  if (!scenarios.length) return null;
  return [
    `**${fr ? 'Simulation de scénario "Et si…" ?' : '"What if?" scenario simulation'}**`,
    ...scenarios,
    `**${fr ? 'Pour explorer davantage' : 'To explore further'}**`,
    fr
      ? 'Si vous avez un scénario spécifique en tête, partagez le code et je tracerai l\'exécution pas à pas.'
      : 'If you have a specific scenario in mind, share the code and I will trace the execution step by step.',
  ].join('\n\n');
};

const LIBRARY_HELP: Record<string, { descEn: string; descFr: string; usageEn: string; usageFr: string }> = {
  requests: {
    descEn: 'HTTP library for making API calls, fetching web pages, and interacting with web services.',
    descFr: 'Bibliothèque HTTP pour les appels API, le téléchargement de pages web et l\'interaction avec les services web.',
    usageEn: '```python\nimport requests\n\n# GET request\nresponse = requests.get("https://api.github.com", timeout=10)\ndata = response.json()  # parse JSON\n\n# POST with data\npayload = {"name": "Noll", "role": "developer"}\nresponse = requests.post("https://httpbin.org/post", json=payload, timeout=10)\nprint(response.status_code, response.json())\n```',
    usageFr: '```python\nimport requests\n\n# Requête GET\nréponse = requests.get("https://api.github.com", timeout=10)\ndonnées = réponse.json()  # analyse JSON\n\n# POST avec données\npayload = {"nom": "Noll", "rôle": "développeur"}\nr = requests.post("https://httpbin.org/post", json=payload, timeout=10)\nprint(r.status_code, r.json())\n```',
  },
  json: {
    descEn: 'Standard-library module for parsing and generating JSON data — converting between JSON strings and Python dicts/lists.',
    descFr: 'Module de la bibliothèque standard pour analyser et générer des données JSON — conversion entre chaînes JSON et dictionnaires/listes Python.',
    usageEn: '```python\nimport json\n\n# Parse JSON string → dict\ndata = \'{"name": "Noll", "age": 30}\'\nparsed = json.loads(data)\nprint(parsed["name"])  # Noll\n\n# Dict → JSON string\noutput = json.dumps(parsed, indent=2)\nprint(output)\n\n# Read/Write JSON files\nwith open("data.json") as f:\n    data = json.load(f)\n\nwith open("data.json", "w") as f:\n    json.dump(data, f, indent=2)\n```',
    usageFr: '```python\nimport json\n\n# Analyser une chaîne JSON → dict\ndonnées = \'{"nom": "Noll", "âge": 30}\'\nanalysé = json.loads(données)\nprint(analysé["nom"])  # Noll\n\n# Dict → chaîne JSON\nsortie = json.dumps(analysé, indent=2)\nprint(sortie)\n\n# Lire/Écrire des fichiers JSON\nwith open("données.json") as f:\n    données = json.load(f)\n\nwith open("données.json", "w") as f:\n    json.dump(données, f, indent=2)\n```',
  },
  pathlib: {
    descEn: 'Modern, object-oriented approach to filesystem paths — replaces `os.path` with `.`-chained Path methods.',
    descFr: 'Approche moderne et orientée objet des chemins du système de fichiers — remplace `os.path` par des méthodes enchaînées de Path.',
    usageEn: '```python\nfrom pathlib import Path\n\n# Create path\nhome = Path.home()\ndata_dir = home / "data" / "project"\ndata_dir.mkdir(parents=True, exist_ok=True)\n\n# Read/write\nfile = data_dir / "notes.txt"\nfile.write_text("Hello, world!")\ncontent = file.read_text()\n\n# Iterate\nfor py_file in data_dir.glob("*.py"):\n    print(py_file.name, py_file.stat().st_size)\n```',
    usageFr: '```python\nfrom pathlib import Path\n\n# Créer un chemin\nhome = Path.home()\ndossier_données = home / "données" / "projet"\ndossier_données.mkdir(parents=True, exist_ok=True)\n\n# Lire/Écrire\nfichier = dossier_données / "notes.txt"\nfichier.write_text("Bonjour tout le monde !")\ncontenu = fichier.read_text()\n\n# Itérer\nfor fichier_py in dossier_données.glob("*.py"):\n    print(fichier_py.name, fichier_py.stat().st_size)\n```',
  },
  datetime: {
    descEn: 'Module for working with dates, times, time deltas, and time zones — parsing, formatting, arithmetic.',
    descFr: 'Module pour travailler avec les dates, heures, intervalles et fuseaux horaires — analyse, formatage, calculs.',
    usageEn: '```python\nfrom datetime import datetime, timedelta, date\n\n# Now\nnow = datetime.now()\nprint(now.strftime("%Y-%m-%d %H:%M"))\n\n# Parse from string\ndt = datetime.strptime("2024-01-15", "%Y-%m-%d")\n\n# Arithmetic\nnext_week = now + timedelta(days=7)\ndelta = next_week - now\nprint(delta.days)\n\n# Date only\ntoday = date.today()\n```',
    usageFr: '```python\nfrom datetime import datetime, timedelta, date\n\n# Maintenant\nmaintenant = datetime.now()\nprint(maintenant.strftime("%d/%m/%Y %H:%M"))\n\n# Analyse depuis une chaîne\ndt = datetime.strptime("15/01/2024", "%d/%m/%Y")\n\n# Calculs\nsemaine_prochaine = maintenant + timedelta(days=7)\ndelta = semaine_prochaine - maintenant\nprint(delta.days)\n```',
  },
  itertools: {
    descEn: 'Module of fast, memory-efficient iterator tools — chain, cycle, count, permutations, combinations, groupby, islice, and more.',
    descFr: 'Module d\'outils d\'itération rapides et économes en mémoire — chain, cycle, count, permutations, combinations, groupby, islice, etc.',
    usageEn: '```python\nfrom itertools import chain, product, groupby, islice\n\n# Chain multiple iterables\ncombined = list(chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]\n\n# Cartesian product\npairs = list(product("AB", [1, 2]))  # [(A,1), (A,2), (B,1), (B,2)]\n\n# Group sorted data\nitems = [("a", 1), ("a", 2), ("b", 3)]\nfor key, group in groupby(items, key=lambda x: x[0]):\n    print(key, list(group))\n\n# Take first 5\nfirst_5 = list(islice(range(100), 5))  # [0, 1, 2, 3, 4]\n```',
    usageFr: '```python\nfrom itertools import chain, product, groupby, islice\n\n# Chaîner plusieurs itérables\ncombiné = list(chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]\n\n# Produit cartésien\npaires = list(product("AB", [1, 2]))  # [(A,1), (A,2), (B,1), (B,2)]\n\n# Grouper des données triées\nitems = [("a", 1), ("a", 2), ("b", 3)]\npour clé, groupe in groupby(items, key=lambda x: x[0]):\n    print(clé, list(groupe))\n\n# Prendre les 5 premiers\npremiers_5 = list(islice(range(100), 5))  # [0, 1, 2, 3, 4]\n```',
  },
};

export const answerPythonLibraryHelp = (question: string, language: AdvancedAiLanguage): string | null => {
  const lowerQ = question.toLowerCase();
  const fr = language === 'fr';
  const matchedLib = Object.entries(LIBRARY_HELP).find(([lib]) => new RegExp(`\\b${lib}\\b`, 'i').test(lowerQ));
  if (!matchedLib) return null;
  const [lib, info] = matchedLib;
  return [
    `**${fr ? 'Bibliothèque' : 'Library'}: ${lib}**`,
    fr ? info.descFr : info.descEn,
    '',
    `**${fr ? 'Utilisation courante' : 'Common usage'}**`,
    fr ? info.usageFr : info.usageEn,
    '',
    `**${fr ? 'Conseil' : 'Tip'}**`,
    fr
      ? `La documentation officielle de \`${lib}\` donne plus de détails : https://docs.python.org/3/library/${lib}.html`
      : `The official \`${lib}\` documentation has full details: https://docs.python.org/3/library/${lib}.html`,
  ].join('\n\n');
};

export const answerPythonDesignRationaleQuestion = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:why (?:does|is|was|did|would|are)|design (?:choice|decision|rationale)|reason (?:behind|for)|rationale)\b/i.test(question)) return null;
  const fr = language === 'fr';
  const lowerQ = question.toLowerCase();

  const rationales: Array<{ pattern: RegExp; answerEn: string; answerFr: string }> = [
    { pattern: /\bsort\b.*\bNone\b|\bNone\b.*\bsort\b/, answerEn: '`list.sort()` mutates in place and returns `None` to avoid confusing the two behaviors. `sorted()` returns a new list. This design forces you to choose explicitly: mutate or copy.', answerFr: '`list.sort()` modifie sur place et renvoie `None` pour éviter de confondre les deux comportements. `sorted()` renvoie une nouvelle liste. Cette conception vous oblige à choisir explicitement : modifier ou copier.' },
    { pattern: /\bjoin\b.*\bstr(?:ing)?\b|\bstr(?:ing)?\b.*\bjoin\b/, answerEn: '`" ".join(list)` is a method on the separator string, not on the list. This works with any iterable of strings and avoids type-checking — any iterable works, not just lists.', answerFr: '`" ".join(liste)` est une méthode sur la chaîne séparatrice, pas sur la liste. Cela fonctionne avec n\'importe quel itérable de chaînes et évite la vérification de type — n\'importe quel itérable fonctionne, pas seulement les listes.' },
    { pattern: /\brandint\b/, answerEn: '`random.randint(1, 6)` includes both endpoints (unlike `range` which excludes the stop). This matches the natural language "pick a number from 1 to 6".', answerFr: '`random.randint(1, 6)` inclut les deux extrémités (contrairement à `range` qui exclut la fin). Cela correspond au langage naturel "choisis un nombre de 1 à 6".' },
    { pattern: /\brange\b.*\bexclu|\brange\b.*\bstop\b|\bstop\b.*\brange\b/, answerEn: '`range(n)` yields 0 to n-1 (exclusive) because zero-based indexing is consistent with lists and slices. `range(len(seq))` matches list indices directly.', answerFr: '`range(n)` produit 0 à n-1 (exclu) car l\'indexation basée sur zéro est cohérente avec les listes et les tranches. `range(len(seq))` correspond directement aux indices de liste.' },
    { pattern: /\bimmutab/, answerEn: 'Strings and tuples are immutable by design. Immutability makes them hashable (usable as dict keys), thread-safe, and enables internal optimizations like string interning.', answerFr: 'Les chaînes et les tuples sont immuables par conception. L\'immuabilité les rend hachables (utilisables comme clés de dictionnaire), thread-safe et permet des optimisations internes comme l\'internement des chaînes.' },
    { pattern: /\btry\b.*\belse\b|\belse\b.*\btry\b/, answerEn: 'The `else` clause on `try` runs only if no exception occurred. This separates success-path code from the `try` block that might accidentally catch exceptions from unrelated code.', answerFr: 'La clause `else` d\'un `try` ne s\'exécute que si aucune exception n\'a eu lieu. Cela sépare le code du chemin de réussite du bloc `try` qui pourrait accidentellement attraper des exceptions de code non lié.' },
    { pattern: /\bpriv[ae]t\b|\bunderscore\b|_\b(?:name|method|attr)/, answerEn: 'Python uses `_` prefix as a convention for "internal use" rather than enforcing true private access. This reflects the philosophy "we are all consenting adults" — trust over enforcement.', answerFr: 'Python utilise le préfixe `_` comme convention pour "usage interne" plutôt que d\'imposer un véritable accès privé. Cela reflète la philosophie "nous sommes tous des adultes consentants" — la confiance plutôt que l\'application.' },
    { pattern: /\bpass\b/, answerEn: '`pass` is a no-op statement required because Python uses indentation for block structure. An empty block would be ambiguous, so `pass` explicitly says "do nothing here".', answerFr: '`pass` est une instruction vide nécessaire car Python utilise l\'indentation pour la structure des blocs. Un bloc vide serait ambigu, donc `pass` dit explicitement "ne rien faire ici".' },
    { pattern: /\bGIL\b|global\s+interpreter\s+lock/, answerEn: 'The GIL ensures only one thread executes Python bytecode at a time, simplifying memory management. True parallelism requires `multiprocessing` (separate processes) or C extensions that release the GIL.', answerFr: 'Le GIL garantit qu\'un seul thread exécute le bytecode Python à la fois, ce qui simplifie la gestion de la mémoire. Le véritable parallélisme nécessite `multiprocessing` (processus séparés) ou des extensions C qui libèrent le GIL.' },
    { pattern: /\biter\b.*\bnext\b|\bnext\b.*\biter\b/, answerEn: 'Separating `iter()` (creates iterator) from `next()` (drives iteration) decouples the "make something iterable" protocol from the "advance one step" protocol. This lets `for` loops work with any iterable via the same interface.', answerFr: 'Séparer `iter()` (crée un itérateur) de `next()` (avance d\'un pas) découple le protocole "rendre quelque chose itérable" du protocole "avancer d\'un pas". Cela permet aux boucles `for` de fonctionner avec n\'importe quel itérable via la même interface.' },
  ];

  const matched = rationales.find(r => r.pattern.test(lowerQ));
  if (!matched) {
    return [
      `**${fr ? 'Conception Python' : 'Python design rationale'}**`,
      fr
        ? 'Je ne connais pas la raison de conception spécifique pour ce sujet. La philosophie de Python est résumée dans le PEP 20 (Zen de Python) : "Il devrait y avoir une — et de préférence une seule — façon évidente de le faire."'
        : 'I do not know the specific design rationale for this topic. Python\'s philosophy is summarized in PEP 20 (The Zen of Python): "There should be one — and preferably only one — obvious way to do it."',
    ].join('\n\n');
  }
  return [
    `**${fr ? 'Raison de conception Python' : 'Python design rationale'}**`,
    matched.answerEn,
    '',
    `**${fr ? 'Philosophie plus large' : 'Broader philosophy'}**`,
    fr
      ? 'Python privilégie la lisibilité, la simplicité et l\'explícite plutôt que l\'implicite. De nombreux choix de conception découlent de ces principes.'
      : 'Python values readability, simplicity, and explicitness over implicitness. Many design choices follow from these principles.',
  ].join('\n\n');
};

const STRING_FORMATTING_COMPARISON: Array<{ method: string; example: string; pros: string; cons: string }> = [
  { method: 'f-strings', example: 'f"Hello, {name}!"', pros: 'Fastest, most readable, supports inline expressions, preferred since Python 3.6', cons: 'Python 3.6+ only, no lazy evaluation, fixed at definition time' },
  { method: '.format()', example: '"Hello, {}!".format(name)', pros: 'Supports positional/named args, reusable format strings, works since Python 2.6', cons: 'Verbose for simple cases, slower than f-strings, can raise KeyError' },
  { method: '%‑formatting', example: '"Hello, %s!" % name', pros: 'Familiar from C/printf, works in Python 2, concise for simple cases', cons: 'Hard to read with many args, limited type specifiers, deprecated in favor of .format()' },
  { method: 'string.Template', example: 'Template("Hello, $name!").substitute(name=name)', pros: 'Safest for user‑supplied format strings, avoids injection issues', cons: 'No type formatting, no expressions, slowest option' },
];

export const answerPythonFormattingGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:f.?string|%.*format|\.?format|template|string.?format|format.*string|printf|%-formatting|%-style)\b/i.test(question) &&
    !/(?:how|when|why|which|difference)\b.*\b(format|style|method|print|string|chaîne|pourcent)/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Comparaison des méthodes de formatage de chaînes' : 'String formatting comparison'}**`,
    '',
    '| Method | Example | Pros | Cons |',
    '|--------|---------|------|------|',
    ...STRING_FORMATTING_COMPARISON.map(r => `| ${r.method} | \`${r.example}\` | ${r.pros} | ${r.cons} |`),
    '',
    `**${fr ? 'Recommandation' : 'Recommendation'}**`,
    fr
      ? 'Utilisez les **f-strings** pour la plupart des cas (Python 3.6+). Utilisez `.format()` quand vous devez séparer le modèle des données. Utilisez `Template` quand des utilisateurs fournissent le modèle. Évitez `%` dans le nouveau code.'
      : 'Use **f-strings** for most cases (Python 3.6+). Use `.format()` when you need to separate the template from the data. Use `Template` when users supply the template. Avoid `%` in new code.',
  ].join('\n\n');
};

export const answerPythonDataStructureChoice = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:which (?:data )?structure|should i use|list vs|set vs|dict vs|tuple vs|difference between|choisir|quelle structure)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Guide de choix des structures de données' : 'Data structure decision guide'}**`,
    '',
    fr
      ? '**Liste** — `[1, 2, 3]` : ordre conservé, accès par index, éléments mutables. Utilisez pour séquences modifiables, piles, files simples.'
      : '**List** — `[1, 2, 3]` : ordered, indexable, mutable elements. Use for modifiable sequences, stacks, simple queues.',
    '',
    fr
      ? '**Tuple** — `(1, 2, 3)` : ordre conservé, hachable, immuable. Utilisez pour clés de dictionnaire, coordonnées fixes, retours de fonctions.'
      : '**Tuple** — `(1, 2, 3)` : ordered, hashable, immutable. Use for dict keys, fixed coordinates, function return values.',
    '',
    fr
      ? '**Set** — `{1, 2, 3}` : non ordonné, élimine les doublons, tests d\'appartenance O(1). Utilisez pour union/intersection/différence, filtrage de doublons.'
      : '**Set** — `{1, 2, 3}` : unordered, deduplicated, O(1) membership tests. Use for union/intersection/difference, duplicate filtering.',
    '',
    fr
      ? '**Dict** — `{"a": 1}` : associations clé→valeur, hachable, O(1) par clé. Utilisez pour tables de correspondance, compteurs, caches.'
      : '**Dict** — `{"a": 1}` : key→value mappings, hashable keys, O(1) by key. Use for lookup tables, counters, caches.',
    '',
    '```python',
    '# Decision flowchart:',
    '# Need key→value mapping? → dict',
    '# Need fast membership/unique items? → set',
    '# Need ordered, mutable sequence? → list',
    '# Need immutable, hashable, ordered? → tuple',
    '```',
  ].join('\n\n');
};

export const answerPythonImportGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:import|sys\.path|__init__|circular import|relative import|absolute import|module.*not found|import.*error|package.*structure)\b/i.test(question) &&
    !/\bhow.*import|\bmodule.*not found|importlib|reload/i.test(question)) return null;
  const code = extractGeneralAiPythonCode(question);
  const fr = language === 'fr';

  const guide: string[] = [
    `**${fr ? 'Guide du système d\'importation Python' : 'Python import system guide'}**`,
    '',
    `1. **${fr ? 'Ordre de recherche' : 'Search order'}**`,
    fr
      ? '`import foo` cherche dans : (1) `sys.modules` (cache), (2) les modules natifs, (3) `sys.path` (répertoire courant, `PYTHONPATH`, chemins des paquets installés).'
      : '`import foo` searches: (1) `sys.modules` (cache), (2) built-in modules, (3) `sys.path` (current dir, `PYTHONPATH`, site-packages).',
  ];

  if (code && /\bimport\b|\bfrom\b.*\bimport\b/.test(code)) {
    guide.push('', `2. **${fr ? 'Analyse du code' : 'Code analysis'}**`);
    if (/from\s+\./.test(code)) {
      guide.push(fr
        ? '- **Import relatif** détecté (`from .module import ...`). Utilisez dans les paquets, jamais dans les scripts principaux. Le nombre de points indique le niveau parent (`.` = même paquet, `..` = paquet parent).'
        : '- **Relative import** detected (`from .module import ...`). Use inside packages only, never in top-level scripts. Dots indicate parent depth (`.` = same package, `..` = parent package).');
    }
    if (/import\s+\*\b/.test(code)) {
      guide.push(fr
        ? '- **Import wildcard** (`from x import *`) détecté. Déconseillé — pollue l\'espace de nommage et rend le code illisible. Importez des noms explicites ou utilisez `__all__`.'
        : '- **Wildcard import** (`from x import *`) detected. Discouraged — pollutes namespace and makes code hard to read. Import explicit names or use `__all__`.');
    }
    if (/\bsys\.path\.append|sys\.path\.insert/.test(code)) {
      guide.push(fr
        ? '- **Modification de `sys.path`** détectée. Préférez un paquet correctement structuré avec `__init__.py` et `pip install -e .` en développement.'
        : '- **`sys.path` modification** detected. Prefer a properly structured package with `__init__.py` and `pip install -e .` during development.');
    }
  }

  guide.push(
    '',
    `3. **${fr ? 'Paquet vs module' : 'Package vs module'}**`,
    fr
      ? '- **Module** : un fichier `.py`. **Paquet** : un dossier avec `__init__.py` (ou implicitement un namespace package). `import pkg.sub` importe `pkg/__init__.py` puis `pkg/sub.py`.'
      : '- **Module**: a `.py` file. **Package**: a directory with `__init__.py` (or implicitly a namespace package). `import pkg.sub` loads `pkg/__init__.py` then `pkg/sub.py`.',
    '',
    `4. **${fr ? 'Importations circulaires' : 'Circular imports'}**`,
    fr
      ? '- Se produisent quand A importe B et B importe A. Solution : déplacer l\'import dans la fonction, restructurer en module partagé C, ou utiliser l\'import tardif (`import` à l\'intérieur de la fonction).'
      : '- Happen when A imports B and B imports A. Fix: move import inside a function, restructure into a shared module C, or use lazy imports (`import` inside the function).',
    '',
    `5. **${fr ? '`__init__.py`' : '`__init__.py`'}**`,
    fr
      ? '- Contrôle ce que `from pkg import *` exporte via `__all__`. S\'exécute une fois au premier import du paquet. Peut importer des sous-modules pour une API plus courte.'
      : '- Controls what `from pkg import *` exports via `__all__`. Runs once on first package import. Can import sub-modules for a shorter public API.',
  );

  return guide.join('\n');
};

export const answerPythonCodeReview = (question: string, language: AdvancedAiLanguage): string | null => {
  const code = extractGeneralAiPythonCode(question);
  if (!code || !/\breview|r[eé]vise|audit|check.*code|correct.*code|review.*code|relire|vérifie.*code\b/i.test(question)) return null;
  const fr = language === 'fr';

  const lines = code.split('\n');

  // Score categories
  let score = 100;
  const issues: Array<{ category: string; severity: 'critical' | 'major' | 'minor'; message: string; line: number | null }> = [];

  lines.forEach((line, i) => {
    const n = i + 1;
    if (/^\s+$/.test(line)) { issues.push({ category: fr ? 'Style' : 'Style', severity: 'minor', message: fr ? 'Ligne vide avec espaces superflus' : 'Blank line with trailing whitespace', line: n }); score -= 1; }
    if (/^\s*except\s*:/.test(line)) { issues.push({ category: fr ? 'Erreurs' : 'Errors', severity: 'critical', message: fr ? '`except:` nu attrape BaseException (inclut KeyboardInterrupt)' : 'Bare `except:` catches BaseException (includes KeyboardInterrupt)', line: n }); score -= 10; }
    if (/^\s*except\s*:\s*\n\s*pass/.test(code)) { issues.push({ category: fr ? 'Erreurs' : 'Errors', severity: 'critical', message: fr ? '`except: pass` avale silencieusement toutes les erreurs' : '`except: pass` silently swallows all errors', line: n }); score -= 5; }
    if (/\btry\s*:[\s\S]*?\bexcept\b(?!\s*(Exception|ValueError|TypeError|KeyError|OSError|IndexError|AttributeError|RuntimeError|IOError|StopIteration|ZeroDivisionError|FileNotFoundError|PermissionError|TimeoutError))/ && /^\s*except\s*:/.test(line)) { /* already caught above */ }
    if (/==\s*True\b|==\s*False\b/.test(line) && !/['"]/.test(line)) { issues.push({ category: fr ? 'Style' : 'Style', severity: 'minor', message: fr ? '`== True`/`== False` redondant — utilisez `if x:`/`if not x:`' : '`== True`/`== False` is redundant — use `if x:`/`if not x:`', line: n }); score -= 2; }
    if (/^\s*for\s+\w+\s+in\s+range\s*\(\s*len\s*\(/.test(line)) { issues.push({ category: fr ? 'Performance' : 'Performance', severity: 'major', message: fr ? '`range(len(...))` est indirect — utilisez `enumerate()` ou l\'itération directe' : '`range(len(...))` is indirect — use `enumerate()` or direct iteration', line: n }); score -= 5; }
    if (/^\s*(?:list|dict|str|int|float|bool|set|type|input|print|len|range)\s*=/.test(line.trim())) { issues.push({ category: fr ? 'Erreurs' : 'Errors', severity: 'critical', message: fr ? 'Masquage d\'un nom natif' : 'Shadowing a built-in', line: n }); score -= 8; }
    if (/\.sort\s*\(\s*\)\s*$/.test(line.trim()) && /\w+\s*=\s*\w+\.sort/.test(line)) { issues.push({ category: fr ? 'Erreurs' : 'Errors', severity: 'major', message: fr ? '`.sort()` renvoie `None` — utilisez `sorted()` pour une nouvelle liste' : '`.sort()` returns `None` — use `sorted()` for a new list', line: n }); score -= 6; }
    if (/\bopen\s*\([^)]+\)\b(?!\s*\.)/.test(line) && !/^\s*with\s+open/.test(line)) { issues.push({ category: fr ? 'Ressources' : 'Resources', severity: 'major', message: fr ? 'Fichier ouvert sans gestionnaire de contexte `with`' : 'File opened without a `with` context manager', line: n }); score -= 5; }
    if (/^\s*def\s+\w+\([^)]*=\s*\[|=\s*\{|=\s*set\(/.test(line)) { issues.push({ category: fr ? 'Erreurs' : 'Errors', severity: 'critical', message: fr ? 'Argument par défaut mutable partagé entre les appels' : 'Mutable default argument shared across calls', line: n }); score -= 8; }
    if (/^\s*import\s+\*\b|^\s*from\s+\w+\s+import\s+\*\b/.test(line)) { issues.push({ category: fr ? 'Style' : 'Style', severity: 'major', message: fr ? 'Import wildcard `*` — importez des noms explicites' : 'Wildcard `*` import — import explicit names', line: n }); score -= 4; }
    if (line.length > 100) { issues.push({ category: fr ? 'Style' : 'Style', severity: 'minor', message: fr ? 'Ligne de plus de 100 caractères' : 'Line exceeds 100 characters', line: n }); score -= 1; }
  });

  if (!issues.length) return null;

  score = Math.max(0, score);
  const grade: string = score >= 90 ? 'A' : score >= 80 ? 'B' : score >= 70 ? 'C' : score >= 60 ? 'D' : 'F';

  const critical = issues.filter(i => i.severity === 'critical');
  const major = issues.filter(i => i.severity === 'major');
  const minor = issues.filter(i => i.severity === 'minor');

  const catLabels = { critical: fr ? '🔴 Critique' : '🔴 Critical', major: fr ? '🟡 Majeur' : '🟡 Major', minor: fr ? '🟢 Mineur' : '🟢 Minor' };

  return [
    `**${fr ? 'Revue de code' : 'Code review'}**`,
    '',
    `**${fr ? 'Score' : 'Score'}: ${score}/100 (${grade})** — ${critical.length} ${fr ? 'critique(s)' : 'critical'}, ${major.length} ${fr ? 'majeur(s)' : 'major'}, ${minor.length} ${fr ? 'mineur(s)' : 'minor'}`,
    '',
    ...issues.map(iss => `${catLabels[iss.severity]} | ${fr ? 'Ligne' : 'Line'} ${iss.line} | ${iss.message}`),
  ].join('\n');
};

const TYPE_HINT_GUIDE: Array<{ pattern: string; example: string; useCase: string }> = [
  { pattern: 'Optional / Union', example: 'def find(id: int | None) -> str | None:', useCase: 'Values that can be None or multiple types' },
  { pattern: 'Protocol', example: 'class Drawable(Protocol):\n    def draw(self) -> None: ...', useCase: 'Structural subtyping (duck typing with types)' },
  { pattern: 'TypedDict', example: 'class Point(TypedDict):\n    x: float\n    y: float', useCase: 'Dicts with known, typed keys' },
  { pattern: 'TypeVar', example: 'T = TypeVar("T")\ndef first(items: list[T]) -> T:', useCase: 'Generic functions preserving type relationships' },
  { pattern: 'Generic', example: 'class Stack[T]:\n    def push(self, item: T) -> None:', useCase: 'Generic classes parameterized by type' },
  { pattern: 'overload', example: '@overload\ndef process(x: int) -> str: ...\n@overload\ndef process(x: str) -> int: ...', useCase: 'Multiple type signatures for one function' },
  { pattern: 'Literal', example: 'from typing import Literal\ndef set_mode(m: Literal["r", "w", "a"]) -> None:', useCase: 'Restricting argument to exact values' },
  { pattern: 'Final', example: 'from typing import Final\nMAX: Final = 100', useCase: 'Constants that should not be reassigned' },
];

export const answerPythonTypeHintGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:type.?hint|type.?annot|typing|Protocol|TypedDict|TypeVar|overload|Generic|Optional|Union)\b/i.test(question) &&
    !/\bhow.*type|comment.*type|what.*type|annotation/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Guide des patrons de typage' : 'Type hint pattern guide'}**`,
    '',
    fr
      ? 'Ces patrons couvrent 90 % des besoins de typage dans les projets réels.'
      : 'These patterns cover 90 % of typing needs in real-world projects.',
    '',
    ...TYPE_HINT_GUIDE.map(p => [
      `**${p.pattern}**`,
      `\`\`\`python\n${p.example}\n\`\`\``,
      `_${fr ? 'Usage' : 'Use case'}: ${p.useCase}_`,
    ].join('\n\n')),
    `**${fr ? 'Conseil' : 'Tip'}**`,
    fr
      ? 'Activez `strict = true` dans `pyproject.toml` pour myrc ou pytype afin de bénéficier de la vérification la plus complète.'
      : 'Enable `strict = true` in `pyproject.toml` for mypy or pytype to get the most thorough type checking.',
  ].join('\n\n');
};

const PACKAGE_ADVICE: Array<{ category: string; recommendation: string; runnerUp: string; advice: string }> = [
  { category: 'HTTP APIs', recommendation: 'httpx', runnerUp: 'requests', advice: 'httpx is async-first, has HTTP/2, and a modern API. Use `requests` for simple sync scripts.' },
  { category: 'CLI tools', recommendation: 'typer', runnerUp: 'argparse / click', advice: 'typer builds on click with type-annotation-based CLI definitions — minimal boilerplate.' },
  { category: 'Testing', recommendation: 'pytest', runnerUp: 'unittest', advice: 'pytest has simpler assertions, fixtures, parameterization, and excellent plugin ecosystem.' },
  { category: 'ORM/DB', recommendation: 'SQLAlchemy', runnerUp: 'Django ORM / peewee', advice: 'SQLAlchemy 2.0 has both ORM and Core SQL. Django ORM is great if you already use Django.' },
  { category: 'Data frames', recommendation: 'polars', runnerUp: 'pandas', advice: 'polars is faster, lazy by default, and has a cleaner API. pandas is older with larger ecosystem.' },
  { category: 'Async framework', recommendation: 'asyncio', runnerUp: 'trio / anyio', advice: 'asyncio is built-in. trio has cleaner cancellation semantics; anyio provides a unified API over both.' },
  { category: 'Validation', recommendation: 'pydantic', runnerUp: 'attrs / msgspec', advice: 'pydantic v2 is the standard for data validation with JSON Schema support.' },
  { category: 'Configuration', recommendation: 'pydantic-settings', runnerUp: 'python-decouple / dynaconf', advice: 'pydantic-settings reads from env vars, .env files, secrets — validated out of the box.' },
  { category: 'Serialization', recommendation: 'orjson / msgspec', runnerUp: 'json (stdlib)', advice: 'orjson is 3-10× faster than stdlib json. msgspec also handles binary protocols.' },
  { category: 'Task queues', recommendation: 'arq (async) / huey (sync)', runnerUp: 'celery / rq', advice: 'arq for Redis-backed async tasks. huey for simple sync. celery is heavy but proven.' },
];

export const answerPythonPackageAdvice = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:best (?:library|package|tool|framework)|recommend|suggestion|what (?:library|package|tool|framework)|which.*(?:library|package|tool|framework)|quel(?:le)? (?:biblioth[eè]que|paquet|outil)|recommande|sugg[eè]re)\b/i.test(question)) return null;
  const fr = language === 'fr';
  const category = PACKAGE_ADVICE.find(p => new RegExp(p.category.replace(/[/\s]/g, '|'), 'i').test(question));
  if (!category) {
    const categories = PACKAGE_ADVICE.map(p => p.category).join(', ');
    return [
      `**${fr ? 'Conseils de paquets Python' : 'Python package advice'}**`,
      fr
        ? `Je connais ces catégories : ${categories}. Précisez le type de projet pour une recommandation ciblée.`
        : `I can advise on: ${categories}. Specify the project type for a targeted recommendation.`,
    ].join('\n\n');
  }
  return [
    `**${category.category}**`,
    fr
      ? `**Recommandation** : ${category.recommendation}` + (category.runnerUp ? `\n**Alternative** : ${category.runnerUp}` : '')
      : `**Recommendation** : ${category.recommendation}` + (category.runnerUp ? `\n**Alternative** : ${category.runnerUp}` : ''),
    category.advice,
  ].join('\n\n');
};

export const answerPythonAsyncPatterns = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:asyncio|async|await|coroutine|gather|TaskGroup|semaphore|queue|timeout|event.?loop)\b/i.test(question) &&
    !/\b(?:how.*async|async.*pattern|concurrent.*task)\b/i.test(question)) return null;
  const fr = language === 'fr';

  const patterns: string[] = [
    `**${fr ? '1. `asyncio.gather()` — exécution parallèle simple' : '1. `asyncio.gather()` — simple parallel execution'}**`,
    '```python',
    'import asyncio',
    '',
    'async def fetch(url: str) -> str:',
    '    await asyncio.sleep(1)',
    '    return f"data from {url}"',
    '',
    'async def main():',
    '    results = await asyncio.gather(',
    '        fetch("a.com"),',
    '        fetch("b.com"),',
    '        fetch("c.com"),',
    '        return_exceptions=True,',
    '    )',
    '    print(results)',
    '',
    "asyncio.run(main())",
    '```',
  ].join('\n');

  patterns.push(
    '',
    `**${fr ? '2. `asyncio.TaskGroup` — structuré avec annulation' : '2. `asyncio.TaskGroup` — structured with cancellation'}**`,
    fr
      ? '`TaskGroup` (Python 3.11+) annule automatiquement toutes les tâches si l\'une échoue. Plus sûr que `gather`.'
      : '`TaskGroup` (Python 3.11+) automatically cancels all tasks if one fails. Safer than `gather`.',
    '```python',
    'async def main():',
    '    async with asyncio.TaskGroup() as tg:',
    '        t1 = tg.create_task(fetch("a.com"))',
    '        t2 = tg.create_task(fetch("b.com"))',
    '    # Both done or all cancelled on first failure',
    '```',
  );

  patterns.push(
    '',
    `**${fr ? '3. `asyncio.Semaphore` — limitation de concurrence' : '3. `asyncio.Semaphore` — concurrency limiting'}**`,
    '```python',
    'sem = asyncio.Semaphore(5)  # max 5 concurrent',
    '',
    'async def rate_limited_fetch(url: str) -> str:',
    '    async with sem:',
    '        return await fetch(url)',
    '```',
  );

  patterns.push(
    '',
    `**${fr ? '4. `asyncio.Queue` — producteur/consommateur' : '4. `asyncio.Queue` — producer/consumer'}**`,
    '```python',
    'async def producer(queue: asyncio.Queue):',
    '    for i in range(20):',
    '        await queue.put(i)',
    '    await queue.join()',
    '',
    'async def consumer(queue: asyncio.Queue, name: str):',
    '    while True:',
    '        item = await queue.get()',
    '        print(f"{name} got {item}")',
    '        queue.task_done()',
    '',
    'async def main():',
    '    q: asyncio.Queue[int] = asyncio.Queue()',
    '    await asyncio.gather(producer(q), consumer(q, "A"), consumer(q, "B"))',
    '```',
  );

  patterns.push(
    '',
    `**${fr ? '5. Timeouts' : '5. Timeouts'}**`,
    '```python',
    'try:',
    '    result = await asyncio.wait_for(fetch("slow.com"), timeout=2.0)',
    'except asyncio.TimeoutError:',
    '    print("Request timed out")',
    '```',
  );

  return patterns.join('\n');
};

export const answerPythonRefactoringRecipes = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:refactor|rewrite|improve|make better|clean.?up|transform|convert|change)\b.*\b(?:loop|comprehension|enumerate|ternary|lambda|filter|map|join|defaultdict|any.?all)\b/i.test(question)) return null;
  const fr = language === 'fr';
  const recipes: Array<{ before: string; after: string; title: string }> = [
    {
      title: 'Replace loop with list comprehension',
      before: 'result = []\nfor x in items:\n    result.append(x * 2)',
      after: 'result = [x * 2 for x in items]',
    },
    {
      title: 'Replace range(len) with enumerate',
      before: 'for i in range(len(items)):\n    print(i, items[i])',
      after: 'for i, item in enumerate(items):\n    print(i, item)',
    },
    {
      title: 'Replace manual counter with enumerate',
      before: 'i = 0\nfor x in items:\n    print(i, x)\n    i += 1',
      after: 'for i, x in enumerate(items):\n    print(i, x)',
    },
    {
      title: 'Replace if/else with ternary',
      before: 'if x > 0:\n    label = "positive"\nelse:\n    label = "non-positive"',
      after: 'label = "positive" if x > 0 else "non-positive"',
    },
    {
      title: 'Replace filter+lambda with comprehension',
      before: 'result = list(filter(lambda x: x > 0, numbers))',
      after: 'result = [x for x in numbers if x > 0]',
    },
    {
      title: 'Replace manual string concat with join',
      before: 's = ""\nfor x in parts:\n    s += x + ","',
      after: 's = ",".join(parts)',
    },
    {
      title: 'Replace repeated .get() with defaultdict',
      before: 'counts = {}\nfor word in words:\n    counts[word] = counts.get(word, 0) + 1',
      after: 'from collections import defaultdict\ncounts: dict[str, int] = defaultdict(int)\nfor word in words:\n    counts[word] += 1',
    },
    {
      title: 'Replace manual file close with with',
      before: 'f = open("file.txt")\ndata = f.read()\nf.close()',
      after: 'with open("file.txt") as f:\n    data = f.read()',
    },
    {
      title: 'Replace repeated boolean checks with any/all',
      before: 'found = False\nfor x in items:\n    if condition(x):\n        found = True\n        break',
      after: 'found = any(condition(x) for x in items)',
    },
    {
      title: 'Replace manual grouping with itertools.groupby',
      before: 'groups = {}\nfor item in items:\n    key = item["type"]\n    if key not in groups:\n        groups[key] = []\n    groups[key].append(item)',
      after: 'from itertools import groupby\nfor key, group in groupby(sorted(items, key=lambda x: x["type"]), key=lambda x: x["type"]):\n    groups[key] = list(group)',
    },
  ];
  return [
    `**${fr ? '10 recettes de refactorisation Python' : '10 Python refactoring recipes'}**`,
    ...recipes.map(r => [
      `**${r.title}**`,
      '```python',
      `# BEFORE\n${r.before}`,
      '',
      `# AFTER\n${r.after}`,
      '```',
    ].join('\n\n')),
    `**${fr ? 'Conseil' : 'Tip'}**`,
    fr
      ? 'Appliquez une transformation à la fois et testez après chaque changement.'
      : 'Apply one transformation at a time and test after each change.',
  ].join('\n\n');
};

export const answerPythonPep8Guide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:pep.?8|style guide|naming convention|import order|line length|docstring convention|whitespace rule|code style|convention de nommage|longueur de ligne|ordre des imports)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Guide de référence PEP 8' : 'PEP 8 quick reference'}**`,
    '',
    `**${fr ? 'Imports' : 'Imports'}**`,
    fr
      ? 'Ordre : (1) stdlib, (2) tiers, (3) local. Séparez chaque groupe par une ligne vide. Pas d\'imports sauvages (`from x import *`).'
      : 'Order: (1) stdlib, (2) third-party, (3) local. Separate groups with blank lines. No wildcard imports (`from x import *`).',
    '```python',
    'import os\nimport sys\n\nimport requests\nimport typer\n\nfrom mypackage import mymodule',
    '```',
    '',
    `**${fr ? 'Longueur de ligne' : 'Line length'}**`,
    fr
      ? '79 caractères pour le code, 72 pour les docstrings/comments. PEP 8 tolère 99 (Django) ou 120 (Black).'
      : '79 characters for code, 72 for docstrings/comments. PEP 8 tolerates 99 (Django style) or 120 (Black default).',
    '',
    `**${fr ? 'Lignes vides' : 'Blank lines'}**`,
    fr
      ? '— 2 lignes vides avant les définitions de classe ou de fonction de niveau supérieur.\n— 1 ligne vide avant les méthodes de classe.\n— 1 ligne vide autour des fonctions auxiliaires dans une classe.'
      : '— 2 blank lines before top-level class/function definitions.\n— 1 blank line before class methods.\n— 1 blank line around helper functions inside a class.',
    '',
    `**${fr ? 'Espaces' : 'Whitespace'}**`,
    fr
      ? '— `spy = 1` (espaces autour de `=`)\n— `func(x, y)` (pas d\'espace avant `(`)\n— `items[0]` (pas d\'espace avant `[`)\n— `x += 1` (espaces autour des opérateurs)\n— `(a + b) * c` (parenthèses pour la priorité)'
      : '— `spy = 1` (spaces around `=`)\n— `func(x, y)` (no space before `(`)\n— `items[0]` (no space before `[`)\n— `x += 1` (spaces around operators)\n— `(a + b) * c` (parentheses for precedence)',
    '',
    `**${fr ? 'Conventions de nommage' : 'Naming conventions'}**`,
    '| Element | Convention | Example |',
    '|---------|-----------|---------|',
    '| Variable | snake_case | `user_name` |',
    '| Function | snake_case | `get_user()` |',
    '| Class | PascalCase | `UserProfile` |',
    '| Constant | UPPER_CASE | `MAX_RETRIES` |',
    '| Module/package | short_lower | `http_utils` |',
    '| "Private" | `_` prefix | `_internal_fn()` |',
    '| Name-mangled | `__` prefix | `__private()` |',
    '| Dunder | `__name__` | avoid creating new |',
    '',
    `**${fr ? 'Docstrings' : 'Docstrings'}**`,
    '```python',
    'def example(param: str) -> int:',
    '    """Single line summary.',
    '',
    '    Longer description if needed.',
    '',
    '    Args:',
    '        param: Description of parameter.',
    '',
    '    Returns:',
    '        Description of return value.',
    '    """',
    '```',
  ].join('\n');
};

export const answerPythonComparisonReference = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:diff(?:erence|érence)|versus|vs|compar(?:e|ison|er)|vs\.|or\s+)\b.*\b(?:is|==|copy|deepcopy|shallow|deep|str|repr|classmethod|staticmethod|new|init|eq|hash)\b/i.test(question)) return null;
  const fr = language === 'fr';

  const comparisons: Array<{ title: string; shortEn: string; shortFr: string }> = [
    { title: '`is` vs `==`', shortEn: '`==` checks value equality. `is` checks object identity (same memory address). Use `is` with None, True, False, and singletons. Use `==` for everything else.', shortFr: '`==` vérifie l\'égalité de valeur. `is` vérifie l\'identité (même adresse mémoire). Utilisez `is` avec None, True, False et les singletons. Utilisez `==` pour tout le reste.' },
    { title: '`copy.copy` vs `copy.deepcopy`', shortEn: '`copy.copy()` creates a shallow copy — the top-level container is new but nested objects are shared. `copy.deepcopy()` recursively duplicates everything — completely independent.', shortFr: '`copy.copy()` crée une copie superficielle — le conteneur est nouveau mais les objets imbriqués sont partagés. `copy.deepcopy()` duplique récursivement tout — complètement indépendant.' },
    { title: '`__str__` vs `__repr__`', shortEn: '`__repr__` is for developers — unambiguous, ideally `eval(repr(x)) == x`. `__str__` is for users — readable. Falls back to `__repr__` if `__str__` is not defined.', shortFr: '`__repr__` est pour les développeurs — non ambigu, idéalement `eval(repr(x)) == x`. `__str__` est pour les utilisateurs — lisible. Utilise `__repr__` par défaut si `__str__` n\'est pas défini.' },
    { title: '`@classmethod` vs `@staticmethod`', shortEn: '`@classmethod` receives `cls` as first arg — can access/modify class state. `@staticmethod` receives nothing extra — just a function namespaced in the class.', shortFr: '`@classmethod` reçoit `cls` comme premier argument — peut accéder/modifier l\'état de la classe. `@staticmethod` ne reçoit rien de plus — juste une fonction dans l\'espace de nommage de la classe.' },
    { title: '`__new__` vs `__init__`', shortEn: '`__new__` creates the instance (called first, returns the instance). `__init__` initializes the instance (called second, returns None). Override `__new__` only for immutable types or metaclasses.', shortFr: '`__new__` crée l\'instance (appelé en premier, renvoie l\'instance). `__init__` initialise l\'instance (appelé en second, renvoie None). Surchargez `__new__` seulement pour les types immuables ou les métaclasses.' },
    { title: '`__eq__` vs `__hash__`', shortEn: '`__eq__` defines equality. `__hash__` enables dict key/set membership. Mutable objects should not be hashable. If you define `__eq__`, set `__hash__ = None` for mutable classes.', shortFr: '`__eq__` définit l\'égalité. `__hash__` permet l\'utilisation comme clé de dict/ensemble. Les objets mutables ne devraient pas être hachables. Si vous définissez `__eq__`, définissez `__hash__ = None` pour les classes mutables.' },
    { title: '`@property` vs regular attribute', shortEn: '`@property` lets you define computed attributes accessed without `()`. Use for derived values, validation, or to maintain backward compatibility when replacing an attribute with logic.', shortFr: '`@property` permet de définir des attributs calculés accessibles sans `()`. Utilisez pour les valeurs dérivées, la validation ou la compatibilité ascendante lors du remplacement d\'un attribut par une logique.' },
  ];

  return [
    `**${fr ? 'Guide de référence des comparaisons Python' : 'Python comparison reference'}**`,
    '',
    ...comparisons.map(c => `**${c.title}**\n${fr ? c.shortFr : c.shortEn}`),
  ].join('\n\n');
};

export const answerPythonProjectStructureGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:project structure|directory structure|folder structure|how to structure|how to organize|package structure|src layout|flat layout|project layout|structure du projet|organisation.*projet|layout.*python)\b/i.test(question)) return null;
  const fr = language === 'fr';

  const srcExample = [
    'my_project/',
    '├── pyproject.toml          # project metadata & deps',
    '├── README.md',
    '├── src/',
    '│   └── my_project/',
    '│       ├── __init__.py',
    '│       ├── core.py',
    '│       └── utils.py',
    '├── tests/',
    '│   ├── __init__.py',
    '│   └── test_core.py',
    '└── .gitignore',
  ].join('\n');

  return [
    `**${fr ? 'Structure de projet Python' : 'Python project structure'}**`,
    '',
    `**${fr ? 'Layout recommandé (src layout)' : 'Recommended layout (src layout)'}**`,
    '```',
    srcExample,
    '```',
    '',
    `**${fr ? 'Pourquoi `src/` ?' : 'Why `src/`?'}**`,
    fr
      ? 'Le dossier `src/` sépare le code de la racine du projet, évitant les imports accidentels depuis le répertoire de travail. `pip install -e .` installe votre paquet proprement.'
      : 'The `src/` directory separates your code from the project root, preventing accidental imports from the working directory. `pip install -e .` installs your package cleanly.',
    '',
    `**${fr ? 'Fichiers clés' : 'Key files'}**`,
    fr
      ? '- `pyproject.toml` : norme moderne pour métadonnées, dépendances, configuration des outils (black, ruff, mypy, pytest).'
      : '- `pyproject.toml` : modern standard for metadata, dependencies, tool config (black, ruff, mypy, pytest).',
    fr
      ? '- `setup.py` : legacy — seulement si nécessaire pour les scripts ou extensions C.'
      : '- `setup.py` : legacy — only if needed for scripts or C extensions.',
    fr
      ? '- `requirements.txt` : facultatif — verrouille les dépendances pour le déploiement.'
      : '- `requirements.txt` : optional — lock dependencies for deployment.',
    '',
    `**${fr ? 'Flat vs src layout' : 'Flat vs src layout'}**`,
    fr
      ? '**Flat** : `my_project/` + `tests/` à la racine. Plus simple mais peut causer des conflits d\'import avec les tests. Préféré pour les petits scripts ou projets < 500 lignes.'
      : '**Flat** : `my_project/` + `tests/` at root. Simpler but can cause import conflicts with tests. Preferred for small scripts or projects < 500 lines.',
    fr
      ? '**Src** : `src/` wrapper. Plus propre pour les paquets distribuables. Recommandé par `pyOpenSci` et `scientific-python.org`.'
      : '**Src** : `src/` wrapper. Cleaner for distributable packages. Recommended by `pyOpenSci` and `scientific-python.org`.',
    '',
    `**${fr ? 'Minimal `pyproject.toml`' : 'Minimal `pyproject.toml`'}**`,
    '```toml',
    '[build-system]',
    'requires = ["setuptools"]',
    'build-backend = "setuptools.backends._legacy:_Backend"',
    '',
    '[project]',
    'name = "my-project"',
    'version = "0.1.0"',
    'requires-python = ">=3.10"',
    '```',
  ].join('\n');
};

export const answerPythonDecoratorPatterns = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:decorator pattern|decorator with arg|decorator.*wraps|class.*decorator|stack.*decorator|@.*decorator|multiple.*decorator|decorator.*param[ée]tre|cr[ée]er.*d[ée]corateur)\b/i.test(question) &&
    !/^how.*decorator/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Patrons de décorateurs Python' : 'Python decorator patterns'}**`,
    '',
    `**1. ${fr ? 'Décorateur simple' : 'Simple decorator'}**`,
    '```python',
    'from functools import wraps',
    '',
    'def log_time(func):',
    '    @wraps(func)  # preserves __name__, __doc__',
    '    def wrapper(*args, **kwargs):',
    '        import time',
    '        start = time.time()',
    '        result = func(*args, **kwargs)',
    '        print(f"{func.__name__} took {time.time() - start:.3f}s")',
    '        return result',
    '    return wrapper',
    '',
    '@log_time',
    'def process(): ...',
    '```',
    '',
    `**2. ${fr ? 'Décorateur avec paramètres' : 'Decorator with arguments'}**`,
    '```python',
    'from functools import wraps',
    '',
    'def retry(max_attempts: int = 3):',
    '    def decorator(func):',
    '        @wraps(func)',
    '        def wrapper(*args, **kwargs):',
    '            for attempt in range(max_attempts):',
    '                try:',
    '                    return func(*args, **kwargs)',
    '                except Exception as e:',
    '                    if attempt == max_attempts - 1:',
    '                        raise',
    '        return wrapper',
    '    return decorator',
    '',
    '@retry(max_attempts=5)',
    'def fetch_data(): ...',
    '```',
    '',
    `**3. ${fr ? 'Décorateur de classe' : 'Class-based decorator'}**`,
    '```python',
    'from functools import wraps',
    '',
    'class CountCalls:',
    '    def __init__(self, func):',
    '        self.func = func',
    '        self.count = 0',
    '    def __call__(self, *args, **kwargs):',
    '        self.count += 1',
    '        print(f"Call #{self.count} of {self.func.__name__}")',
    '        return self.func(*args, **kwargs)',
    '',
    '@CountCalls',
    'def say_hello():',
    '    print("Hello!")',
    '```',
    '',
    `**4. ${fr ? 'Empilement de décorateurs' : 'Stacking decorators'}**`,
    '```python',
    '@log_time',
    '@retry(max_attempts=3)',
    'def unstable_operation():',
    '    ...',
    '# Executes bottom-up: retry wraps first, then log_time wraps that',
    '```',
    '',
    `**${fr ? 'Conseil' : 'Tip'}**`,
    fr
      ? 'Utilisez toujours `@functools.wraps` dans les décorateurs de fonction. Sans lui, l\'introspection (aide, débogueur) montre le `wrapper` au lieu de la fonction originale.'
      : 'Always use `@functools.wraps` in function decorators. Without it, introspection (help, debugger) shows the `wrapper` instead of the original function.',
  ].join('\n');
};

export const answerPythonTestingPatterns = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:pytest|unit.?test|test.?case|fixture|parametrize|mock|monkey.?patch|tmp.?path|caplog|how to test|test.*pattern|test.*écrire|comment tester|tester.*code)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Patrons de test pytest' : 'pytest testing patterns'}**`,
    '',
    `**1. ${fr ? 'Fixture de base' : 'Basic fixture'}**`,
    '```python',
    'import pytest',
    '',
    '@pytest.fixture',
    'def db_connection():',
    '    conn = create_connection()',
    '    yield conn  # setup before, teardown after',
    '    conn.close()',
    '',
    'def test_query(db_connection):',
    '    result = db_connection.query("SELECT 1")',
    '    assert result == 1',
    '```',
    '',
    `**2. ${fr ? 'Paramétrage' : 'Parametrize'}**`,
    '```python',
    '@pytest.mark.parametrize("input,expected", [',
    '    (1, 2),',
    '    (2, 4),',
    '    (3, 6),',
    '])',
    'def test_double(input, expected):',
    '    assert double(input) == expected',
    '```',
    '',
    `**3. ${fr ? 'Mocking' : 'Mocking'}**`,
    '```python',
    'from unittest.mock import patch, Mock',
    '',
    'def test_fetch_data():',
    '    mock_response = Mock(status_code=200)',
    '    mock_response.json.return_value = {"key": "value"}',
    '',
    '    with patch("requests.get", return_value=mock_response):',
    '        result = fetch_data("http://example.com")',
    '        assert result["key"] == "value"',
    '```',
    '',
    `**4. ${fr ? 'Fichiers temporaires' : 'Temp files'}**`,
    '```python',
    'def test_write_read(tmp_path):',
    '    file = tmp_path / "test.txt"',
    '    file.write_text("hello")',
    '    assert file.read_text() == "hello"',
    '```',
    '',
    `**5. ${fr ? 'Capture de logs' : 'Log capture'}**`,
    '```python',
    'def test_logging(caplog):',
    '    import logging',
    '    caplog.set_level(logging.INFO)',
    '    my_function()',
    '    assert "expected message" in caplog.text',
    '```',
  ].join('\n');
};

export const answerPythonCliPatterns = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:if __name__|__name__ ==.|main|argparse|click|typer|sys\.argv|entry.?point|console.?script|CLI|command.?line|ligne de commande|point d['’]entr[eé]e)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Patrons CLI Python' : 'Python CLI patterns'}**`,
    '',
    `**1. ${fr ? 'Garde `if __name__ == "__main__"`' : 'The `if __name__ == "__main__"` guard'}**`,
    '```python',
    'def main():',
    '    """Entry point of the script."""',
    '    print("Running as script")',
    '',
    'if __name__ == "__main__":',
    '    main()',
    '```',
    fr
      ? 'Le code sous ce garde ne s\'exécute que quand le fichier est lancé directement (pas importé). Permet de réutiliser les fonctions depuis un autre module.'
      : 'Code under this guard runs only when the file is executed directly (not imported). Allows reusing functions from other modules.',
    '',
    `**2. ${fr ? '`sys.argv` — arguments bruts' : '`sys.argv` — raw arguments'}**`,
    '```python',
    'import sys',
    'if len(sys.argv) > 1:',
    '    print(f"Args: {sys.argv[1:]}")',
    'else:',
    '    print("No arguments")',
    '```',
    '',
    `**3. ${fr ? '`argparse` — arguments structurés' : '`argparse` — structured arguments'}**`,
    '```python',
    'import argparse',
    '',
    'parser = argparse.ArgumentParser(description="Process some data.")',
    'parser.add_argument("input", help="input file path")',
    'parser.add_argument("-o", "--output", default="out.txt")',
    'parser.add_argument("-v", "--verbose", action="store_true")',
    'args = parser.parse_args()',
    '',
    'print(args.input, args.output, args.verbose)',
    '```',
    '',
    `**4. ${fr ? 'Codes de sortie' : 'Exit codes'}**`,
    '```python',
    'import sys',
    'def main():',
    '    if error_condition:',
    '        print("Error occurred", file=sys.stderr)',
    '        sys.exit(1)  # non-zero = failure',
    '    sys.exit(0)  # 0 = success',
    '```',
    '',
    `**5. ${fr ? 'Point d\'entrée `pyproject.toml`' : '`pyproject.toml` entry point'}**`,
    '```toml',
    '[project.scripts]',
    'my-cli = "my_project.cli:main"',
    '```',
    fr
      ? 'Après `pip install .`, la commande `my-cli` est disponible dans le terminal.'
      : 'After `pip install .`, the `my-cli` command is available in your terminal.',
  ].join('\n');
};

export const answerPythonEdgeCases = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:edge.?case|gotcha|surprise|weird|unexpected behavior|strange|floating.*point|NaN||short.?circuit|truthy|falsy|mutable.*default|late.?bind|scope.*loop|integer.*cache|is vs ==)\b/i.test(question) &&
    !/\b(?:why.*(?:None|wrong|change|weird|strange|unexpected)|what.*happens? when)\b/i.test(question)) return null;
  const fr = language === 'fr';

  const edgeCases: Array<{ title: string; descEn: string; descFr: string; code: string }> = [
    {
      title: 'Mutable default arguments',
      descEn: 'Default arguments are evaluated once at function definition, not each call. A mutable default (like `[]`) is shared across all calls.',
      descFr: 'Les arguments par défaut sont évalués une fois à la définition, pas à chaque appel. Un défaut mutable (comme `[]`) est partagé entre tous les appels.',
      code: 'def add(item, items=[]):\n    items.append(item)\n    return items\n\nprint(add(1))  # [1]\nprint(add(2))  # [1, 2] — not [2]!\n\n# Fix:\ndef add(item, items=None):\n    if items is None:\n        items = []\n    items.append(item)\n    return items',
    },
    {
      title: 'Late-binding closures in loops',
      descEn: 'Functions created in a loop capture the loop variable by reference, not by value. All functions see the final value of the loop variable.',
      descFr: 'Les fonctions créées dans une boucle capturent la variable par référence, pas par valeur. Toutes les fonctions voient la valeur finale de la variable de boucle.',
      code: 'funcs = [lambda: i for i in range(5)]\nprint([f() for f in funcs])  # [4, 4, 4, 4, 4]\n\n# Fix:\nfuncs = [lambda x=i: x for i in range(5)]\nprint([f() for f in funcs])  # [0, 1, 2, 3, 4]',
    },
    {
      title: 'Floating point precision',
      descEn: '`0.1 + 0.2 != 0.3` due to IEEE 754 binary floating-point representation. Use `math.isclose()` or `decimal.Decimal` for exact decimal arithmetic.',
      descFr: '`0.1 + 0.2 != 0.3` à cause de la représentation binaire IEEE 754. Utilisez `math.isclose()` ou `decimal.Decimal` pour les calculs décimaux exacts.',
      code: 'print(0.1 + 0.2)        # 0.30000000000000004\nprint(0.1 + 0.2 == 0.3) # False\n\n# Fix:\nimport math\nprint(math.isclose(0.1 + 0.2, 0.3))  # True',
    },
    {
      title: 'Short-circuit `or` and `and`',
      descEn: '`or` returns the first truthy value (or the last falsy), `and` returns the first falsy (or the last truthy). Not boolean — they return one of the operands.',
      descFr: '`or` renvoie la première valeur vraie (ou la dernière fausse), `and` renvoie la première fausse (ou la dernière vraie). Pas booléen — il renvoie l\'un des opérandes.',
      code: 'print(0 or 42)     # 42 — 0 is falsy\nprint("" or "fallback")  # "fallback"\nprint(42 and 0)  # 0 — 42 is truthy, returns 0\n\n# Using for default:\nname = user_input or "default_name"',
    },
    {
      title: 'Integer interning / small integer cache',
      descEn: 'Python caches integers from -5 to 256. `a is b` may be True for small ints but False for larger ones — always use `==` for value comparison.',
      descFr: 'Python met en cache les entiers de -5 à 256. `a is b` peut être True pour les petits entiers mais False pour les plus grands — utilisez toujours `==` pour comparer des valeurs.',
      code: 'a, b = 256, 256\nprint(a is b)   # True (cached)\n\nx, y = 257, 257\nprint(x is y)   # False (or True — implementation-dependent)\nprint(x == y)   # True — always correct',
    },
    {
      title: '`NaN` comparison always False',
      descEn: '`float("nan")` is not equal to itself (`NaN != NaN`). Use `math.isnan(x)` to check for NaN.',
      descFr: '`float("nan")` n\'est pas égal à lui-même (`NaN != NaN`). Utilisez `math.isnan(x)` pour vérifier.',
      code: 'nan = float("nan")\nprint(nan == nan)               # False!\nprint(nan is nan)               # True (same object)\n\nimport math\nprint(math.isnan(nan))          # True — correct check',
    },
  ];

  return [
    `**${fr ? 'Pièges Python courants' : 'Common Python gotchas'}**`,
    ...edgeCases.map((e, i) => [
      `**${i + 1}. ${e.title}**`,
      fr ? e.descFr : e.descEn,
      '```python',
      e.code,
      '```',
    ].join('\n\n')),
    `**${fr ? 'Règle générale' : 'General rule'}**`,
    fr
      ? 'Quand le comportement semble étrange, vérifiez : (1) l\'identité vs l\'égalité, (2) la mutabilité, (3) la portée des variables, (4) l\'évaluation paresseuse (générateurs, `or`/`and`).'
      : 'When behavior seems strange, check: (1) identity vs equality, (2) mutability, (3) variable scope, (4) lazy evaluation (generators, `or`/`and`).',
  ].join('\n\n');
};

const STRING_METHODS = [
  { category: 'Transform', methods: [
    { name: '.upper()', desc: '→ uppercase', example: '"hello".upper() → "HELLO"' },
    { name: '.lower()', desc: '→ lowercase', example: '"HELLO".lower() → "hello"' },
    { name: '.capitalize()', desc: 'First char uppercase, rest lower', example: '"hello".capitalize() → "Hello"' },
    { name: '.title()', desc: 'First char of each word uppercase', example: '"hello world".title() → "Hello World"' },
    { name: '.swapcase()', desc: 'Swap upper↔lower', example: '"Hello".swapcase() → "hELLO"' },
  ]},
  { category: 'Strip/Pad', methods: [
    { name: '.strip([chars])', desc: 'Remove leading/trailing chars (default: whitespace)', example: '"  hi  ".strip() → "hi"' },
    { name: '.lstrip()', desc: 'Remove leading chars', example: '"  hi".lstrip() → "hi"' },
    { name: '.rstrip()', desc: 'Remove trailing chars', example: '"hi  ".rstrip() → "hi"' },
    { name: '.zfill(width)', desc: 'Pad with zeros on left', example: '"42".zfill(5) → "00042"' },
    { name: '.center(width)', desc: 'Center in field of given width', example: '"hi".center(5) → "  hi  "' },
  ]},
  { category: 'Split/Join', methods: [
    { name: '.split([sep])', desc: '→ list of substrings', example: '"a,b,c".split(",") → ["a","b","c"]' },
    { name: '.rsplit([sep])', desc: 'Split from right', example: '"a,b,c".rsplit(",", 1) → ["a,b","c"]' },
    { name: '.splitlines()', desc: 'Split on line breaks', example: '"a\\nb".splitlines() → ["a","b"]' },
    { name: '.join(iterable)', desc: 'Join strings with separator', example: '",".join(["a","b"]) → "a,b"' },
    { name: '.partition(sep)', desc: '→ (head, sep, tail)', example: '"a-b".partition("-") → ("a","-","b")' },
  ]},
  { category: 'Search/Replace', methods: [
    { name: '.find(sub)', desc: '→ index of first occurrence (-1 if not found)', example: '"hello".find("l") → 2' },
    { name: '.index(sub)', desc: 'Like find but raises ValueError', example: '"hello".index("l") → 2' },
    { name: '.count(sub)', desc: 'Count non-overlapping occurrences', example: '"ababa".count("aba") → 1' },
    { name: '.replace(old, new)', desc: 'Replace all occurrences', example: '"a b a".replace("a","x") → "x b x"' },
    { name: '.startswith(prefix)', desc: 'Check prefix', example: '"hello".startswith("he") → True' },
    { name: '.endswith(suffix)', desc: 'Check suffix', example: '"hello".endswith("lo") → True' },
  ]},
  { category: 'Test/Check', methods: [
    { name: '.isalpha()', desc: 'All letters?', example: '"abc".isalpha() → True' },
    { name: '.isdigit()', desc: 'All digits?', example: '"123".isdigit() → True' },
    { name: '.isalnum()', desc: 'Letters + digits only?', example: '"ab123".isalnum() → True' },
    { name: '.isspace()', desc: 'All whitespace?', example: '"   ".isspace() → True' },
    { name: '.isupper()', desc: 'All uppercase?', example: '"HI".isupper() → True' },
    { name: '.islower()', desc: 'All lowercase?', example: '"hi".islower() → True' },
  ]},
  { category: 'Formatting', methods: [
    { name: '.format(*args)', desc: 'Format with placeholders', example: '"Hello {}!".format("world")' },
    { name: '.ljust(width)', desc: 'Left-justify in field', example: '"hi".ljust(5) → "hi   "' },
    { name: '.rjust(width)', desc: 'Right-justify in field', example: '"hi".rjust(5) → "   hi"' },
    { name: '.expandtabs(size)', desc: 'Replace tabs with spaces', example: '"\\t".expandtabs(4) → "    "' },
    { name: '.removeprefix(prefix)', desc: 'Remove prefix if present (3.9+)', example: '"hello".removeprefix("he") → "llo"' },
    { name: '.removesuffix(suffix)', desc: 'Remove suffix if present (3.9+)', example: '"hello".removesuffix("lo") → "hel"' },
  ]},
];

export const answerPythonStringMethods = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:string.*method|str\.|method.*string|m[ée]thode.*cha[îi]ne|cha[îi]ne.*m[ée]thode|\.upper|\.lower|\.strip|\.split|\.join|\.replace|\.find|\.format)\b/i.test(question) &&
    !/^(?:list|show|tell|what|which).*(?:string.*method|method.*string)/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Référence des méthodes str' : 'str methods reference'}**`,
    ...STRING_METHODS.map(cat => [
      `**${cat.category}**`,
      '| Method | Description | Example |',
      '|--------|-------------|---------|',
      ...cat.methods.map(m => `| \`${m.name}\` | ${m.desc} | \`${m.example}\` |`),
    ].join('\n')),
    `**${fr ? 'Exemple complet' : 'Full example'}**`,
    '```python',
    'text = "  Hello, World!  "',
    'print(text.strip())          # "Hello, World!"',
    'print(text.lower())          # "  hello, world!  "',
    'print(text.split(","))       # ["  Hello", " World!  "]',
    'print(" ".join(["a","b"]))   # "a b"',
    'print("hello".replace("l", "x"))  # "hexxo"',
    '```',
  ].join('\n\n');
};

const LIST_METHODS = [
  { category: 'Add/Extend', methods: [
    { name: '.append(x)', desc: 'Add x to end. O(1)', example: '[1,2].append(3) → [1,2,3]' },
    { name: '.extend(iter)', desc: 'Extend with iterable elements. O(k)', example: '[1,2].extend([3,4]) → [1,2,3,4]' },
    { name: '.insert(i, x)', desc: 'Insert x at index i. O(n)', example: '[1,3].insert(1,2) → [1,2,3]' },
  ]},
  { category: 'Remove', methods: [
    { name: '.remove(x)', desc: 'Remove first occurrence of x. O(n)', example: '[1,2,1].remove(1) → [2,1]' },
    { name: '.pop([i])', desc: 'Remove & return element at i (default: last). O(1) from end, O(n) from start', example: '[1,2,3].pop(0) → 1, list is [2,3]' },
    { name: '.clear()', desc: 'Remove all elements. O(n)', example: '[1,2].clear() → []' },
  ]},
  { category: 'Query', methods: [
    { name: '.index(x)', desc: 'Index of first occurrence (raises ValueError)', example: '[10,20,30].index(20) → 1' },
    { name: '.count(x)', desc: 'Count occurrences of x', example: '[1,2,1,1].count(1) → 3' },
  ]},
  { category: 'Order', methods: [
    { name: '.sort(key, reverse)', desc: 'Sort in-place. O(n log n). Returns None', example: '[3,1,2].sort() → [1,2,3]' },
    { name: '.reverse()', desc: 'Reverse in-place. O(n). Returns None', example: '[1,2,3].reverse() → [3,2,1]' },
  ]},
  { category: 'Copy', methods: [
    { name: '.copy()', desc: 'Shallow copy of list. O(n)', example: 'orig.copy() → new list with same refs' },
  ]},
];

export const answerPythonListMethods = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:list.*method|\.append|\.extend|\.insert|\.remove|\.pop|\.sort|\.reverse|\.index|\.count|\.copy|m[ée]thode.*liste)\b/i.test(question) &&
    !/^(?:how|what|list|show).*list.*method/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Référence des méthodes list' : 'list methods reference'}**`,
    '',
    ...LIST_METHODS.map(cat => [
      `**${cat.category}**`,
      '| Method | Description | Example |',
      '|--------|-------------|---------|',
      ...cat.methods.map(m => `| \`${m.name}\` | ${m.desc} | \`${m.example}\` |`),
    ].join('\n')),
    '',
    `**${fr ? 'Différence clé' : 'Key difference'}**`,
    fr
      ? '`.append(x)` ajoute `x` comme UN élément (même si `x` est une liste). `.extend(iter)` ajoute chaque élément de l\'itérable.'
      : '`.append(x)` adds `x` as ONE element (even if `x` is a list). `.extend(iter)` adds each element of the iterable.',
    '```python',
    'items = [1, 2]',
    'items.append([3, 4])    # [1, 2, [3, 4]]',
    'items = [1, 2]',
    'items.extend([3, 4])    # [1, 2, 3, 4]',
    '```',
  ].join('\n');
};

const DICT_METHODS = [
  { category: 'Access', methods: [
    { name: 'd[key]', desc: 'Get value for key (raises KeyError if missing)', example: 'd["a"] → 1 (if key exists)' },
    { name: '.get(key, default)', desc: 'Get value or default (no error)', example: 'd.get("x", 0) → 0' },
    { name: '.setdefault(key, default)', desc: 'Get value or insert default and return it', example: 'd.setdefault("k", []).append(1)' },
    { name: 'd[key] = val', desc: 'Set value for key', example: 'd["b"] = 2' },
  ]},
  { category: 'Remove', methods: [
    { name: '.pop(key, default)', desc: 'Remove key & return value (raises KeyError or returns default)', example: 'd.pop("a", None) → 1' },
    { name: '.popitem()', desc: 'Remove & return last inserted (key, value). O(1)', example: 'd.popitem() → ("b", 2)' },
    { name: '.clear()', desc: 'Remove all items', example: 'd.clear() → {}' },
    { name: 'del d[key]', desc: 'Delete specific key (raises KeyError)', example: 'del d["a"]' },
  ]},
  { category: 'Iteration', methods: [
    { name: '.keys()', desc: 'View of keys', example: 'list(d.keys()) → ["a", "b"]' },
    { name: '.values()', desc: 'View of values', example: 'list(d.values()) → [1, 2]' },
    { name: '.items()', desc: 'View of (key, value) pairs', example: 'for k, v in d.items():' },
  ]},
  { category: 'Merge/Update', methods: [
    { name: '.update(other)', desc: 'Merge dict into this one (overwrites)', example: 'd.update({"c": 3})' },
    { name: 'd1 | d2', desc: 'New merged dict (3.9+)', example: 'merged = a | b' },
    { name: 'd1 |= d2', desc: 'In-place merge (3.9+)', example: 'a |= b' },
  ]},
  { category: 'Query', methods: [
    { name: 'key in d', desc: 'Check if key exists (preferred)', example: '"a" in d → True/False' },
    { name: 'len(d)', desc: 'Number of key/value pairs', example: 'len({"a":1}) → 1' },
    { name: '.copy()', desc: 'Shallow copy', example: 'd.copy() → new dict' },
    { name: '@dataclass', desc: 'Typed dict alternative', example: 'from dataclasses import dataclass' },
  ]},
];

export const answerPythonDictMethods = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:dict.*method|dictionar|\.get|\.keys|\.values|\.items|\.setdefault|\.update|\.pop|\.popitem|m[ée]thode.*dict|m[ée]thode.*dictionnaire)\b/i.test(question) &&
    !/^(?:how|what|list|show).*dict.*method/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Référence des méthodes dict' : 'dict methods reference'}**`,
    '',
    ...DICT_METHODS.map(cat => [
      `**${cat.category}**`,
      '| Method | Description | Example |',
      '|--------|-------------|---------|',
      ...cat.methods.map(m => `| \`${m.name}\` | ${m.desc} | \`${m.example}\` |`),
    ].join('\n')),
    '',
    `**${fr ? '`.get()` vs `[key]` vs `.setdefault()`' : '`.get()` vs `[key]` vs `.setdefault()`'}**`,
    '```python',
    'd = {"a": 1}',
    '',
    'val = d["b"]       # KeyError — crashes if missing',
    'val = d.get("b", 0)  # 0 — safe, no exception',
    'val = d.setdefault("b", 0)  # 0 AND sets d["b"] = 0',
    '```',
  ].join('\n');
};

export const answerPythonFileIoPatterns = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:file.?io|file.?read|file.?write|open.*file|with.*open|encoding|binary.*file|text.*file|\\.txt|pathlib|StringIO|BytesIO|tempfile|os\.path|.*fichier|encodage)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Patrons d\'entrée/sortie de fichiers' : 'File I/O patterns'}**`,
    '',
    `**1. ${fr ? 'Lecture/écriture texte' : 'Text read/write'}**`,
    '```python',
    'with open("file.txt", encoding="utf-8") as f:',
    '    content = f.read()          # entire file → str',
    '    lines = f.readlines()       # → list[str]',
    '    for line in f:              # lazy iteration',
    '        process(line)',
    '',
    'with open("out.txt", "w", encoding="utf-8") as f:',
    '    f.write("hello\\n")',
    '    print("world", file=f)',
    '```',
    '',
    `**2. ${fr ? 'Fichiers binaires' : 'Binary files'}**`,
    '```python',
    'with open("data.bin", "rb") as f:',
    '    raw = f.read(1024)  # first 1024 bytes',
    '',
    'with open("out.bin", "wb") as f:',
    '    f.write(b"\\x00\\x01\\x02")',
    '```',
    '',
    `**3. ${fr ? '`pathlib` (moderne, recommandé)' : '`pathlib` (modern, recommended)'}**`,
    '```python',
    'from pathlib import Path',
    '',
    'p = Path("data/file.txt")',
    'p.parent.mkdir(parents=True, exist_ok=True)',
    'p.write_text("hello", encoding="utf-8")',
    'content = p.read_text(encoding="utf-8")',
    'p.write_bytes(b"binary")',
    'raw = p.read_bytes()',
    '',
    '# Iterate directory',
    'for py_file in Path("src").rglob("*.py"):',
    '    print(py_file.name)',
    '```',
    '',
    `**4. ${fr ? 'Flux en mémoire (StringIO / BytesIO)' : 'In-memory streams (StringIO / BytesIO)'}**`,
    '```python',
    'from io import StringIO, BytesIO',
    '',
    'buf = StringIO()',
    'print("hello", file=buf)',
    'print("world", file=buf)',
    'result = buf.getvalue()  # "hello\\nworld\\n"',
    '',
    'buf = BytesIO()',
    'buf.write(b"\\x00\\x01")',
    'buf.seek(0)',
    'data = buf.read()',
    '```',
    '',
    `**5. ${fr ? 'Fichiers temporaires' : 'Temporary files'}**`,
    '```python',
    'from tempfile import NamedTemporaryFile, TemporaryDirectory',
    '',
    'with NamedTemporaryFile(mode="w", suffix=".txt", delete=True) as f:',
    '    f.write("temporary data")',
    '    path = f.name  # automatically cleaned up',
    '',
    'with TemporaryDirectory() as tmpdir:',
    '    tmp = Path(tmpdir) / "work.txt"',
    '    tmp.write_text("data")',
    '```',
  ].join('\n');
};

export const answerPythonLoggingPatterns = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:log|logging|logger|handler|formatter|basicConfig|loguru|debug.*log|info.*log|error.*log|journalisation|log.*fichier)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Patrons de logging Python' : 'Python logging patterns'}**`,
    '',
    `**1. ${fr ? 'Configuration rapide' : 'Quick setup'}**`,
    '```python',
    'import logging',
    '',
    'logging.basicConfig(',
    '    level=logging.INFO,',
    '    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",',
    '    datefmt="%H:%M:%S",',
    ')',
    'log = logging.getLogger(__name__)',
    'log.info("App started")  # 14:30:01 | INFO     | __main__ | App started',
    '```',
    '',
    `**2. ${fr ? 'Niveaux de log' : 'Log levels'}**`,
    '```python',
    'logging.debug("verbose detail")     # 10 — dev only',
    'logging.info("normal operation")    # 20 — default if no config',
    'logging.warning("something odd")    # 30',
    'logging.error("failed!")            # 40',
    'logging.critical("crash!")          # 50',
    '```',
    '',
    `**3. ${fr ? 'Logger hiérarchique' : 'Hierarchical logger'}**`,
    '```python',
    '# In mypackage/module.py',
    'log = logging.getLogger(__name__)  # "mypackage.module"',
    '# Inherits config from "mypackage" or root logger',
    'log.info("module loaded")',
    '',
    '# Control by name:',
    'logging.getLogger("mypackage").setLevel(logging.DEBUG)',
    'logging.getLogger("mypackage.module").setLevel(logging.WARNING)',
    '```',
    '',
    `**4. ${fr ? 'Plusieurs handlers' : 'Multiple handlers'}**`,
    '```python',
    'log = logging.getLogger("app")',
    'log.setLevel(logging.DEBUG)',
    '',
    '# Console: INFO+',
    'console = logging.StreamHandler()',
    'console.setLevel(logging.INFO)',
    'console.setFormatter(logging.Formatter("%(message)s"))',
    'log.addHandler(console)',
    '',
    '# File: DEBUG+ with timestamps',
    'file_h = logging.FileHandler("app.log")',
    'file_h.setLevel(logging.DEBUG)',
    `file_h.setFormatter(logging.Formatter('`,
    `    "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s"`,
    `))`,
    'log.addHandler(file_h)',
    '```',
    '',
    `**5. ${fr ? 'Configuration depuis un dict' : 'Config from dict'}**`,
    '```python',
    'import logging.config',
    '',
    'LOGGING_CONFIG = {',
    '    "version": 1,',
    '    "formatters": {"simple": {"format": "%(levelname)s | %(message)s"}},',
    '    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "simple"}},',
    '    "root": {"level": "INFO", "handlers": ["console"]},',
    '}',
    'logging.config.dictConfig(LOGGING_CONFIG)',
    '```',
    '',
    `**${fr ? 'Conseil' : 'Tip'}**`,
    fr
      ? 'N\'utilisez pas `print()` pour les logs — le module `logging` gère les niveaux, les fichiers, les timestamps et la rotation. Utilisez `log.exception()` dans les blocs `except` pour capturer la trace complète.'
      : 'Never use `print()` for logs — the `logging` module handles levels, files, timestamps, and rotation. Use `log.exception()` in `except` blocks to capture the full traceback.',
  ].join('\n');
};

export const answerPythonEnvGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:venv|virtual.?env|virtual environment|conda|poetry|pip|pipenv|environnement virtuel|gestionnaire de paquets|package manager|requirements\.txt|install.*package)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Guide de gestion d\'environnement Python' : 'Python environment management guide'}**`,
    '',
    `**1. ${fr ? 'Environnement virtuel (`venv`)' : 'Virtual environment (`venv`)**'}`,
    '```bash',
    'python -m venv .venv          # create environment',
    'source .venv/bin/activate     # activate (macOS/Linux)',
    '.venv\\Scripts\\activate       # activate (Windows)',
    'deactivate                    # exit environment',
    '```',
    fr
      ? 'Toujours créer un environnement virtuel par projet. Il isole les dépendances pour éviter les conflits.'
      : 'Always create one virtual environment per project. It isolates dependencies to avoid conflicts.',
    '',
    `**2. ${fr ? 'Installer des paquets (`pip`)' : 'Installing packages (`pip`)**'}`,
    '```bash',
    'pip install requests          # latest version',
    'pip install requests==2.31.0  # exact version',
    'pip install "requests>=2.0"   # minimum version',
    'pip install -r requirements.txt  # from file',
    'pip list                      # show installed',
    'pip freeze > requirements.txt # save current versions',
    '```',
    '',
    `**3. ${fr ? '`requirements.txt` vs `pyproject.toml`' : '`requirements.txt` vs `pyproject.toml`**'}`,
    fr
      ? '`requirements.txt` : verrouillage pour déploiement (`pip freeze > requirements.txt`). `pyproject.toml` : métadonnées du projet, dépendances déclaratives. Préférez `pyproject.toml` pour les projets distribuables.'
      : '`requirements.txt` : deployment lock (`pip freeze > requirements.txt`). `pyproject.toml` : project metadata, declarative deps. Prefer `pyproject.toml` for distributable projects.',
    '',
    `**4. ${fr ? '`conda`' : '`conda`**'}`,
    '```bash',
    'conda create -n myenv python=3.12  # create env with Python version',
    'conda activate myenv               # activate',
    'conda install numpy pandas         # install from conda-forge',
    'conda env export > environment.yml # export',
    '```',
    fr
      ? 'Conda gère aussi les binaires non-Python (CUDA, BLAS, etc.). Utile pour la data science.'
      : 'Conda also manages non-Python binaries (CUDA, BLAS, etc.). Useful for data science.',
    '',
    `**5. ${fr ? '`poetry` — gestionnaire moderne' : '`poetry` — modern package manager**'}`,
    '```bash',
    'poetry new my-project          # create new project',
    'poetry add requests            # add dependency',
    'poetry add --dev pytest        # dev dependency',
    'poetry install                 # install all deps',
    'poetry shell                   # activate env',
    '```',
    '',
    `**6. ${fr ? 'Bonnes pratiques' : 'Best practices'}**`,
    (fr ? '- .gitignore : incluez .venv/, __pycache__/, *.pyc.' : '- .gitignore: include .venv/, __pycache__/, *.pyc.'),
    (fr ? '- Ne commitez jamais .venv/.' : '- Never commit .venv/.'),
    (fr ? '- Utilisez des versions exactes dans requirements.txt pour la reproductibilite.' : '- Use exact versions in requirements.txt for reproducibility.'),
    (fr ? '- Un seul environnement par projet, pas un global pour tout.' : '- One environment per project, not one global environment for everything.'),
  ].join('\n');
};

export const answerPythonToolingGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:pdb|debug(?:ger|ging)|breakpoint|linter|lint|ruff|flake8|mypy|type.?check|black|formatter|code.?style|vs.?code|ide|extension|outil|formateur)\b/i.test(question) &&
    !/\b(?:comment.*debug|how.*debug|what.*debug|setting? up|configure.*python|python.*configure|install.*python.*tool)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    `**${fr ? 'Guide des outils Python' : 'Python tooling guide'}**`,
    '',
    `**1. ${fr ? 'Débogage avec `pdb`' : 'Debugging with `pdb`**'}`,
    '```python',
    'import pdb; pdb.set_trace()   # Python < 3.7',
    'breakpoint()                   # Python 3.7+ — same thing',
    '',
    '# Once in debugger:',
    '# n      — next line',
    '# s      — step into function',
    '# c      — continue to next breakpoint',
    '# p x    — print variable x',
    '# l      — list source around current line',
    '# q      — quit',
    '```',
    '',
    `**2. ${fr ? 'Post-mortem debugging' : 'Post-mortem debugging**'}`,
    '```bash',
    'python -m pdb script.py  # run under debugger, stops on exception',
    '',
    '# Or from code:',
    'import traceback; traceback.print_exc()  # print full traceback',
    '```',
    '',
    `**3. ${fr ? 'Linters et formateurs' : 'Linters and formatters'}**`,
    (fr ? '| Outil | Role | Usage |' : '| Tool | Role | Usage |'),
    (fr ? '|-------|------|-------|' : '|------|------|-------|'),
    '| ruff | Linter + formatter (rapide, remplace flake8 + isort) | `ruff check .` / `ruff format .` |',
    '| black | Formateur auto (opinionated, zéro config) | `black .` |',
    '| mypy | Vérificateur de types statique | `mypy src/` |',
    '| isort | Trie les imports | `isort .` |',
    '| flake8 | Linter classique (pyflakes + pycodestyle) | `flake8 src/` |',
    '',
    `**4. ${fr ? 'Configuration VS Code' : 'VS Code setup'}**`,
    (fr ? 'Extensions recommandees : Python (Microsoft), Pylance, Ruff. Creez .vscode/settings.json :' : 'Recommended extensions: Python (Microsoft), Pylance, Ruff. Create .vscode/settings.json:'),
    '```json',
    '{',
    '    "python.defaultInterpreterPath": ".venv/bin/python",',
    '    "python.analysis.typeCheckingMode": "basic",',
    '    "[python]": { "editor.formatOnSave": true, "editor.defaultFormatter": "charliermarsh.ruff" },',
    '    "python.terminal.activateEnvironment": true',
    '}',
    '```',
    '',
    (fr ? '**5. Configuration pyproject.toml**' : '**5. pyproject.toml tool config**'),
    '```toml',
    '[tool.ruff]',
    'line-length = 100',
    'target-version = "py312"',
    '',
    '[tool.ruff.lint]',
    'select = ["E", "F", "I", "N", "W", "UP"]',
    '',
    '[tool.mypy]',
    'strict = true',
    'python_version = "3.12"',
    '```',
  ].join('\n');
};

export const TOPIC_RELATIONSHIPS: Record<string, Array<{ topic: string; questionEn: string; questionFr: string }>> = {
  'list': [
    { topic: 'tuple', questionEn: 'When should I use a tuple instead of a list?', questionFr: 'Quand utiliser un tuple plutôt qu\'une liste ?' },
    { topic: 'list-comprehension', questionEn: 'How do list comprehensions work?', questionFr: 'Comment fonctionnent les compréhensions de liste ?' },
    { topic: 'dictionary', questionEn: 'What about dictionaries?', questionFr: 'Et les dictionnaires ?' },
  ],
  'tuple': [
    { topic: 'list', questionEn: 'When should I use a list instead of a tuple?', questionFr: 'Quand utiliser une liste plutôt qu\'un tuple ?' },
    { topic: 'dictionary', questionEn: 'Can I use a tuple as a dict key?', questionFr: 'Puis-je utiliser un tuple comme clé de dict ?' },
    { topic: 'unpacking', questionEn: 'How does tuple unpacking work?', questionFr: 'Comment fonctionne le déballage de tuple ?' },
  ],
  'dictionary': [
    { topic: 'set', questionEn: 'What\'s the difference between dict and set?', questionFr: 'Quelle est la différence entre dict et set ?' },
    { topic: 'defaultdict', questionEn: 'How does defaultdict help?', questionFr: 'Comment defaultdict peut-il aider ?' },
    { topic: 'json', questionEn: 'How do I convert dict to JSON?', questionFr: 'Comment convertir un dict en JSON ?' },
  ],
  'set': [
    { topic: 'list', questionEn: 'When to use set vs list?', questionFr: 'Quand utiliser set vs list ?' },
    { topic: 'dictionary', questionEn: 'How is a set different from a dict?', questionFr: 'En quoi set diffère de dict ?' },
    { topic: 'frozenset', questionEn: 'What is a frozenset?', questionFr: 'Qu\'est-ce qu\'un frozenset ?' },
  ],
  'string': [
    { topic: 'formatting', questionEn: 'How do I choose an f-string vs .format()?', questionFr: 'Comment choisir entre f-string et .format() ?' },
    { topic: 'regex', questionEn: 'How do I use regex with strings?', questionFr: 'Comment utiliser les regex avec les chaînes ?' },
    { topic: 'bytes', questionEn: 'What\'s the difference between str and bytes?', questionFr: 'Quelle est la différence entre str et bytes ?' },
  ],
  'function': [
    { topic: 'lambda', questionEn: 'When should I use a lambda?', questionFr: 'Quand utiliser une lambda ?' },
    { topic: 'decorator', questionEn: 'How do decorators work?', questionFr: 'Comment fonctionnent les décorateurs ?' },
    { topic: 'args-kwargs', questionEn: 'How do *args and **kwargs work?', questionFr: 'Comment fonctionnent *args et **kwargs ?' },
  ],
  'class': [
    { topic: 'inheritance', questionEn: 'How does inheritance work?', questionFr: 'Comment fonctionne l\'héritage ?' },
    { topic: 'dataclass', questionEn: 'What are dataclasses?', questionFr: 'Que sont les dataclasses ?' },
    { topic: 'type-hints', questionEn: 'How do I type-hint a class?', questionFr: 'Comment typer une classe ?' },
  ],
  'exception': [
    { topic: 'exception-chaining', questionEn: 'How does exception chaining work?', questionFr: 'Comment fonctionne le chaînage d\'exceptions ?' },
    { topic: 'try-except-finally', questionEn: 'How do try/except/finally work?', questionFr: 'Comment fonctionne try/except/finally ?' },
    { topic: 'logging', questionEn: 'How do I log exceptions properly?', questionFr: 'Comment journaliser les exceptions correctement ?' },
  ],
  'import': [
    { topic: 'project-structure', questionEn: 'How should I structure my project?', questionFr: 'Comment structurer mon projet ?' },
    { topic: 'module', questionEn: 'What is a Python module?', questionFr: 'Qu\'est-ce qu\'un module Python ?' },
    { topic: 'package', questionEn: 'How do I create a package?', questionFr: 'Comment créer un paquet ?' },
  ],
  'file-io': [
    { topic: 'pathlib', questionEn: 'How does pathlib work?', questionFr: 'Comment fonctionne pathlib ?' },
    { topic: 'encoding', questionEn: 'How do I handle file encodings?', questionFr: 'Comment gérer les encodages de fichiers ?' },
    { topic: 'tempfile', questionEn: 'How do I use temporary files?', questionFr: 'Comment utiliser les fichiers temporaires ?' },
  ],
  'for-loop': [
    { topic: 'while-loop', questionEn: 'When to use for vs while?', questionFr: 'Quand utiliser for vs while ?' },
    { topic: 'enumerate', questionEn: 'How does enumerate work?', questionFr: 'Comment fonctionne enumerate ?' },
    { topic: 'list-comprehension', questionEn: 'Can I replace this for-loop with a comprehension?', questionFr: 'Puis-je remplacer cette boucle par une compréhension ?' },
  ],
  'decorator': [
    { topic: 'closure', questionEn: 'How do closures relate to decorators?', questionFr: 'Quel est le lien entre fermetures et décorateurs ?' },
    { topic: 'classmethod', questionEn: 'What\'s the difference between @classmethod and @staticmethod?', questionFr: 'Différence entre @classmethod et @staticmethod ?' },
    { topic: 'wraps', questionEn: 'Why use @functools.wraps?', questionFr: 'Pourquoi utiliser @functools.wraps ?' },
  ],
  'async-await': [
    { topic: 'coroutine', questionEn: 'How do coroutines work?', questionFr: 'Comment fonctionnent les coroutines ?' },
    { topic: 'asyncio-gather', questionEn: 'How does asyncio.gather() compare to TaskGroup?', questionFr: 'Comparaison asyncio.gather() vs TaskGroup ?' },
    { topic: 'concurrency', questionEn: 'When to use asyncio vs threading vs multiprocessing?', questionFr: 'Quand utiliser asyncio vs threading vs multiprocessing ?' },
  ],
  'type-hints': [
    { topic: 'mypy', questionEn: 'How do I set up mypy?', questionFr: 'Comment configurer mypy ?' },
    { topic: 'protocol', questionEn: 'What is typing.Protocol?', questionFr: 'Qu\'est-ce que typing.Protocol ?' },
    { topic: 'typeddict', questionEn: 'How does TypedDict work?', questionFr: 'Comment fonctionne TypedDict ?' },
  ],
  'generator': [
    { topic: 'iterator', questionEn: 'What\'s the difference between a generator and an iterator?', questionFr: 'Différence entre générateur et itérateur ?' },
    { topic: 'yield', questionEn: 'How does yield work?', questionFr: 'Comment fonctionne yield ?' },
    { topic: 'comprehension', questionEn: 'Generator expression vs list comprehension?', questionFr: 'Expression génératrice vs compréhension de liste ?' },
  ],
  'comprehension': [
    { topic: 'generator', questionEn: 'Generator expression vs list comprehension?', questionFr: 'Expression génératrice vs compréhension de liste ?' },
    { topic: 'map-filter-reduce', questionEn: 'Should I use map/filter or comprehension?', questionFr: 'Faut-il utiliser map/filter ou les compréhensions ?' },
    { topic: 'for-loop', questionEn: 'Can I rewrite this loop as a comprehension?', questionFr: 'Puis-je réécrire cette boucle en compréhension ?' },
  ],
  'venv': [
    { topic: 'pip', questionEn: 'How do I install packages with pip?', questionFr: 'Comment installer des paquets avec pip ?' },
    { topic: 'poetry', questionEn: 'What is poetry and should I use it?', questionFr: 'Qu\'est-ce que poetry et devrais-je l\'utiliser ?' },
    { topic: 'pyproject-toml', questionEn: 'How does pyproject.toml work?', questionFr: 'Comment fonctionne pyproject.toml ?' },
  ],
  'pip': [
    { topic: 'venv', questionEn: 'How do virtual environments work?', questionFr: 'Comment fonctionnent les environnements virtuels ?' },
    { topic: 'requirements-txt', questionEn: 'What is requirements.txt?', questionFr: 'Qu\'est-ce que requirements.txt ?' },
    { topic: 'pyproject-toml', questionEn: 'pyproject.toml vs requirements.txt?', questionFr: 'pyproject.toml vs requirements.txt ?' },
  ],
  'pdb': [
    { topic: 'debugging', questionEn: 'What debugging tools exist?', questionFr: 'Quels outils de débogage existent ?' },
    { topic: 'breakpoint', questionEn: 'How does breakpoint() work?', questionFr: 'Comment fonctionne breakpoint() ?' },
    { topic: 'logging', questionEn: 'When to use logging vs print?', questionFr: 'Quand utiliser logging vs print ?' },
  ],
  'logging': [
    { topic: 'debugging', questionEn: 'How do I debug Python code?', questionFr: 'Comment déboguer du code Python ?' },
    { topic: 'exception-handling', questionEn: 'How to log exceptions properly?', questionFr: 'Comment journaliser les exceptions ?' },
    { topic: 'print', questionEn: 'Why not use print for logging?', questionFr: 'Pourquoi ne pas utiliser print pour journaliser ?' },
  ],
};



export const answerPythonConcurrencyGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:threading|multiprocessing|gil|race.?condition|deadlock|thread.?safe|parallelis|concurrent\.futures|executor|pool)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide de la concurrence Python' : 'Python concurrency guide') + '**',
    '',
    '**' + (fr ? '1. threading — E/S-bound, leger' : '1. threading — I/O-bound, lightweight') + '**',
    (fr ? 'Utile quand le programme attend des E/S (reseau, fichier). Le GIL empeche le vrai parallelisme CPU.' : 'Useful when the program waits for I/O (network, file). The GIL prevents true CPU parallelism.'),
    '```python',
    "import threading",
    "results = []",
    "def work(n): results.append(n * n)",
    "threads = [threading.Thread(target=work, args=(i,)) for i in range(10)]",
    "for t in threads: t.start()",
    "for t in threads: t.join()",
    '```',
    '',
    '**' + (fr ? '2. multiprocessing — CPU-bound, parallele' : '2. multiprocessing — CPU-bound, parallel') + '**',
    (fr ? 'Chaque processus a son propre interpreteur et sa memoire. Pas de GIL. Communication par Queue ou Pipe.' : 'Each process has its own interpreter and memory. No GIL. Communication via Queue or Pipe.'),
    '```python',
    "from multiprocessing import Pool",
    "with Pool(4) as pool:",
    "    results = pool.map(expensive_cpu_func, data)",
    '```',
    '',
    '**' + (fr ? '3. asyncio — E/S-bound, cooperatif' : '3. asyncio — I/O-bound, cooperative') + '**',
    (fr ? 'Monothread, mais commute entre les taches pendant les attentes E/S. Ideal pour de nombreuses connexions reseaux.' : 'Single-threaded, but switches between tasks during I/O waits. Ideal for many network connections.'),
    '```python',
    "import asyncio",
    "async def fetch(url):",
    "    async with httpx.AsyncClient() as client:",
    "        return await client.get(url)",
    "results = asyncio.run(asyncio.gather(fetch(u) for u in urls))",
    '```',
    '',
    '**' + (fr ? '4. Le GIL (Global Interpreter Lock)' : '4. The GIL (Global Interpreter Lock)') + '**',
    (fr ? 'Le GIL permet a un seul thread d executor du bytecode Python a la fois. Pour contourner : multiprocessing, C-extensions, ou asyncio.' : 'The GIL allows only one thread to execute Python bytecode at a time. To bypass: multiprocessing, C-extensions, or asyncio.'),
    '',
    '**' + (fr ? '5. concurrent.futures — abstraction unifiee' : '5. concurrent.futures — unified abstraction') + '**',
    '```python',
    "from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor",
    "with ThreadPoolExecutor(max_workers=4) as ex:",
    "    futures = [ex.submit(fn, arg) for arg in args]",
    "    for f in futures: print(f.result())",
    '```',
  ].join('\n');
};

export const answerPythonHttpApiGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:http|requests?|httpx|api|rest|endpoint|session|retry|pagination|webhook)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide HTTP / API Python' : 'Python HTTP / API guide') + '**',
    '',
    '**1. ' + (fr ? 'La bibliotheque requests' : 'The requests library') + '**',
    '```python',
    "import requests",
    "resp = requests.get('https://api.example.com/data', params={'page': 1})",
    "resp.raise_for_status()           # raise on 4xx/5xx",
    "data = resp.json()                # parse JSON body",
    "headers = resp.headers            # response headers",
    "status = resp.status_code         # 200, 404, etc.",
    '```',
    '',
    '**2. ' + (fr ? 'Sessions avec requests.Session' : 'Sessions with requests.Session') + '**',
    (fr ? 'Reutilise la connexion TCP, garde les cookies. 6x plus rapide pour des requetes multiples.' : 'Reuses TCP connection, keeps cookies. 6x faster for multiple requests.'),
    '```python',
    "with requests.Session() as s:",
    '    s.headers.update({"Authorization": "Bearer xxx"})',
    "    resp = s.get('https://api.example.com/me')",
    '```',
    '',
    '**3. ' + (fr ? 'Gerer les erreurs' : 'Error handling') + '**',
    '```python',
    "try:",
    "    resp = requests.get(url, timeout=10)",
    "    resp.raise_for_status()",
    "except requests.Timeout:",
    "    print('Request timed out')",
    "except requests.ConnectionError:",
    "    print('DNS or connection failed')",
    "except requests.HTTPError as e:",
    "    print(f\"HTTP {e.response.status_code}\")",
    '```',
    '',
    '**4. ' + (fr ? 'Retry automatique' : 'Automatic retries') + '**',
    '```python',
    "from urllib3.util.retry import Retry",
    "from requests.adapters import HTTPAdapter",
    "session = requests.Session()",
    "retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503])",
    "session.mount('https://', HTTPAdapter(max_retries=retries))",
    '```',
    '',
    '**5. ' + (fr ? 'httpx — alternative moderne' : 'httpx — modern alternative') + '**',
    (fr ? 'Support natif async, HTTP/2, et interface similaire a requests.' : 'Native async support, HTTP/2, and requests-like interface.'),
  ].join('\n');
};

export const answerPythonDatabaseGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:sql(?:ite|alchemy)?|database|orm|query|migration|connection.?pool|cursor|insert|select|db\.)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide des bases de donnees Python' : 'Python database guide') + '**',
    '',
    '**1. ' + (fr ? 'SQLite avec le module sqlite3' : 'SQLite with the sqlite3 module') + '**',
    '```python',
    "import sqlite3",
    "conn = sqlite3.connect('app.db')",
    "conn.row_factory = sqlite3.Row",
    "cur = conn.cursor()",
    "cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')",
    "cur.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))",
    "conn.commit()",
    "conn.close()",
    '```',
    '',
    '**2. ' + (fr ? 'Requetes parametrees (safe)' : 'Parameterized queries (safe)') + '**',
    (fr ? 'TOUJOURS utiliser ? ou :nom pour eviter les injections SQL.' : 'ALWAYS use ? or :name to avoid SQL injection.'),
    '```python',
    "cur.execute('SELECT * FROM users WHERE name = ? AND age > ?', (name, min_age))",
    "cur.execute('SELECT * FROM users WHERE name = :name', {'name': name})",
    '```',
    '',
    '**3. ' + (fr ? 'SQLAlchemy — ORM complet' : 'SQLAlchemy — full ORM') + '**',
    '```python',
    "from sqlalchemy import create_engine, Column, Integer, String",
    "from sqlalchemy.orm import declarative_base, Session",
    "Base = declarative_base()",
    "class User(Base):",
    "    __tablename__ = 'users'",
    "    id = Column(Integer, primary_key=True)",
    "    name = Column(String)",
    "engine = create_engine('sqlite:///app.db')",
    "Base.metadata.create_all(engine)",
    "with Session(engine) as session:",
    "    session.add(User(name='Bob'))",
    "    session.commit()",
    '```',
    '',
    '**4. ' + (fr ? 'Connection pooling' : 'Connection pooling') + '**',
    (fr ? 'SQLAlchemy gere un pool de connexions automatiquement. Configurez avec pool_size=5, max_overflow=10.' : 'SQLAlchemy manages a connection pool automatically. Configure with pool_size=5, max_overflow=10.'),
    '',
    '**5. ' + (fr ? 'Migrations avec Alembic' : 'Migrations with Alembic') + '**',
    '```bash',
    "alembic init alembic          # initialize",
    'alembic revision --autogenerate -m "add email"  # detect changes',
    "alembic upgrade head          # apply migrations",
    '```',
  ].join('\n');
};

export const answerPythonSerializationGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:serialize|deserialize|json|pickle|msgpack|yaml|marshal|dump.*load|encode.*object|decode.*object)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide de serialisation Python' : 'Python serialization guide') + '**',
    '',
    '**1. JSON — ' + (fr ? 'standard web' : 'web standard') + '**',
    '```python',
    "import json",
    "# write",
    "with open('data.json', 'w') as f: json.dump({'key': 'value', 'num': 42}, f)",
    "# read",
    "with open('data.json') as f: data = json.load(f)",
    "# custom encoder for non-standard types",
    "from datetime import datetime",
    "class DateTimeEncoder(json.JSONEncoder):",
    "    def default(self, obj):",
    "        if isinstance(obj, datetime): return obj.isoformat()",
    "        return super().default(obj)",
    "json.dumps(obj, cls=DateTimeEncoder)",
    '```',
    '',
    '**2. ' + (fr ? 'Pickle — objets Python natifs' : 'Pickle — native Python objects') + '**',
    '```python',
    "import pickle",
    "with open('data.pkl', 'wb') as f: pickle.dump(obj, f)",
    "with open('data.pkl', 'rb') as f: obj = pickle.load(f)",
    '```',
    (fr ? 'Danger : pickle.load() execute du code arbitraire. Ne jamais depickler des donnees non fiables.' : 'Danger: pickle.load() executes arbitrary code. Never unpickle untrusted data.'),
    '',
    '**3. ' + (fr ? 'Msgpack — compact et rapide' : 'Msgpack — compact and fast') + '**',
    '```bash',
    "pip install msgpack",
    '```',
    '```python',
    "import msgpack",
    "packed = msgpack.packb({'key': 'value', 'num': 42})",
    "unpacked = msgpack.unpackb(packed)",
    '```',
    '',
    '**4. ' + (fr ? 'YAML — lisible par l humain' : 'YAML — human-readable') + '**',
    '```python',
    "import yaml",
    "with open('config.yaml') as f: config = yaml.safe_load(f)",
    '```',
    (fr ? 'Utilisez safe_load() pour eviter l execution de code.' : 'Use safe_load() to prevent code execution.'),
    '',
    '**5. ' + (fr ? 'Choisir le bon format' : 'Choosing the right format') + '**',
    (fr ? '| Format | Cas d usage | Securite | Performance |' : '| Format | Use case | Security | Performance |'),
    (fr ? '|--------|-------------|----------|-------------|' : '|--------|----------|----------|-------------|'),
    '| JSON | APIs, config | Safe | Moderate |',
    '| Pickle | Python interne, cache | Unsafe (code exec) | Fast |',
    '| Msgpack | Performance critique | Safe (data only) | Very fast |',
    '| YAML | Config humaine | Use safe_load | Slow |',
  ].join('\n');
};

export const answerPythonDatetimeGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:datetime|date.*time|timezone|strftime|strptime|timedelta|dateutil|pytz|tzinfo)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide des dates et heures Python' : 'Python date/time guide') + '**',
    '',
    '**1. ' + (fr ? 'Creer et manipuler' : 'Creating and manipulating') + '**',
    '```python',
    "from datetime import datetime, date, time, timedelta, timezone",
    "now = datetime.now()                         # local time (naive)",
    "utc_now = datetime.now(timezone.utc)         # timezone-aware UTC",
    "specific = datetime(2025, 12, 25, 10, 30)    # 2025-12-25 10:30",
    "today = date.today()",
    '```',
    '',
    '**2. ' + (fr ? 'Formatter et analyser' : 'Formatting and parsing') + '**',
    '```python',
    "from datetime import datetime",
    "# format",
    "dt = datetime(2025, 12, 25, 10, 30)",
    "dt.strftime('%Y-%m-%d %H:%M')        # '2025-12-25 10:30'",
    "dt.strftime('%A, %d %B %Y')          # 'Thursday, 25 December 2025'",
    "# parse",
    "parsed = datetime.strptime('2025-12-25', '%Y-%m-%d')",
    '```',
    '',
    '**3. ' + (fr ? 'Calculs avec timedelta' : 'Arithmetic with timedelta') + '**',
    '```python',
    "from datetime import timedelta",
    "tomorrow = today + timedelta(days=1)",
    "last_week = today - timedelta(weeks=1)",
    "diff = date(2025, 12, 31) - date(2025, 1, 1)  # timedelta(days=364)",
    '```',
    '',
    '**4. ' + (fr ? 'Fuseaux horaires' : 'Timezones') + '**',
    '```python',
    "# Python 3.9+ uses zoneinfo (stdlib)",
    "from zoneinfo import ZoneInfo",
    "paris = datetime(2025, 6, 15, 14, 0, tzinfo=ZoneInfo('Europe/Paris'))",
    "ny = paris.astimezone(ZoneInfo('America/New_York'))",
    "# for Python < 3.9, use dateutil or pytz",
    '```',
    '',
    '**5. ' + (fr ? 'Bonnes pratiques' : 'Best practices') + '**',
    (fr ? '- Stockez les dates en UTC. Convertissez pour l affichage.' : '- Store dates in UTC. Convert for display only.'),
    (fr ? '- Utilisez datetime.now(timezone.utc) pas datetime.utcnow() (deprecie).' : '- Use datetime.now(timezone.utc) not datetime.utcnow() (deprecated).'),
    (fr ? '- Pour des sequences de dates, utilisez dateutil.rrule.' : '- For date sequences, use dateutil.rrule.'),
  ].join('\n');
};

export const answerPythonProfilingGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:profile|profiler|cprofile|timeit|benchmark|optimize|bottleneck|memory.?usage|cpu.?time|perf_counter)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide de profiling Python' : 'Python profiling guide') + '**',
    '',
    '**1. ' + (fr ? 'Mesurer avec timeit' : 'Measuring with timeit') + '**',
    '```python',
    "import timeit",
    "timeit.timeit('sum(range(100))', number=10000)",
    '# from IPython: %timeit sum(range(100))',
    '```',
    '',
    '**2. ' + (fr ? 'Profiler avec cProfile' : 'Profiling with cProfile') + '**',
    '```bash',
    "python -m cProfile -o output.prof my_script.py",
    '```',
    '```python',
    "import pstats",
    'p = pstats.Stats("output.prof")',
    'p.sort_stats("cumtime").print_stats(20)',
    '```',
    '',
    '**3. ' + (fr ? 'Analyse visuelle avec SnakeViz' : 'Visual analysis with SnakeViz') + '**',
    '```bash',
    "pip install snakeviz",
    "snakeviz output.prof  # opens interactive flame chart in browser",
    '```',
    '',
    '**4. ' + (fr ? 'Optimisations rapides' : 'Quick optimizations') + '**',
    (fr ? '| Technique | Gain | Exemple |' : '| Technique | Gain | Example |'),
    (fr ? '|-----------|------|---------|' : '|-----------|------|---------|'),
    '| __slots__ | Memoire (-50%) | class Point: __slots__ = (x, y) |',
    '| Comprehensions | 2x | [x*2 for x in data] vs for loop |',
    '| @lru_cache | Cache | @functools.lru_cache(maxsize=128) |',
    '| Local bindings | 1.5x | local_func = obj.method; local_func() |',
    '| map not list | Memoire | Use map() lazy instead of list comprehension |',
    '',
    '**5. ' + (fr ? 'Regle d or' : 'Golden rule') + '**',
    (fr ? 'Ne devinez pas ce qui est lent. Profilez d abord, optimisez ensuite. 90% du temps est dans 10% du code.' : 'Don\'t guess what is slow. Profile first, optimize second. 90% of time is in 10% of code.'),
  ].join('\n');
};

export const answerPythonPackagingGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:publish|distribute|pypi|setuptools|wheel|egg|twine|package.*build|upload.*pip|pip.*publish)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide de packaging Python' : 'Python packaging guide') + '**',
    '',
    '**1. ' + (fr ? 'Structure du projet' : 'Project structure') + '**',
    '```',
    'my-package/',
    '  pyproject.toml',
    '  src/',
    '    my_package/',
    '      __init__.py',
    '      core.py',
    '  tests/',
    '    test_core.py',
    '  README.md',
    '```',
    '',
    '**2. pyproject.toml**',
    '```toml',
    '[build-system]',
    'requires = ["setuptools>=68"]',
    'build-backend = "setuptools.backends._legacy:_Backend"',
    '',
    '[project]',
    'name = "my-package"',
    'version = "0.1.0"',
    'description = "A useful package"',
    'requires-python = ">=3.10"',
    'dependencies = ["requests>=2"]',
    '',
    '[project.scripts]',
    'my-cli = "my_package.core:main"',
    '```',
    '',
    '**3. ' + (fr ? 'Construire et publier' : 'Build and publish') + '**',
    '```bash',
    'python -m build                    # creates dist/*.whl and dist/*.tar.gz',
    'twine check dist/*                # verify',
    'twine upload dist/*               # publish to PyPI',
    '',
    '# test first on TestPyPI',
    'twine upload --repository testpypi dist/*',
    'pip install --index-url https://test.pypi.org/simple/ my-package',
    '```',
    '',
    '**4. ' + (fr ? 'Entry points (CLI)' : 'Entry points (CLI)') + '**',
    (fr ? 'Le [project.scripts] dans pyproject.toml cree une commande shell automatiquement.' : 'The [project.scripts] in pyproject.toml auto-creates a shell command.'),
    '```python',
    "def main():",
    "    import sys",
    "    print('Hello from my-cli!')",
    "    sys.exit(0 if run() else 1)",
    '```',
    '',
    '**5. ' + (fr ? 'Bonnes pratiques' : 'Best practices') + '**',
    (fr ? '- Versionnement semantique (MAJOR.MINOR.PATCH)' : '- Semantic versioning (MAJOR.MINOR.PATCH)'),
    (fr ? '- Inclure README.md, LICENSE' : '- Include README.md, LICENSE'),
    (fr ? '- Utiliser src/ layout (evite les imports avant build)' : '- Use src/ layout (avoids pre-build import issues)'),
    (fr ? '- Ajouter __version__ dans __init__.py' : '- Add __version__ in __init__.py'),
  ].join('\n');
};

export const answerPythonFunctionalGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:itertools|functools|map.*filter|filter.*map|reduce.*list|partial|compose|operator\.\w+|curry|pure.?function)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide de programmation fonctionnelle Python' : 'Python functional programming guide') + '**',
    '',
    '**1. itertools — ' + (fr ? 'boucles efficaces' : 'efficient looping') + '**',
    '```python',
    "from itertools import chain, cycle, islice, product, permutations, groupby",
    "list(chain([1,2], [3,4]))       # [1,2,3,4]",
    'list(islice(cycle("AB"), 6))    # ["A","B","A","B","A","B"]',
    'list(product([1,2], ["a","b"])) # [(1,"a"),(1,"b"),(2,"a"),(2,"b")]',
    "list(permutations([1,2,3], 2))  # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]",
    "for key, group in groupby(sorted(data), key=lambda x: x['type']):",
    "    process(key, list(group))",
    '```',
    '',
    '**2. functools — ' + (fr ? 'outils fonctionnels' : 'functional tools') + '**',
    '```python',
    "from functools import partial, reduce, lru_cache, wraps",
    "# partial",
    "import json; load_json = partial(json.loads, cls=CustomDecoder)",
    "# reduce",
    "product = reduce(lambda a, b: a * b, [1,2,3,4,5])",
    "# lru_cache",
    "@lru_cache(maxsize=128)",
    "def fib(n):",
    "    return n if n < 2 else fib(n-1) + fib(n-2)",
    '```',
    '',
    '**3. operator — ' + (fr ? 'evite les lambdas' : 'avoid lambdas') + '**',
    '```python',
    'from operator import itemgetter, attrgetter, methodcaller, add, mul',
    'sorted(users, key=itemgetter("age"))',
    'sum = reduce(add, [1,2,3,4,5])',
    'mult = reduce(mul, [1,2,3,4,5])',
    '```',
    '',
    '**4. map, filter, reduce**',
    (fr ? 'Ces fonctions retournent des iterateurs (paresseux). Preferez les comprehensions pour la lisibilite sauf pour les pipelines.' : 'These return lazy iterators. Prefer comprehensions for readability except for pipelines.'),
    '```python',
    "squares = map(lambda x: x**2, range(10))",
    "evens = filter(lambda x: x % 2 == 0, range(10))",
    "result = reduce(lambda a, x: a | x, flags, 0)",
    '```',
    '',
    '**5. ' + (fr ? 'Composition et pipelines' : 'Composition and pipelines') + '**',
    '```python',
    "from functools import reduce",
    "def pipe(*funcs):",
    "    return lambda x: reduce(lambda v, f: f(v), funcs, x)",
    "process = pipe(str.strip, str.lower, json.loads)",
    "result = process(raw)",
    '```',
  ].join('\n');
};

export const answerPythonSecurityGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:security|hash|encrypt|sanitize|injection|sql.*inject|secret|env.*var(?:iable)?|token|password.*safe)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide de securite Python' : 'Python security guide') + '**',
    '',
    '**1. ' + (fr ? 'Hacher les mots de passe' : 'Hashing passwords') + '**',
    '```python',
    "import hashlib",
    "# NEVER use plain sha256 or md5 for passwords",
    "from hashlib import pbkdf2_hmac",
    "salt = os.urandom(16)",
    "hash = pbkdf2_hmac('sha256', password.encode(), salt, 100_000)",
    "# Better: use bcrypt",
    "import bcrypt",
    "hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())",
    "bcrypt.checkpw(password.encode(), hash)  # True/False",
    '```',
    '',
    '**2. ' + (fr ? 'Variables d environnement (secrets)' : 'Environment variables (secrets)') + '**',
    '```python',
    "import os",
    "from dotenv import load_dotenv",
    "load_dotenv()",
    "api_key = os.environ.get('API_KEY')",
    "if not api_key: raise ValueError('API_KEY not set')",
    '```',
    '```bash',
    "# .env file -- NEVER commit this!",
    'API_KEY=sk-abc123...',
    'DATABASE_URL=postgresql://user:pass@localhost/db',
    '```',
    '',
    '**3. ' + (fr ? 'Protection contre les injections SQL' : 'SQL injection prevention') + '**',
    '```python',
    "# BAD - string formatting",
    "cur.execute(f\"SELECT * FROM users WHERE name = '{name}'\")  # NO",
    "# GOOD - parameterized query",
    "cur.execute('SELECT * FROM users WHERE name = ?', (name,))",
    '```',
    '',
    '**4. ' + (fr ? 'Nettoyer les entrees utilisateur' : 'Sanitizing user input') + '**',
    '```python',
    "email = input('Email: ').strip()",
    "if not re.match(r'^[^@]+@[^@]+\\.[^@]+$', email):",
    "    raise ValueError('Invalid email')",
    "# For HTML output, always escape",
    "import html",
    "safe = html.escape(user_input)  # <script> -> &lt;script&gt;",
    '```',
  ].join('\n');
};

export const answerPythonContextManagerGuide = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:context.?manager|with.*statement|contextlib|contextvar|exitstack|@contextmanager|__enter__|__exit__)\b/i.test(question)) return null;
  const fr = language === 'fr';
  return [
    '**' + (fr ? 'Guide des context managers Python' : 'Python context manager guide') + '**',
    '',
    '**1. ' + (fr ? 'Le mot-cle with' : 'The with statement') + '**',
    '```python',
    "with open('file.txt') as f:",
    "    content = f.read()",
    "file automatically closed after the block",
    '```',
    '',
    '**2. ' + (fr ? 'Implementer un context manager (classe)' : 'Implementing a context manager (class)') + '**',
    '```python',
    "class Timer:",
    "    def __enter__(self):",
    "        self.start = time.perf_counter()",
    "        return self",
    "    def __exit__(self, exc_type, exc_val, exc_tb):",
    "        elapsed = time.perf_counter() - self.start",
    "        print(f'Took {elapsed:.3f}s')",
    "        return False  # propagate exceptions",
    "with Timer():",
    "    expensive_operation()",
    '```',
    '',
    '**3. ' + (fr ? '@contextmanager (generator)' : '@contextmanager (generator)') + '**',
    '```python',
    "from contextlib import contextmanager",
    "@contextmanager",
    "def temporary_change(obj, attr, value):",
    "    original = getattr(obj, attr)",
    "    setattr(obj, attr, value)",
    "    try:",
    "        yield",
    "    finally:",
    "        setattr(obj, attr, original)",
    "with temporary_change(config, 'debug', True):",
    "    run_tests()",
    '```',
    '',
    '**4. ' + (fr ? 'contextlib utilitaires' : 'contextlib utilities') + '**',
    '```python',
    "from contextlib import suppress, redirect_stdout, ExitStack",
    "# suppress specific exceptions",
    "with suppress(FileNotFoundError):",
    "    os.remove('temp.txt')",
    "# ExitStack -- manage dynamic resources",
    "with ExitStack() as stack:",
    "    files = [stack.enter_context(open(f)) for f in filenames]",
    '```',
    '',
    '**5. contextvars — ' + (fr ? 'variables de contexte' : 'context variables') + '**',
    (fr ? 'contextvars permet d avoir des variables isolees par tache asyncio. Utile pour les IDs de requete, les connexions DB par contexte.' : 'contextvars provides task-local variables for asyncio. Useful for request IDs, per-context DB connections.'),
    '```python',
    "from contextvars import ContextVar",
    "request_id: ContextVar[str] = ContextVar('request_id')",
    "async def handle_request(req):",
    "    token = request_id.set(req.id)",
    "    await process_request()",
    "    request_id.reset(token)",
    '```',
  ].join('\n');
};

export const answerPythonScopeVariable = (question: string, language: AdvancedAiLanguage): string | null => {
  if (!/\b(?:global(?:\s+(?:variable|keyword|scope|vs|and|local))?|local(?:\s+(?:variable|scope|vs|and|global))?|nonlocal\b|scope\s+(?:of\s+)?variable|LEGB\b|variable\s+(?:scope|visibility)|port[e\u00e9]e\s+(?:des\s+)?variables?|globale?\s+(?:variable|port[e\u00e9]e)|locale?\s+(?:variable|port[e\u00e9]e)|diff(?:\u00e9rence|erence)\s+(?:entre|between)\s+(?:global|local))\b/i.test(question)) return null;
  const fr = language === 'fr';
  const parts: string[] = [];

  parts.push(`**${fr ? "Port\u00e9e des variables en Python (Global vs Local)" : "Variable scope in Python (Global vs Local)"}**`);
  parts.push('');

  parts.push(`**${fr ? "1. Qu\u2019est-ce qu\u2019une variable globale ?" : "1. What is a global variable?"}**`);
  parts.push(fr
    ? "Une variable **globale** est d\u00e9finie en dehors de toute fonction, au niveau du module. Elle est accessible depuis n\u2019importe o\u00f9 dans le fichier (fonctions, classes, autres modules apr\u00e8s import). Sa dur\u00e9e de vie est celle du programme."
    : "A **global** variable is defined outside any function, at the module level. It is accessible from anywhere in the file (functions, classes, other modules after import). Its lifetime equals the program\u2019s lifetime.");
  parts.push('');
  parts.push('```python');
  parts.push('# Global variable');
  parts.push("count = 0  # 'count' is global \u2014 defined at module level");
  parts.push('');
  parts.push('def increment():');
  parts.push('    print(count)  # Accessible here \u2014 reads 0');
  parts.push('');
  parts.push('increment()');
  parts.push('```');
  parts.push('');

  parts.push(`**${fr ? "2. Qu\u2019est-ce qu\u2019une variable locale ?" : "2. What is a local variable?"}**`);
  parts.push(fr
    ? "Une variable **locale** est d\u00e9finie \u00e0 l\u2019int\u00e9rieur d\u2019une fonction. Elle n\u2019existe que pendant l\u2019appel de cette fonction et n\u2019est pas accessible en dehors. Chaque appel de fonction cr\u00e9e un nouvel espace de noms local."
    : "A **local** variable is defined inside a function. It exists only during that function call and is not accessible outside. Each function call creates a fresh local namespace.");
  parts.push('');
  parts.push('```python');
  parts.push('def show():');
  parts.push("    msg = 'Hello'  # 'msg' is local \u2014 only exists inside show()");
  parts.push('    print(msg)');
  parts.push('');
  parts.push('show()            # prints: Hello');
  parts.push("print(msg)        # NameError: name 'msg' is not defined");
  parts.push('```');
  parts.push('');

  parts.push(`**${fr ? "3. Le mot-cl\u00e9 `global`" : "3. The `global` keyword"}**`);
  parts.push(fr
    ? "Par d\u00e9faut, assigner une valeur \u00e0 une variable dans une fonction la cr\u00e9e comme **locale**. Pour modifier une variable globale, d\u00e9clarez-la avec `global` dans la fonction."
    : "By default, assigning to a variable inside a function creates it as **local**. To modify a global variable, declare it with `global` inside the function.");
  parts.push('');
  parts.push('```python');
  parts.push('count = 0              # global');
  parts.push('');
  parts.push('def increment():');
  parts.push("    global count        # 'count' now refers to the global");
  parts.push('    count += 1');
  parts.push('');
  parts.push('increment()');
  parts.push('print(count)          # 1');
  parts.push('');
  parts.push('def broken():');
  parts.push("    count = 5          # creates NEW local, does NOT modify global");
  parts.push('');
  parts.push('broken()');
  parts.push('print(count)          # still 1');
  parts.push('```');
  parts.push('');

  parts.push(`**${fr ? "4. Le mot-cl\u00e9 `nonlocal`" : "4. The `nonlocal` keyword"}**`);
  parts.push(fr
    ? "`nonlocal` est utilis\u00e9 dans les fonctions imbriqu\u00e9es pour modifier une variable de la fonction englobante (ni globale, ni locale \u2014 la port\u00e9e interm\u00e9diaire)."
    : "`nonlocal` is used in nested functions to modify a variable from the enclosing function (neither global nor local \u2014 the scope in between).");
  parts.push('');
  parts.push('```python');
  parts.push('def outer():');
  parts.push("    x = 'outer'       # enclosing scope");
  parts.push('');
  parts.push('    def inner():');
  parts.push('        nonlocal x    # refer to x from outer');
  parts.push("        x = 'inner'   # modifies outer\u2019s x");
  parts.push('');
  parts.push('    inner()');
  parts.push('    print(x)          # "inner" \u2014 modified by inner()');
  parts.push('```');
  parts.push('');

  parts.push(`**${fr ? "5. La r\u00e8gle LEGB (ordre de r\u00e9solution des noms)" : "5. The LEGB rule (name resolution order)"}**`);
  parts.push(fr
    ? "Quand Python rencontre un nom, il le cherche dans cet ordre :"
    : "When Python encounters a name, it looks it up in this order:");
  parts.push('');
  for (const entry of [
    { letter: 'L', nameEn: 'Local', nameFr: 'Locale', descEn: 'Inside the current function', descFr: "À l\u2019intérieur de la fonction courante" },
    { letter: 'E', nameEn: 'Enclosing', nameFr: 'Englobante', descEn: 'Any enclosing function (outer functions in nested scopes)', descFr: 'Les fonctions englobantes (port\u00e9es ext\u00e9rieures)' },
    { letter: 'G', nameEn: 'Global', nameFr: 'Globale', descEn: 'The module level (top-level names)', descFr: 'Le niveau du module (noms de premier niveau)' },
    { letter: 'B', nameEn: 'Built-in', nameFr: 'Int\u00e9gr\u00e9e', descEn: "Python\u2019s built-in namespace (print, len, etc.)", descFr: "L\u2019espace de noms int\u00e9gr\u00e9 de Python (print, len, etc.)" },
  ]) {
    parts.push(`**${entry.letter}** \u2014 ${fr ? entry.nameFr : entry.nameEn}: ${fr ? entry.descFr : entry.descEn}`);
  }
  parts.push('');
  parts.push('```python');
  parts.push('x = "global"          # G');
  parts.push('');
  parts.push('def outer():');
  parts.push("    x = 'enclosing'   # E");
  parts.push('');
  parts.push('    def inner():');
  parts.push("        x = 'local'   # L \u2014 shadows enclosing and global");
  parts.push('        print(x)      # "local"');
  parts.push('    inner()');
  parts.push('outer()');
  parts.push('```');
  parts.push('');

  parts.push(`**${fr ? "6. Erreurs fr\u00e9quentes" : "6. Common mistakes"}**`);
  const mistakes = [
    { en: "**UnboundLocalError**: assigning to a variable inside a function makes it local \u2014 even if a global with the same name exists. Use `global` to opt in.", fr: "**UnboundLocalError** : assigner \u00e0 une variable dans une fonction la rend locale, m\u00eame si une variable globale du m\u00eame nom existe. Utilisez `global` pour l\u2019indiquer." },
    { en: "**Shadowing**: a local variable with the same name as a global one silently hides the global inside the function.", fr: "**Shadowing (masquage)** : une variable locale du m\u00eame nom qu\u2019une variable globale cache silencieusement la globale dans la fonction." },
    { en: "**Overusing `global`**: modifying globals from many functions makes code hard to reason about. Prefer passing parameters and returning values.", fr: "**Utilisation excessive de `global`** : modifier des globales depuis plusieurs fonctions rend le code difficile \u00e0 suivre. Pr\u00e9f\u00e9rez passer des param\u00e8tres et retourner des valeurs." },
    { en: "**Forgetting `nonlocal`**: assigning to a variable in a nested function creates a local \u2014 use `nonlocal` to modify the enclosing scope variable.", fr: "**Oubli de `nonlocal`** : assigner \u00e0 une variable dans une fonction imbriqu\u00e9e cr\u00e9e une locale \u2014 utilisez `nonlocal` pour modifier la variable de la port\u00e9e englobante." },
    { en: "**Mutable globals without `global`**: modifying a mutable global (e.g., `my_list.append(1)`) works without `global` because you\u2019re mutating, not reassigning. But reassigning (`my_list = []`) requires `global`.", fr: "**Globale mutable sans `global`** : modifier une globale mutable (ex. `my_list.append(1)`) fonctionne sans `global` car vous muteze, pas r\u00e9assignez. Mais r\u00e9assigner (`my_list = []`) n\u00e9cessite `global`." },
  ];
  for (const m of mistakes) {
    parts.push(`- ${fr ? m.fr : m.en}`);
  }
  parts.push('');

  parts.push(`**${fr ? "7. Aide-m\u00e9moire rapide" : "7. Quick reference"}**`);
  parts.push('');
  parts.push('| ' + (fr ? 'Situation' : 'Situation') + ' | ' + (fr ? 'Code' : 'Code') + ' | ' + (fr ? 'R\u00e9sultat' : 'Result') + ' |');
  parts.push('|---|---|---|');
  parts.push('| ' + (fr ? 'Lire une globale' : 'Read a global') + ' | `print(x)` | \u2705 ' + (fr ? 'Lit la globale' : 'Reads the global') + ' |');
  parts.push('| ' + (fr ? 'Assigner sans `global`' : 'Assign without `global`') + ' | `x = 1` | \u274c ' + (fr ? 'Cr\u00e9e une locale' : 'Creates local') + ' |');
  parts.push('| ' + (fr ? 'Assigner avec `global`' : 'Assign with `global`') + ' | `global x; x = 1` | \u2705 ' + (fr ? 'Modifie la globale' : 'Modifies global') + ' |');
  parts.push('| ' + (fr ? 'Muter une globale' : 'Mutate a global') + ' | `lst.append(1)` | \u2705 ' + (fr ? 'Mute sans `global`' : 'Mutates without `global`') + ' |');
  parts.push('| ' + (fr ? 'Fct imbriqu\u00e9e, assigner' : 'Nested, assign') + ' | `nonlocal x; x = 1` | \u2705 ' + (fr ? 'Modifie la port\u00e9e englobante' : 'Modifies enclosing scope') + ' |');

  return parts.join('\n');
};







// BUILTIN_SPECS — comprehensive reference for all built-in functions, types, and constructs
// Each entry: name, type, signature, description_en, description_fr, return_type, examples_en, examples_fr, order_en, order_fr, mistakes_en, mistakes_fr
interface BuiltinSpec {
  name: string;
  type: string;
  signature: string;
  descriptionEn: string;
  descriptionFr: string;
  returnType: string;
  examplesEn: string[];
  examplesFr: string[];
  orderEn: string[];
  orderFr: string[];
  mistakesEn: string[];
  mistakesFr: string[];
}

const BUILTIN_SPECS: Record<string, BuiltinSpec> = {
  "abs": {
    name: "abs",
    type: "function",
    signature: "abs(x) -> number",
    descriptionEn: "Returns the absolute value of a number. Works with int, float, and complex numbers.",
    descriptionFr: "Retourne la valeur absolue d\'un nombre. Fonctionne avec int, float et les nombres complexes.",
    returnType: "int, float, or complex",
    examplesEn: [
      "abs(-5)           # 5",
      "abs(3.14)          # 3.14",
      "abs(3+4j)          # 5.0",
    ],
    examplesFr: [
      "abs(-5)           # 5",
      "abs(3.14)          # 3.14",
      "abs(3+4j)          # 5.0",
    ],
    orderEn: [
      "1. Python checks the argument type",
      "2. If complex: returns sqrt(real^2 + imag^2)",
      "3. Otherwise: returns the non-negative value",
    ],
    orderFr: [
      "1. Python verifie le type de l'argument",
      "2. Si complexe : retourne sqrt(reel^2 + imag^2)",
      "3. Sinon : retourne la valeur non negative",
    ],
    mistakesEn: [
      "Confusing absolute value with `math.fabs()` — `abs()` works on int/float/complex, `math.fabs()` only on float",
    ],
    mistakesFr: [
      "Confondre valeur absolue avec `math.fabs()` — `abs()` marche avec int/float/complex, `math.fabs()` seulement float",
    ],
  },
  "all": {
    name: "all",
    type: "function",
    signature: "all(iterable) -> bool",
    descriptionEn: "Returns True if every element of the iterable is truthy. Short-circuits on the first falsy value.",
    descriptionFr: "Retourne True si tous les elements de l\'iterable sont vrais. S\'arrete au premier element faux.",
    returnType: "bool",
    examplesEn: [
      "all([1, 2, 3])         # True",
      "all([1, 0, 3])         # False (0 is falsy)",
      "all([])                 # True (vacuous truth)",
    ],
    examplesFr: [
      "all([1, 2, 3])         # True",
      "all([1, 0, 3])         # False (0 est faux)",
      "all([])                 # True (verite vide)",
    ],
    orderEn: [
      "1. Iterates over each element",
      "2. If any element is falsy (0, '', None, False, []), immediately returns False",
      "3. If all elements are truthy, returns True",
      "4. Empty iterable returns True (vacuous truth)",
    ],
    orderFr: [
      "1. Parcourt chaque element",
      "2. Si un element est faux (0, '', None, False, []), retourne False immediatement",
      "3. Si tous sont vrais, retourne True",
      "4. Iterable vide retourne True (verite vide)",
    ],
    mistakesEn: [
      "`all([])` returns True (vacuous truth) — surprising to beginners",
      "`all()` checks truthiness, not equality — `all([1, 2, 3])` is True, not about any specific value",
    ],
    mistakesFr: [
      "`all([])` retourne True (verite vide) — surprenant pour les debutants",
      "`all()` verifie la veracite, pas l'egalite",
    ],
  },
  "any": {
    name: "any",
    type: "function",
    signature: "any(iterable) -> bool",
    descriptionEn: "Returns True if at least one element of the iterable is truthy. Short-circuits on the first truthy value.",
    descriptionFr: "Retourne True si au moins un element de l\'iterable est vrai. S\'arrete au premier vrai.",
    returnType: "bool",
    examplesEn: [
      "any([0, 0, 1])         # True",
      "any([0, 0, 0])         # False",
      "any([])                 # False",
    ],
    examplesFr: [
      "any([0, 0, 1])         # True",
      "any([0, 0, 0])         # False",
      "any([])                 # False",
    ],
    orderEn: [
      "1. Iterates over each element",
      "2. If any element is truthy, immediately returns True",
      "3. If all are falsy, returns False",
      "4. Empty iterable returns False",
    ],
    orderFr: [
      "1. Parcourt chaque element",
      "2. Si un element est vrai, retourne True immediatement",
      "3. Si tous sont faux, retourne False",
      "4. Iterable vide retourne False",
    ],
    mistakesEn: [
      "`any([])` returns False (unlike `all([])` which returns True)",
      "Empty iterable always returns the identity element — False for `or`, True for `and`",
    ],
    mistakesFr: [
      "`any([])` retourne False (contrairement a `all([])` qui retourne True)",
      "Iterable vide retourne toujours l'element identite",
    ],
  },
  "ascii": {
    name: "ascii",
    type: "function",
    signature: "ascii(obj) -> str",
      descriptionEn: "Returns a string containing a printable representation of an object, escaping non-ASCII characters with backslash x, backslash u, or backslash U escapes.",
      descriptionFr: "Retourne une chaine contenant une representation imprimable d\\'un objet, en echappant les caracteres non-ASCII.",
    returnType: "str",
    examplesEn: [
      "ascii('cafe')      # \"'cafe'\"",
      "ascii('caf\u00e9')     # \"'caf\\xe9'\"",
      "ascii(42)            # '42'",
    ],
    examplesFr: [
      "ascii('cafe')       # \"'cafe'\"",
      "ascii('caf\u00e9')     # \"'caf\\xe9'\"",
      "ascii(42)            # '42'",
    ],
    orderEn: [
      "1. Calls `repr()` on the object",
      "2. Replaces non-ASCII characters with escape sequences",
    ],
    orderFr: [
      "1. Appelle `repr()` sur l'objet",
      "2. Remplace les caracteres non-ASCII par des sequences d'echappement",
    ],
    mistakesEn: [
      "Confusing `ascii()` with `repr()` — `ascii()` forces ASCII-only output",
      "`ascii()` is Python 3+; Python 2 had `repr()` that behaved similarly",
    ],
    mistakesFr: [
      "Confondre `ascii()` et `repr()` — `ascii()` force une sortie ASCII uniquement",
    ],
  },
  "bin": {
    name: "bin",
    type: "function",
    signature: "bin(x) -> str",
    descriptionEn: "Converts an integer to its binary string representation prefixed with \'0b\'.",
    descriptionFr: "Convertit un entier en sa representation binaire prefixee de \'0b\'.",
    returnType: "str",
    examplesEn: [
      "bin(5)              # '0b101'",
      "bin(255)             # '0b11111111'",
      "bin(42)              # '0b101010'",
    ],
    examplesFr: [
      "bin(5)              # '0b101'",
      "bin(255)             # '0b11111111'",
      "bin(42)              # '0b101010'",
    ],
    orderEn: [
      "1. Python converts the integer to base-2",
      "2. Prepends '0b' to indicate binary format",
    ],
    orderFr: [
      "1. Python convertit l'entier en base 2",
      "2. Ajoute '0b' pour indiquer le format binaire",
    ],
    mistakesEn: [
      "`bin()` only works on integers — use `format()` for other types",
      "The result is a string, not a number",
    ],
    mistakesFr: [
      "`bin()` ne fonctionne qu'avec les entiers",
    ],
  },
  "bool": {
    name: "bool",
    type: "type",
    signature: "bool(x=False) -> bool",
    descriptionEn: "Returns a Boolean value (True or False). When called with no argument or with a falsy value, returns False. With any truthy value, returns True.",
    descriptionFr: "Retourne une valeur booleenne (True ou False). Sans argument ou avec une valeur fausse, retourne False.",
    returnType: "bool",
    examplesEn: [
      "bool(1)              # True",
      "bool(0)              # False",
      "bool([])             # False",
      "bool('hello')        # True",
    ],
    examplesFr: [
      "bool(1)              # True",
      "bool(0)              # False",
      "bool([])             # False",
      "bool('hello')        # True",
    ],
    orderEn: [
      "1. Python checks the truthiness of the argument",
      "2. Returns False if the argument is falsy (0, '', None, False, 0.0, [], (), {}, empty range, zero in numeric types)",
      "3. Returns True otherwise",
    ],
    orderFr: [
      "1. Python verifie la veracite de l'argument",
      "2. Retourne False si l'argument est faux",
      "3. Retourne True sinon",
    ],
    mistakesEn: [
      "`bool` is a subclass of `int` — True == 1 and False == 0",
      "Some objects are falsy by default if `__bool__` or `__len__` returns 0",
    ],
    mistakesFr: [
      "`bool` est une sous-classe de `int`",
    ],
  },
  "bytearray": {
    name: "bytearray",
    type: "type",
    signature: "bytearray(source=b'') -> bytearray",
    descriptionEn: "Returns a mutable array of bytes (0-255). Can be created from a string (with encoding), iterable of ints, or bytes-like object.",
    descriptionFr: "Retourne un tableau mutable d\'octets (0-255). Cree depuis une chaine (avec encodage), un iterable d\'entiers, ou un objet bytes.",
    returnType: "bytearray",
    examplesEn: [
      "bytearray(5)         # bytearray(b'\\x00\\x00\\x00\\x00\\x00')",
      "bytearray([65, 66, 67])  # bytearray(b'ABC')",
      "bytearray('abc', 'utf-8')  # bytearray(b'abc')",
    ],
    examplesFr: [
      "bytearray(5)         # bytearray(b'\\x00\\x00\\x00\\x00\\x00')",
      "bytearray([65, 66, 67])  # bytearray(b'ABC')",
      "bytearray('abc', 'utf-8')  # bytearray(b'abc')",
    ],
    orderEn: [
      "1. Determines the source type: int creates a zero-filled array of that size",
      "2. String + encoding encodes the string to bytes",
      "3. Iterable of ints creates bytes from each integer value",
    ],
    orderFr: [
      "1. Determine le type de la source : int cree un tableau de cette taille rempli de zeros",
      "2. Chaine + encodage encode la chaine en octets",
      "3. Iterable d'entiers cree les octets",
    ],
    mistakesEn: [
      "`bytearray` is mutable, `bytes` is immutable",
      "Elements must be integers in range 0-255",
    ],
    mistakesFr: [
      "`bytearray` est mutable, `bytes` est immuable",
    ],
  },
  "bytes": {
    name: "bytes",
    type: "type",
    signature: "bytes(source=b'') -> bytes",
    descriptionEn: "Returns an immutable sequence of bytes (0-255). Similar to `bytearray` but read-only.",
    descriptionFr: "Retourne une sequence immuable d\'octets (0-255). Similaire a `bytearray` mais en lecture seule.",
    returnType: "bytes",
    examplesEn: [
      "bytes(5)           # b'\\x00\\x00\\x00\\x00\\x00'",
      "bytes([65, 66, 67])  # b'ABC'",
      "b'hello'             # bytes literal",
    ],
    examplesFr: [
      "bytes(5)           # b'\\x00\\x00\\x00\\x00\\x00'",
      "bytes([65, 66, 67])  # b'ABC'",
      "b'hello'             # bytes literal",
    ],
    orderEn: [
      "1. Same construction rules as `bytearray`",
      "2. The resulting bytes object is immutable",
    ],
    orderFr: [
      "1. Memes regles de construction que `bytearray`",
      "2. L'objet bytes resultant est immuable",
    ],
    mistakesEn: [
      "`bytes` vs `bytearray` — immutable vs mutable",
      "`b'...'` literal produces bytes, not str",
    ],
    mistakesFr: [
      "`bytes` vs `bytearray` — immuable vs mutable",
    ],
  },
  "callable": {
    name: "callable",
    type: "function",
    signature: "callable(obj) -> bool",
    descriptionEn: "Returns True if the object appears callable (can be invoked with ()).",
    descriptionFr: "Retourne True si l\'objet semble appelable (peut etre invoque avec ()).",
    returnType: "bool",
    examplesEn: [
      "callable(len)        # True",
      "callable(42)          # False",
      "callable(lambda x: x) # True",
    ],
    examplesFr: [
      "callable(len)        # True",
      "callable(42)          # False",
      "callable(lambda x: x) # True",
    ],
    orderEn: [
      "1. Checks if the object has a `__call__` method",
      "2. Returns True for functions, methods, classes, lambdas, and objects with `__call__`",
    ],
    orderFr: [
      "1. Verifie si l'objet a une methode `__call__`",
      "2. Retourne True pour les fonctions, methodes, classes, lambdas",
    ],
    mistakesEn: [
      "`callable()` can return True but calling may still fail (e.g., `__call__` raises)",
      "Classes are callable — calling a class creates an instance",
    ],
    mistakesFr: [
      "`callable()` peut retourner True meme si l'appel echoue",
    ],
  },
  "chr": {
    name: "chr",
    type: "function",
    signature: "chr(i) -> str",
    descriptionEn: "Returns the Unicode string character for the given integer codepoint. Inverse of `ord()`.",
    descriptionFr: "Retourne le caractere Unicode pour le point de code entier donne. Inverse de `ord()`.",
    returnType: "str",
    examplesEn: [
      "chr(65)             # 'A'",
      "chr(8364)            # '\u20ac' (Euro sign)",
      "chr(128640)          # '\U0001f680' (rocket)",
    ],
    examplesFr: [
      "chr(65)             # 'A'",
      "chr(8364)            # '\u20ac' (Euro sign)",
      "chr(128640)          # '\U0001f680' (rocket)",
    ],
    orderEn: [
      "1. Validates that i is an integer in range 0-0x10FFFF (Unicode maximum)",
      "2. Raises ValueError if out of range",
      "3. Returns the single-character string for that codepoint",
    ],
    orderFr: [
      "1. Valide que i est un entier dans la plage 0-0x10FFFF (maximum Unicode)",
      "2. Leve ValueError si hors plage",
      "3. Retourne la chaine d'un seul caractere",
    ],
    mistakesEn: [
      "`chr(65)` is 'A' not 65 — converts int to character",
      "`chr()` takes an int, `ord()` takes a str — they are inverses",
    ],
    mistakesFr: [
      "`chr(65)` est 'A' pas 65 — convertit entier en caractere",
    ],
  },
  "classmethod": {
    name: "classmethod",
    type: "function",
    signature: "classmethod(function) -> classmethod descriptor",
    descriptionEn: "Transforms a method into a class method. A class method receives the class as the first implicit argument (cls), not the instance.",
    descriptionFr: "Transforme une methode en methode de classe. Une methode de classe recoit la classe comme premier argument implicite (cls).",
    returnType: "classmethod descriptor",
    examplesEn: [
      "class MyClass:\n    @classmethod\n    def create(cls, val):\n        return cls()",
    ],
    examplesFr: [
      "class MyClass:\n    @classmethod\n    def create(cls, val):\n        return cls()",
    ],
    orderEn: [
      "1. `@classmethod` decorator wraps the function in a classmethod descriptor",
      "2. When accessed on an instance or class, it binds the method to the class",
      "3. The class (cls) is automatically passed as the first argument",
    ],
    orderFr: [
      "1. Le decorateur `@classmethod` enveloppe la fonction dans un descripteur",
      "2. Quand il est accede sur une instance ou classe, il lie la methode a la classe",
      "3. La classe (cls) est automatiquement passee comme premier argument",
    ],
    mistakesEn: [
      "Confusing `@classmethod` with `@staticmethod` — classmethod receives `cls`, staticmethod receives nothing",
      "Can be called on both instances and classes",
    ],
    mistakesFr: [
      "Confondre `@classmethod` et `@staticmethod`",
    ],
  },
  "compile": {
    name: "compile",
    type: "function",
    signature: "compile(source, filename, mode) -> code object",
    descriptionEn: "Compiles source code into a code object that can be executed with `exec()` or `eval()`. Mode: \'exec\', \'eval\', or \'single\'.",
    descriptionFr: "Compile du code source en un objet code qui peut etre execute avec `exec()` ou `eval()`.",
    returnType: "code object",
    examplesEn: [
      "code = compile('x = 42', '<string>', 'exec')\nexec(code)",
    ],
    examplesFr: [
      "code = compile('x = 42', '<string>', 'exec')\nexec(code)",
    ],
    orderEn: [
      "1. Parses the source string into an AST",
      "2. Compiles the AST into bytecode",
      "3. Returns a code object ready for execution",
    ],
    orderFr: [
      "1. Analyse la chaine source en AST",
      "2. Compile l'AST en bytecode",
      "3. Retourne un objet code pret pour l'execution",
    ],
    mistakesEn: [
      "`compile()` does NOT execute the code — use `exec()` or `eval()` for that",
      "Filename is used for traceback messages",
    ],
    mistakesFr: [
      "`compile()` n'execute PAS le code",
    ],
  },
  "complex": {
    name: "complex",
    type: "type",
    signature: "complex(real=0, imag=0) -> complex",
    descriptionEn: "Creates a complex number from real and imaginary parts. Can also parse a string representation.",
    descriptionFr: "Cree un nombre complexe a partir de parties reelles et imaginaires.",
    returnType: "complex",
    examplesEn: [
      "complex(3, 4)       # (3+4j)",
      "complex('3+4j')      # (3+4j)",
      "3 + 4j               # complex literal",
    ],
    examplesFr: [
      "complex(3, 4)       # (3+4j)",
      "complex('3+4j')      # (3+4j)",
      "3 + 4j               # complex literal",
    ],
    orderEn: [
      "1. If a string is provided, parse it as a complex number literal",
      "2. Otherwise, creates complex(real, imag)",
      "3. The 'j' suffix denotes the imaginary unit",
    ],
    orderFr: [
      "1. Si une chaine est fournie, l'analyser comme un litteral complexe",
      "2. Sinon, cree complex(reel, imag)",
      "3. Le suffixe 'j' denote l'unite imaginaire",
    ],
    mistakesEn: [
      "Python uses `j` not `i` for the imaginary unit",
      "Use `z.real` and `z.imag` to access parts",
    ],
    mistakesFr: [
      "Python utilise `j` pas `i` pour l'unite imaginaire",
    ],
  },
  "delattr": {
    name: "delattr",
    type: "function",
    signature: "delattr(obj, name) -> None",
    descriptionEn: "Deletes an attribute from an object by name string. Equivalent to `del obj.name`.",
    descriptionFr: "Supprime un attribut d\'un objet par son nom (chaine). Equivalent a `del obj.name`.",
    returnType: "None",
    examplesEn: [
      "delattr(obj, 'x')   # same as del obj.x",
    ],
    examplesFr: [
      "delattr(obj, 'x')   # identique a del obj.x",
    ],
    orderEn: [
      "1. Looks up the attribute name on the object",
      "2. Calls `__delattr__` to remove it",
      "3. Raises AttributeError if the attribute doesn't exist",
    ],
    orderFr: [
      "1. Cherche l'attribut sur l'objet",
      "2. Appelle `__delattr__` pour le supprimer",
      "3. Leve AttributeError si l'attribut n'existe pas",
    ],
    mistakesEn: [
      "Use `delattr(obj, 'name')` when the attribute name is dynamic (a variable)",
      "`del obj.name` is preferred when the name is known statically",
    ],
    mistakesFr: [
      "Utilisez `delattr(obj, 'nom')` quand le nom est dynamique",
    ],
  },
  "dict": {
    name: "dict",
    type: "type",
    signature: "dict(**kwargs) -> dict",
    descriptionEn: "Creates a dictionary (mapping of keys to values). Keys must be hashable.",
    descriptionFr: "Cree un dictionnaire (association de cles a des valeurs). Les cles doivent etre hachables.",
    returnType: "dict",
    examplesEn: [
      "dict(a=1, b=2)      # {'a': 1, 'b': 2}",
      "dict([('x', 1), ('y', 2)])  # {'x': 1, 'y': 2}",
      "{}                    # empty dict literal",
    ],
    examplesFr: [
      "dict(a=1, b=2)      # {'a': 1, 'b': 2}",
      "dict([('x', 1), ('y', 2)])  # {'x': 1, 'y': 2}",
      "{}                    # dict vide",
    ],
    orderEn: [
      "1. From keyword args: maps each key to its value",
      "2. From iterable of pairs: each (key, value) becomes an entry",
      "3. Keys must be hashable (immutable types like str, int, tuple of immutables)",
    ],
    orderFr: [
      "1. Depuis des arguments nommes : associe chaque cle a sa valeur",
      "2. Depuis un iterable de paires : chaque (cle, valeur) devient une entree",
      "3. Les cles doivent etre hachables",
    ],
    mistakesEn: [
      "Keys must be immutable/hashable — lists and dicts cannot be keys",
      "Python 3.7+ preserves insertion order of dictionaries",
    ],
    mistakesFr: [
      "Les cles doivent etre immuables/hachables",
    ],
  },
  "dir": {
    name: "dir",
    type: "function",
    signature: "dir([object]) -> list of str",
    descriptionEn: "Without arguments: returns the names in the current local scope. With an object: returns a sorted list of valid attribute names for that object.",
    descriptionFr: "Sans argument : retourne les noms dans la portee locale actuelle. Avec un objet : retourne la liste triee des noms d\'attributs valides.",
    returnType: "list of str",
    examplesEn: [
      "dir()                # names in current scope",
      "dir([])              # list methods",
      "dir(\"hello\")         # string methods",
    ],
    examplesFr: [
      "dir()                # noms dans la portee actuelle",
      "dir([])              # methodes de liste",
      "dir(\"hello\")         # methodes de chaine",
    ],
    orderEn: [
      "1. Without args: returns sorted list of names in current scope",
      "2. With object: returns sorted list of the object's attribute names",
      "3. Tries to use `__dir__()` method if available",
    ],
    orderFr: [
      "1. Sans argument : retourne la liste triee des noms de la portee actuelle",
      "2. Avec objet : retourne la liste triee des noms d'attributs",
      "3. Essaie d'utiliser `__dir__()` si disponible",
    ],
    mistakesEn: [
      "`dir()` includes inherited attributes and special methods (__xxx__)",
      "For more detail, use `help()` or `vars()`",
    ],
    mistakesFr: [
      "`dir()` inclut les attributs herites et les methodes speciales",
    ],
  },
  "divmod": {
    name: "divmod",
    type: "function",
    signature: "divmod(a, b) -> tuple[int, int]",
    descriptionEn: "Returns a tuple (a // b, a % b). Takes two numbers and returns both the quotient and remainder.",
    descriptionFr: "Retourne un tuple (a // b, a % b). Prend deux nombres et retourne le quotient et le reste.",
    returnType: "tuple of two numbers",
    examplesEn: [
      "divmod(13, 4)       # (3, 1)  -- 13 = 3*4 + 1",
      "divmod(25, 7)        # (3, 4)  -- 25 = 3*7 + 4",
    ],
    examplesFr: [
      "divmod(13, 4)       # (3, 1)  -- 13 = 3*4 + 1",
      "divmod(25, 7)        # (3, 4)  -- 25 = 3*7 + 4",
    ],
    orderEn: [
      "1. Computes floor division: a // b",
      "2. Computes modulo: a % b",
      "3. Returns both as a tuple",
    ],
    orderFr: [
      "1. Calcule la division entiere : a // b",
      "2. Calcule le modulo : a % b",
      "3. Retourne les deux sous forme de tuple",
    ],
    mistakesEn: [
      "For negative numbers, Python's `//` floors toward negative infinity",
      "`divmod(a, b)[0] * b + divmod(a, b)[1] == a` always holds",
    ],
    mistakesFr: [
      "Pour les nombres negatifs, `//` arrondit vers -infini",
    ],
  },
  "enumerate": {
    name: "enumerate",
    type: "function",
    signature: "enumerate(iterable, start=0) -> iterator of (index, value)",
    descriptionEn: "Returns an iterator yielding pairs of (index, value) from an iterable. Useful for getting both the index and element in a loop.",
    descriptionFr: "Retourne un iterateur produisant des paires (index, valeur) depuis un iterable. Utile pour obtenir index et element dans une boucle.",
    returnType: "iterator of (int, T) tuples",
    examplesEn: [
      "list(enumerate(['a', 'b', 'c']))  # [(0, 'a'), (1, 'b'), (2, 'c')]",
      "list(enumerate(['a', 'b'], start=1))  # [(1, 'a'), (2, 'b')]",
    ],
    examplesFr: [
      "list(enumerate(['a', 'b', 'c']))  # [(0, 'a'), (1, 'b'), (2, 'c')]",
      "list(enumerate(['a', 'b'], start=1))  # [(1, 'a'), (2, 'b')]",
    ],
    orderEn: [
      "1. Creates an iterator from the iterable",
      "2. On each iteration: yields (current_index, next_value)",
      "3. Increments the counter by start (default 0)",
    ],
    orderFr: [
      "1. Cree un iterateur depuis l'iterable",
      "2. A chaque iteration : produit (index_courant, valeur_suivante)",
      "3. Incremente le compteur par start (defaut 0)",
    ],
    mistakesEn: [
      "`enumerate()` returns an iterator, not a list — use `list(enumerate(...))` to materialize",
      "Common pattern: `for i, val in enumerate(items):`",
    ],
    mistakesFr: [
      "`enumerate()` retourne un iterateur, pas une liste",
    ],
  },
  "eval": {
    name: "eval",
    type: "function",
    signature: "eval(expression, globals=None, locals=None) -> object",
    descriptionEn: "Parses and evaluates a single Python expression from a string and returns the result.",
    descriptionFr: "Analyse et evalue une seule expression Python depuis une chaine et retourne le resultat.",
    returnType: "result of the expression",
    examplesEn: [
      "eval('2 + 3 * 4')   # 14",
      "eval('pow(2, 10)')   # 1024",
      "x = 42\neval('x + 1')   # 43",
    ],
    examplesFr: [
      "eval('2 + 3 * 4')   # 14",
      "eval('pow(2, 10)')   # 1024",
      "x = 42\neval('x + 1')   # 43",
    ],
    orderEn: [
      "1. Parses the string as a Python expression",
      "2. Compiles it to bytecode",
      "3. Executes in the given namespace (or current scope)",
      "4. Returns the result value",
    ],
    orderFr: [
      "1. Analyse la chaine comme une expression Python",
      "2. La compile en bytecode",
      "3. Execute dans l'espace de noms donne",
      "4. Retourne la valeur resultat",
    ],
    mistakesEn: [
      "`eval()` only evaluates expressions (not statements like `if`, `for`, `def`)",
      "NEVER use `eval()` on untrusted input — it can execute arbitrary code",
    ],
    mistakesFr: [
      "`eval()` evalue seulement les expressions (pas les instructions)",
    ],
  },
  "exec": {
    name: "exec",
    type: "function",
    signature: "exec(source, globals=None, locals=None) -> None",
    descriptionEn: "Executes Python code (statements or expressions) from a string or code object. Unlike `eval()`, can execute arbitrary statements.",
    descriptionFr: "Execute du code Python (instructions ou expressions) depuis une chaine ou un objet code.",
    returnType: "None",
    examplesEn: [
      "exec('x = 42')      # sets x = 42 in current scope",
      "exec('def f(): return 1')  # defines f",
    ],
    examplesFr: [
      "exec('x = 42')      # definit x = 42 dans la portee courante",
      "exec('def f(): return 1')  # definit f",
    ],
    orderEn: [
      "1. Parses the source as Python code (statements allowed)",
      "2. Compiles and executes it",
      "3. Modifications to the namespace persist",
    ],
    orderFr: [
      "1. Analyse la source comme du code Python (instructions autorisees)",
      "2. Compile et execute",
      "3. Les modifications de l'espace de noms persistent",
    ],
    mistakesEn: [
      "`exec()` can execute statements, `eval()` only expressions",
      "NEVER use `exec()` on untrusted input",
    ],
    mistakesFr: [
      "`exec()` peut executer des instructions, `eval()` seulement des expressions",
    ],
  },
  "filter": {
    name: "filter",
    type: "function",
    signature: "filter(function, iterable) -> iterator",
    descriptionEn: "Constructs an iterator that yields elements of iterable for which function returns True. If function is None, yields truthy elements.",
    descriptionFr: "Construit un iterateur qui produit les elements de iterable pour lesquels la fonction retourne True.",
    returnType: "iterator",
    examplesEn: [
      "list(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # [1, 2]",
      "list(filter(None, [0, 1, '', 'hello']))  # [1, 'hello']",
    ],
    examplesFr: [
      "list(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # [1, 2]",
      "list(filter(None, [0, 1, '', 'hello']))  # [1, 'hello']",
    ],
    orderEn: [
      "1. Takes each element from the iterable",
      "2. Calls function(element) — if function is None, uses the element's truthiness",
      "3. If the result is truthy, yields the element",
      "4. Returns a lazy iterator",
    ],
    orderFr: [
      "1. Prend chaque element de l'iterable",
      "2. Appelle fonction(element) — si None, utilise la veracite de l'element",
      "3. Si le resultat est vrai, produit l'element",
      "4. Retourne un iterateur paresseux",
    ],
    mistakesEn: [
      "`filter()` returns an iterator in Python 3 (not a list like Python 2)",
      "Comprehensions are often more readable: `[x for x in items if x > 0]`",
    ],
    mistakesFr: [
      "`filter()` retourne un iterateur en Python 3",
    ],
  },
  "float": {
    name: "float",
    type: "type",
    signature: "float(x=0.0) -> float",
    descriptionEn: "Converts a number or string to a floating-point number (double precision).",
    descriptionFr: "Convertit un nombre ou une chaine en nombre a virgule flottante (double precision).",
    returnType: "float",
    examplesEn: [
      "float(42)           # 42.0",
      "float('3.14')        # 3.14",
      "float('inf')         # inf",
      "float('nan')         # nan",
    ],
    examplesFr: [
      "float(42)           # 42.0",
      "float('3.14')        # 3.14",
      "float('inf')         # inf",
      "float('nan')         # nan",
    ],
    orderEn: [
      "1. If x is a string, parse it as a floating-point literal",
      "2. If x is a number, convert it to float",
      "3. Special strings: 'inf', '-inf', 'nan'",
    ],
    orderFr: [
      "1. Si x est une chaine, l'analyser comme un litteral flottant",
      "2. Si x est un nombre, le convertir en float",
      "3. Chaines speciales : 'inf', '-inf', 'nan'",
    ],
    mistakesEn: [
      "Floating-point precision issues: `0.1 + 0.2 != 0.3`",
      "Use `math.isclose()` for float comparison",
    ],
    mistakesFr: [
      "Problemes de precision : `0.1 + 0.2 != 0.3`",
    ],
  },
  "format": {
    name: "format",
    type: "function",
    signature: "format(value, format_spec='') -> str",
    descriptionEn: "Converts a value to a formatted string using the format specification mini-language.",
    descriptionFr: "Convertit une valeur en chaine formatee utilisant le mini-langage de specification de format.",
    returnType: "str",
    examplesEn: [
      "format(42, 'b')     # '101010' (binary)",
      "format(255, 'x')     # 'ff' (hex)",
      "format(3.14159, '.2f')  # '3.14'",
    ],
    examplesFr: [
      "format(42, 'b')     # '101010' (binaire)",
      "format(255, 'x')     # 'ff' (hex)",
      "format(3.14159, '.2f')  # '3.14'",
    ],
    orderEn: [
      "1. Calls `value.__format__(format_spec)`",
      "2. The format spec determines alignment, padding, precision, type representation",
      "3. Returns the formatted string",
    ],
    orderFr: [
      "1. Appelle `value.__format__(format_spec)`",
      "2. Le spec de format determine alignement, remplissage, precision",
      "3. Retourne la chaine formatee",
    ],
    mistakesEn: [
      "`format()` is the underlying function for f-strings: `f'{value:spec}'`",
      "Each type has its own format spec (int: b, x, o; float: .precisionf)",
    ],
    mistakesFr: [
      "`format()` est la fonction sous-jacente des f-strings",
    ],
  },
  "frozenset": {
    name: "frozenset",
    type: "type",
    signature: "frozenset(iterable=set()) -> frozenset",
    descriptionEn: "Returns an immutable (unchangeable) set. Can be used as a dictionary key or set element.",
    descriptionFr: "Retourne un ensemble immuable (non modifiable). Peut etre utilise comme cle de dictionnaire ou element d\'ensemble.",
    returnType: "frozenset",
    examplesEn: [
      "frozenset([1, 2, 2, 3])  # frozenset({1, 2, 3})",
      "frozenset()          # empty frozenset",
    ],
    examplesFr: [
      "frozenset([1, 2, 2, 3])  # frozenset({1, 2, 3})",
      "frozenset()          # frozenset vide",
    ],
    orderEn: [
      "1. Creates a set from the iterable (duplicates removed)",
      "2. Wraps it in an immutable container",
    ],
    orderFr: [
      "1. Cree un ensemble depuis l'iterable (doublons supprimes)",
      "2. L'enveloppe dans un conteneur immuable",
    ],
    mistakesEn: [
      "`frozenset` is hashable (can be a dict key); `set` is not",
      "`frozenset()` is the only built-in mutable→immutable converter",
    ],
    mistakesFr: [
      "`frozenset` est hachable (peut etre une cle de dict)",
    ],
  },
  "getattr": {
    name: "getattr",
    type: "function",
    signature: "getattr(object, name[, default]) -> value",
    descriptionEn: "Returns the value of the named attribute of an object. If not found, returns default if provided, otherwise raises AttributeError.",
    descriptionFr: "Retourne la valeur de l\'attribut nomme d\'un objet. Si absent, retourne default ou leve AttributeError.",
    returnType: "any",
    examplesEn: [
      "getattr(obj, 'x')         # obj.x",
      "getattr(obj, 'y', 42)      # 42 if no y attribute",
    ],
    examplesFr: [
      "getattr(obj, 'x')         # obj.x",
      "getattr(obj, 'y', 42)      # 42 si pas d'attribut y",
    ],
    orderEn: [
      "1. Looks up the attribute name on the object using `__getattribute__`",
      "2. If not found and default is given, returns default",
      "3. If not found and no default, raises AttributeError",
    ],
    orderFr: [
      "1. Cherche l'attribut sur l'objet via `__getattribute__`",
      "2. Si absent et default fourni, retourne default",
      "3. Si absent et pas de default, leve AttributeError",
    ],
    mistakesEn: [
      "Use `getattr(obj, 'attr')` when the attribute name is dynamic",
      "`getattr(obj, 'attr', default)` is cleaner than try/except AttributeError",
    ],
    mistakesFr: [
      "Utilisez `getattr(obj, 'attr')` quand le nom est dynamique",
    ],
  },
  "globals": {
    name: "globals",
    type: "function",
    signature: "globals() -> dict",
    descriptionEn: "Returns the dictionary implementing the current module\'s global namespace.",
    descriptionFr: "Retourne le dictionnaire implementant l\'espace de noms global du module courant.",
    returnType: "dict",
    examplesEn: [
      "globals()           # {'__name__': '__main__', ...}",
    ],
    examplesFr: [
      "globals()           # {'__name__': '__main__', ...}",
    ],
    orderEn: [
      "1. Returns a reference to the global namespace dict",
      "2. Modifications to this dict affect the global scope",
    ],
    orderFr: [
      "1. Retourne une reference au dict de l'espace de noms global",
      "2. Les modifications affectent la portee globale",
    ],
    mistakesEn: [
      "Modifying `globals()` adds/removes global variables — use with caution",
      "`globals()` returns the actual dict, not a copy",
    ],
    mistakesFr: [
      "Modifier `globals()` ajoute/supprime des variables globales",
    ],
  },
  "hasattr": {
    name: "hasattr",
    type: "function",
    signature: "hasattr(object, name) -> bool",
    descriptionEn: "Returns True if the object has an attribute with the given name.",
    descriptionFr: "Retourne True si l\'objet a un attribut avec le nom donne.",
    returnType: "bool",
    examplesEn: [
      "hasattr(obj, 'x')  # True if obj has x attribute",
      "hasattr([], 'sort') # True (list has sort method)",
    ],
    examplesFr: [
      "hasattr(obj, 'x')  # True si obj a l'attribut x",
      "hasattr([], 'sort') # True (list a la methode sort)",
    ],
    orderEn: [
      "1. Calls `getattr(object, name)` behind the scenes",
      "2. Returns True if no AttributeError is raised",
      "3. Returns False if AttributeError is raised",
    ],
    orderFr: [
      "1. Appelle `getattr(object, name)` en coulisses",
      "2. Retourne True si aucune AttributeError n'est levee",
      "3. Retourne False si AttributeError est levee",
    ],
    mistakesEn: [
      "`hasattr()` catches ALL AttributeErrors including those raised inside properties",
      "Prefer EAFP (try/except) over LBYL (hasattr) in some cases",
    ],
    mistakesFr: [
      "`hasattr()` attrape TOUTES les AttributeError",
    ],
  },
  "hash": {
    name: "hash",
    type: "function",
    signature: "hash(object) -> int",
    descriptionEn: "Returns the hash value of an object (an integer). Hashable objects can be used as dictionary keys and set members.",
    descriptionFr: "Retourne la valeur de hachage d\'un objet (un entier). Les objets hachables peuvent etre des cles de dictionnaire.",
    returnType: "int",
    examplesEn: [
      "hash(42)            # 42",
      "hash('hello')        # some integer",
      "hash((1, 2, 3))      # hash depends on contents",
    ],
    examplesFr: [
      "hash(42)            # 42",
      "hash('hello')        # un entier",
      "hash((1, 2, 3))      # le hachage depend du contenu",
    ],
    orderEn: [
      "1. Calls `object.__hash__()`",
      "2. Returns an integer",
      "3. Equal objects must have equal hashes (but the converse is not required)",
    ],
    orderFr: [
      "1. Appelle `object.__hash__()`",
      "2. Retourne un entier",
      "3. Les objets egaux doivent avoir des hash egaux",
    ],
    mistakesEn: [
      "Lists and dicts are unhashable (mutable)",
      "Hash collisions are possible — `__eq__` and `__hash__` must be consistent",
    ],
    mistakesFr: [
      "Les listes et dicts ne sont pas hachables",
    ],
  },
  "help": {
    name: "help",
    type: "function",
    signature: "help([object]) -> None",
    descriptionEn: "Invokes the built-in help system. Without arguments, starts interactive help. With an object, shows documentation.",
    descriptionFr: "Invoque le systeme d\'aide integre. Sans argument, demarre l\'aide interactive. Avec un objet, affiche la documentation.",
    returnType: "None",
    examplesEn: [
      "help(len)           # shows documentation for len",
      "help(str)           # shows string documentation",
    ],
    examplesFr: [
      "help(len)           # affiche la documentation de len",
      "help(str)           # affiche la documentation de str",
    ],
    orderEn: [
      "1. Without args: enters interactive help viewer",
      "2. With object: formats and displays the object's `__doc__` and other metadata",
      "3. Pages through a pager for long output",
    ],
    orderFr: [
      "1. Sans argument : entre dans le visualiseur d'aide interactif",
      "2. Avec objet : formate et affiche la documentation",
    ],
    mistakesEn: [
      "`help()` uses the pydoc module to format output",
      "For a plain string docstring, use `object.__doc__`",
    ],
    mistakesFr: [
      "Pour une docstring brute, utilisez `object.__doc__`",
    ],
  },
  "hex": {
    name: "hex",
    type: "function",
    signature: "hex(x) -> str",
    descriptionEn: "Converts an integer to a hexadecimal string prefixed with \'0x\'.",
    descriptionFr: "Convertit un entier en chaine hexadecimale prefixee de \'0x\'.",
    returnType: "str",
    examplesEn: [
      "hex(255)           # '0xff'",
      "hex(42)             # '0x2a'",
      "hex(0)              # '0x0'",
    ],
    examplesFr: [
      "hex(255)           # '0xff'",
      "hex(42)             # '0x2a'",
      "hex(0)              # '0x0'",
    ],
    orderEn: [
      "1. Converts the integer to base-16",
      "2. Prepends '0x' to indicate hexadecimal format",
    ],
    orderFr: [
      "1. Convertit l'entier en base 16",
      "2. Ajoute '0x' pour indiquer le format hexadecimal",
    ],
    mistakesEn: [
      "`hex()` only works on integers",
      "Use `format(x, '04x')` for zero-padded hex without '0x' prefix",
    ],
    mistakesFr: [
      "Utilisez `format(x, '04x')` pour du hex avec remplissage",
    ],
  },
  "id": {
    name: "id",
    type: "function",
    signature: "id(object) -> int",
    descriptionEn: "Returns the memory address (identity) of an object as an integer. The identity is unique and constant for the object\'s lifetime.",
    descriptionFr: "Retourne l\'adresse memoire (identite) d\'un objet sous forme d\'entier. L\'identite est unique et constante.",
    returnType: "int",
    examplesEn: [
      "id(42)             # 4345956784 (varies)",
      "x = [1, 2]; id(x)   # same before and after modification",
    ],
    examplesFr: [
      "id(42)             # 4345956784 (varie)",
      "x = [1, 2]; id(x)   # identique avant et apres modification",
    ],
    orderEn: [
      "1. Returns the CPython memory address of the object",
      "2. Use `is` operator to check identity, not `id()` directly",
    ],
    orderFr: [
      "1. Retourne l'adresse memoire CPython de l'objet",
      "2. Utilisez `is` pour verifier l'identite",
    ],
    mistakesEn: [
      "`a is b` is equivalent to `id(a) == id(b)`",
      "Small integers (-5 to 256) are cached and may share ids",
      "After an object is garbage collected, its id can be reused",
    ],
    mistakesFr: [
      "Les petits entiers (-5 a 256) sont mis en cache",
    ],
  },
  "input": {
    name: "input",
    type: "function",
    signature: "input([prompt]) -> str",
    descriptionEn: "Reads a line from standard input, strips the trailing newline, and returns it. The prompt string is printed to stdout first if given.",
    descriptionFr: "Lit une ligne depuis l\'entree standard, supprime le saut de ligne final et la retourne.",
    returnType: "str",
    examplesEn: [
      "name = input('Enter name: ')  # waits for user input",
    ],
    examplesFr: [
      "name = input('Enter name: ')  # attend la saisie utilisateur",
    ],
    orderEn: [
      "1. If prompt is provided, prints it to stdout without newline",
      "2. Reads a line from stdin",
      "3. Strips the trailing newline character",
      "4. Returns the string",
    ],
    orderFr: [
      "1. Si prompt est fourni, l'affiche sans saut de ligne",
      "2. Lit une ligne depuis stdin",
      "3. Supprime le caractere de nouvelle ligne",
      "4. Retourne la chaine",
    ],
    mistakesEn: [
      "`input()` always returns a string — convert with `int()` or `float()` if needed",
      "In Python 2, `input()` evaluated the input as Python code — in Python 3+ it's safe",
    ],
    mistakesFr: [
      "`input()` retourne toujours une chaine",
    ],
  },
  "int": {
    name: "int",
    type: "type",
    signature: "int(x=0, base=10) -> int",
    descriptionEn: "Converts a number or string to an integer. The base parameter specifies the number base (2-36) for string conversion.",
    descriptionFr: "Convertit un nombre ou une chaine en entier. Le parametre base specifie la base numerique (2-36).",
    returnType: "int",
    examplesEn: [
      "int(3.14)          # 3 (truncates toward zero)",
      "int('42')           # 42",
      "int('1010', 2)      # 10 (binary)",
      "int('ff', 16)       # 255 (hex)",
    ],
    examplesFr: [
      "int(3.14)          # 3 (tronque vers zero)",
      "int('42')           # 42",
      "int('1010', 2)      # 10 (binaire)",
      "int('ff', 16)       # 255 (hex)",
    ],
    orderEn: [
      "1. If x is a string, parse using the given base (default 10)",
      "2. If x is a float, truncate toward zero",
      "3. If x is another int, return it unchanged",
    ],
    orderFr: [
      "1. Si x est une chaine, l'analyser avec la base donnee",
      "2. Si x est un float, tronquer vers zero",
      "3. Si x est un autre int, le retourner inchang",
    ],
    mistakesEn: [
      "`int()` truncates toward zero (not floor) — `int(-3.9)` is -3, not -4",
      "String `int('42')` vs float `int(42.0)` behave differently",
    ],
    mistakesFr: [
      "`int()` tronque vers zero (pas plancher)",
    ],
  },
  "isinstance": {
    name: "isinstance",
    type: "function",
    signature: "isinstance(obj, classinfo) -> bool",
    descriptionEn: "Returns True if obj is an instance of classinfo (or any subclass). classinfo can be a type or a tuple of types.",
    descriptionFr: "Retourne True si obj est une instance de classinfo (ou d\'une sous-classe). classinfo peut etre un type ou un tuple de types.",
    returnType: "bool",
    examplesEn: [
      "isinstance(42, int)        # True",
      "isinstance('hello', str)   # True",
      "isinstance([1,2], (list, tuple))  # True",
      "isinstance(True, int)       # True (bool is subclass of int)",
    ],
    examplesFr: [
      "isinstance(42, int)        # True",
      "isinstance('hello', str)   # True",
      "isinstance([1,2], (list, tuple))  # True",
      "isinstance(True, int)       # True (bool est sous-classe de int)",
    ],
    orderEn: [
      "1. Checks if type(obj) is classinfo or any subclass of classinfo",
      "2. If classinfo is a tuple, checks against each element (OR logic)",
      "3. Returns True on first match, False if none match",
    ],
    orderFr: [
      "1. Verifie si type(obj) est classinfo ou une sous-classe",
      "2. Si classinfo est un tuple, verifie chaque element (OU logique)",
      "3. Retourne True au premier match, False sinon",
    ],
    mistakesEn: [
      "`isinstance()` considers inheritance, `type(obj) == T` does not",
      "`isinstance(True, int)` is True because bool is a subclass of int",
    ],
    mistakesFr: [
      "`isinstance()` considere l'heritage, pas `type(obj) == T`",
    ],
  },
  "issubclass": {
    name: "issubclass",
    type: "function",
    signature: "issubclass(cls, classinfo) -> bool",
    descriptionEn: "Returns True if cls is a subclass of classinfo. classinfo can be a type or a tuple of types.",
    descriptionFr: "Retourne True si cls est une sous-classe de classinfo. classinfo peut etre un type ou un tuple de types.",
    returnType: "bool",
    examplesEn: [
      "issubclass(bool, int)  # True",
      "issubclass(bool, (int, str))  # True",
      "issubclass(int, bool)  # False",
    ],
    examplesFr: [
      "issubclass(bool, int)  # True",
      "issubclass(bool, (int, str))  # True",
      "issubclass(int, bool)  # False",
    ],
    orderEn: [
      "1. Checks if cls inherits from classinfo",
      "2. A class is considered a subclass of itself",
      "3. If classinfo is a tuple, checks against each element",
    ],
    orderFr: [
      "1. Verifie si cls herite de classinfo",
      "2. Une classe est consideree comme sous-classe d'elle-meme",
      "3. Si classinfo est un tuple, verifie chaque element",
    ],
    mistakesEn: [
      "`issubclass(bool, int)` is True but `issubclass(int, bool)` is False",
      "`issubclass(A, A)` is always True (a class is a subclass of itself)",
    ],
    mistakesFr: [
      "`issubclass(A, A)` est toujours True",
    ],
  },
  "iter": {
    name: "iter",
    type: "function",
    signature: "iter(object[, sentinel]) -> iterator",
    descriptionEn: "Returns an iterator object. With one arg: creates an iterator from an iterable. With two args: calls callable until it returns sentinel.",
    descriptionFr: "Retourne un objet iterateur. Avec un argument : cree un iterateur depuis un iterable. Avec deux : appelle callable jusqu\'a sentinel.",
    returnType: "iterator",
    examplesEn: [
      "iter([1, 2, 3])    # list_iterator",
      "iter('hello')       # str_iterator",
    ],
    examplesFr: [
      "iter([1, 2, 3])    # list_iterator",
      "iter('hello')       # str_iterator",
    ],
    orderEn: [
      "1. Single arg: calls `object.__iter__()` to get an iterator",
      "2. Two args: repeatedly calls callable, yields results until sentinel is returned",
    ],
    orderFr: [
      "1. Un argument : appelle `object.__iter__()`",
      "2. Deux arguments : appelle callable jusqu'a sentinel",
    ],
    mistakesEn: [
      "`next(iterator)` manually advances the iterator",
      "Not all iterables are iterators (iterators are exhausted after one pass)",
    ],
    mistakesFr: [
      "`next(iterator)` avance manuellement l'iterateur",
    ],
  },
  "len": {
    name: "len",
    type: "function",
    signature: "len(obj) -> int",
    descriptionEn: "Returns the length (number of items) of a container. Works with sequences, mappings, and sets.",
    descriptionFr: "Retourne la longueur (nombre d\'elements) d\'un conteneur. Fonctionne avec les sequences, mappings et ensembles.",
    returnType: "int",
    examplesEn: [
      "len([1, 2, 3])     # 3",
      "len('hello')        # 5",
      "len({'a': 1, 'b': 2})  # 2",
    ],
    examplesFr: [
      "len([1, 2, 3])     # 3",
      "len('hello')        # 5",
      "len({'a': 1, 'b': 2})  # 2",
    ],
    orderEn: [
      "1. Calls `obj.__len__()`",
      "2. Returns the result as an integer",
    ],
    orderFr: [
      "1. Appelle `obj.__len__()`",
      "2. Retourne le resultat sous forme d'entier",
    ],
    mistakesEn: [
      "`len()` only works on objects that define `__len__`",
      "For iterators, count with `sum(1 for _ in iterator)`",
    ],
    mistakesFr: [
      "`len()` ne fonctionne que sur les objets qui definissent `__len__`",
    ],
  },
  "list": {
    name: "list",
    type: "type",
    signature: "list(iterable=()) -> list",
    descriptionEn: "Creates a list from an iterable. Lists are mutable, ordered sequences that can hold items of any type.",
    descriptionFr: "Cree une liste a partir d\'un iterable. Les listes sont des sequences mutables et ordonnees.",
    returnType: "list",
    examplesEn: [
      "list('hello')      # ['h', 'e', 'l', 'l', 'o']",
      "list(range(5))      # [0, 1, 2, 3, 4]",
      "[1, 2, 3]           # list literal",
    ],
    examplesFr: [
      "list('hello')      # ['h', 'e', 'l', 'l', 'o']",
      "list(range(5))      # [0, 1, 2, 3, 4]",
      "[1, 2, 3]           # liste litterale",
    ],
    orderEn: [
      "1. Iterates over the iterable",
      "2. Collects all items into a new list",
      "3. Returns the list",
    ],
    orderFr: [
      "1. Parcourt l'iterable",
      "2. Collecte tous les elements dans une nouvelle liste",
      "3. Retourne la liste",
    ],
    mistakesEn: [
      "`list()` creates a shallow copy — nested objects are shared",
      "Empty list literal `[]` is faster than `list()`",
    ],
    mistakesFr: [
      "`list()` cree une copie superficielle",
    ],
  },
  "locals": {
    name: "locals",
    type: "function",
    signature: "locals() -> dict",
    descriptionEn: "Returns a dictionary of the current local symbol table (variables in the current scope).",
    descriptionFr: "Retourne un dictionnaire de la table des symboles locaux actuels (variables dans la portee courante).",
    returnType: "dict",
    examplesEn: [
      "def f():\n    x = 42\n    print(locals())  # {'x': 42}",
    ],
    examplesFr: [
      "def f():\n    x = 42\n    print(locals())  # {'x': 42}",
    ],
    orderEn: [
      "1. Returns a dictionary of local variable names to values",
      "2. At module level, `locals()` returns the same as `globals()`",
    ],
    orderFr: [
      "1. Retourne un dictionnaire des noms de variables locales vers leurs valeurs",
      "2. Au niveau module, `locals()` retourne la meme chose que `globals()`",
    ],
    mistakesEn: [
      "Modifications to the `locals()` dict do NOT always affect local variables",
      "In a function, `locals()` returns a copy, not the actual namespace",
    ],
    mistakesFr: [
      "Les modifications du dict `locals()` n'affectent pas toujours les variables",
    ],
  },
  "map": {
    name: "map",
    type: "function",
    signature: "map(function, *iterables) -> iterator",
    descriptionEn: "Applies function to each item of the iterable(s) and yields the results. If multiple iterables, function must take that many arguments.",
    descriptionFr: "Applique fonction a chaque element de l\'iterable et produit les resultats. Si plusieurs iterables, la fonction doit prendre autant d\'arguments.",
    returnType: "iterator",
    examplesEn: [
      "list(map(str.upper, ['a', 'b']))  # ['A', 'B']",
      "list(map(lambda x, y: x + y, [1, 2], [3, 4]))  # [4, 6]",
    ],
    examplesFr: [
      "list(map(str.upper, ['a', 'b']))  # ['A', 'B']",
      "list(map(lambda x, y: x + y, [1, 2], [3, 4]))  # [4, 6]",
    ],
    orderEn: [
      "1. Function is called FIRST (applied)",
      "2. Iterable is consumed SECOND (as data)",
      "3. For each item in iterable, calls function(item)",
      "4. Yields results lazily (one at a time)",
      "5. Stops when the shortest iterable is exhausted",
    ],
    orderFr: [
      "1. La fonction est appelee en PREMIER (appliquee)",
      "2. L'iterable est consomme en SECOND (donnees)",
      "3. Pour chaque element, appelle fonction(element)",
      "4. Produit les resultats paresseusement",
      "5. S'arrete quand l'iterable le plus court est epuise",
    ],
    mistakesEn: [
      "`map()` returns an iterator in Python 3 (not a list like Python 2)",
      "Wrap with `list()` to materialize results",
      "Comprehensions are often more readable: `[str.upper(x) for x in items]`",
    ],
    mistakesFr: [
      "`map()` retourne un iterateur en Python 3",
    ],
  },
  "max": {
    name: "max",
    type: "function",
    signature: "max(iterable, *[, key, default]) -> value",
    descriptionEn: "Returns the largest item in an iterable or the largest of two or more arguments.",
    descriptionFr: "Retourne le plus grand element d\'un iterable ou le plus grand de deux ou plusieurs arguments.",
    returnType: "any",
    examplesEn: [
      "max([3, 1, 4, 1, 5])  # 5",
      "max('a', 'b', 'c')   # 'c'",
      "max([], default=0)   # 0 (empty with default)",
    ],
    examplesFr: [
      "max([3, 1, 4, 1, 5])  # 5",
      "max('a', 'b', 'c')   # 'c'",
      "max([], default=0)   # 0 (vide avec default)",
    ],
    orderEn: [
      "1. If single iterable: iterates over items and finds the maximum",
      "2. If multiple args: compares them directly",
      "3. Uses `>` comparisons (objects must support them)",
      "4. If iterable is empty and default is given, returns default",
    ],
    orderFr: [
      "1. Si un seul iterable : parcourt et trouve le maximum",
      "2. Si plusieurs arguments : les compare directement",
      "3. Utilise les comparaisons `>`",
      "4. Si iterable vide et default donne, retourne default",
    ],
    mistakesEn: [
      "`max()` raises ValueError on empty iterable without default",
      "Use `key=str.lower` for case-insensitive comparison",
    ],
    mistakesFr: [
      "`max()` leve ValueError si iterable vide sans default",
    ],
  },
  "memoryview": {
    name: "memoryview",
    type: "function",
    signature: "memoryview(obj) -> memoryview",
    descriptionEn: "Returns a memory view object that exposes an object\'s internal buffer (allows direct memory access without copying).",
    descriptionFr: "Retourne un objet de vue memoire qui expose le tampon interne d\'un objet (acces memoire direct sans copie).",
    returnType: "memoryview",
    examplesEn: [
      "mv = memoryview(b'hello')\nmv[0]  # 104 (b'h' as int)",
    ],
    examplesFr: [
      "mv = memoryview(b'hello')\nmv[0]  # 104 (b'h' comme int)",
    ],
    orderEn: [
      "1. Takes a buffer-supporting object (bytes, bytearray, array.array)",
      "2. Exposes the buffer without copying the underlying data",
      "3. Supports slicing and indexing",
    ],
    orderFr: [
      "1. Prend un objet supportant le tampon",
      "2. Expose le tampon sans copier les donnees sous-jacentes",
      "3. Supporte le decoupage et l'indexation",
    ],
    mistakesEn: [
      "`memoryview` avoids copying large binary data",
      "Use `.tobytes()` or `.tolist()` to convert the view",
    ],
    mistakesFr: [
      "`memoryview` evite de copier de grandes donnees binaires",
    ],
  },
  "min": {
    name: "min",
    type: "function",
    signature: "min(iterable, *[, key, default]) -> value",
    descriptionEn: "Returns the smallest item in an iterable or the smallest of two or more arguments.",
    descriptionFr: "Retourne le plus petit element d\'un iterable ou le plus petit de deux ou plusieurs arguments.",
    returnType: "any",
    examplesEn: [
      "min([3, 1, 4, 1, 5])  # 1",
      "min('a', 'b', 'c')   # 'a'",
      "min([], default=0)   # 0 (empty with default)",
    ],
    examplesFr: [
      "min([3, 1, 4, 1, 5])  # 1",
      "min('a', 'b', 'c')   # 'a'",
      "min([], default=0)   # 0 (vide avec default)",
    ],
    orderEn: [
      "1. If single iterable: iterates and finds the minimum",
      "2. If multiple args: compares them",
      "3. Uses `<` comparisons",
      "4. If iterable is empty and default given, returns default",
    ],
    orderFr: [
      "1. Si un seul iterable : parcourt et trouve le minimum",
      "2. Si plusieurs arguments : les compare",
      "3. Utilise les comparaisons `<`",
      "4. Si iterable vide et default donne, retourne default",
    ],
    mistakesEn: [
      "`min()` raises ValueError on empty iterable without default",
      "Same behavior as `max()` but reversed",
    ],
    mistakesFr: [
      "`min()` leve ValueError si iterable vide sans default",
    ],
  },
  "next": {
    name: "next",
    type: "function",
    signature: "next(iterator[, default]) -> value",
    descriptionEn: "Returns the next item from an iterator. If the iterator is exhausted and default is given, returns default — otherwise raises StopIteration.",
    descriptionFr: "Retourne l\'element suivant d\'un iterateur. Si epuise et default donne, retourne default — sinon leve StopIteration.",
    returnType: "any",
    examplesEn: [
      "it = iter([1, 2, 3])\nnext(it)  # 1\nnext(it)  # 2\nnext(it)  # 3\nnext(it, 'done')  # 'done'",
    ],
    examplesFr: [
      "it = iter([1, 2, 3])\nnext(it)  # 1\nnext(it)  # 2\nnext(it)  # 3\nnext(it, 'done')  # 'done'",
    ],
    orderEn: [
      "1. Calls `iterator.__next__()`",
      "2. If there is a next item, returns it",
      "3. If exhausted and default given, returns default",
      "4. If exhausted and no default, raises StopIteration",
    ],
    orderFr: [
      "1. Appelle `iterator.__next__()`",
      "2. S'il y a un element suivant, le retourne",
      "3. Si epuise et default donne, retourne default",
      "4. Si epuise et pas de default, leve StopIteration",
    ],
    mistakesEn: [
      "`for` loops implicitly call `next()` and catch StopIteration",
      "Use `next(iterator, default)` instead of try/except StopIteration",
    ],
    mistakesFr: [
      "Les boucles `for` appellent implicitement `next()`",
    ],
  },
  "object": {
    name: "object",
    type: "type",
    signature: "object() -> object",
    descriptionEn: "Returns a new featureless object. `object` is the base class for all classes in Python.",
    descriptionFr: "Retourne un nouvel objet sans caracteristiques. `object` est la classe de base de toutes les classes en Python.",
    returnType: "object",
    examplesEn: [
      "obj = object()     # creates a base object",
      "isinstance(obj, object)  # True for everything",
    ],
    examplesFr: [
      "obj = object()     # cree un objet de base",
      "isinstance(obj, object)  # True pour tout",
    ],
    orderEn: [
      "1. Allocates a new base object",
      "2. All classes inherit from `object` implicitly",
    ],
    orderFr: [
      "1. Alloue un nouvel objet de base",
      "2. Toutes les classes heritent de `object` implicitement",
    ],
    mistakesEn: [
      "`object()` instances are featureless — no attributes by default",
      "All Python classes are subclasses of `object`",
    ],
    mistakesFr: [
      "Les instances de `object()` sont sans caracteristiques",
    ],
  },
  "oct": {
    name: "oct",
    type: "function",
    signature: "oct(x) -> str",
    descriptionEn: "Converts an integer to an octal string prefixed with \'0o\'.",
    descriptionFr: "Convertit un entier en chaine octale prefixee de \'0o\'.",
    returnType: "str",
    examplesEn: [
      "oct(8)             # '0o10'",
      "oct(255)            # '0o377'",
      "oct(42)             # '0o52'",
    ],
    examplesFr: [
      "oct(8)             # '0o10'",
      "oct(255)            # '0o377'",
      "oct(42)             # '0o52'",
    ],
    orderEn: [
      "1. Converts the integer to base-8",
      "2. Prepends '0o' to indicate octal",
    ],
    orderFr: [
      "1. Convertit l'entier en base 8",
      "2. Ajoute '0o' pour indiquer l'octal",
    ],
    mistakesEn: [
      "In Python 3, `010` is a syntax error — use `0o10` for octal literal",
      "`oct()` only works with integers",
    ],
    mistakesFr: [
      "En Python 3, `010` est une erreur de syntaxe",
    ],
  },
  "open": {
    name: "open",
    type: "function",
    signature: "open(file, mode='r', ...) -> file object",
    descriptionEn: "Opens a file and returns a file object. Mode: \'r\' (read), \'w\' (write), \'a\' (append), \'b\' (binary), \'x\' (exclusive create).",
    descriptionFr: "Ouvre un fichier et retourne un objet fichier. Mode : \'r\' (lecture), \'w\' (ecriture), \'a\' (ajout), \'b\' (binaire), \'x\' (creation exclusive).",
    returnType: "file object",
    examplesEn: [
      "open('file.txt')            # read text",
      "open('file.txt', 'w')        # write text",
      "open('file.txt', 'rb')       # read binary",
      "open('file.txt', encoding='utf-8')  # specify encoding",
    ],
    examplesFr: [
      "open('fichier.txt')         # lire texte",
      "open('fichier.txt', 'w')     # ecrire texte",
      "open('fichier.txt', 'rb')    # lire binaire",
    ],
    orderEn: [
      "1. Checks the file exists and permissions (for read)",
      "2. Creates/truncates if writing",
      "3. Returns a file object that supports iteration and reading/writing",
      "4. Always use `with open(...) as f:` for automatic cleanup",
    ],
    orderFr: [
      "1. Verifie l'existence du fichier et les permissions",
      "2. Cree/tronque si ecriture",
      "3. Retourne un objet fichier",
    ],
    mistakesEn: [
      "ALWAYS use `with open(...) as f:` to automatically close the file",
      "Specify `encoding='utf-8'` for text files to avoid platform-dependent behavior",
      "Binary mode ('rb', 'wb') returns bytes, not str",
    ],
    mistakesFr: [
      "TOUJOURS utiliser `with open(...) as f:`",
    ],
  },
  "ord": {
    name: "ord",
    type: "function",
    signature: "ord(c) -> int",
    descriptionEn: "Returns the Unicode codepoint (integer) for a single character string. Inverse of `chr()`.",
    descriptionFr: "Retourne le point de code Unicode (entier) pour une chaine d\'un seul caractere. Inverse de `chr()`.",
    returnType: "int",
    examplesEn: [
      "ord('A')           # 65",
      "ord('\u20ac')        # 8364 (Euro sign)",
      "ord('\U0001f680')    # 128640 (rocket)",
    ],
    examplesFr: [
      "ord('A')           # 65",
      "ord('\u20ac')        # 8364 (Euro sign)",
      "ord('\U0001f680')    # 128640 (rocket)",
    ],
    orderEn: [
      "1. Takes a single character string",
      "2. Returns its Unicode codepoint as an integer",
      "3. Raises TypeError if c is not a string or len(c) != 1",
    ],
    orderFr: [
      "1. Prend une chaine d'un seul caractere",
      "2. Retourne son point de code Unicode",
      "3. Leve TypeError si ce n'est pas un seul caractere",
    ],
    mistakesEn: [
      "`ord('A')` is 65, `chr(65)` is 'A' — they are inverses",
      "Only works on single characters",
    ],
    mistakesFr: [
      "`ord()` ne fonctionne que sur un seul caractere",
    ],
  },
  "pow": {
    name: "pow",
    type: "function",
    signature: "pow(base, exp[, mod]) -> number",
    descriptionEn: "Returns base raised to power exp. If mod is given, returns (base ** exp) % mod efficiently (modular exponentiation).",
    descriptionFr: "Retourne base eleve a la puissance exp. Si mod est donne, retourne (base ** exp) % mod efficacement.",
    returnType: "int or float",
    examplesEn: [
      "pow(2, 10)         # 1024",
      "pow(2, 10, 100)     # 24 (modular exponentiation)",
      "pow(9, 0.5)         # 3.0 (square root)",
    ],
    examplesFr: [
      "pow(2, 10)         # 1024",
      "pow(2, 10, 100)     # 24 (exponentiation modulaire)",
      "pow(9, 0.5)         # 3.0 (racine carree)",
    ],
    orderEn: [
      "1. Computes base ** exp",
      "2. If mod is given, computes (base ** exp) % mod efficiently",
      "3. Three-argument form only works with integers",
    ],
    orderFr: [
      "1. Calcule base ** exp",
      "2. Si mod est donne, calcule (base ** exp) % mod efficacement",
      "3. La forme a trois arguments ne marche qu'avec les entiers",
    ],
    mistakesEn: [
      "`pow(base, exp, mod)` is much faster than `(base ** exp) % mod` for large exponents",
      "The three-argument form requires all three arguments to be integers",
    ],
    mistakesFr: [
      "`pow(base, exp, mod)` est bien plus rapide",
    ],
  },
  "print": {
    name: "print",
    type: "function",
    signature: "print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> None",
    descriptionEn: "Prints objects to the text stream, separated by sep and followed by end. All non-keyword arguments are converted to strings.",
    descriptionFr: "Affiche les objets dans le flux texte, separes par sep et suivis de end.",
    returnType: "None",
    examplesEn: [
      "print('hello')              # hello",
      "print(1, 2, 3, sep=', ')    # 1, 2, 3",
      "print('loading', end='')     # no newline at end",
    ],
    examplesFr: [
      "print('bonjour')            # bonjour",
      "print(1, 2, 3, sep=', ')    # 1, 2, 3",
      "print('chargement', end='')  # pas de nouvelle ligne",
    ],
    orderEn: [
      "1. Converts each argument to string via `str()`",
      "2. Joins them with sep (default space)",
      "3. Writes to file (default stdout)",
      "4. Appends end (default newline)",
      "5. If flush=True, flushes the buffer",
    ],
    orderFr: [
      "1. Convertit chaque argument en chaine via `str()`",
      "2. Les joint avec sep (espace par defaut)",
      "3. Ecrit dans file (stdout par defaut)",
      "4. Ajoute end (nouvelle ligne par defaut)",
      "5. Si flush=True, vide le tampon",
    ],
    mistakesEn: [
      "`print()` adds a space between arguments and a newline at the end",
      "Use `print(..., file=sys.stderr)` to print to stderr",
      "In Python 2, `print` was a statement, not a function",
    ],
    mistakesFr: [
      "`print()` ajoute un espace entre les arguments",
    ],
  },
  "property": {
    name: "property",
    type: "function",
    signature: "property(fget=None, fset=None, fdel=None, doc=None) -> property",
    descriptionEn: "Returns a property attribute. When accessed, calls fget; when assigned, calls fset; when deleted, calls fdel.",
    descriptionFr: "Retourne un attribut de propriete. Quand il est accede, appelle fget ; quand assigne, appelle fset ; quand supprime, appelle fdel.",
    returnType: "property descriptor",
    examplesEn: [
      "class C:\n    @property\n    def x(self):\n        return self._x",
    ],
    examplesFr: [
      "class C:\n    @property\n    def x(self):\n        return self._x",
    ],
    orderEn: [
      "1. Creates a descriptor that intercepts attribute access",
      "2. `obj.prop` calls the getter function",
      "3. `obj.prop = value` calls the setter",
      "4. `del obj.prop` calls the deleter",
    ],
    orderFr: [
      "1. Cree un descripteur qui intercepte l'acces aux attributs",
      "2. `obj.prop` appelle le getter",
      "3. `obj.prop = valeur` appelle le setter",
      "4. `del obj.prop` appelle le deleter",
    ],
    mistakesEn: [
      "`@property` makes computed attributes look like plain attributes",
      "Avoid expensive operations in property getters (users expect O(1) attribute access)",
    ],
    mistakesFr: [
      "`@property` fait ressembler les attributs calcules a des attributs simples",
    ],
  },
  "range": {
    name: "range",
    type: "type",
    signature: "range(start, stop[, step]) -> range",
    descriptionEn: "Returns an immutable sequence of numbers from start (inclusive) to stop (exclusive) with step increment. Memory-efficient (lazy).",
    descriptionFr: "Retourne une sequence immuable de nombres de start (inclus) a stop (exclu) avec un pas step. Econome en memoire (paresseux).",
    returnType: "range",
    examplesEn: [
      "list(range(5))         # [0, 1, 2, 3, 4]",
      "list(range(2, 7))       # [2, 3, 4, 5, 6]",
      "list(range(0, 10, 2))   # [0, 2, 4, 6, 8]",
      "list(range(5, 0, -1))   # [5, 4, 3, 2, 1]",
    ],
    examplesFr: [
      "list(range(5))         # [0, 1, 2, 3, 4]",
      "list(range(2, 7))       # [2, 3, 4, 5, 6]",
      "list(range(0, 10, 2))   # [0, 2, 4, 6, 8]",
      "list(range(5, 0, -1))   # [5, 4, 3, 2, 1]",
    ],
    orderEn: [
      "1. Validates parameters: start, stop, step must be integers",
      "2. Step must be non-zero (default 1)",
      "3. Generates values lazily (not stored in memory)",
      "4. Supports O(1) membership testing and indexing",
    ],
    orderFr: [
      "1. Valide les parametres : start, stop, step doivent etre des entiers",
      "2. Step doit etre non nul (defaut 1)",
      "3. Genere les valeurs paresseusement",
      "4. Supporte le test d'appartenance et l'indexation en O(1)",
    ],
    mistakesEn: [
      "`range()` in Python 3 returns a lazy range object (not a list like Python 2)",
      "`range(10)` is NOT a list — wrap with `list()` if needed",
      "Negative step works: `range(5, 0, -1)`",
    ],
    mistakesFr: [
      "`range()` renvoie un objet range paresseux",
    ],
  },
  "repr": {
    name: "repr",
    type: "function",
    signature: "repr(obj) -> str",
    descriptionEn: "Returns a string containing a printable representation of an object. For most types, `eval(repr(obj)) == obj`.",
    descriptionFr: "Retourne une chaine contenant une representation imprimable d\'un objet. Pour la plupart des types, `eval(repr(obj)) == obj`.",
    returnType: "str",
    examplesEn: [
      "repr('hello')      # \"'hello'\" (includes quotes)",
      "repr([1, 2, 3])     # '[1, 2, 3]'",
      "repr(42)            # '42'",
    ],
    examplesFr: [
      "repr('hello')      # \"'hello'\" (inclut les guillemets)",
      "repr([1, 2, 3])     # '[1, 2, 3]'",
      "repr(42)            # '42'",
    ],
    orderEn: [
      "1. Calls `obj.__repr__()`",
      "2. Returns a string that should be unambiguous (ideally recreation of the object)",
      "3. Falls back to `<ClassName object at 0x...>` if `__repr__` is not defined",
    ],
    orderFr: [
      "1. Appelle `obj.__repr__()`",
      "2. Retourne une chaine non ambigue",
      "3. Utilise `<ClassName object at 0x...>` si `__repr__` n'est pas defini",
    ],
    mistakesEn: [
      "`repr()` vs `str()` — `str()` is for humans, `repr()` is for developers",
      "If `eval(repr(obj))` works, `repr()` output is a valid Python expression",
    ],
    mistakesFr: [
      "`repr()` vs `str()` — `str()` est pour les humains, `repr()` pour les developpeurs",
    ],
  },
  "reversed": {
    name: "reversed",
    type: "function",
    signature: "reversed(seq) -> reverse iterator",
    descriptionEn: "Returns a reverse iterator that iterates over a sequence in reverse order. The sequence must implement `__reversed__` or `__len__` + `__getitem__`.",
    descriptionFr: "Retourne un iterateur inversee qui parcourt une sequence en ordre inverse.",
    returnType: "reverse iterator",
    examplesEn: [
      "list(reversed([1, 2, 3]))  # [3, 2, 1]",
      "''.join(reversed('hello'))  # 'olleh'",
    ],
    examplesFr: [
      "list(reversed([1, 2, 3]))  # [3, 2, 1]",
      "''.join(reversed('bonjour'))  # 'ruojnob'",
    ],
    orderEn: [
      "1. Checks for `__reversed__` method (optimized)",
      "2. Falls back to `__len__` + `__getitem__` for generic sequences",
      "3. Returns a lazy iterator (not a list)",
    ],
    orderFr: [
      "1. Verifie la methode `__reversed__` (optimisee)",
      "2. Utilise `__len__` + `__getitem__` comme repli",
      "3. Retourne un iterateur paresseux",
    ],
    mistakesEn: [
      "`reversed()` returns an iterator (not a list)",
      "For dicts in Python 3.8+, `list(reversed(d))` reverses insertion order",
    ],
    mistakesFr: [
      "`reversed()` retourne un iterateur",
    ],
  },
  "round": {
    name: "round",
    type: "function",
    signature: "round(number[, ndigits]) -> number",
    descriptionEn: "Rounds a number to ndigits precision after the decimal point. If ndigits is omitted or None, returns the nearest integer (as int).",
    descriptionFr: "Arrondit un nombre a ndigits decimales. Si ndigits est omis, retourne l\'entier le plus proche.",
    returnType: "int or float",
    examplesEn: [
      "round(3.14159)     # 3",
      "round(3.14159, 2)   # 3.14",
      "round(2.5)          # 2 (banker's rounding)",
      "round(3.5)          # 4 (banker's rounding)",
    ],
    examplesFr: [
      "round(3.14159)     # 3",
      "round(3.14159, 2)   # 3.14",
      "round(2.5)          # 2 (arrondi bancaire)",
      "round(3.5)          # 4 (arrondi bancaire)",
    ],
    orderEn: [
      "1. Computes the rounded value",
      "2. Uses banker's rounding (round half to even) for .5 cases",
      "3. Without ndigits: returns int; with ndigits: returns float",
    ],
    orderFr: [
      "1. Calcule la valeur arrondie",
      "2. Utilise l'arrondi bancaire (demi arrondi au pair) pour .5",
      "3. Sans ndigits : retourne int ; avec ndigits : retourne float",
    ],
    mistakesEn: [
      "Python uses banker's rounding (tie goes to even): `round(2.5)` is 2, not 3",
      "Floating-point precision can cause unexpected results: `round(2.675, 2)` is 2.67, not 2.68",
    ],
    mistakesFr: [
      "Python utilise l'arrondi bancaire",
    ],
  },
  "set": {
    name: "set",
    type: "type",
    signature: "set(iterable=()) -> set",
    descriptionEn: "Creates a mutable, unordered collection of unique, hashable elements.",
    descriptionFr: "Cree un ensemble mutable et non ordonne d\'elements uniques et hachables.",
    returnType: "set",
    examplesEn: [
      "set([1, 2, 2, 3])  # {1, 2, 3}",
      "set('hello')        # {'h', 'e', 'l', 'o'}",
      "{1, 2, 3}           # set literal",
    ],
    examplesFr: [
      "set([1, 2, 2, 3])  # {1, 2, 3}",
      "set('hello')        # {'h', 'e', 'l', 'o'}",
      "{1, 2, 3}           # ensemble litteral",
    ],
    orderEn: [
      "1. Iterates over the iterable",
      "2. Inserts each element into the set (duplicates are discarded)",
      "3. Elements must be hashable (immutable)",
    ],
    orderFr: [
      "1. Parcourt l'iterable",
      "2. Insere chaque element dans l'ensemble (les doublons sont ignores)",
      "3. Les elements doivent etre hachables",
    ],
    mistakesEn: [
      "Sets are unordered — do not rely on iteration order",
      "`{1, 2, 3}` is a set, `{}` is an empty dict (not empty set)",
      "Frozenset is the immutable version",
    ],
    mistakesFr: [
      "Les ensembles ne sont pas ordonnes",
    ],
  },
  "setattr": {
    name: "setattr",
    type: "function",
    signature: "setattr(obj, name, value) -> None",
    descriptionEn: "Sets the named attribute on an object to the given value. Equivalent to `obj.name = value`.",
    descriptionFr: "Definit l\'attribut nomme d\'un objet a la valeur donnee. Equivalent a `obj.name = value`.",
    returnType: "None",
    examplesEn: [
      "setattr(obj, 'x', 42)  # same as obj.x = 42",
    ],
    examplesFr: [
      "setattr(obj, 'x', 42)  # identique a obj.x = 42",
    ],
    orderEn: [
      "1. Looks up the attribute on the object",
      "2. Calls `__setattr__` to assign the value",
    ],
    orderFr: [
      "1. Cherche l'attribut sur l'objet",
      "2. Appelle `__setattr__` pour assigner la valeur",
    ],
    mistakesEn: [
      "Use `setattr(obj, name, val)` when the attribute name is dynamic",
      "`obj.name = val` is preferred when the name is known statically",
    ],
    mistakesFr: [
      "Utilisez `setattr(obj, nom, val)` quand le nom est dynamique",
    ],
  },
  "slice": {
    name: "slice",
    type: "function",
    signature: "slice(start, stop[, step]) -> slice",
    descriptionEn: "Returns a slice object representing a range for indexing sequences. Used internally by `obj[start:stop:step]`.",
    descriptionFr: "Retourne un objet slice representant une plage pour l\'indexation de sequences.",
    returnType: "slice",
    examplesEn: [
      "s = slice(1, 5, 2)\nlist(range(10)[s])  # [1, 3]",
      "'hello'[slice(1, 4)]   # 'ell'",
    ],
    examplesFr: [
      "s = slice(1, 5, 2)\nlist(range(10)[s])  # [1, 3]",
      "'bonjour'[slice(1, 4)]   # 'onj'",
    ],
    orderEn: [
      "1. Stores start, stop, step parameters",
      "2. Passed to `__getitem__` when using subscript notation",
      "3. Slices are themselves slice objects",
    ],
    orderFr: [
      "1. Stocke les parametres start, stop, step",
      "2. Passe a `__getitem__` lors de l'utilisation de la notation entre crochets",
      "3. Les slices sont eux-memes des objets",
    ],
    mistakesEn: [
      "`obj[1:5:2]` is syntactic sugar for `obj[slice(1, 5, 2)]`",
      "Negative indices work when the slice is applied to a sequence",
    ],
    mistakesFr: [
      "`obj[1:5:2]` est du sucre syntaxique pour `obj[slice(1, 5, 2)]`",
    ],
  },
  "sorted": {
    name: "sorted",
    type: "function",
    signature: "sorted(iterable, *, key=None, reverse=False) -> list",
    descriptionEn: "Returns a new sorted list from the items in iterable. The original iterable is not modified.",
    descriptionFr: "Retourne une nouvelle liste triee a partir des elements de l\'iterable. L\'iterable original n\'est pas modifie.",
    returnType: "list",
    examplesEn: [
      "sorted([3, 1, 2])              # [1, 2, 3]",
      "sorted('hello')                 # ['e', 'h', 'l', 'l', 'o']",
    ],
    examplesFr: [
      "sorted([3, 1, 2])              # [1, 2, 3]",
      "sorted('bonjour')               # ['b', 'j', 'n', 'o', 'o', 'r', 'u']",
    ],
    orderEn: [
      "1. Creates a list from the iterable",
      "2. Sorts the list using Timsort algorithm (O(n log n))",
      "3. Key function is applied to each element for comparison",
      "4. If reverse=True, sorts in descending order",
      "5. Returns the new sorted list",
    ],
    orderFr: [
      "1. Cree une liste a partir de l'iterable",
      "2. Trie la liste avec l'algorithme Timsort (O(n log n))",
      "3. La fonction key est appliquee a chaque element pour la comparaison",
      "4. Si reverse=True, tri en ordre descendant",
      "5. Retourne la nouvelle liste triee",
    ],
    mistakesEn: [
      "`sorted()` returns a new list — `list.sort()` sorts in-place (and returns None)",
      "Use `key=str.lower` for case-insensitive sorting",
      "`sorted()` works on ANY iterable, not just lists",
    ],
    mistakesFr: [
      "`sorted()` retourne une nouvelle liste",
    ],
  },
  "staticmethod": {
    name: "staticmethod",
    type: "function",
    signature: "staticmethod(function) -> staticmethod descriptor",
    descriptionEn: "Transforms a method into a static method. A static method does NOT receive an implicit first argument (neither cls nor self).",
    descriptionFr: "Transforme une methode en methode statique. Une methode statique ne recoit PAS de premier argument implicite.",
    returnType: "staticmethod descriptor",
    examplesEn: [
      "class MyClass:\n    @staticmethod\n    def util(x):\n        return x * 2",
    ],
    examplesFr: [
      "class MyClass:\n    @staticmethod\n    def util(x):\n        return x * 2",
    ],
    orderEn: [
      "1. Wraps the function in a staticmethod descriptor",
      "2. When accessed, returns the original function directly (no binding)",
    ],
    orderFr: [
      "1. Enveloppe la fonction dans un descripteur staticmethod",
      "2. Quand il est accede, retourne la fonction originale directement",
    ],
    mistakesEn: [
      "`@staticmethod` receives nothing extra (no `self` or `cls`)",
      "Use `@classmethod` when you need access to the class, `@staticmethod` when you don't",
    ],
    mistakesFr: [
      "`@staticmethod` ne recoit rien de supplementaire",
    ],
  },
  "str": {
    name: "str",
    type: "type",
    signature: "str(object='') -> str",
    descriptionEn: "Returns a string version of object. Strings are immutable sequences of Unicode codepoints.",
    descriptionFr: "Retourne une version chaine de l\'objet. Les chaines sont des sequences immuables de points de code Unicode.",
    returnType: "str",
    examplesEn: [
      "str(42)            # '42'",
      "str([1, 2, 3])      # '[1, 2, 3]'",
      "str(3.14)           # '3.14'",
    ],
    examplesFr: [
      "str(42)            # '42'",
      "str([1, 2, 3])      # '[1, 2, 3]'",
      "str(3.14)           # '3.14'",
    ],
    orderEn: [
      "1. Calls `object.__str__()`",
      "2. Falls back to `__repr__()` if `__str__` is not defined",
    ],
    orderFr: [
      "1. Appelle `object.__str__()`",
      "2. Utilise `__repr__()` si `__str__` n'est pas defini",
    ],
    mistakesEn: [
      "`str()` is for readable output, `repr()` for unambiguous",
      "Strings are immutable — every operation returns a new string",
    ],
    mistakesFr: [
      "`str()` est pour une sortie lisible",
    ],
  },
  "sum": {
    name: "sum",
    type: "function",
    signature: "sum(iterable, start=0) -> number",
    descriptionEn: "Sums all items of an iterable and returns the total, starting from start (default 0). The items must support addition.",
    descriptionFr: "Additionne tous les elements d\'un iterable et retourne le total, en commencant par start (defaut 0).",
    returnType: "number",
    examplesEn: [
      "sum([1, 2, 3, 4, 5])  # 15",
      "sum([1, 2, 3], 10)      # 16 (start at 10)",
      "sum(range(101))         # 5050",
    ],
    examplesFr: [
      "sum([1, 2, 3, 4, 5])  # 15",
      "sum([1, 2, 3], 10)      # 16 (commence a 10)",
      "sum(range(101))         # 5050",
    ],
    orderEn: [
      "1. Starts with the start value",
      "2. For each item in the iterable: total += item",
      "3. Returns the final total",
    ],
    orderFr: [
      "1. Commence avec la valeur start",
      "2. Pour chaque element : total += element",
      "3. Retourne le total final",
    ],
    mistakesEn: [
      "`sum()` does not work with strings — use `''.join(seq)` instead",
      "For nested lists, use `itertools.chain.from_iterable()`",
    ],
    mistakesFr: [
      "`sum()` ne fonctionne pas avec les chaines",
    ],
  },
  "super": {
    name: "super",
    type: "function",
    signature: "super([type[, object-or-type]]) -> super object",
    descriptionEn: "Returns a proxy object that delegates method calls to the parent or sibling class. Used to call parent class methods.",
    descriptionFr: "Retourne un objet proxy qui delegue les appels de methode a la classe parente ou soeur.",
    returnType: "super object",
    examplesEn: [
      "class Dog(Animal):\n    def speak(self):\n        return super().speak()",
    ],
    examplesFr: [
      "class Dog(Animal):\n    def speak(self):\n        return super().speak()",
    ],
    orderEn: [
      "1. Returns a proxy that follows the MRO (Method Resolution Order)",
      "2. Calls the next class in the MRO that defines the method",
      "3. Without arguments in Python 3, automatically uses current class and self",
    ],
    orderFr: [
      "1. Retourne un proxy qui suit le MRO (Method Resolution Order)",
      "2. Appelle la classe suivante dans le MRO qui definit la methode",
      "3. Sans arguments en Python 3, utilise automatiquement la classe courante",
    ],
    mistakesEn: [
      "`super()` without args works in Python 3 (not Python 2)",
      "`super().__init__()` is the standard way to call parent constructors",
      "`super()` works with multiple inheritance via C3 linearization",
    ],
    mistakesFr: [
      "`super()` sans arguments fonctionne en Python 3",
    ],
  },
  "tuple": {
    name: "tuple",
    type: "type",
    signature: "tuple(iterable=()) -> tuple",
    descriptionEn: "Creates a tuple from an iterable. Tuples are immutable, ordered sequences that can hold items of any type.",
    descriptionFr: "Cree un tuple a partir d\'un iterable. Les tuples sont des sequences immuables et ordonnees.",
    returnType: "tuple",
    examplesEn: [
      "tuple('hello')     # ('h', 'e', 'l', 'l', 'o')",
      "tuple([1, 2, 3])    # (1, 2, 3)",
      "(1, 2, 3)           # tuple literal",
    ],
    examplesFr: [
      "tuple('hello')     # (\'h\', \'e\', \'l\', \'l\', \'o\')",
      "tuple([1, 2, 3])    # (1, 2, 3)",
      "(1, 2, 3)           # tuple litteral",
    ],
    orderEn: [
      "1. Iterates over the iterable",
      "2. Collects items into a new tuple",
      "3. Tuples are immutable — cannot be modified after creation",
    ],
    orderFr: [
      "1. Parcourt l'iterable",
      "2. Collecte les elements dans un nouveau tuple",
      "3. Les tuples sont immuables",
    ],
    mistakesEn: [
      "`(1)` is just the integer 1 — use `(1,)` for a single-element tuple",
      "Tuples are hashable (usable as dict keys) if all elements are hashable",
    ],
    mistakesFr: [
      "`(1)` est juste l'entier 1",
    ],
  },
  "type": {
    name: "type",
    type: "function",
    signature: "type(object) -> type / type(name, bases, dict) -> type",
    descriptionEn: "With one argument: returns the type of an object. With three arguments: creates a new type (dynamic class).",
    descriptionFr: "Avec un argument : retourne le type d\'un objet. Avec trois arguments : cree un nouveau type (classe dynamique).",
    returnType: "type (the type of the object, or a new type)",
    examplesEn: [
      "type(42)            # <class 'int'>",
      "type('hello')        # <class 'str'>",
      "type('Dog', (Animal,), {'speak': lambda self: 'Woof'})  # dynamic class",
    ],
    examplesFr: [
      "type(42)            # <class 'int'>",
      "type('hello')        # <class 'str'>",
      "type('Dog', (Animal,), {'speak': lambda self: 'Woof'})  # classe dynamique",
    ],
    orderEn: [
      "1. One arg: returns `object.__class__` (the object's type)",
      "2. Three args: creates a new class with name, bases (tuple of parent classes), and namespace dict",
    ],
    orderFr: [
      "1. Un argument : retourne `object.__class__` (le type de l'objet)",
      "2. Trois arguments : cree une nouvelle classe avec nom, bases et dict d'espace de noms",
    ],
    mistakesEn: [
      "`type(obj)` does NOT consider inheritance — use `isinstance()` for that",
      "`type(True)` is `<class 'bool'>`, `type(True) == int` is False (but isinstance is True)",
    ],
    mistakesFr: [
      "`type(obj)` ne considere PAS l'heritage",
    ],
  },
  "vars": {
    name: "vars",
    type: "function",
    signature: "vars([object]) -> dict",
    descriptionEn: "Without arguments: returns the local namespace (same as `locals()`). With an object: returns the object\'s `__dict__` attribute.",
    descriptionFr: "Sans argument : retourne l\'espace de noms local (identique a `locals()`). Avec un objet : retourne l\'attribut `__dict__`.",
    returnType: "dict",
    examplesEn: [
      "vars()             # local namespace",
      "vars([])            # list.__dict__ (attributes of list object)",
    ],
    examplesFr: [
      "vars()             # espace de noms local",
      "vars([])            # list.__dict__",
    ],
    orderEn: [
      "1. Without args: returns local scope dict",
      "2. With object: returns `object.__dict__` (the object's writable attributes)",
    ],
    orderFr: [
      "1. Sans argument : retourne le dict de la portee locale",
      "2. Avec objet : retourne `object.__dict__`",
    ],
    mistakesEn: [
      "`vars(obj)` raises TypeError if obj doesn't have `__dict__`",
      "Use `dir(obj)` to see all attributes (including inherited)",
    ],
    mistakesFr: [
      "`vars(obj)` leve TypeError si obj n'a pas `__dict__`",
    ],
  },
  "zip": {
    name: "zip",
    type: "function",
    signature: "zip(*iterables, strict=False) -> iterator of tuples",
    descriptionEn: "Iterates over multiple iterables in parallel, yielding tuples of the i-th elements. Stops when the shortest iterable is exhausted (unless strict=True).",
    descriptionFr: "Parcourt plusieurs iterables en parallele, produisant des tuples des i-emes elements. S\'arrete quand le plus court est epuise.",
    returnType: "iterator of tuples",
    examplesEn: [
      "list(zip([1, 2, 3], ['a', 'b', 'c']))  # [(1, 'a'), (2, 'b'), (3, 'c')]",
      "list(zip([1, 2], ['a', 'b', 'c']))   # [(1, 'a'), (2, 'b')] (shortest wins)",
    ],
    examplesFr: [
      "list(zip([1, 2, 3], ['a', 'b', 'c']))  # [(1, 'a'), (2, 'b'), (3, 'c')]",
      "list(zip([1, 2], ['a', 'b', 'c']))   # [(1, 'a'), (2, 'b')] (le plus court gagne)",
    ],
    orderEn: [
      "1. Retrieves the i-th element from each iterable",
      "2. Zips them into a tuple",
      "3. Stops when the shortest iterable is exhausted (default) or raises ValueError if strict=True and lengths differ",
      "4. Returns a lazy iterator",
    ],
    orderFr: [
      "1. Recupere le i-eme element de chaque iterable",
      "2. Les assemble en un tuple",
      "3. S'arrete quand le plus court est epuise (ou leve ValueError si strict=True)",
      "4. Retourne un iterateur paresseux",
    ],
    mistakesEn: [
      "`zip()` returns an iterator in Python 3 (not a list like Python 2)",
      "Use `zip(..., strict=True)` (Python 3.10+) to require equal-length iterables",
      "`zip(*pairs)` unzips: `list(zip(*[(1,'a'),(2,'b')]))` => [(1,2), ('a','b')]",
    ],
    mistakesFr: [
      "`zip()` retourne un iterateur en Python 3",
    ],
  },
  "__import__": {
    name: "__import__",
    type: "function",
    signature: "__import__(name, globals=None, locals=None, fromlist=(), level=0) -> module",
    descriptionEn: "Called by the import statement. Allows importing modules dynamically. Prefer importlib.import_module() for readability.",
    descriptionFr: "Appele par l'instruction import. Permet d'importer des modules dynamiquement. Preference pour importlib.import_module().",
    returnType: "module",
    examplesEn: ["os_module = __import__('os')", "sys = __import__('sys')"],
    examplesFr: ["module_os = __import__('os')", "sys = __import__('sys')"],
    orderEn: ["1. Searches for the module in sys.path", "2. Loads and initializes the module", "3. Returns the module object"],
    orderFr: ["1. Cherche le module dans sys.path", "2. Charge et initialise le module", "3. Retourne l'objet module"],
    mistakesEn: ["Prefer importlib.import_module() over __import__() for dynamic imports", "import statement is syntactic sugar for __import__()"],
    mistakesFr: ["Preferez importlib.import_module() a __import__()", "L'instruction import est du sucre syntaxique pour __import__()"],
  },
  "breakpoint": {
    name: "breakpoint",
    type: "function",
    signature: "breakpoint(*args, **kws) -> None",
    descriptionEn: "Drops into the debugger at the call site. Python 3.7+. Calls sys.breakpointhook() which by default starts pdb.",
    descriptionFr: "Entre dans le debogueur au point d'appel. Python 3.7+. Appelle sys.breakpointhook() qui demarre pdb par defaut.",
    returnType: "None",
    examplesEn: ["def calc(x):\n    breakpoint()  # debugger stops here\n    return x * 2"],
    examplesFr: ["def calc(x):\n    breakpoint()  # le debogueur s'arrete ici\n    return x * 2"],
    orderEn: ["1. Calls sys.breakpointhook()", "2. By default starts pdb (Python Debugger)", "3. PYTHONBREAKPOINT env var can change the debugger"],
    orderFr: ["1. Appelle sys.breakpointhook()", "2. Par defaut demarre pdb", "3. PYTHONBREAKPOINT peut changer le debogueur"],
    mistakesEn: ["In Python < 3.7, use import pdb; pdb.set_trace() instead", "breakpoint() is removed by -O optimization flag"],
    mistakesFr: ["En Python < 3.7, utilisez import pdb; pdb.set_trace()", "breakpoint() est supprime par l'option -O"],
  },
  "lambda": {
    name: "lambda",
    type: "keyword",
    signature: "lambda args: expression",
    descriptionEn: "Creates an anonymous inline function. Can take any number of arguments but only one expression (implicitly returned).",
    descriptionFr: "Cree une fonction anonyme en ligne. Peut prendre plusieurs arguments mais une seule expression (retournee implicitement).",
    returnType: "function",
    examplesEn: ["lambda x: x * 2", "lambda a, b: a + b", "sorted(items, key=lambda x: x['name'])"],
    examplesFr: ["lambda x: x * 2", "lambda a, b: a + b", "sorted(items, key=lambda x: x['name'])"],
    orderEn: ["1. The lambda keyword captures the arguments and expression", "2. Returns a function object (no assignment needed)", "3. When called, the expression is evaluated and its value is returned"],
    orderFr: ["1. Le mot-cle lambda capture les arguments et l'expression", "2. Retourne un objet fonction", "3. Quand appele, l'expression est evaluee et sa valeur est retournee"],
    mistakesEn: ["Lambdas can only contain a single expression (no statements like if/for)", "Prefer def for named functions — lambdas are for short, throw-away functions", "The expression is implicitly returned"],
    mistakesFr: ["Les lambdas ne contiennent qu'une seule expression (pas d'instructions)", "Preferez def pour les fonctions nommees"],
  },
  "yield": {
    name: "yield",
    type: "keyword",
    signature: "yield [expression]",
    descriptionEn: "Used inside a function to make it a generator. Suspends the function, saves state, and returns a value. The generator can be resumed later.",
    descriptionFr: "Utilise a l'interieur d'une fonction pour en faire un generateur. Suspend la fonction, sauvegarde l'etat et retourne une valeur.",
    returnType: "generator object",
    examplesEn: ["def count(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1\nlist(count(3))  # [0, 1, 2]"],
    examplesFr: ["def compter(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1\nlist(compter(3))  # [0, 1, 2]"],
    orderEn: ["1. The function becomes a generator function (returns a generator object when called)", "2. On each call to next(), the function runs until yield", "3. The yielded value is returned to the caller", "4. The function's state is frozen until the next call"],
    orderFr: ["1. La fonction devient un generateur", "2. A chaque appel de next(), la fonction s'execute jusqu'a yield", "3. La valeur est retournee a l'appelant", "4. L'etat est gele jusqu'au prochain appel"],
    mistakesEn: ["yield vs return: yield produces a sequence, return ends the generator", "yield from delegates to another generator", "A generator can only be iterated once"],
    mistakesFr: ["yield vs return : yield produit une sequence, return termine le generateur"],
  },
  "if": {
    name: "if",
    type: "keyword",
    signature: "if condition:\n    body\nelif condition:\n    body\nelse:\n    body",
    descriptionEn: "Conditional execution. Evaluates a condition and executes the first block whose condition is True. elif and else are optional.",
    descriptionFr: "Execution conditionnelle. Evalue une condition et execute le premier bloc dont la condition est vraie.",
    returnType: "None (statement)",
    examplesEn: ["x = 10\nif x > 0:\n    print('positive')\nelif x == 0:\n    print('zero')\nelse:\n    print('negative')"],
    examplesFr: ["x = 10\nif x > 0:\n    print('positif')\nelif x == 0:\n    print('zero')\nelse:\n    print('negatif')"],
    orderEn: ["1. Evaluates the condition expression", "2. If truthy, executes the if block and skips elif/else", "3. If falsy, moves to the next elif (if any)", "4. If no condition was True, executes the else block (if present)"],
    orderFr: ["1. Evalue l'expression de condition", "2. Si vrai, execute le bloc if et saute elif/else", "3. Si faux, passe au elif suivant", "4. Si aucune condition vraie, execute le bloc else"],
    mistakesEn: ["Use elif, not else if (syntax error)", "Indentation matters — incorrect indentation causes IndentationError", "Non-boolean values are tested for truthiness (0, '', None, [] are falsy)"],
    mistakesFr: ["Utilisez elif, pas else if (erreur de syntaxe)", "L'indentation est significative"],
  },
  "for": {
    name: "for",
    type: "keyword",
    signature: "for var in iterable:\n    body\nelse:\n    body",
    descriptionEn: "Iterates over an iterable, assigning each element to the loop variable. Optionally has an else clause that runs if the loop completes without break.",
    descriptionFr: "Parcourt un iterable, assignant chaque element a la variable de boucle. Peut avoir une clause else qui s'execute si la boucle termine sans break.",
    returnType: "None (statement)",
    examplesEn: ["for i in range(3):\n    print(i)  # 0, 1, 2", "for key, val in {'a': 1}.items():\n    print(key, val)"],
    examplesFr: ["for i in range(3):\n    print(i)  # 0, 1, 2", "for key, val in {'a': 1}.items():\n    print(key, val)"],
    orderEn: ["1. Calls iter() on the iterable to get an iterator", "2. Repeatedly calls next() on the iterator", "3. Assigns each value to the loop variable", "4. Executes the body for each value", "5. Stops when StopIteration is raised", "6. If break was not called, runs the else block"],
    orderFr: ["1. Appelle iter() sur l'iterable", "2. Appelle next() sur l'iterateur", "3. Assigne chaque valeur a la variable", "4. Execute le corps pour chaque valeur", "5. S'arrete quand StopIteration est levee"],
    mistakesEn: ["Modifying a list while iterating over it can skip elements", "The loop variable leaks in Python < 3.8 (exists after the loop)", "else clause runs if no break occurred"],
    mistakesFr: ["Modifier une liste pendant l'iteration peut sauter des elements"],
  },
  "while": {
    name: "while",
    type: "keyword",
    signature: "while condition:\n    body\nelse:\n    body",
    descriptionEn: "Repeatedly executes a block as long as the condition is truthy. Has an optional else clause that runs if the loop completes without break.",
    descriptionFr: "Execute un bloc tant que la condition est vraie. Clause else optionnelle qui s'execute si la boucle termine sans break.",
    returnType: "None (statement)",
    examplesEn: ["i = 0\nwhile i < 3:\n    print(i)\n    i += 1", "while True:\n    data = get_data()\n    if not data: break"],
    examplesFr: ["i = 0\nwhile i < 3:\n    print(i)\n    i += 1", "while True:\n    data = get_data()\n    if not data: break"],
    orderEn: ["1. Evaluates the condition", "2. If falsy, exits the loop (runs else if no break)", "3. If truthy, executes the body", "4. Repeats from step 1"],
    orderFr: ["1. Evalue la condition", "2. Si faux, quitte la boucle (execute else si pas de break)", "3. Si vrai, execute le corps", "4. Repete depuis l'etape 1"],
    mistakesEn: ["Ensure the condition can become False — infinite loops are common", "while loops do not have an automatic iteration variable (unlike for)", "Use break to exit early"],
    mistakesFr: ["Assurez-vous que la condition peut devenir False"],
  },
  "def": {
    name: "def",
    type: "keyword",
    signature: "def name(params):\n    body\nreturn value",
    descriptionEn: "Defines a function. Functions are first-class objects in Python (can be passed around like any other value).",
    descriptionFr: "Definit une fonction. Les fonctions sont des objets de premiere classe en Python.",
    returnType: "function object",
    examplesEn: ["def add(a, b):\n    return a + b\nresult = add(3, 4)  # 7"],
    examplesFr: ["def add(a, b):\n    return a + b\nresult = add(3, 4)  # 7"],
    orderEn: ["1. def creates a function object with the given name", "2. The body is NOT executed at definition time", "3. When called, a new local scope is created", "4. Arguments are bound to parameters", "5. The body executes, optionally returning a value via return"],
    orderFr: ["1. def cree un objet fonction avec le nom donne", "2. Le corps n'est PAS execute a la definition", "3. Quand appele, un nouvel espace local est cree", "4. Les arguments sont lies aux parametres", "5. Le corps s'execute"],
    mistakesEn: ["Functions without a return statement return None", "Default arguments are evaluated once at definition time (not call time)", "Mutable default arguments persist across calls"],
    mistakesFr: ["Les fonctions sans return retournent None"],
  },
  "class": {
    name: "class",
    type: "keyword",
    signature: "class Name(Base):\n    body",
    descriptionEn: "Defines a class. Classes are blueprints for creating objects. All classes implicitly inherit from object.",
    descriptionFr: "Definit une classe. Les classes sont des plans pour creer des objets. Toutes les classes heritent implicitement de object.",
    returnType: "class object",
    examplesEn: ["class Dog(Animal):\n    def speak(self):\n        return 'Woof'\nd = Dog()\nd.speak()  # 'Woof'"],
    examplesFr: ["class Dog(Animal):\n    def speak(self):\n        return 'Ouaf'\nd = Dog()\nd.speak()  # 'Ouaf'"],
    orderEn: ["1. class creates a class object with a namespace", "2. The body defines attributes (methods are functions in the class dict)", "3. Instances are created by calling the class: MyClass()", "4. __init__ initializes each new instance"],
    orderFr: ["1. class cree un objet classe", "2. Le corps definit les attributs", "3. Les instances sont creees en appelant la classe", "4. __init__ initialise chaque instance"],
    mistakesEn: ["self is the first parameter of instance methods (passed automatically)", "Inheritance: class Child(Parent) — not using () makes it inherit from object", "Class variables are shared across all instances (unless shadowed by instance vars)"],
    mistakesFr: ["self est le premier parametre des methodes d'instance"],
  },
  "return": {
    name: "return",
    type: "keyword",
    signature: "return [expression]",
    descriptionEn: "Exits a function and returns a value to the caller. If no expression is given, returns None.",
    descriptionFr: "Quitte une fonction et retourne une valeur a l'appelant. Sans expression, retourne None.",
    returnType: "the value of the expression, or None",
    examplesEn: ["def square(x):\n    return x * x\nresult = square(5)  # 25"],
    examplesFr: ["def square(x):\n    return x * x\nresult = square(5)  # 25"],
    orderEn: ["1. The expression is evaluated", "2. The function is immediately exited", "3. The value is passed back to the caller", "4. Any code after return is not executed"],
    orderFr: ["1. L'expression est evaluee", "2. La fonction est immediatement quittee", "3. La valeur est transmise a l'appelant", "4. Tout code apres return n'est pas execute"],
    mistakesEn: ["return outside a function raises SyntaxError", "A function without return returns None", "Multiple return values are returned as a tuple (or use explicit tuple)"],
    mistakesFr: ["return hors d'une fonction leve SyntaxError"],
  },
  "try": {
    name: "try",
    type: "keyword",
    signature: "try:\n    body\nexcept SomeError as e:\n    handler\nelse:\n    no_error_body\nfinally:\n    cleanup_body",
    descriptionEn: "Defines an exception handling block. The try block is executed; if an exception occurs, the matching except block handles it. else runs if no exception. finally always runs.",
    descriptionFr: "Definit un bloc de gestion d'exception. Le bloc try est execute ; si une exception se produit, le bloc except correspondant la gere.",
    returnType: "None (statement)",
    examplesEn: ["try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('cannot divide by zero')"],
    examplesFr: ["try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('impossible de diviser par zero')"],
    orderEn: ["1. Executes the try block", "2. If no exception: runs the else block", "3. If exception: searches except blocks for a matching type", "4. If no except matches: the exception propagates upward", "5. In all cases: executes the finally block"],
    orderFr: ["1. Execute le bloc try", "2. Si pas d'exception : execute le bloc else", "3. Si exception : cherche un bloc except correspondant", "4. Aucun except ne correspond : l'exception remonte", "5. Dans tous les cas : execute finally"],
    mistakesEn: ["Bare except: catches ALL exceptions (including KeyboardInterrupt)", "Prefer specific exception types (except ValueError:)", "finally always runs, even after return, break, or continue"],
    mistakesFr: ["except: nu attrape TOUTES les exceptions", "Preferez des types d'exception specifiques"],
  },
  "raise": {
    name: "raise",
    type: "keyword",
    signature: "raise [exception]",
    descriptionEn: "Raises an exception. Can raise a new exception or re-raise the current exception (bare raise).",
    descriptionFr: "Leve une exception. Peut lever une nouvelle exception ou relancer l'exception courante (raise nu).",
    returnType: "None (exception)",
    examplesEn: ["raise ValueError('invalid input')", "try:\n    ...\nexcept:\n    raise  # re-raise current exception"],
    examplesFr: ["raise ValueError('entree invalide')", "try:\n    ...\nexcept:\n    raise  # relance l'exception courante"],
    orderEn: ["1. The exception object is created (or the current exception is re-raised)", "2. The call stack is unwound looking for an except handler", "3. If none found, the program terminates with a traceback"],
    orderFr: ["1. L'objet exception est cree", "2. La pile d'appels est remontee a la recherche d'un handler", "3. Si aucun trouve, le programme se termine"],
    mistakesEn: ["raise expects an exception instance or class", "Don't use raise without an active exception (outside an except block)", "Re-raise with bare raise (not raise e) to preserve traceback"],
    mistakesFr: ["raise attend une instance ou classe d'exception"],
  },
  "pass": {
    name: "pass",
    type: "keyword",
    signature: "pass",
    descriptionEn: "A no-operation statement. Does nothing. Used as a placeholder where syntax requires a statement but no action is needed.",
    descriptionFr: "Une instruction no-operation. Ne fait rien. Utilise comme placeholder la ou la syntaxe necessite une instruction.",
    returnType: "None (statement)",
    examplesEn: ["def not_implemented_yet():\n    pass", "class MyException(Exception):\n    pass"],
    examplesFr: ["def pas_encore_implemente():\n    pass", "class MonException(Exception):\n    pass"],
    orderEn: ["1. Does absolutely nothing", "2. Syntax requires a block — pass satisfies this without effect"],
    orderFr: ["1. Ne fait absolument rien", "2. La syntaxe necessite un bloc — pass satisfait ceci sans effet"],
    mistakesEn: ["pass is not a comment — docstrings serve a different purpose", "Use ... (Ellipsis) as an alternative placeholder", "Unlike return, pass does NOT exit the function"],
    mistakesFr: ["pass n'est pas un commentaire"],
  },
  "del": {
    name: "del",
    type: "keyword",
    signature: "del target",
    descriptionEn: "Deletes a reference to an object. Removes a variable, list element, dictionary key, or attribute. Does NOT delete the object itself (garbage collection handles that).",
    descriptionFr: "Supprime une reference a un objet. Supprime une variable, un element de liste, une cle de dictionnaire ou un attribut.",
    returnType: "None (statement)",
    examplesEn: ["x = 42\ndel x  # x no longer exists", "d = {'a': 1}\ndel d['a']  # remove key", "lst = [1, 2, 3]\ndel lst[1]  # [1, 3]"],
    examplesFr: ["x = 42\ndel x  # x n'existe plus", "d = {'a': 1}\ndel d['a']  # supprime la cle", "lst = [1, 2, 3]\ndel lst[1]  # [1, 3]"],
    orderEn: ["1. Removes the reference binding (variable, key, index, attribute)", "2. The object may remain in memory if other references exist", "3. del on a local variable can cause UnboundLocalError if accessed later"],
    orderFr: ["1. Supprime la liaison de reference", "2. L'objet peut rester en memoire si d'autres references existent"],
    mistakesEn: ["del does NOT delete the object — it only removes the reference", "Cannot delete local variables in enclosing scopes", "Deleting from a list while iterating causes issues"],
    mistakesFr: ["del ne supprime PAS l'objet — seulement la reference"],
  },
  "with": {
    name: "with",
    type: "keyword",
    signature: "with expr as var:\n    body",
    descriptionEn: "Context manager statement. Wraps a block with enter and exit logic. The expr provides a context manager that sets up and tears down resources automatically.",
    descriptionFr: "Instruction de gestionnaire de contexte. Encadre un bloc avec une logique d'entree et de sortie.",
    returnType: "None (statement)",
    examplesEn: ["with open('file.txt') as f:\n    content = f.read()  # file auto-closed", "with lock:\n    # critical section"],
    examplesFr: ["with open('fichier.txt') as f:\n    contenu = f.read()  # fichier ferme auto", "with lock:\n    # section critique"],
    orderEn: ["1. Calls expr.__enter__() — result is bound to var (if as clause)", "2. Executes the body", "3. Calls expr.__exit__() on exit (normal or exception)", "4. If an exception occurred, __exit__ can suppress it by returning True"],
    orderFr: ["1. Appelle expr.__enter__()", "2. Execute le corps", "3. Appelle expr.__exit__() en sortie", "4. Si une exception s'est produite, __exit__ peut la supprimer"],
    mistakesEn: ["Always use with for file/network resources", "Multiple context managers: with open('a') as a, open('b') as b:", "In Python 3.10+: parenthesized context managers for multiple lines"],
    mistakesFr: ["Utilisez toujours with pour les fichiers/ressources"],
  },
  "import": {
    name: "import",
    type: "keyword",
    signature: "import module\nfrom module import name\nfrom module import name as alias",
    descriptionEn: "Loads and executes a module, making its contents available. Modules are cached in sys.modules after first import.",
    descriptionFr: "Charge et execute un module, rendant son contenu disponible. Les modules sont mis en cache dans sys.modules.",
    returnType: "None (statement)",
    examplesEn: ["import math\nmath.sqrt(16)  # 4.0", "from os import path\npath.join('a', 'b')  # 'a/b'"],
    examplesFr: ["import math\nmath.sqrt(16)  # 4.0", "from os import path\npath.join('a', 'b')  # 'a/b'"],
    orderEn: ["1. Searches for the module in sys.path", "2. Checks sys.modules cache (skips loading if already imported)", "3. If not cached: loads the module file, compiles, and executes it", "4. Binds the module name in the current namespace"],
    orderFr: ["1. Cherche le module dans sys.path", "2. Verifie le cache sys.modules", "3. Si non en cache : charge, compile et execute le module", "4. Lie le nom du module dans l'espace de noms courant"],
    mistakesEn: ["Circular imports cause partial module loading", "import is cached — reload(module) forces re-import", "from X import * is discouraged (pollutes namespace)"],
    mistakesFr: ["Les imports circulaires causent un chargement partiel"],
  },
  "in": {
    name: "in",
    type: "keyword",
    signature: "value in container -> bool\nfor var in iterable:",
    descriptionEn: "Membership test operator. Returns True if value is found in container. Also used in for loops to iterate.",
    descriptionFr: "Operateur de test d'appartenance. Retourne True si la valeur est trouvee dans le conteneur.",
    returnType: "bool (also used as loop keyword)",
    examplesEn: ["'a' in 'hello'        # False", "3 in [1, 2, 3]         # True", "'key' in {'key': 1}    # True (checks keys)"],
    examplesFr: ["'a' in 'bonjour'      # False", "3 in [1, 2, 3]         # True", "'cle' in {'cle': 1}    # True (verifie les cles)"],
    orderEn: ["1. Calls container.__contains__(value)", "2. Falls back to iterating with __iter__ and == comparisons", "3. Returns True if found, False otherwise"],
    orderFr: ["1. Appelle conteneur.__contains__(valeur)", "2. Sinon parcourt avec __iter__ et ==", "3. Retourne True si trouve, False sinon"],
    mistakesEn: ["For dicts, in checks keys (not values)", "in is O(n) for lists, O(1) for sets and dicts"],
    mistakesFr: ["Pour les dicts, in verifie les cles (pas les valeurs)"],
  },
  "is": {
    name: "is",
    type: "keyword",
    signature: "a is b -> bool",
    descriptionEn: "Identity operator. Returns True if a and b are the SAME object (same memory address). Not the same as == (which checks equality).",
    descriptionFr: "Operateur d'identite. Retourne True si a et b sont le MEME objet (meme adresse memoire).",
    returnType: "bool",
    examplesEn: ["x = [1, 2]; y = [1, 2]; x == y  # True (equal)", "x is y  # False (different objects)", "x = y = [1, 2]; x is y  # True (same object)"],
    examplesFr: ["x = [1, 2]; y = [1, 2]; x == y  # True (egaux)", "x is y  # False (objets differents)", "x = y = [1, 2]; x is y  # True (meme objet)"],
    orderEn: ["1. Compares the memory addresses of a and b", "2. Returns True if they are the same object, False otherwise", "3. Equivalent to id(a) == id(b)"],
    orderFr: ["1. Compare les adresses memoires de a et b", "2. Retourne True si meme objet, False sinon", "3. Equivalent a id(a) == id(b)"],
    mistakesEn: ["Never use is for value comparison — use == (equality operator)", "Use is None, is True, is False for singleton comparison", "Small integers (typically -5 to 256) may be cached and share identity"],
    mistakesFr: ["N'utilisez jamais is pour comparer des valeurs"],
  },
  "not": {
    name: "not",
    type: "keyword",
    signature: "not x -> bool",
    descriptionEn: "Logical NOT operator. Returns the opposite truth value of x. If x is truthy, returns False; if x is falsy, returns True.",
    descriptionFr: "Operateur logique NON. Retourne la valeur de verite opposee de x.",
    returnType: "bool",
    examplesEn: ["not True              # False", "not False             # True", "not 0                 # True", "not 'hello'           # False"],
    examplesFr: ["not True              # False", "not False             # True", "not 0                 # True", "not 'bonjour'         # False"],
    orderEn: ["1. Evaluates the truthiness of x", "2. Returns the boolean opposite"],
    orderFr: ["1. Evalue la veracite de x", "2. Retourne l'oppose booleen"],
    mistakesEn: ["not has lower precedence than == and <", "Use not in (two words) for membership negation, not ! operator like C"],
    mistakesFr: ["not a une precedence plus faible que == et <"],
  },
  "and": {
    name: "and",
    type: "keyword",
    signature: "a and b -> bool",
    descriptionEn: "Logical AND operator. Returns the first falsy value, or the last value if all are truthy. Short-circuits: if a is falsy, b is not evaluated.",
    descriptionFr: "Operateur logique ET. Retourne la premiere valeur fausse, ou la derniere valeur si toutes sont vraies.",
    returnType: "the first falsy value, or the last value",
    examplesEn: ["True and False        # False", "True and True         # True", "0 and 42              # 0 (short-circuits)", "42 and 'hello'        # 'hello'"],
    examplesFr: ["True and False        # False", "True and True         # True", "0 and 42              # 0 (court-circuit)", "42 and 'bonjour'      # 'bonjour'"],
    orderEn: ["1. Evaluates the left operand", "2. If left is falsy, returns left (short-circuit, right is NOT evaluated)", "3. If left is truthy, evaluates and returns the right operand"],
    orderFr: ["1. Evalue l'operande gauche", "2. Si gauche est faux, retourne gauche (court-circuit)", "3. Si gauche est vrai, evalue et retourne l'operande droite"],
    mistakesEn: ["and returns the actual value, not True/False", "Use and/or for conditional expressions: x = condition and value or default", "Precedence: and binds tighter than or"],
    mistakesFr: ["and retourne la valeur reelle, pas True/False"],
  },
  "or": {
    name: "or",
    type: "keyword",
    signature: "a or b -> bool",
    descriptionEn: "Logical OR operator. Returns the first truthy value, or the last value if all are falsy. Short-circuits: if a is truthy, b is not evaluated.",
    descriptionFr: "Operateur logique OU. Retourne la premiere valeur vraie, ou la derniere valeur si toutes sont fausses.",
    returnType: "the first truthy value, or the last value",
    examplesEn: ["True or False         # True", "False or True         # True", "42 or 0               # 42 (short-circuits)", "0 or '' or 'fallback' # 'fallback'"],
    examplesFr: ["True or False         # True", "False or True         # True", "42 or 0               # 42 (court-circuit)", "0 or '' or 'repli'   # 'repli'"],
    orderEn: ["1. Evaluates the left operand", "2. If left is truthy, returns left (short-circuit, right is NOT evaluated)", "3. If left is falsy, evaluates and returns the right operand"],
    orderFr: ["1. Evalue l'operande gauche", "2. Si gauche est vrai, retourne gauche (court-circuit)", "3. Si gauche est faux, evalue et retourne l'operande droite"],
    mistakesEn: ["or returns the actual value, not True/False", "Common pattern: name = input_name or 'default'", "Be careful with chained or: 0 or False or '' returns '' (all falsy)"],
    mistakesFr: ["or retourne la valeur reelle, pas True/False"],
  },
  "None": {
    name: "None",
    type: "constant",
    signature: "None",
    descriptionEn: "The null value in Python. Represents the absence of a value. None is a singleton (only one None exists) and is falsy.",
    descriptionFr: "La valeur nulle en Python. Represente l'absence de valeur. None est un singleton et est considere comme faux.",
    returnType: "NoneType",
    examplesEn: ["result = function_that_returns_nothing()  # None", "x = None\nif x is None: print('no value')  # use is, not =="],
    examplesFr: ["resultat = fonction_qui_ne_renvoie_rien()  # None", "x = None\nif x is None: print('pas de valeur')  # utilisez is"],
    orderEn: ["1. The Python runtime creates a single None object at startup", "2. Functions without a return statement return None implicitly", "3. None is the only instance of NoneType"],
    orderFr: ["1. Python cree un seul objet None au demarrage", "2. Les fonctions sans return retournent None implicitement", "3. None est la seule instance de NoneType"],
    mistakesEn: ["Always compare to None with is (not ==)", "None is falsy: bool(None) is False", "None can be assigned to (defeating the purpose) — avoid reassigning it"],
    mistakesFr: ["Comparez toujours None avec is (pas ==)"],
  },
  "True": {
    name: "True",
    type: "constant",
    signature: "True / False",
    descriptionEn: "The boolean True value. True == 1 (bool is a subclass of int). Can be used in numeric contexts.",
    descriptionFr: "La valeur booleenne True. True == 1 (bool est une sous-classe de int).",
    returnType: "bool",
    examplesEn: ["isinstance(True, int)  # True (bool is subclass of int)", "True + True  # 2"],
    examplesFr: ["isinstance(True, int)  # True (bool est sous-classe de int)", "True + True  # 2"],
    orderEn: ["1. True is a singleton", "2. It is the only value that satisfies True is True"],
    orderFr: ["1. True est un singleton", "2. C'est la seule valeur qui satisfait True is True"],
    mistakesEn: ["True is 1 (but don't rely on this — use bool for clarity)", "bool is a subclass of int — isinstance(True, int) is True"],
    mistakesFr: ["True est 1 (mais ne vous y fiez pas)"],
  },
  "False": {
    name: "False",
    type: "constant",
    signature: "False",
    descriptionEn: "The boolean False value. False == 0 (bool is a subclass of int).",
    descriptionFr: "La valeur booleenne False. False == 0 (bool est une sous-classe de int).",
    returnType: "bool",
    examplesEn: ["isinstance(False, int)  # True", "int(False)  # 0"],
    examplesFr: ["isinstance(False, int)  # True", "int(False)  # 0"],
    orderEn: ["1. False is a singleton", "2. It is falsy (bool(False) = False)"],
    orderFr: ["1. False est un singleton", "2. Il est faux (bool(False) = False)"],
    mistakesEn: ["False is 0 (but use is False for comparison)", "is and ==: False == 0 is True, False is 0 is False (different objects)"],
    mistakesFr: ["False est 0 (mais utilisez is False pour comparer)"],
  },
  "__init__": {
    name: "__init__",
    type: "dunder method",
    signature: "__init__(self, ...)",
    descriptionEn: "The instance initializer method. Called automatically after __new__() when an instance is created. Sets up initial state for the object.",
    descriptionFr: "La m\u00e9thode d\u2019initialisation d\u2019instance. Appel\u00e9e automatiquement apr\u00e8s __new__() lors de la cr\u00e9ation d\u2019une instance.",
    returnType: "None",
    examplesEn: ["class Person:\n    def __init__(self, name):\n        self.name = name\np = Person('Alice')  # calls __init__"],
    examplesFr: ["class Personne:\n    def __init__(self, nom):\n        self.nom = nom\np = Personne('Alice')"],
    orderEn: ["1. __new__() creates the raw instance", "2. __init__() is called with the instance and the constructor arguments"],
    orderFr: ["1. __new__() cr\u00e9e l\u2019instance brute", "2. __init__() est appel\u00e9e avec l\u2019instance et les arguments du constructeur"],
    mistakesEn: ["__init__ must return None (returning a value raises TypeError)", "__init__ is not the constructor (__new__ is). __init__ initializes, it does not allocate"],
    mistakesFr: ["__init__ doit retourner None (retourner une valeur l\u00e8ve TypeError)", "__init__ n\u2019est pas le constructeur (__new__ l\u2019est)"],
  },
  "__str__": {
    name: "__str__",
    type: "dunder method",
    signature: "__str__(self) -> str",
    descriptionEn: "Called by str(), print(), and format() to get an informal, human-readable string representation of an object.",
    descriptionFr: "Appel\u00e9e par str(), print() et format() pour obtenir une repr\u00e9sentation lisible pour un humain.",
    returnType: "str",
    examplesEn: ["class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __str__(self):\n        return f'({self.x}, {self.y})'\nprint(Point(1, 2))  # (1, 2)"],
    examplesFr: ["class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __str__(self):\n        return f'({self.x}, {self.y})'\nprint(Point(1, 2))  # (1, 2)"],
    orderEn: ["1. str(obj) or print(obj) calls obj.__str__()", "2. Falls back to __repr__() if __str__ is not defined"],
    orderFr: ["1. str(obj) ou print(obj) appelle obj.__str__()", "2. Utilise __repr__() si __str__ n\u2019est pas d\u00e9fini"],
    mistakesEn: ["__str__ must return a string object (not print it!)", "Use __repr__ for debugging/developer representation, __str__ for end-user display"],
    mistakesFr: ["__str__ doit retourner une cha\u00eene (pas l\u2019afficher !)", "Utilisez __repr__ pour le d\u00e9bogage, __str__ pour l\u2019affichage utilisateur"],
  },
  "__repr__": {
    name: "__repr__",
    type: "dunder method",
    signature: "__repr__(self) -> str",
    descriptionEn: "Called by repr() and the interactive interpreter. Should return an unambiguous, developer-friendly string, ideally one that recreates the object.",
    descriptionFr: "Appel\u00e9e par repr() et l\u2019interpr\u00e9teur interactif. Doit retourner une cha\u00eene non ambigu\u00eb qui id\u00e9alement recr\u00e9e l\u2019objet.",
    returnType: "str",
    examplesEn: ["class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __repr__(self):\n        return f'Point({self.x}, {self.y})'\np = Point(1, 2)\nrepr(p)  # \"Point(1, 2)\""],
    examplesFr: ["class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __repr__(self):\n        return f'Point({self.x}, {self.y})'\np = Point(1, 2)\nrepr(p)  # \"Point(1, 2)\""],
    orderEn: ["1. repr(obj) calls obj.__repr__()", "2. Falls back to the default implementation (class name + memory address)"],
    orderFr: ["1. repr(obj) appelle obj.__repr__()", "2. Utilise l'impl\u00e9mentation par d\u00e9faut (nom de classe + adresse m\u00e9moire)"],
    mistakesEn: ["If both __repr__ and __str__ are defined, __str__ takes priority in print/str, __repr__ in repr/interactive", "Without __repr__, the default shows <MyClass object at 0x...>"],
    mistakesFr: ["Si les deux sont d\u00e9finis, __str__ est prioritaire dans print/str, __repr__ dans l\u2019interpr\u00e9teur"],
  },
  "__len__": {
    name: "__len__",
    type: "dunder method",
    signature: "__len__(self) -> int",
    descriptionEn: "Called by len(obj). Returns the length (number of items) of a container object. Also used by bool() — if __len__ returns 0, the object is falsy.",
    descriptionFr: "Appel\u00e9e par len(obj). Retourne la longueur d\u2019un conteneur. Utilis\u00e9e aussi par bool() — si __len__ retourne 0, l\u2019objet est faux.",
    returnType: "int",
    examplesEn: ["class Team:\n    def __init__(self):\n        self.members = []\n    def __len__(self):\n        return len(self.members)\nteam = Team()\nlen(team)  # 0"],
    examplesFr: ["class Equipe:\n    def __init__(self):\n        self.membres = []\n    def __len__(self):\n        return len(self.membres)\ne = Equipe()\nlen(e)  # 0"],
    orderEn: ["1. len(obj) calls obj.__len__()", "2. If __len__ returns 0 and no __bool__ is defined, bool(obj) is False"],
    orderFr: ["1. len(obj) appelle obj.__len__()", "2. Si __len__ retourne 0 et que __bool__ n\u2019est pas d\u00e9fini, bool(obj) est False"],
    mistakesEn: ["__len__ must return a non-negative integer", "__len__ should be O(1), not O(n) — store the length, don\u2019t recompute it"],
    mistakesFr: ["__len__ doit retourner un entier positif ou nul"],
  },
  "__call__": {
    name: "__call__",
    type: "dunder method",
    signature: "__call__(self, ...) -> Any",
    descriptionEn: "Makes an instance callable like a function. Called when you use obj(...). Useful for creating function-like objects with state.",
    descriptionFr: "Rend une instance appelable comme une fonction. Appel\u00e9e quand vous utilisez obj(...). Utile pour cr\u00e9er des objets fonctionnels avec \u00e9tat.",
    returnType: "Any",
    examplesEn: ["class Counter:\n    def __init__(self):\n        self.n = 0\n    def __call__(self):\n        self.n += 1\n        return self.n\nc = Counter()\nc()  # 1\nc()  # 2"],
    examplesFr: ["class Compteur:\n    def __init__(self):\n        self.n = 0\n    def __call__(self):\n        self.n += 1\n        return self.n\nc = Compteur()\nc()  # 1\nc()  # 2"],
    orderEn: ["1. obj(args) calls type(obj).__call__(obj, args)", "2. Commonly used for decorators, currying, and function-like objects"],
    orderFr: ["1. obj(args) appelle type(obj).__call__(obj, args)", "2. Utilis\u00e9 pour les d\u00e9corateurs, le curryfication et les objets fonctionnels"],
    mistakesEn: ["__call__ can take any arguments (like a normal function)", "Functors (callable objects) are an alternative to closures"],
    mistakesFr: ["__call__ peut prendre n\u2019importe quels arguments"],
  },
  "__getitem__": {
    name: "__getitem__",
    type: "dunder method",
    signature: "__getitem__(self, key) -> Any",
    descriptionEn: "Called by self[key] indexing. Enables bracket access on custom objects. Also called for iteration if __iter__ is not defined.",
    descriptionFr: "Appel\u00e9e par self[key] (indexation). Permet l\u2019acc\u00e8s par crochets sur les objets personnalis\u00e9s.",
    returnType: "Any",
    examplesEn: ["class MyList:\n    def __init__(self, items):\n        self.items = items\n    def __getitem__(self, index):\n        return self.items[index]\nml = MyList([10, 20, 30])\nml[1]  # 20"],
    examplesFr: ["class MaListe:\n    def __init__(self, items):\n        self.items = items\n    def __getitem__(self, index):\n        return self.items[index]\nml = MaListe([10, 20, 30])\nml[1]  # 20"],
    orderEn: ["1. obj[key] calls type(obj).__getitem__(obj, key)", "2. Also enables iteration via for x in obj (if no __iter__)"],
    orderFr: ["1. obj[cl\u00e9] appelle type(obj).__getitem__(obj, cl\u00e9)", "2. Permet aussi l\u2019it\u00e9ration via for x in obj (si pas de __iter__)"],
    mistakesEn: ["__getitem__ with integer keys should raise IndexError for out-of-bounds", "__getitem__ with non-integer keys should raise KeyError if not found"],
    mistakesFr: ["__getitem__ avec des cl\u00e9s enti\u00e8res doit lever IndexError si hors limites"],
  },
  "__setitem__": {
    name: "__setitem__",
    type: "dunder method",
    signature: "__setitem__(self, key, value) -> None",
    descriptionEn: "Called by self[key] = value assignment. Enables item assignment on custom objects.",
    descriptionFr: "Appel\u00e9e par self[key] = valeur (assignation). Permet l\u2019assignation par index sur les objets personnalis\u00e9s.",
    returnType: "None",
    examplesEn: ["class MyDict:\n    def __init__(self):\n        self.data = {}\n    def __setitem__(self, key, value):\n        self.data[key] = value\nmd = MyDict()\nmd['a'] = 1"],
    examplesFr: ["class MonDict:\n    def __init__(self):\n        self.data = {}\n    def __setitem__(self, key, value):\n        self.data[key] = value\nmd = MonDict()\nmd['a'] = 1"],
    orderEn: ["1. obj[key] = value calls type(obj).__setitem__(obj, key, value)"],
    orderFr: ["1. obj[cl\u00e9] = valeur appelle type(obj).__setitem__(obj, cl\u00e9, valeur)"],
    mistakesEn: ["Missing __setitem__ while having __getitem__ makes the object read-only via brackets"],
    mistakesFr: ["L\u2019absence de __setitem__ avec __getitem__ rend l\u2019objet en lecture seule via les crochets"],
  },
  "__iter__": {
    name: "__iter__",
    type: "dunder method",
    signature: "__iter__(self) -> Iterator",
    descriptionEn: "Called by iter(obj) and for x in obj. Should return an iterator object (usually self for iterables). Part of the iterator protocol.",
    descriptionFr: "Appel\u00e9e par iter(obj) et for x in obj. Doit retourner un it\u00e9rateur (g\u00e9n\u00e9ralement self pour les it\u00e9rables).",
    returnType: "Iterator",
    examplesEn: ["class MyRange:\n    def __init__(self, n):\n        self.n = n\n    def __iter__(self):\n        self.i = 0\n        return self\n    def __next__(self):\n        if self.i >= self.n: raise StopIteration\n        val = self.i\n        self.i += 1\n        return val"],
    examplesFr: ["class MaRange:\n    def __init__(self, n):\n        self.n = n\n    def __iter__(self):\n        self.i = 0\n        return self\n    def __next__(self):\n        if self.i >= self.n: raise StopIteration\n        val = self.i\n        self.i += 1\n        return val"],
    orderEn: ["1. for x in obj calls iter(obj) which calls __iter__(obj)", "2. __iter__ should return an iterator object (with __next__)"],
    orderFr: ["1. for x in obj appelle iter(obj) qui appelle __iter__(obj)", "2. __iter__ doit retourner un it\u00e9rateur (avec __next__)"],
    mistakesEn: ["An iterable has __iter__ (returns iterator), an iterator has __iter__ (returns self) + __next__", "If __iter__ is not defined, Python falls back to __getitem__ with sequential integer keys"],
    mistakesFr: ["Un it\u00e9rable a __iter__, un it\u00e9rateur a __iter__ + __next__"],
  },
  "__next__": {
    name: "__next__",
    type: "dunder method",
    signature: "__next__(self) -> Any",
    descriptionEn: "Called by next(iterator). Returns the next item in the iteration. Raises StopIteration when there are no more items.",
    descriptionFr: "Appel\u00e9e par next(it\u00e9rateur). Retourne l\u2019\u00e9l\u00e9ment suivant. L\u00e8ve StopIteration quand il n\u2019y a plus d\u2019\u00e9l\u00e9ments.",
    returnType: "Any",
    examplesEn: ["class Counter:\n    def __init__(self, max):\n        self.n = 0\n        self.max = max\n    def __next__(self):\n        if self.n >= self.max: raise StopIteration\n        self.n += 1\n        return self.n"],
    examplesFr: ["class Compteur:\n    def __init__(self, max):\n        self.n = 0\n        self.max = max\n    def __next__(self):\n        if self.n >= self.max: raise StopIteration\n        self.n += 1\n        return self.n"],
    orderEn: ["1. next(iterator) calls iterator.__next__()", "2. for loops call __next__ internally until StopIteration is raised"],
    orderFr: ["1. next(it\u00e9rateur) appelle it\u00e9rateur.__next__()", "2. Les boucles for appellent __next__ jusqu\u2019\u00e0 StopIteration"],
    mistakesEn: ["__next__ must raise StopIteration (not return None) to signal completion", "A generator function automatically implements __next__"],
    mistakesFr: ["__next__ doit lever StopIteration (pas retourner None) pour signaler la fin"],
  },
  "__enter__": {
    name: "__enter__",
    type: "dunder method",
    signature: "__enter__(self) -> Any",
    descriptionEn: "Called when entering a with statement block. Sets up the context and returns the value bound to the as variable.",
    descriptionFr: "Appel\u00e9e \u00e0 l\u2019entr\u00e9e d\u2019un bloc with. Configure le contexte et retourne la valeur li\u00e9e \u00e0 la variable as.",
    returnType: "Any (typically self)",
    examplesEn: ["class File:\n    def __init__(self, name):\n        self.name = name\n    def __enter__(self):\n        print(f'Opening {self.name}')\n        return self\n    def __exit__(self, *args):\n        print(f'Closing {self.name}')\nwith File('test.txt') as f:\n    print('Working')"],
    examplesFr: ["class Fichier:\n    def __init__(self, nom):\n        self.nom = nom\n    def __enter__(self):\n        print(f'Ouverture de {self.nom}')\n        return self\n    def __exit__(self, *args):\n        print(f'Fermeture de {self.nom}')\nwith Fichier('test.txt') as f:\n    print('Travail')"],
    orderEn: ["1. The with expression is evaluated", "2. __enter__ is called on the context manager", "3. The return value is bound to the as variable", "4. The with block executes", "5. __exit__ is called (even if an exception occurred)"],
    orderFr: ["1. L\u2019expression with est \u00e9valu\u00e9e", "2. __enter__ est appel\u00e9e sur le gestionnaire", "3. La valeur retourn\u00e9e est li\u00e9e \u00e0 la variable as", "4. Le bloc with s\u2019ex\u00e9cute", "5. __exit__ est appel\u00e9e (m\u00eame en cas d\u2019exception)"],
    mistakesEn: ["Without __enter__/__exit__, the object cannot be used with with", "__enter__ should return the managed resource (often self)"],
    mistakesFr: ["Sans __enter__/__exit__, l\u2019objet ne peut pas \u00eatre utilis\u00e9 avec with"],
  },
  "__exit__": {
    name: "__exit__",
    type: "dunder method",
    signature: "__exit__(self, exc_type, exc_val, exc_tb) -> bool",
    descriptionEn: "Called when exiting a with statement block. Handles cleanup and optionally suppresses exceptions. Parameters are None / the exception info if an error occurred.",
    descriptionFr: "Appel\u00e9e \u00e0 la sortie d\u2019un bloc with. G\u00e8re le nettoyage et peut supprimer les exceptions si elle retourne True.",
    returnType: "bool (or None — implicit False)",
    examplesEn: ["class Manager:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if exc_type:\n            print(f'Error: {exc_val}')\n        return True  # suppress exception\nwith Manager():\n    1/0  # no crash"],
    examplesFr: ["class Gestionnaire:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if exc_type:\n            print(f'Erreur: {exc_val}')\n        return True  # supprime l'exception\nwith Gestionnaire():\n    1/0  # pas de crash"],
    orderEn: ["1. The with block finishes (or an exception occurs)", "2. __exit__ is called with exception info (or three Nones)", "3. If __exit__ returns True, any exception is suppressed"],
    orderFr: ["1. Le bloc with se termine (ou une exception survient)", "2. __exit__ est appel\u00e9e avec les infos d\u2019exception", "3. Si __exit__ retourne True, l\u2019exception est supprim\u00e9e"],
    mistakesEn: ["__exit__ swallowing all exceptions by returning True can hide bugs", "__exit__ is always called — even on return, break, or exception in the with block"],
    mistakesFr: ["__exit__ qui retourne True peut cacher des bugs", "__exit__ est toujours appel\u00e9e — m\u00eame sur return, break ou exception"],
  },
};


// Regex to detect any builtin name in a question
function builtinNameRegex(specs: Record<string, BuiltinSpec>): RegExp {
  const names = Object.keys(specs);
  // Sort by length descending so longer names match before shorter (e.g., "isinstance" before "is")
  const sorted = names.sort((a, b) => b.length - a.length).map(n => n.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
  return new RegExp(
    `(?:what\\s+(?:is|does|are|about)\\s+)?` +
    `(?:explain\\s+(?:to\\s+me\\s+)?)?` +
    `(?:can\\s+you\\s+(?:explain|tell\\s+me)\\s+)?` +
    `(?:how\\s+(?:does|do)\\s+)?` +
    `(?:the\\s+)?` +
    `(?:\\b(?:${sorted.join('|')})\\b)` +
    `(?:\\(\\))?` +
    `(?:\\s+(?:function|method|built.?in))?` +
    `(?:\\?)?$`,
    'i'
  );
}

// Common misspellings for built-in functions, keywords, and Python concepts
const BUILTIN_TYPOS: Record<string, string> = {
  "isintance": "isinstance",
  "isintances": "isinstance",
  "instace": "isinstance",
  "instaces": "isinstance",
  "isintence": "isinstance",
  "lenght": "len",
  "legnth": "len",
  "prnt": "print",
  "pritn": "print",
  "retrun": "return",
  "retruns": "return",
  "retruning": "return",
  "defintion": "definition",
  "definitoin": "definition",
  "funciton": "function",
  "funcitons": "function",
  "fucntion": "function",
  "dictonary": "dict",
  "dictonaries": "dict",
  "dicionary": "dict",
  "touple": "tuple",
  "touples": "tuple",
  "tupple": "tuple",
  "boollen": "bool",
  "booleen": "bool",
  "flaot": "float",
  "stirng": "str",
  "stirngs": "str",
  "integar": "int",
  "interger": "int",
  "variabel": "variable",
  "variabels": "variable",
  "enviroment": "environment",
  "inheritence": "inheritance",
  "inhertiance": "inheritance",
  "iterateable": "iterable",
  "iteratable": "iterable",
  "iteratore": "iterator",
  "generatore": "generator",
  "decoratore": "decorator",
  "contxt manager": "context manager",
  "comprehesion": "comprehension",
  "appened": "append",
  "apped": "append",
  "extendd": "extend",
  "remve": "remove",
  "delte": "delete",
  "sliice": "slice",
  "writen": "write",
  "writtn": "write",
  "perfomance": "performance",
  "optmize": "optimize",
  "concanate": "concatenate",
  "concatenate": "concatenate",
  "concatonate": "concatenate",
  "concanation": "concatenation",
  "concatenation": "concatenation",
  "capitilize": "capitalize",
  "capitilized": "capitalized",
  "capitilization": "capitalization",
  "cabability": "capability",
  "charecter": "character",
  "charecters": "character",
  "seperate": "separate",
  "seperator": "separator",
  "seperators": "separators",
  "recieve": "receive",
  "recieved": "received",
  "sqeuence": "sequence",
  "sequece": "sequence",
  "sequeces": "sequence",
  "squence": "sequence",
  "datatype": "type",
  "datatypes": "type",
  "pseudocode": "pseudo-code",
  "exeption": "exception",
  "exeptions": "exception",
  "excepton": "exception",
  "impliment": "implement",
  "implimentation": "implementation",
  "decendant": "descendant",
  "decendants": "descendants",
  "markdown": "markdown",
  "synax": "syntax",
  "syntx": "syntax",
  "syntatic": "syntactic",
  "semantec": "semantic",
  "semantecs": "semantics",
  "argumant": "argument",
  "argumants": "argument",
  "paramater": "parameter",
  "paramaters": "parameter",
  "parametr": "parameter",
  "paremeter": "parameter",
  "iterarion": "iteration",
  "iterations": "iteration",
  "recursive": "recursion",
  "recurtion": "recursion",
  "recurson": "recursion",
  "immutable": "immutable",
  "imutable": "immutable",
  "heriarchy": "hierarchy",
  "hierarcy": "hierarchy",
  "hierachy": "hierarchy",
};

const formatBuiltinSpec = (spec: BuiltinSpec, language: AdvancedAiLanguage, prefixLines?: string[]): string => {
  const fr = language === 'fr';
  const desc = fr ? spec.descriptionFr : spec.descriptionEn;
  const examples = fr ? spec.examplesFr : spec.examplesEn;
  const order = fr ? spec.orderFr : spec.orderEn;
  const mistakes = fr ? spec.mistakesFr : spec.mistakesEn;
  const parts = [
    ...(prefixLines || []),
    ...(prefixLines?.length ? [''] : []),
    `**${spec.name}()** — ${spec.signature}`,
    '',
    `**${fr ? 'Description' : 'Description'}**:`,
    desc,
    '',
    `**${fr ? 'Signature' : 'Signature'}**: \`${spec.signature}\``,
    '',
    `**${fr ? 'Valeur de retour' : 'Return type'}**: \`${spec.returnType}\``,
    '',
    `**${fr ? 'Ordre des operations' : 'Order of operations'}**:`,
    ...order.map((s: string, i: number) => `${i + 1}. ${s}`),
    '',
    `**${fr ? 'Exemples' : 'Examples'}**:`,
    '```python',
    ...examples,
    '```',
    '',
    `**${fr ? 'Erreurs frequentes' : 'Common mistakes'}**:`,
    ...mistakes.map((s: string) => `- ${s}`),
  ];
  return parts.join('\n');
};

// Fast exact-match lookup against any spec name (plain or with ())
const matchBuiltinExact = (text: string): [string, BuiltinSpec] | null => {
  for (const [name, spec] of Object.entries(BUILTIN_SPECS)) {
    if (text === name || text === `${name}()` || text === `${name}?`) {
      return [name, spec];
    }
  }
  return null;
};

export const answerPythonBuiltinQuery = (question: string, language: AdvancedAiLanguage): string | null => {
  const fr = language === 'fr';
  const lower = question.toLowerCase().trim();
  const cleaned = lower.replace(/[?!.]+$/g, '').trim();
  const stripped = cleaned.replace(/[()+]/g, '').trim();
  const bareMatch = stripped === cleaned ? null : stripped;

  // 1. Exact match against any spec name (bare word or with ())
  const exact = matchBuiltinExact(cleaned);
  if (exact) return formatBuiltinSpec(exact[1], language);

  // 2. Try extracting the last bare word from multi-word queries
  //    e.g., "what is dir" -> try "dir" and "what is dir"
  const words = cleaned.split(/\s+/);
  for (let i = words.length - 1; i >= 0; i--) {
    const candidate = words.slice(i).join(' ').replace(/[?!]+$/, '');
    const match = matchBuiltinExact(candidate) || matchBuiltinExact(`${candidate}()`);
    if (match) return formatBuiltinSpec(match[1], language);
  }

  // 3. Check for typo correction
  const typoInput = bareMatch || cleaned;
  if (BUILTIN_TYPOS[typoInput]) {
    const corrected = BUILTIN_TYPOS[typoInput];
    const spec = BUILTIN_SPECS[corrected];
    if (spec) {
      return formatBuiltinSpec(spec, language, [
        fr
          ? `**Correction probable**\nJ\u2019ai interpr\u00e9t\u00e9 \`${typoInput}\` comme \`${corrected}\`.`
          : `**Likely correction**\nI interpreted \`${typoInput}\` as \`${corrected}\`.`,
      ]);
    }
  }

  // 4. Regex pattern matching against all spec names
  const names = Object.keys(BUILTIN_SPECS).sort((a, b) => b.length - a.length);
  for (const name of names) {
    const patterns = [
      new RegExp(`what\\s+(?:is|are)\\s+(?:a\\s+|an\\s+)?${name}`, 'i'),
      new RegExp(`what\\s+does\\s+${name}\\s+do`, 'i'),
      new RegExp(`explain\\s+${name}`, 'i'),
      new RegExp(`how\\s+does\\s+${name}\\s+work`, 'i'),
      new RegExp(`tell\\s+me\\s+(?:about|how)\\s+${name}`, 'i'),
      new RegExp(`\\b${name}\\s+(?:function|keyword|method|build.?in)`, 'i'),
      new RegExp(`define\\s+${name}`, 'i'),
      new RegExp(`what\\s+means?\\s+${name}`, 'i'),
      new RegExp(`what\\s+${name}\\s+means?`, 'i'),
    ];

    let matched = false;
    for (const p of patterns) {
      if (p.test(lower)) { matched = true; break; }
    }
    if (matched) {
      const spec = BUILTIN_SPECS[name];
      if (spec) return formatBuiltinSpec(spec, language);
    }
  }
  return null;
};

// ---- Method specs ----

interface MethodSpec {
  name: string;
  type: string;
  signature: string;
  descriptionEn: string;
  descriptionFr: string;
  returnType: string;
  examplesEn: string[];
  examplesFr: string[];
  orderEn: string[];
  orderFr: string[];
  mistakesEn: string[];
  mistakesFr: string[];
}

const BUILTIN_METHOD_SPECS: Record<string, MethodSpec> = {
  "str.capitalize": {
    name: "str.capitalize",
    type: "method",
    signature: "str.capitalize()",
    descriptionEn: "Returns a copy of the string with its first character capitalized and the rest lowercased. Does not modify the original string.",
    descriptionFr: "Retourne une copie de la cha\u00eene avec la premi\u00e8re lettre en majuscule et le reste en minuscule. Ne modifie pas la cha\u00eene originale.",
    returnType: "str",
    examplesEn: ["'hello world'.capitalize()  # 'Hello world'"],
    examplesFr: ["'bonjour tout le monde'.capitalize()  # 'Bonjour tout le monde'"],
    orderEn: ["1. Take the first character of the string", "2. Convert it to uppercase via Unicode case-folding", "3. Convert all remaining characters to lowercase", "4. Return the resulting new string"],
    orderFr: ["1. Prendre le premier caract\u00e8re de la cha\u00eene", "2. Le convertir en majuscule", "3. Convertir tous les caract\u00e8res restants en minuscule", "4. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["capitalize() lowercases the REST of the string (unlike title())", "Only the very first character is uppercased; words after spaces are NOT capitalized", "Original string is never modified (strings are immutable)"],
    mistakesFr: ["capitalize() met le RESTE en minuscule (contrairement \u00e0 title())", "Seul le premier caract\u00e8re est mis en majuscule", "La cha\u00eene originale n'est jamais modifi\u00e9e"],
  },
  "str.upper": {
    name: "str.upper",
    type: "method",
    signature: "str.upper()",
    descriptionEn: "Returns a copy of the string with all cased characters converted to uppercase. Locale-independent (uses Unicode case mapping).",
    descriptionFr: "Retourne une copie de la cha\u00eene avec tous les caract\u00e8res en majuscule. Ind\u00e9pendant de la locale (utilise le mappage Unicode).",
    returnType: "str",
    examplesEn: ["'Hello World'.upper()  # 'HELLO WORLD'"],
    examplesFr: ["'Bonjour tout le monde'.upper()  # 'BONJOUR TOUT LE MONDE'"],
    orderEn: ["1. For each character in the string, look up its uppercase equivalent via Unicode case mapping", "2. Characters without an uppercase mapping (e.g., digits, symbols) pass through unchanged", "3. Return the new string"],
    orderFr: ["1. Pour chaque caract\u00e8re, chercher son \u00e9quivalent majuscule dans le mappage Unicode", "2. Les caract\u00e8res sans \u00e9quivalent majuscule (chiffres, symboles) restent inchang\u00e9s", "3. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["upper() does NOT modify in place (strings are immutable)", "upper() handles non-ASCII letters: '\\u00e9'.upper() == '\\u00c9'", "For case-insensitive comparison, use str.casefold() instead, which is more aggressive"],
    mistakesFr: ["upper() ne modifie PAS sur place (les cha\u00eenes sont immuables)", "upper() g\u00e8re les lettres non-ASCII", "Pour une comparaison insensible \u00e0 la casse, pr\u00e9f\u00e9rez str.casefold()"],
  },
  "str.lower": {
    name: "str.lower",
    type: "method",
    signature: "str.lower()",
    descriptionEn: "Returns a copy of the string with all cased characters converted to lowercase.",
    descriptionFr: "Retourne une copie de la cha\u00eene avec tous les caract\u00e8res en minuscule.",
    returnType: "str",
    examplesEn: ["'HELLO World'.lower()  # 'hello world'"],
    examplesFr: ["'BONJOUR TOUT LE MONDE'.lower()  # 'bonjour tout le monde'"],
    orderEn: ["1. For each character, look up its lowercase equivalent via Unicode case mapping", "2. Characters without a lowercase mapping pass through unchanged", "3. Return the new string"],
    orderFr: ["1. Pour chaque caract\u00e8re, chercher son \u00e9quivalent minuscule", "2. Les caract\u00e8res sans \u00e9quivalent restent inchang\u00e9s", "3. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["lower() returns a NEW string (strings are immutable)", "For aggressive case-folding (e.g., German '\u00df'), use str.casefold()"],
    mistakesFr: ["lower() retourne une NOUVELLE cha\u00eene", "Pour un pliage de casse agressif, utilisez str.casefold()"],
  },
  "str.split": {
    name: "str.split",
    type: "method",
    signature: "str.split(sep=None, maxsplit=-1)",
    descriptionEn: "Splits the string into a list of substrings using sep as the delimiter. If sep is None, splits on whitespace and discards empty strings. If maxsplit is given, at most maxsplit splits are performed.",
    descriptionFr: "Divise la cha\u00eene en une liste de sous-cha\u00eenes en utilisant sep comme d\u00e9limiteur. Si sep est None, divise sur les espaces et ignore les cha\u00eenes vides.",
    returnType: "list of str",
    examplesEn: ["'a b   c'.split()         # ['a', 'b', 'c']", "'a,b,c'.split(',')      # ['a', 'b', 'c']", "'a,b,c'.split(',', 1)   # ['a', 'b,c']"],
    examplesFr: ["'a b   c'.split()         # ['a', 'b', 'c']", "'a,b,c'.split(',')      # ['a', 'b', 'c']", "'a,b,c'.split(',', 1)   # ['a', 'b,c']"],
    orderEn: ["1. If sep is None (default), split on any whitespace sequence, discarding empty results", "2. If sep is a string, use it as the exact delimiter; consecutive delimiters produce empty strings", "3. If maxsplit > 0, stop after maxsplit splits (the last element contains the remainder)", "4. Return the list of substrings"],
    orderFr: ["1. Si sep est None (d\u00e9faut), diviser sur les espaces en ignorant les r\u00e9sultats vides", "2. Si sep est une cha\u00eene, l'utiliser comme d\u00e9limiteur exact", "3. Si maxsplit > 0, s'arr\u00eater apr\u00e8s maxsplit divisions", "4. Retourner la liste de sous-cha\u00eenes"],
    mistakesEn: ["split() with no arguments splits on ANY whitespace and discards empties; split(' ') splits on single spaces only", "split() without arguments treats leading/trailing whitespace differently from split(' ')", "The original string is never modified"],
    mistakesFr: ["split() sans argument divise sur TOUS les espaces ; split(' ') divise sur les espaces simples seulement"],
  },
  "str.join": {
    name: "str.join",
    type: "method",
    signature: "str.join(iterable)",
    descriptionEn: "Concatenates an iterable of strings using self as the separator between each element. The iterable must contain only strings.",
    descriptionFr: "Concat\u00e8ne un it\u00e9rable de cha\u00eenes en utilisant self comme s\u00e9parateur entre chaque \u00e9l\u00e9ment.",
    returnType: "str",
    examplesEn: ["','.join(['a', 'b', 'c'])  # 'a,b,c'", "' '.join(['hello', 'world'])  # 'hello world'", "''.join(['a', 'b', 'c'])     # 'abc'"],
    examplesFr: ["','.join(['a', 'b', 'c'])  # 'a,b,c'", "' '.join(['bonjour', 'monde'])  # 'bonjour monde'", "''.join(['a', 'b', 'c'])     # 'abc'"],
    orderEn: ["1. Create a new empty list for building the result", "2. Iterate over the iterable: append each element, then append self (except after the last element)", "3. Join the built list into a single string (efficient O(n) approach)", "4. Return the final string"],
    orderFr: ["1. Cr\u00e9er une nouvelle liste pour construire le r\u00e9sultat", "2. It\u00e9rer sur l'it\u00e9rable: ajouter chaque \u00e9l\u00e9ment, puis ajouter self (sauf apr\u00e8s le dernier)", "3. Joindre la liste en une seule cha\u00eene", "4. Retourner la cha\u00eene finale"],
    mistakesEn: ["join is called ON the separator, not on the list: separator.join(list)", "All elements must be strings; join will raise TypeError if any element is not a string", "join does NOT add trailing separator"],
    mistakesFr: ["join s'appelle SUR le s\u00e9parateur, pas sur la liste : s\u00e9parateur.join(liste)", "Tous les \u00e9l\u00e9ments doivent \u00eatre des cha\u00eenes"],
  },
  "str.strip": {
    name: "str.strip",
    type: "method",
    signature: "str.strip(chars=None)",
    descriptionEn: "Returns a copy of the string with leading and trailing characters removed. If chars is None, removes whitespace. If chars is given, removes any characters in that string (not a prefix/suffix match).",
    descriptionFr: "Retourne une copie de la cha\u00eene sans les caract\u00e8res de d\u00e9but et de fin. Si chars est None, supprime les espaces.",
    returnType: "str",
    examplesEn: ["'  hello  '.strip()        # 'hello'", "'...hello...'.strip('.')  # 'hello'", "'abchelloabc'.strip('abc') # 'hello'"],
    examplesFr: ["'  bonjour  '.strip()        # 'bonjour'", "'...bonjour...'.strip('.')  # 'bonjour'"],
    orderEn: ["1. If chars is None, strip all Unicode whitespace characters from both ends", "2. If chars is given, strip any character in chars from both ends until a non-matching char is found on each side", "3. Return the resulting string"],
    orderFr: ["1. Si chars est None, supprimer tous les espaces Unicode aux deux extr\u00e9mit\u00e9s", "2. Si chars est donn\u00e9, supprimer tout caract\u00e8re dans chars aux deux extr\u00e9mit\u00e9s", "3. Retourner la cha\u00eene r\u00e9sultante"],
    mistakesEn: ["strip() removes INDIVIDUAL characters, not a whole prefix/suffix string", "Use removeprefix()/removesuffix() (Python 3.9+) for exact prefix/suffix removal", "strip('abc') removes 'a', 'b', AND 'c' individually, not the substring 'abc'"],
    mistakesFr: ["strip() supprime des caract\u00e8res INDIVIDUELS, pas une cha\u00eene enti\u00e8re", "Utilisez removeprefix()/removesuffix() (Python 3.9+) pour une suppression exacte"],
  },
  "str.replace": {
    name: "str.replace",
    type: "method",
    signature: "str.replace(old, new, count=-1)",
    descriptionEn: "Returns a copy of the string with all occurrences of substring old replaced by new. If count is given, only the first count occurrences are replaced.",
    descriptionFr: "Retourne une copie de la cha\u00eene avec toutes les occurrences de old remplac\u00e9es par new. Si count est donn\u00e9, seules les premi\u00e8res count occurrences sont remplac\u00e9es.",
    returnType: "str",
    examplesEn: ["'hello world'.replace('world', 'Python')  # 'hello Python'", "'a,a,a'.replace('a', 'b', 2)  # 'b,b,a'"],
    examplesFr: ["'bonjour le monde'.replace('monde', 'Python')  # 'bonjour le Python'"],
    orderEn: ["1. Scan the string for non-overlapping occurrences of old", "2. For each occurrence (up to count), replace it with new", "3. If count is -1 (default), replace ALL occurrences", "4. Return the new string"],
    orderFr: ["1. Parcourir la cha\u00eene pour les occurrences non chevauchantes de old", "2. Pour chaque occurrence (jusqu'\u00e0 count), la remplacer par new", "3. Si count est -1 (d\u00e9faut), remplacer TOUTES les occurrences", "4. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["replace returns a new string (strings are immutable)", "replace does NOT support regex; use re.sub() for regex replacements", "replace replaces substrings, not individual characters (use str.translate() for that)"],
    mistakesFr: ["replace retourne une nouvelle cha\u00eene (les cha\u00eenes sont immuables)"],
  },
  "str.find": {
    name: "str.find",
    type: "method",
    signature: "str.find(sub, start=0, end=len(str))",
    descriptionEn: "Returns the lowest index where substring sub is found in the slice s[start:end]. Returns -1 if sub is not found. Use index() for an error-raising alternative.",
    descriptionFr: "Retourne l'indice le plus bas o\u00f9 la sous-cha\u00eene sub est trouv\u00e9e dans s[start:end]. Retourne -1 si sub n'est pas trouv\u00e9e.",
    returnType: "int",
    examplesEn: ["'hello world'.find('world')  # 6", "'hello world'.find('xyz')    # -1", "'hello hello'.find('hello', 3)  # 6"],
    examplesFr: ["'bonjour le monde'.find('monde')  # 12"],
    orderEn: ["1. Check the substring s[start:end]", "2. Scan left to right for the first occurrence of sub", "3. If found, return its start index", "4. If not found, return -1"],
    orderFr: ["1. Examiner la tranche s[start:end]", "2. Parcourir de gauche \u00e0 droite pour la premi\u00e8re occurrence de sub", "3. Si trouv\u00e9e, retourner son indice de d\u00e9but", "4. Si non trouv\u00e9e, retourner -1"],
    mistakesEn: ["str.find returns -1 (not an exception) when not found; use str.index() to raise ValueError", "find only finds the FIRST occurrence; use rfind() for the last", "find is case-sensitive; use lower() before find for case-insensitive search"],
    mistakesFr: ["str.find retourne -1 (pas une exception) si non trouv\u00e9"],
  },
  "str.index": {
    name: "str.index",
    type: "method",
    signature: "str.index(sub, start=0, end=len(str))",
    descriptionEn: "Like str.find() but raises ValueError if the substring is not found, instead of returning -1.",
    descriptionFr: "Comme str.find() mais l\u00e8ve ValueError si la sous-cha\u00eene n'est pas trouv\u00e9e.",
    returnType: "int",
    examplesEn: ["'hello world'.index('world')  # 6", "'hello world'.index('xyz')    # ValueError"],
    examplesFr: ["'bonjour monde'.index('monde')  # 8"],
    orderEn: ["1. Same search as find()", "2. If substring is found, return the start index", "3. If not found, raise ValueError instead of returning -1"],
    orderFr: ["1. M\u00eame recherche que find()", "2. Si trouv\u00e9e, retourner l'indice", "3. Si non trouv\u00e9e, lever ValueError"],
    mistakesEn: ["Uncaught ValueError from index() will crash your program; use find() if you want to test existence", "index() on an empty substring always returns 0 (empty string is found at index 0)"],
    mistakesFr: ["index() non attrap\u00e9e fera planter le programme"],
  },
  "str.startswith": {
    name: "str.startswith",
    type: "method",
    signature: "str.startswith(prefix, start=0, end=len(str))",
    descriptionEn: "Returns True if the string starts with the given prefix (or one of the prefixes in a tuple), within the optional start/end slice.",
    descriptionFr: "Retourne True si la cha\u00eene commence par le pr\u00e9fixe donn\u00e9 (ou l'un des pr\u00e9fixes dans un tuple).",
    returnType: "bool",
    examplesEn: ["'hello.py'.startswith('hello')  # True", "'hello.py'.startswith(('hello', 'bye'))  # True"],
    examplesFr: ["'bonjour.py'.startswith('bonjour')  # True"],
    orderEn: ["1. Slice the string using start/end if provided", "2. Compare the beginning of the sliced string with prefix", "3. If prefix is a tuple, check each element", "4. Return True if any matches, False otherwise"],
    orderFr: ["1. Trancher la cha\u00eene si start/end sont fournis", "2. Comparer le d\u00e9but avec prefix", "3. Si prefix est un tuple, v\u00e9rifier chaque \u00e9l\u00e9ment", "4. Retourner True si correspondance, False sinon"],
    mistakesEn: ["startswith accepts a TUPLE of prefixes, not a list (use tuple(prefixes))", "startswith with start/end slices the string virtually (does not create a new string)"],
    mistakesFr: ["startswith accepte un TUPLE de pr\u00e9fixes, pas une liste"],
  },
  "str.endswith": {
    name: "str.endswith",
    type: "method",
    signature: "str.endswith(suffix, start=0, end=len(str))",
    descriptionEn: "Returns True if the string ends with the given suffix (or one of the suffixes in a tuple), within the optional start/end slice.",
    descriptionFr: "Retourne True si la cha\u00eene se termine par le suffixe donn\u00e9 (ou l'un des suffixes dans un tuple).",
    returnType: "bool",
    examplesEn: ["'file.txt'.endswith('.txt')  # True", "'file.txt'.endswith(('.txt', '.md'))  # True"],
    examplesFr: ["'fichier.txt'.endswith('.txt')  # True"],
    orderEn: ["1. Slice the string using start/end if provided", "2. Compare the end of the sliced string with suffix", "3. If suffix is a tuple, check each element", "4. Return True if any matches, False otherwise"],
    orderFr: ["1. Trancher la cha\u00eene si start/end sont fournis", "2. Comparer la fin avec suffix", "3. Si suffix est un tuple, v\u00e9rifier chaque \u00e9l\u00e9ment", "4. Retourner True si correspondance, False sinon"],
    mistakesEn: ["endswith accepts a TUPLE of suffixes, not a list", "Checking file extension with endswith('.py') is case-sensitive on Linux"],
    mistakesFr: ["endswith accepte un TUPLE de suffixes, pas une liste"],
  },
  "list.append": {
    name: "list.append",
    type: "method",
    signature: "list.append(x)",
    descriptionEn: "Adds item x to the end of the list. Modifies the list in place and returns None (not the modified list).",
    descriptionFr: "Ajoute l'\u00e9l\u00e9ment x \u00e0 la fin de la liste. Modifie la liste sur place et retourne None.",
    returnType: "None",
    examplesEn: ["nums = [1, 2]\nnums.append(3)\nprint(nums)  # [1, 2, 3]"],
    examplesFr: ["nombres = [1, 2]\nnombres.append(3)\nprint(nombres)  # [1, 2, 3]"],
    orderEn: ["1. Add x as the last element of the list", "2. The list grows by one slot (amortized O(1), occasional resize)", "3. Return None"],
    orderFr: ["1. Ajouter x comme dernier \u00e9l\u00e9ment de la liste", "2. La liste grandit d'un emplacement (O(1) amorti)", "3. Retourner None"],
    mistakesEn: ["append returns None, NOT the modified list (common beginner mistake: my_list = my_list.append(x))", "append adds ONE element; use extend() to add multiple elements from an iterable", "append does NOT create a new list — it mutates in place"],
    mistakesFr: ["append retourne None, PAS la liste modifi\u00e9e", "append ajoute UN \u00e9l\u00e9ment; utilisez extend() pour plusieurs"],
  },
  "list.extend": {
    name: "list.extend",
    type: "method",
    signature: "list.extend(iterable)",
    descriptionEn: "Extends the list by appending all elements from the iterable. Modifies in place and returns None.",
    descriptionFr: "\u00c9tend la liste en ajoutant tous les \u00e9l\u00e9ments de l'it\u00e9rable. Modifie sur place et retourne None.",
    returnType: "None",
    examplesEn: ["nums = [1, 2]\nnums.extend([3, 4])\nprint(nums)  # [1, 2, 3, 4]"],
    examplesFr: ["nombres = [1, 2]\nnombres.extend([3, 4])\nprint(nombres)  # [1, 2, 3, 4]"],
    orderEn: ["1. Iterate over the provided iterable", "2. Append each element to the end of the list (in order)", "3. Return None"],
    orderFr: ["1. It\u00e9rer sur l'it\u00e9rable fourni", "2. Ajouter chaque \u00e9l\u00e9ment \u00e0 la fin de la liste", "3. Retourner None"],
    mistakesEn: ["extend mutates in place and returns None (like append)", "extend expects an iterable; passing a string extends with characters, not the string itself", "extend is different from + which creates a new list"],
    mistakesFr: ["extend modifie sur place et retourne None", "extend attend un it\u00e9rable; passer une cha\u00eene ajoute les caract\u00e8res, pas la cha\u00eene"],
  },
  "list.pop": {
    name: "list.pop",
    type: "method",
    signature: "list.pop(index=-1)",
    descriptionEn: "Removes and returns the item at the given index. If no index is given, removes and returns the last item. Raises IndexError if the list is empty or index is out of range.",
    descriptionFr: "Supprime et retourne l'\u00e9l\u00e9ment \u00e0 l'indice donn\u00e9. Sans indice, supprime et retourne le dernier \u00e9l\u00e9ment. L\u00e8ve IndexError si la liste est vide.",
    returnType: "Any (the removed element)",
    examplesEn: ["nums = [10, 20, 30]\nlast = nums.pop()\nprint(last)      # 30\nprint(nums)      # [10, 20]"],
    examplesFr: ["nombres = [10, 20, 30]\nder = nombres.pop()\nprint(der)       # 30\nprint(nombres)   # [10, 20]"],
    orderEn: ["1. Check that the index is valid (within bounds)", "2. Save the item at that index", "3. Remove the item from the list (shift subsequent elements left)", "4. Return the saved item"],
    orderFr: ["1. V\u00e9rifier que l'indice est valide", "2. Sauvegarder l'\u00e9l\u00e9ment \u00e0 cet indice", "3. Supprimer l'\u00e9l\u00e9ment (d\u00e9caler les suivants vers la gauche)", "4. Retourner l'\u00e9l\u00e9ment sauvegard\u00e9"],
    mistakesEn: ["pop on an empty list raises IndexError (check len(list) > 0 first)", "pop(0) is O(n) because all following elements shift left; collections.deque is better for popping from the front", "pop with no argument pops the LAST element (like a stack)"],
    mistakesFr: ["pop sur une liste vide l\u00e8ve IndexError", "pop(0) est O(n); utilisez collections.deque pour la file d'attente"],
  },
  "list.remove": {
    name: "list.remove",
    type: "method",
    signature: "list.remove(x)",
    descriptionEn: "Removes the first occurrence of value x from the list. Raises ValueError if x is not found. Modifies in place and returns None.",
    descriptionFr: "Supprime la premi\u00e8re occurrence de la valeur x de la liste. L\u00e8ve ValueError si x n'est pas trouv\u00e9.",
    returnType: "None",
    examplesEn: ["nums = [1, 2, 3, 2]\nnums.remove(2)\nprint(nums)  # [1, 3, 2]"],
    examplesFr: ["nombres = [1, 2, 3, 2]\nnombres.remove(2)\nprint(nombres)  # [1, 3, 2]"],
    orderEn: ["1. Scan the list from left to right for an element equal to x (using ==)", "2. If found, remove it (shift subsequent elements left) and return None", "3. If not found, raise ValueError"],
    orderFr: ["1. Parcourir la liste de gauche \u00e0 droite pour un \u00e9l\u00e9ment \u00e9gal \u00e0 x", "2. Si trouv\u00e9, le supprimer et retourner None", "3. Si non trouv\u00e9, lever ValueError"],
    mistakesEn: ["remove only removes the FIRST occurrence (not all of them)", "remove mutates the list in place and returns None", "remove compares by value (==), not by identity (is)"],
    mistakesFr: ["remove supprime seulement la PREMI\u00c8RE occurrence"],
  },
  "list.sort": {
    name: "list.sort",
    type: "method",
    signature: "list.sort(*, key=None, reverse=False)",
    descriptionEn: "Sorts the list in place. Uses Python's Timsort algorithm. Returns None. The key parameter specifies a function of one argument used to extract comparison keys.",
    descriptionFr: "Trie la liste sur place. Utilise l'algorithme Timsort de Python. Retourne None.",
    returnType: "None",
    examplesEn: ["nums = [3, 1, 2]\nnums.sort()\nprint(nums)       # [1, 2, 3]", "words = ['aa', 'b', 'ccc']\nwords.sort(key=len)\nprint(words)  # ['b', 'aa', 'ccc']"],
    examplesFr: ["nombres = [3, 1, 2]\nnombres.sort()\nprint(nombres)  # [1, 2, 3]"],
    orderEn: ["1. Timsort checks for pre-existing sorted runs in the data (best case O(n))", "2. Merge sorted runs using a stable merge sort", "3. If key is provided, compute the key for each element once (Schwartzian transform)", "4. If reverse=True, reverse the final sorted order", "5. Return None"],
    orderFr: ["1. Timsort v\u00e9rifie les s\u00e9quences tri\u00e9es existantes", "2. Fusionner les s\u00e9quences avec un tri stable", "3. Si key est fournie, calculer la cl\u00e9 une fois par \u00e9l\u00e9ment", "4. Si reverse=True, inverser l'ordre final", "5. Retourner None"],
    mistakesEn: ["list.sort() returns None, NOT the sorted list (use sorted() for a new list)", "list.sort() modifies the list in place; sorted() returns a new list", "list.sort() is stable: elements with equal keys maintain their original relative order"],
    mistakesFr: ["list.sort() retourne None, PAS la liste tri\u00e9e (utilisez sorted() pour une nouvelle liste)"],
  },
  "list.reverse": {
    name: "list.reverse",
    type: "method",
    signature: "list.reverse()",
    descriptionEn: "Reverses the list in place. Returns None. For a reversed copy or iterator, use reversed() or slicing [::-1].",
    descriptionFr: "Inverse la liste sur place. Retourne None. Pour une copie invers\u00e9e, utilisez reversed() ou le slicing [::-1].",
    returnType: "None",
    examplesEn: ["nums = [1, 2, 3]\nnums.reverse()\nprint(nums)  # [3, 2, 1]"],
    examplesFr: ["nombres = [1, 2, 3]\nnombres.reverse()\nprint(nombres)  # [3, 2, 1]"],
    orderEn: ["1. Swap elements pairwise from the ends toward the center", "2. Time complexity O(n)", "3. Return None"],
    orderFr: ["1. \u00c9changer les \u00e9l\u00e9ments par paires des extr\u00e9mit\u00e9s vers le centre", "2. Complexit\u00e9 temporelle O(n)", "3. Retourner None"],
    mistakesEn: ["list.reverse() returns None (not the reversed list)", "Use reversed(list) for an iterator or list[::-1] for a reversed copy", "reverse acts on the list in place"],
    mistakesFr: ["list.reverse() retourne None (pas la liste invers\u00e9e)"],
  },
  "list.insert": {
    name: "list.insert",
    type: "method",
    signature: "list.insert(index, x)",
    descriptionEn: "Inserts item x at the given index. Elements after index shift right. Modifies in place, returns None. If index >= len(list), x is appended.",
    descriptionFr: "Ins\u00e8re l'\u00e9l\u00e9ment x \u00e0 l'indice donn\u00e9. Les \u00e9l\u00e9ments apr\u00e8s index se d\u00e9calent vers la droite.",
    returnType: "None",
    examplesEn: ["nums = [1, 3]\nnums.insert(1, 2)\nprint(nums)  # [1, 2, 3]"],
    examplesFr: ["nombres = [1, 3]\nnombres.insert(1, 2)\nprint(nombres)  # [1, 2, 3]"],
    orderEn: ["1. Shift all elements from index to the end one position right", "2. Place x at the now-vacant index position", "3. Return None"],
    orderFr: ["1. D\u00e9caler tous les \u00e9l\u00e9ments de index \u00e0 la fin d'une position", "2. Placer x \u00e0 la position index", "3. Retourner None"],
    mistakesEn: ["insert(0, x) is O(n) (shifts the entire list right); use collections.deque for front insertion", "insert with an index >= len(list) appends to the end (same as append)", "insert returns None (common mistake: my_list = my_list.insert(0, x))"],
    mistakesFr: ["insert(0, x) est O(n); utilisez collections.deque pour l'insertion en t\u00eate"],
  },
  "list.count": {
    name: "list.count",
    type: "method",
    signature: "list.count(x)",
    descriptionEn: "Returns the number of times x appears in the list. Compares by value (==).",
    descriptionFr: "Retourne le nombre d'occurrences de x dans la liste. Compare par valeur (==).",
    returnType: "int",
    examplesEn: ["[1, 2, 2, 3].count(2)  # 2"],
    examplesFr: ["[1, 2, 2, 3].count(2)  # 2"],
    orderEn: ["1. Scan the list from left to right", "2. Count each element equal to x (using ==)", "3. Return the total count"],
    orderFr: ["1. Parcourir la liste de gauche \u00e0 droite", "2. Compter chaque \u00e9l\u00e9ment \u00e9gal \u00e0 x", "3. Retourner le total"],
    mistakesEn: ["list.count scans the entire list (O(n)); for repeated counting, use collections.Counter", "count compares by value (==), not identity (is)"],
    mistakesFr: ["list.count parcourt toute la liste (O(n))"],
  },
  "list.index": {
    name: "list.index",
    type: "method",
    signature: "list.index(x, start=0, end=len(list))",
    descriptionEn: "Returns the index of the first occurrence of x in the list (within optional start/end slice). Raises ValueError if not found.",
    descriptionFr: "Retourne l'indice de la premi\u00e8re occurrence de x dans la liste. L\u00e8ve ValueError si non trouv\u00e9.",
    returnType: "int",
    examplesEn: ["[10, 20, 30].index(20)  # 1"],
    examplesFr: ["[10, 20, 30].index(20)  # 1"],
    orderEn: ["1. Scan the slice list[start:end] from left to right", "2. Find the first element equal to x (using ==)", "3. Return its absolute index (not relative to start)", "4. If not found, raise ValueError"],
    orderFr: ["1. Parcourir la tranche list[start:end] de gauche \u00e0 droite", "2. Trouver le premier \u00e9l\u00e9ment \u00e9gal \u00e0 x", "3. Retourner l'indice absolu", "4. Si non trouv\u00e9, lever ValueError"],
    mistakesEn: ["list.index raises ValueError (not -1) if not found", "index scans the list (O(n)); for repeated lookups, consider a dict or set", "start and end slice the list VIRTUALLY (no copy created)"],
    mistakesFr: ["list.index l\u00e8ve ValueError (pas -1) si non trouv\u00e9"],
  },
  "list.clear": {
    name: "list.clear",
    type: "method",
    signature: "list.clear()",
    descriptionEn: "Removes all items from the list. Modifies in place and returns None. Equivalent to del list[:].",
    descriptionFr: "Supprime tous les \u00e9l\u00e9ments de la liste. Modifie sur place et retourne None.",
    returnType: "None",
    examplesEn: ["nums = [1, 2, 3]\nnums.clear()\nprint(nums)  # []"],
    examplesFr: ["nombres = [1, 2, 3]\nnombres.clear()\nprint(nombres)  # []"],
    orderEn: ["1. Remove all elements from the list", "2. The list becomes empty (length 0)", "3. Return None"],
    orderFr: ["1. Supprimer tous les \u00e9l\u00e9ments de la liste", "2. La liste devient vide", "3. Retourner None"],
    mistakesEn: ["list.clear() returns None (not [])", "Unlike reassignment (list = []), clear() affects all references to the same list object", "clear() is O(n) for the references, but the objects themselves are garbage-collected separately"],
    mistakesFr: ["list.clear() retourne None (pas [])"],
  },
  "list.copy": {
    name: "list.copy",
    type: "method",
    signature: "list.copy()",
    descriptionEn: "Returns a shallow copy of the list. Equivalent to list[:]. The new list contains references to the same objects as the original.",
    descriptionFr: "Retourne une copie superficielle de la liste. \u00c9quivalent \u00e0 list[:].",
    returnType: "list",
    examplesEn: ["nums = [1, 2, 3]\nnums2 = nums.copy()\nnums2.append(4)\nprint(nums)   # [1, 2, 3]\nprint(nums2)  # [1, 2, 3, 4]"],
    examplesFr: ["nombres = [1, 2, 3]\ncopie = nombres.copy()\ncopie.append(4)\nprint(nombres)  # [1, 2, 3]\nprint(copie)    # [1, 2, 3, 4]"],
    orderEn: ["1. Create a new list object", "2. Copy each reference from the original list to the new list (shallow copy)", "3. Return the new list"],
    orderFr: ["1. Cr\u00e9er un nouvel objet liste", "2. Copier chaque r\u00e9f\u00e9rence de la liste originale dans la nouvelle", "3. Retourner la nouvelle liste"],
    mistakesEn: ["copy() is a SHALLOW copy: nested objects are shared, not cloned", "For deep copying of nested structures, use copy.deepcopy()", "Simply assigning (list2 = list1) does NOT create a copy (same object)"],
    mistakesFr: ["copy() est une copie SUPERFICIELLE: les objets imbriqu\u00e9s sont partag\u00e9s"],
  },
  "dict.keys": {
    name: "dict.keys",
    type: "method",
    signature: "dict.keys()",
    descriptionEn: "Returns a dynamic view object of the dictionary's keys. The view reflects changes to the dictionary. Use list() to get a static list.",
    descriptionFr: "Retourne une vue dynamique des cl\u00e9s du dictionnaire. La vue refl\u00e8te les modifications. Utilisez list() pour une liste statique.",
    returnType: "dict_keys (view)",
    examplesEn: ["d = {'a': 1, 'b': 2}\nlist(d.keys())  # ['a', 'b']"],
    examplesFr: ["d = {'a': 1, 'b': 2}\nlist(d.keys())  # ['a', 'b']"],
    orderEn: ["1. Return a dict_keys view that dynamically reflects the current keys", "2. The view supports iteration, membership testing (in), and len()", "3. Convert to list() if you need a static snapshot"],
    orderFr: ["1. Retourner une vue dict_keys qui refl\u00e8te dynamiquement les cl\u00e9s", "2. La vue supporte l'it\u00e9ration, le test d'appartenance et len()", "3. Convertir avec list() pour un instantan\u00e9 statique"],
    mistakesEn: ["dict.keys() returns a VIEW, not a list; it's dynamic", "Iterating directly over a dict (for key in dict) is equivalent to dict.keys()", "In Python 2, dict.keys() returned a list; in Python 3, it returns a view"],
    mistakesFr: ["dict.keys() retourne une VUE, pas une liste"],
  },
  "dict.values": {
    name: "dict.values",
    type: "method",
    signature: "dict.values()",
    descriptionEn: "Returns a dynamic view object of the dictionary's values. The view reflects changes to the dictionary.",
    descriptionFr: "Retourne une vue dynamique des valeurs du dictionnaire. La vue refl\u00e8te les modifications.",
    returnType: "dict_values (view)",
    examplesEn: ["d = {'a': 1, 'b': 2}\nlist(d.values())  # [1, 2]"],
    examplesFr: ["d = {'a': 1, 'b': 2}\nlist(d.values())  # [1, 2]"],
    orderEn: ["1. Return a dict_values view over the current values", "2. Supports iteration, membership (in), len(), but NOT indexing"],
    orderFr: ["1. Retourner une vue dict_values sur les valeurs actuelles", "2. Supporte l'it\u00e9ration, l'appartenance, len(), mais PAS l'indexation"],
    mistakesEn: ["Values view does NOT support indexing (use list(dict.values())[0] instead)", "Values are not guaranteed to be unique (unlike keys)", "The view is dynamic; convert to list() for a snapshot"],
    mistakesFr: ["La vue values ne supporte PAS l'indexation"],
  },
  "dict.items": {
    name: "dict.items",
    type: "method",
    signature: "dict.items()",
    descriptionEn: "Returns a dynamic view of (key, value) pairs as 2-tuples. The most common way to iterate over a dictionary.",
    descriptionFr: "Retourne une vue dynamique des paires (cl\u00e9, valeur) sous forme de 2-uplets.",
    returnType: "dict_items (view of tuples)",
    examplesEn: ["d = {'a': 1, 'b': 2}\nfor k, v in d.items():\n    print(k, v)\n# a 1\n# b 2"],
    examplesFr: ["d = {'a': 1, 'b': 2}\nfor k, v in d.items():\n    print(k, v)\n# a 1\n# b 2"],
    orderEn: ["1. Return a dict_items view of (key, value) pairs", "2. The order matches insertion order (Python 3.7+)"],
    orderFr: ["1. Retourner une vue dict_items des paires (cl\u00e9, valeur)", "2. L'ordre correspond \u00e0 l'ordre d'insertion (Python 3.7+)"],
    mistakesEn: ["In Python 2, iteritems() was used instead of items()", "items() returns a VIEW, not a list", "Modifying the dict while iterating over items() can raise RuntimeError"],
    mistakesFr: ["items() retourne une VUE, pas une liste"],
  },
  "dict.get": {
    name: "dict.get",
    type: "method",
    signature: "dict.get(key, default=None)",
    descriptionEn: "Returns the value for key if it exists, otherwise returns default (no KeyError raised). Safe alternative to bracket access.",
    descriptionFr: "Retourne la valeur pour la cl\u00e9 si elle existe, sinon retourne default (pas de KeyError). Alternative s\u00e9curis\u00e9e \u00e0 l'acc\u00e8s par crochets.",
    returnType: "Any (or default if key not found)",
    examplesEn: ["d = {'a': 1}\nd.get('a')        # 1\nd.get('b')        # None (no KeyError)\nd.get('b', 0)     # 0"],
    examplesFr: ["d = {'a': 1}\nd.get('a')        # 1\nd.get('b')        # None (pas de KeyError)\nd.get('b', 0)     # 0"],
    orderEn: ["1. Check if key exists in the dictionary", "2. If yes, return dict[key]", "3. If no, return default (None if not specified)"],
    orderFr: ["1. V\u00e9rifier si la cl\u00e9 existe dans le dictionnaire", "2. Si oui, retourner dict[cl\u00e9]", "3. Si non, retourner default (None si non sp\u00e9cifi\u00e9)"],
    mistakesEn: ["get() NEVER raises KeyError (that's the whole point)", "Default is None, not an empty string or 0", "get() does NOT add the key to the dict (use setdefault() for that)"],
    mistakesFr: ["get() ne l\u00e8ve JAMAIS KeyError (c'est le but)"],
  },
  "dict.setdefault": {
    name: "dict.setdefault",
    type: "method",
    signature: "dict.setdefault(key, default=None)",
    descriptionEn: "If key is in the dictionary, returns its value. If not, inserts key with default and returns default. Useful for initializing nested structures.",
    descriptionFr: "Si la cl\u00e9 existe, retourne sa valeur. Sinon, ins\u00e8re la cl\u00e9 avec default et retourne default.",
    returnType: "Any (existing or default value)",
    examplesEn: ["d = {}\nd.setdefault('count', 0)  # 0 (inserts 'count': 0)\nd.setdefault('count', 5)  # 0 (already exists)"],
    examplesFr: ["d = {}\nd.setdefault('count', 0)  # 0 (ins\u00e8re 'count': 0)\nd.setdefault('count', 5)  # 0 (existe d\u00e9j\u00e0)"],
    orderEn: ["1. Check if key exists in the dictionary", "2. If yes, return dict[key] (do NOT modify)", "3. If no, insert dict[key] = default, then return default"],
    orderFr: ["1. V\u00e9rifier si la cl\u00e9 existe", "2. Si oui, retourner dict[cl\u00e9] (ne pas modifier)", "3. Si non, ins\u00e9rer dict[cl\u00e9] = default, retourner default"],
    mistakesEn: ["Unlike get(), setdefault() MUTATES the dict when the key is missing", "default is always evaluated (even if key exists); use defaultdict or a conditional for expensive defaults", "setdefault is often better replaced by collections.defaultdict"],
    mistakesFr: ["Contrairement \u00e0 get(), setdefault() MODIFIE le dict si la cl\u00e9 manque"],
  },
  "dict.pop": {
    name: "dict.pop",
    type: "method",
    signature: "dict.pop(key, default=<no default>)",
    descriptionEn: "Removes the key and returns its value. If key is not found, returns default if provided, otherwise raises KeyError.",
    descriptionFr: "Supprime la cl\u00e9 et retourne sa valeur. Si la cl\u00e9 n'existe pas, retourne default si fourni, sinon l\u00e8ve KeyError.",
    returnType: "Any (the removed value)",
    examplesEn: ["d = {'a': 1, 'b': 2}\nd.pop('a')     # 1 (d becomes {'b': 2})\nd.pop('z', -1)  # -1 (no KeyError)"],
    examplesFr: ["d = {'a': 1, 'b': 2}\nd.pop('a')     # 1 (d devient {'b': 2})\nd.pop('z', -1)  # -1"],
    orderEn: ["1. Check if key exists in the dictionary", "2. If yes, remove the key-value pair and return the value", "3. If no: if default provided, return default; otherwise raise KeyError"],
    orderFr: ["1. V\u00e9rifier si la cl\u00e9 existe", "2. Si oui, supprimer et retourner la valeur", "3. Si non: si default fourni, retourner default; sinon lever KeyError"],
    mistakesEn: ["dict.pop with NO default raises KeyError for missing keys", "Unlike list.pop(), dict.pop() requires a key argument"],
    mistakesFr: ["dict.pop SANS default l\u00e8ve KeyError pour les cl\u00e9s manquantes"],
  },
  "dict.update": {
    name: "dict.update",
    type: "method",
    signature: "dict.update(other_dict_or_iterable)",
    descriptionEn: "Updates the dictionary with key-value pairs from other, overwriting existing keys. Accepts another dict, an iterable of (key, value) pairs, or keyword arguments.",
    descriptionFr: "Met \u00e0 jour le dictionnaire avec les paires cl\u00e9-valeur de other, en \u00e9crasant les cl\u00e9s existantes.",
    returnType: "None",
    examplesEn: ["d = {'a': 1}\nd.update({'b': 2, 'a': 99})\nprint(d)  # {'a': 99, 'b': 2}"],
    examplesFr: ["d = {'a': 1}\nd.update({'b': 2, 'a': 99})\nprint(d)  # {'a': 99, 'b': 2}"],
    orderEn: ["1. Iterate over the provided key-value pairs", "2. For each (key, value), set dict[key] = value (overwrites existing keys)", "3. Return None"],
    orderFr: ["1. It\u00e9rer sur les paires cl\u00e9-valeur fournies", "2. Pour chaque (cl\u00e9, valeur), d\u00e9finir dict[cl\u00e9] = valeur", "3. Retourner None"],
    mistakesEn: ["update() mutates the dict IN PLACE and returns None", "update() can be called with keyword arguments: dict.update(a=1, b=2)", "update() overwrites existing keys (use setdefault to preserve)"],
    mistakesFr: ["update() modifie le dict SUR PLACE et retourne None"],
  },
  "dict.popitem": {
    name: "dict.popitem",
    type: "method",
    signature: "dict.popitem()",
    descriptionEn: "Removes and returns a (key, value) pair from the dictionary. In Python 3.7+, returns the most recently inserted pair (LIFO). Raises KeyError on an empty dict.",
    descriptionFr: "Supprime et retourne une paire (cl\u00e9, valeur) du dictionnaire. En Python 3.7+, retourne la paire la plus r\u00e9cemment ins\u00e9r\u00e9e (LIFO). L\u00e8ve KeyError sur un dict vide.",
    returnType: "tuple (key, value)",
    examplesEn: ["d = {'a': 1, 'b': 2}\nd.popitem()  # ('b', 2)  (most recently inserted)"],
    examplesFr: ["d = {'a': 1, 'b': 2}\nd.popitem()  # ('b', 2)"],
    orderEn: ["1. Check if dict is non-empty", "2. If empty, raise KeyError", "3. Remove and return the most recently inserted (key, value) pair (LIFO order, Python 3.7+)"],
    orderFr: ["1. V\u00e9rifier si le dict n'est pas vide", "2. Si vide, lever KeyError", "3. Supprimer et retourner la paire la plus r\u00e9cente (ordre LIFO)"],
    mistakesEn: ["popitem() on an empty dict raises KeyError", "Before Python 3.7, popitem() returned an ARBITRARY pair (not LIFO)", "popitem() is atomic (thread-safe) for individual calls"],
    mistakesFr: ["popitem() sur un dict vide l\u00e8ve KeyError"],
  },
  "dict.clear": {
    name: "dict.clear",
    type: "method",
    signature: "dict.clear()",
    descriptionEn: "Removes all items from the dictionary. Modifies in place and returns None. Affects all references to the same dict object.",
    descriptionFr: "Supprime tous les \u00e9l\u00e9ments du dictionnaire. Modifie sur place et retourne None.",
    returnType: "None",
    examplesEn: ["d = {'a': 1, 'b': 2}\nd.clear()\nprint(d)  # {}"],
    examplesFr: ["d = {'a': 1, 'b': 2}\nd.clear()\nprint(d)  # {}"],
    orderEn: ["1. Remove all key-value pairs from the dict", "2. The dict becomes empty (length 0)", "3. Return None"],
    orderFr: ["1. Supprimer toutes les paires cl\u00e9-valeur", "2. Le dict devient vide", "3. Retourner None"],
    mistakesEn: ["clear() returns None (not {})", "clear() affects ALL references to the dict object (unlike reassignment d = {})"],
    mistakesFr: ["clear() retourne None (pas {})"],
  },
  "dict.copy": {
    name: "dict.copy",
    type: "method",
    signature: "dict.copy()",
    descriptionEn: "Returns a shallow copy of the dictionary. The new dict contains the same key-value references as the original. Equivalent to dict(d).",
    descriptionFr: "Retourne une copie superficielle du dictionnaire. Le nouveau dict contient les m\u00eames r\u00e9f\u00e9rences cl\u00e9-valeur.",
    returnType: "dict",
    examplesEn: ["d = {'a': 1, 'b': 2}\nc = d.copy()\nc['a'] = 99\nprint(d)  # {'a': 1, 'b': 2}\nprint(c)  # {'a': 99, 'b': 2}"],
    examplesFr: ["d = {'a': 1, 'b': 2}\nc = d.copy()\nc['a'] = 99\nprint(d)  # {'a': 1, 'b': 2}\nprint(c)  # {'a': 99, 'b': 2}"],
    orderEn: ["1. Create a new empty dict", "2. For each (key, value) pair in the original, insert it into the new dict", "3. Return the new dict"],
    orderFr: ["1. Cr\u00e9er un nouveau dict vide", "2. Pour chaque paire (cl\u00e9, valeur) de l'original, l'ins\u00e9rer dans le nouveau", "3. Retourner le nouveau dict"],
    mistakesEn: ["copy() is SHALLOW: nested dicts/lists are shared, not cloned", "For deep copying of nested structures, use copy.deepcopy()"],
    mistakesFr: ["copy() est une copie SUPERFICIELLE: les dicts/listes imbriqu\u00e9s sont partag\u00e9s"],
  },
  "dict.fromkeys": {
    name: "dict.fromkeys",
    type: "method",
    signature: "dict.fromkeys(iterable, value=None)",
    descriptionEn: "Creates a new dictionary with keys from iterable and values set to value. All keys share the same value object (important for mutable defaults).",
    descriptionFr: "Cr\u00e9e un nouveau dictionnaire avec les cl\u00e9s de iterable et les valeurs d\u00e9finies \u00e0 value. Toutes les cl\u00e9s partagent le m\u00eame objet valeur.",
    returnType: "dict",
    examplesEn: ["dict.fromkeys(['a', 'b'], 0)  # {'a': 0, 'b': 0}"],
    examplesFr: ["dict.fromkeys(['a', 'b'], 0)  # {'a': 0, 'b': 0}"],
    orderEn: ["1. Create a new empty dict", "2. For each element in iterable, set dict[element] = value (all point to THE SAME value object)", "3. Return the new dict"],
    orderFr: ["1. Cr\u00e9er un nouveau dict vide", "2. Pour chaque \u00e9l\u00e9ment dans iterable, d\u00e9finir dict[\u00e9l\u00e9ment] = value", "3. Retourner le nouveau dict"],
    mistakesEn: ["All values reference THE SAME object; mutating one affects all: dict.fromkeys(keys, []) makes all keys share one list", "Use a dict comprehension for independent mutable values: {k: [] for k in keys}", "fromkeys is a class method (called on dict, not on an instance)"],
    mistakesFr: ["Toutes les valeurs r\u00e9f\u00e9rencent le M\u00caME objet; muter une affecte toutes les cl\u00e9s"],
  },
  "str.format": {
    name: "str.format",
    type: "method",
    signature: "str.format(*args, **kwargs)",
    descriptionEn: "Performs string formatting with positional and keyword arguments. Uses curly braces {} as replacement fields with optional format specifiers.",
    descriptionFr: "Effectue le formatage de cha\u00eene avec des arguments positionnels et nomm\u00e9s. Utilise des accolades {} comme champs de remplacement.",
    returnType: "str",
    examplesEn: ["'Hello, {}!'.format('world')  # 'Hello, world!'", "'{a} + {b} = {c}'.format(a=1, b=2, c=3)  # '1 + 2 = 3'"],
    examplesFr: ["'Bonjour, {}!'.format('monde')  # 'Bonjour, monde!'"],
    orderEn: ["1. Parse the template string for {} replacement fields", "2. Match positional fields to positional args, named fields to kwargs", "3. Apply any format specifiers (e.g., :.2f)", "4. Return the filled string"],
    orderFr: ["1. Analyser la cha\u00eene pour les champs {}", "2. Associer les champs positionnels aux args, les champs nomm\u00e9s aux kwargs", "3. Appliquer les sp\u00e9cificateurs de format", "4. Retourner la cha\u00eene remplie"],
    mistakesEn: ["format() can raise KeyError if a named field is missing a kwarg", "IndexError if a positional field exceeds the number of args", "For Python 3.6+, f-strings are faster and more readable than .format()"],
    mistakesFr: ["format() peut lever KeyError si un champ nomm\u00e9 manque"],
  },
  "str.casefold": {
    name: "str.casefold",
    type: "method",
    signature: "str.casefold()",
    descriptionEn: "Returns a casefolded copy of the string, suitable for caseless matching. More aggressive than lower(): handles Unicode characters like German \u00df (which casefolds to 'ss').",
    descriptionFr: "Retourne une copie pli\u00e9e de la cha\u00eene, adapt\u00e9e \u00e0 la correspondance insensible \u00e0 la casse. Plus agressif que lower().",
    returnType: "str",
    examplesEn: ["'Stra\u00dfe'.casefold()  # 'strasse'  (more aggressive than lower())"],
    examplesFr: ["'Stra\u00dfe'.casefold()  # 'strasse'"],
    orderEn: ["1. Apply Unicode case-folding rules (more aggressive than lower())", "2. Return the folded string"],
    orderFr: ["1. Appliquer les r\u00e8gles de pliage de casse Unicode", "2. Retourner la cha\u00eene pli\u00e9e"],
    mistakesEn: ["casefold() is NOT the same as lower() for all scripts (e.g., German \u00df, Greek sigma)", "Use casefold() for case-INSENSITIVE comparison, not lower()"],
    mistakesFr: ["casefold() n'est PAS la m\u00eame chose que lower() pour tous les alphabets"],
  },
  "str.count": {
    name: "str.count",
    type: "method",
    signature: "str.count(sub, start=0, end=len(str))",
    descriptionEn: "Returns the number of non-overlapping occurrences of substring sub in the slice s[start:end].",
    descriptionFr: "Retourne le nombre d'occurrences non chevauchantes de la sous-cha\u00eene sub dans la tranche s[start:end].",
    returnType: "int",
    examplesEn: ["'hello hello'.count('hello')  # 2", "'ababa'.count('aba')  # 1 (non-overlapping)"],
    examplesFr: ["'bonjour bonjour'.count('bonjour')  # 2"],
    orderEn: ["1. Scan the slice s[start:end] left to right", "2. Count non-overlapping matches of sub", "3. Return the count"],
    orderFr: ["1. Parcourir la tranche s[start:end] de gauche \u00e0 droite", "2. Compter les occurrences non chevauchantes", "3. Retourner le compte"],
    mistakesEn: ["count counts NON-OVERLAPPING matches (e.g., 'aaa'.count('aa') is 1, not 2)", "start/end slice the string virtually (no copy)"],
    mistakesFr: ["count compte les occurrences NON CHEVAUCHANTES"],
  },
  "str.encode": {
    name: "str.encode",
    type: "method",
    signature: "str.encode(encoding='utf-8', errors='strict')",
    descriptionEn: "Encodes the string to bytes using the specified encoding. Raises UnicodeEncodeError if the string cannot be encoded (unless errors is set to 'ignore' or 'replace').",
    descriptionFr: "Encode la cha\u00eene en octets avec l'encodage sp\u00e9cifi\u00e9. L\u00e8ve UnicodeEncodeError si l'encodage \u00e9choue.",
    returnType: "bytes",
    examplesEn: ["'hello'.encode()            # b'hello'", "'hello'.encode('utf-16')     # b'\\xff\\xfeh\\x00...'"],
    examplesFr: ["'bonjour'.encode()         # b'bonjour'"],
    orderEn: ["1. Convert each character to its byte representation using the given encoding", "2. If a character cannot be encoded: strict raises error, ignore skips it, replace uses ?", "3. Return the resulting bytes object"],
    orderFr: ["1. Convertir chaque caract\u00e8re en octets selon l'encodage", "2. Si un caract\u00e8re ne peut pas \u00eatre encod\u00e9: strict l\u00e8ve une erreur, ignore le saute, replace utilise ?", "3. Retourner les octets"],
    mistakesEn: ["encode() returns bytes, NOT a string", "Default encoding is UTF-8 (Python 3); Python 2 defaulted to ASCII", "errors='strict' is default and WILL raise UnicodeEncodeError for non-encodable characters"],
    mistakesFr: ["encode() retourne des octets, PAS une cha\u00eene"],
  },
  "str.expandtabs": {
    name: "str.expandtabs",
    type: "method",
    signature: "str.expandtabs(tabsize=8)",
    descriptionEn: "Returns a copy of the string where tab characters (\\t) are replaced with spaces, using tabsize spaces per tab (default 8). Tabs align to the next tab stop.",
    descriptionFr: "Retourne une copie o\u00f9 les tabulations (\\t) sont remplac\u00e9es par des espaces, en utilisant tabsize espaces (d\u00e9faut 8).",
    returnType: "str",
    examplesEn: ["'a\\tb'.expandtabs(4)   # 'a   b'", "'a\\tb\\tc'.expandtabs(4)  # 'a   b   c'"],
    examplesFr: ["'a\\tb'.expandtabs(4)   # 'a   b'"],
    orderEn: ["1. Scan the string for tab characters (\\t)", "2. For each tab, compute how many spaces until the next tab stop", "3. Tab stops occur every tabsize characters", "4. Replace the tab with the calculated number of spaces", "5. Return the new string"],
    orderFr: ["1. Parcourir la cha\u00eene pour les caract\u00e8res de tabulation", "2. Pour chaque tabulation, calculer le nombre d'espaces jusqu'au prochain taquet", "3. Les taquets sont espac\u00e9s de tabsize caract\u00e8res", "4. Remplacer la tabulation par les espaces", "5. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["expandtabs does NOT affect non-tab whitespace (spaces, newlines)", "The calculation considers characters before the tab as already consuming columns", "expandtabs does NOT handle backspace or carriage return for column counting"],
    mistakesFr: ["expandtabs n'affecte PAS les espaces non-tabulation"],
  },
  "str.lstrip": {
    name: "str.lstrip",
    type: "method",
    signature: "str.lstrip(chars=None)",
    descriptionEn: "Returns a copy of the string with leading characters removed. If chars is None, removes whitespace. Removes any character in chars, not a prefix string.",
    descriptionFr: "Retourne une copie sans les caract\u00e8res de d\u00e9but. Si chars est None, supprime les espaces.",
    returnType: "str",
    examplesEn: ["'  hello  '.lstrip()   # 'hello  '", "'xyzhello'.lstrip('xyz')  # 'hello'"],
    examplesFr: ["'  bonjour  '.lstrip()   # 'bonjour  '"],
    orderEn: ["1. Scan from the left, removing each character while it's in chars (or whitespace if chars is None)", "2. Stop at the first character NOT in chars", "3. Return the remaining string"],
    orderFr: ["1. Parcourir depuis la gauche en supprimant chaque caract\u00e8re dans chars", "2. S'arr\u00eater au premier caract\u00e8re PAS dans chars", "3. Retourner la cha\u00eene restante"],
    mistakesEn: ["lstrip removes INDIVIDUAL characters, not a prefix string", "lstrip('abc') removes 'a', 'b', 'c' individually if they appear at the start", "Original string is not modified (returns a new string)"],
    mistakesFr: ["lstrip supprime des caract\u00e8res INDIVIDUELS, pas un pr\u00e9fixe"],
  },
  "str.rstrip": {
    name: "str.rstrip",
    type: "method",
    signature: "str.rstrip(chars=None)",
    descriptionEn: "Returns a copy of the string with trailing characters removed. If chars is None, removes whitespace.",
    descriptionFr: "Retourne une copie sans les caract\u00e8res de fin. Si chars est None, supprime les espaces.",
    returnType: "str",
    examplesEn: ["'  hello  '.rstrip()   # '  hello'"],
    examplesFr: ["'  bonjour  '.rstrip()   # '  bonjour'"],
    orderEn: ["1. Scan from the right, removing characters while they're in chars", "2. Stop at the first character NOT in chars", "3. Return the remaining string"],
    orderFr: ["1. Parcourir depuis la droite en supprimant les caract\u00e8res dans chars", "2. S'arr\u00eater au premier caract\u00e8re PAS dans chars", "3. Retourner la cha\u00eene restante"],
    mistakesEn: ["rstrip removes INDIVIDUAL characters, not a suffix string", "Use removesuffix() (Python 3.9+) for exact suffix removal"],
    mistakesFr: ["rstrip supprime des caract\u00e8res INDIVIDUELS"],
  },
  "str.rsplit": {
    name: "str.rsplit",
    type: "method",
    signature: "str.rsplit(sep=None, maxsplit=-1)",
    descriptionEn: "Like split() but scans from the right. If maxsplit is given, splits from the right at most maxsplit times.",
    descriptionFr: "Comme split() mais parcourt depuis la droite. Si maxsplit est donn\u00e9, divise depuis la droite au plus maxsplit fois.",
    returnType: "list of str",
    examplesEn: ["'a,b,c'.rsplit(',', 1)  # ['a,b', 'c']"],
    examplesFr: ["'a,b,c'.rsplit(',', 1)  # ['a,b', 'c']"],
    orderEn: ["1. If sep is None, split on whitespace (same as split())", "2. If sep is given, split from the RIGHT, at most maxsplit times", "3. Return the list of substrings"],
    orderFr: ["1. Si sep est None, diviser sur les espaces (comme split())", "2. Si sep est donn\u00e9, diviser depuis la DROITE", "3. Retourner la liste"],
    mistakesEn: ["rsplit with no sep and maxsplit behaves the same as split()", "rsplit is useful for splitting on the last occurrence"],
    mistakesFr: ["rsplit sans s\u00e9parateur se comporte comme split()"],
  },
  "str.splitlines": {
    name: "str.splitlines",
    type: "method",
    signature: "str.splitlines(keepends=False)",
    descriptionEn: "Splits the string at line boundaries (\\n, \\r\\n, \\r, etc.). If keepends is True, the line break characters are included in each element.",
    descriptionFr: "Divise la cha\u00eene aux limites de ligne. Si keepends est True, les caract\u00e8res de saut de ligne sont inclus.",
    returnType: "list of str",
    examplesEn: ["'line1\\nline2\\n'.splitlines()      # ['line1', 'line2']", "'line1\\nline2\\n'.splitlines(True)  # ['line1\\n', 'line2\\n']"],
    examplesFr: ["'ligne1\\nligne2\\n'.splitlines()      # ['ligne1', 'ligne2']"],
    orderEn: ["1. Scan the string for Unicode line boundary characters", "2. Split at each boundary", "3. If keepends is True, retain the boundary characters in each element", "4. Return the list of lines"],
    orderFr: ["1. Parcourir la cha\u00eene pour les caract\u00e8res de fin de ligne", "2. Diviser \u00e0 chaque limite", "3. Si keepends est True, garder les caract\u00e8res de fin", "4. Retourner la liste"],
    mistakesEn: ["splitlines() removes TRAILING empty strings (unlike split('\\n'))", "splitlines() splits on more line boundaries than just \\n (e.g., \\v, \\f, \\x1c-\\x1e)"],
    mistakesFr: ["splitlines() supprime les cha\u00eenes vides finales"],
  },
  "str.title": {
    name: "str.title",
    type: "method",
    signature: "str.title()",
    descriptionEn: "Returns a titlecased version of the string: uppercase the first character of each word, lowercase the rest. Uses a language-independent algorithm.",
    descriptionFr: "Retourne une version o\u00f9 chaque mot commence par une majuscule, le reste en minuscule.",
    returnType: "str",
    examplesEn: ["'hello world'.title()  # 'Hello World'"],
    examplesFr: ["'bonjour tout le monde'.title()  # 'Bonjour Tout Le Monde'"],
    orderEn: ["1. Identify word boundaries (sequences of letters separated by non-letters)", "2. For each word: uppercase the first character, lowercase the rest", "3. Return the new string"],
    orderFr: ["1. Identifier les limites de mots", "2. Pour chaque mot: mettre la premi\u00e8re lettre en majuscule, le reste en minuscule", "3. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["title() also uppercases characters AFTER apostrophes (e.g., 'don't' -> 'Don'T')", "Use string.capwords() or regex for more accurate title case", "title() uses a simple Unicode algorithm, not locale-aware"],
    mistakesFr: ["title() met aussi en majuscule apr\u00e8s les apostrophes"],
  },
  "str.swapcase": {
    name: "str.swapcase",
    type: "method",
    signature: "str.swapcase()",
    descriptionEn: "Returns a copy of the string with uppercase characters converted to lowercase and vice versa.",
    descriptionFr: "Retourne une copie avec les majuscules converties en minuscules et vice versa.",
    returnType: "str",
    examplesEn: ["'Hello World'.swapcase()  # 'hELLO wORLD'"],
    examplesFr: ["'Bonjour le Monde'.swapcase()  # 'bONJOUR LE mONDE'"],
    orderEn: ["1. For each character, check its case", "2. If uppercase, convert to lowercase; if lowercase, convert to uppercase", "3. Return the new string"],
    orderFr: ["1. Pour chaque caract\u00e8re, v\u00e9rifier sa casse", "2. Majuscule -> minuscule, minuscule -> majuscule", "3. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["swapcase may not be symmetric for all Unicode characters (some have multiple case mappings)", "swapcase is rarely the right tool; consider upper(), lower(), or casefold() instead"],
    mistakesFr: ["swapcase peut ne pas \u00eatre sym\u00e9trique pour tous les caract\u00e8res Unicode"],
  },
  "str.zfill": {
    name: "str.zfill",
    type: "method",
    signature: "str.zfill(width)",
    descriptionEn: "Pads the string on the left with '0' digits to fill the specified width. If the string starts with a sign prefix (+/-), the zeros are inserted after the sign.",
    descriptionFr: "Remplit la cha\u00eene \u00e0 gauche avec des '0' pour atteindre la largeur sp\u00e9cifi\u00e9e.",
    returnType: "str",
    examplesEn: ["'42'.zfill(5)      # '00042'", "'-42'.zfill(5)     # '-0042'", "'abc'.zfill(5)    # '00abc'"],
    examplesFr: ["'42'.zfill(5)      # '00042'"],
    orderEn: ["1. Check if the string starts with + or -", "2. If yes, pad zeros between the sign and the rest", "3. If no, pad zeros at the beginning", "4. Return the new string"],
    orderFr: ["1. V\u00e9rifier si la cha\u00eene commence par + ou -", "2. Si oui, ajouter les z\u00e9ros entre le signe et le reste", "3. Si non, ajouter les z\u00e9ros au d\u00e9but", "4. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["zfill does NOT truncate if the string is longer than width", "zfill is different from rjust(5, '0') because of sign handling"],
    mistakesFr: ["zfill ne tronque PAS si la cha\u00eene est plus longue que width"],
  },
  "str.center": {
    name: "str.center",
    type: "method",
    signature: "str.center(width, fillchar=' ')",
    descriptionEn: "Returns a centered string of the specified width, padded on both sides with fillchar.",
    descriptionFr: "Retourne une cha\u00eene centr\u00e9e de la largeur sp\u00e9cifi\u00e9e, rembourr\u00e9e des deux c\u00f4t\u00e9s avec fillchar.",
    returnType: "str",
    examplesEn: ["'hello'.center(11)       # '   hello   '", "'hello'.center(11, '-')  # '---hello---'"],
    examplesFr: ["'bonjour'.center(15)     # '    bonjour    '"],
    orderEn: ["1. Compute left and right padding amounts (if odd width, left gets the extra space)", "2. Pad the string on both sides with fillchar", "3. Return the new string"],
    orderFr: ["1. Calculer le rembourrage gauche et droit", "2. Rembourrer des deux c\u00f4t\u00e9s avec fillchar", "3. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["center() will NOT truncate if the string is already longer than width", "fillchar must be exactly ONE character (or TypeError is raised)"],
    mistakesFr: ["center() ne tronque PAS si la cha\u00eene est d\u00e9j\u00e0 plus longue"],
  },
  "str.ljust": {
    name: "str.ljust",
    type: "method",
    signature: "str.ljust(width, fillchar=' ')",
    descriptionEn: "Returns the string left-justified in a string of the specified width, padded on the right with fillchar.",
    descriptionFr: "Retourne la cha\u00eene justifi\u00e9e \u00e0 gauche dans une cha\u00eene de la largeur sp\u00e9cifi\u00e9e.",
    returnType: "str",
    examplesEn: ["'hello'.ljust(8)       # 'hello   '"],
    examplesFr: ["'bonjour'.ljust(10)   # 'bonjour   '"],
    orderEn: ["1. If the string length >= width, return the string unchanged", "2. Otherwise, pad on the right with fillchar up to width", "3. Return the new string"],
    orderFr: ["1. Si la cha\u00eene a d\u00e9j\u00e0 la largeur, retourner inchang\u00e9e", "2. Sinon, rembourrer \u00e0 droite jusqu'\u00e0 width", "3. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["ljust does NOT truncate (unlike formatting specifiers)"],
    mistakesFr: ["ljust ne tronque PAS"],
  },
  "str.rjust": {
    name: "str.rjust",
    type: "method",
    signature: "str.rjust(width, fillchar=' ')",
    descriptionEn: "Returns the string right-justified in a string of the specified width, padded on the left with fillchar.",
    descriptionFr: "Retourne la cha\u00eene justifi\u00e9e \u00e0 droite dans une cha\u00eene de la largeur sp\u00e9cifi\u00e9e.",
    returnType: "str",
    examplesEn: ["'hello'.rjust(8)       # '   hello'"],
    examplesFr: ["'42'.rjust(5)         # '   42'"],
    orderEn: ["1. If the string length >= width, return unchanged", "2. Otherwise, pad on the left with fillchar up to width", "3. Return the new string"],
    orderFr: ["1. Si la cha\u00eene a d\u00e9j\u00e0 la largeur, retourner inchang\u00e9e", "2. Sinon, rembourrer \u00e0 gauche jusqu'\u00e0 width", "3. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["rjust does NOT truncate"],
    mistakesFr: ["rjust ne tronque PAS"],
  },
  "str.isalpha": {
    name: "str.isalpha",
    type: "method",
    signature: "str.isalpha()",
    descriptionEn: "Returns True if all characters in the string are alphabetic letters and the string is non-empty. False otherwise.",
    descriptionFr: "Retourne True si tous les caract\u00e8res sont alphab\u00e9tiques et non vides.",
    returnType: "bool",
    examplesEn: ["'hello'.isalpha()   # True", "'hello123'.isalpha()  # False", "''.isalpha()       # False"],
    examplesFr: ["'bonjour'.isalpha()   # True"],
    orderEn: ["1. If the string is empty, return False", "2. For each character, check if it is a Unicode letter (category L)", "3. If any character is NOT a letter, return False", "4. Return True"],
    orderFr: ["1. Si la cha\u00eene est vide, retourner False", "2. Pour chaque caract\u00e8re, v\u00e9rifier s'il s'agit d'une lettre", "3. Si un caract\u00e8re n'est PAS une lettre, retourner False", "4. Retourner True"],
    mistakesEn: ["isalpha() returns False for empty strings", "isalpha() returns True for non-English letters (e.g., '\u00e9', '\u4e2d')", "Spaces, digits, and punctuation return False"],
    mistakesFr: ["isalpha() retourne False pour les cha\u00eenes vides"],
  },
  "str.isdigit": {
    name: "str.isdigit",
    type: "method",
    signature: "str.isdigit()",
    descriptionEn: "Returns True if all characters are digits and the string is non-empty. Handles Unicode decimal digits like '\u00b2' (superscript 2).",
    descriptionFr: "Retourne True si tous les caract\u00e8res sont des chiffres et non vides.",
    returnType: "bool",
    examplesEn: ["'123'.isdigit()   # True", "'12.3'.isdigit()  # False (the dot is not a digit)", "'\u00b2'.isdigit()  # True (superscript 2)"],
    examplesFr: ["'123'.isdigit()   # True"],
    orderEn: ["1. If empty, return False", "2. Check each character with Unicode digit property", "3. Return True only if all are digits"],
    orderFr: ["1. Si vide, retourner False", "2. V\u00e9rifier chaque caract\u00e8re avec la propri\u00e9t\u00e9 Unicode chiffre", "3. Retourner True seulement si tous sont des chiffres"],
    mistakesEn: ["isdigit() returns True for Unicode superscripts like '\u00b2' but int() cannot parse them", "For numeric strings with decimals (e.g., '12.3'), use try/except with float(), not isdigit()", "Negative numbers ('-5') return False for isdigit()"],
    mistakesFr: ["isdigit() retourne True pour les exposants Unicode que int() ne peut pas analyser"],
  },
  "str.isdecimal": {
    name: "str.isdecimal",
    type: "method",
    signature: "str.isdecimal()",
    descriptionEn: "Returns True if all characters are decimal characters (0-9 and Unicode decimal digits) and the string is non-empty. Narrower than isdigit() — excludes superscripts, fractions, and Roman numerals.",
    descriptionFr: "Retourne True si tous les caract\u00e8res sont d\u00e9cimaux et non vides. Plus \u00e9troit que isdigit() — exclut exposants, fractions, chiffres romains.",
    returnType: "bool",
    examplesEn: ["'123'.isdecimal()   # True", "'\u00b2'.isdecimal()  # False (superscript)", "'\u00bd'.isdecimal()  # False (fraction)"],
    examplesFr: ["'123'.isdecimal()   # True", "'\u00b2'.isdecimal()  # False (exposant)", "'\u00bd'.isdecimal()  # False (fraction)"],
    orderEn: ["1. If empty, return False", "2. Check each character is a Unicode decimal digit (Nd category)", "3. Return True only if all are decimal digits"],
    orderFr: ["1. Si vide, retourner False", "2. V\u00e9rifier que chaque caract\u00e8re est un chiffre d\u00e9cimal Unicode (cat\u00e9gorie Nd)", "3. Retourner True seulement si tous sont d\u00e9cimaux"],
    mistakesEn: ["isdecimal() is the NARROWEST numeric check: isdecimal -> isdigit -> isnumeric (inclusive)", "int() can parse strings that pass isdecimal() (unlike isdigit/isnumeric for some Unicode)", "Negative numbers ('-5') and decimals ('12.3') return False"],
    mistakesFr: ["isdecimal() est le test num\u00e9rique le PLUS \u00c9TROIT: isdecimal -> isdigit -> isnumeric"],
  },
  "str.isnumeric": {
    name: "str.isnumeric",
    type: "method",
    signature: "str.isnumeric()",
    descriptionEn: "Returns True if all characters are numeric and the string is non-empty. Broader than isdigit() — includes fractions, Roman numerals, and other numeric characters.",
    descriptionFr: "Retourne True si tous les caract\u00e8res sont num\u00e9riques. Plus large que isdigit() — inclut fractions, chiffres romains.",
    returnType: "bool",
    examplesEn: ["'\u00bd'.isnumeric()  # True (fraction)", "'123'.isnumeric()  # True"],
    examplesFr: ["'\u00bd'.isnumeric()  # True"],
    orderEn: ["1. If empty, return False", "2. Check each character with Unicode numeric property", "3. Return True only if all are numeric"],
    orderFr: ["1. Si vide, retourner False", "2. V\u00e9rifier la propri\u00e9t\u00e9 num\u00e9rique Unicode", "3. Retourner True seulement si tous sont num\u00e9riques"],
    mistakesEn: ["isnumeric() is VERY broad: '\u00bd', '\u2169' (Roman numeral) are all True", "int() can fail on strings that pass isnumeric() (e.g., '\u00bd')"],
    mistakesFr: ["isnumeric() est TR\u00c8S large: '\u00bd' retourne True"],
  },
  "str.isalnum": {
    name: "str.isalnum",
    type: "method",
    signature: "str.isalnum()",
    descriptionEn: "Returns True if all characters are alphanumeric (letters or digits) and the string is non-empty. Equivalent to isalpha() or isdigit() or isnumeric() or isdecimal() for each character.",
    descriptionFr: "Retourne True si tous les caract\u00e8res sont alphanum\u00e9riques et non vides.",
    returnType: "bool",
    examplesEn: ["'abc123'.isalnum()  # True", "'abc 123'.isalnum()  # False (space)"],
    examplesFr: ["'abc123'.isalnum()  # True"],
    orderEn: ["1. If empty, return False", "2. Check each character is a letter, digit, or numeric character", "3. Return True only if all pass"],
    orderFr: ["1. Si vide, retourner False", "2. V\u00e9rifier que chaque caract\u00e8re est alphanum\u00e9rique", "3. Retourner True seulement si tous passent"],
    mistakesEn: ["isalnum() returns False for empty strings and strings with spaces/punctuation"],
    mistakesFr: ["isalnum() retourne False pour les cha\u00eenes vides ou avec espaces"],
  },
  "str.isspace": {
    name: "str.isspace",
    type: "method",
    signature: "str.isspace()",
    descriptionEn: "Returns True if all characters are whitespace characters and the string is non-empty.",
    descriptionFr: "Retourne True si tous les caract\u00e8res sont des espaces et non vides.",
    returnType: "bool",
    examplesEn: ["'   '.isspace()  # True", "'\\t\\n'.isspace()  # True", "''.isspace()     # False"],
    examplesFr: ["'   '.isspace()  # True"],
    orderEn: ["1. If empty, return False", "2. Check each character is Unicode whitespace", "3. Return True only if all are whitespace"],
    orderFr: ["1. Si vide, retourner False", "2. V\u00e9rifier que chaque caract\u00e8re est un espace", "3. Retourner True seulement si tous sont des espaces"],
    mistakesEn: ["''.isspace() returns False (empty string)", "isspace() is True for ALL Unicode whitespace, including non-breaking space and thin space"],
    mistakesFr: ["''.isspace() retourne False"],
  },
  "str.isprintable": {
    name: "str.isprintable",
    type: "method",
    signature: "str.isprintable()",
    descriptionEn: "Returns True if all characters in the string are printable (or the string is empty). Non-printable characters include control characters like \\n, \\r, \\t, and surrogates.",
    descriptionFr: "Retourne True si tous les caract\u00e8res sont imprimables (ou la cha\u00eene est vide). Caract\u00e8res non imprimables: \\n, \\r, \\t, etc.",
    returnType: "bool",
    examplesEn: ["'hello'.isprintable()     # True", "'hello\\nworld'.isprintable()  # False", "''.isprintable()         # True (empty string is printable)"],
    examplesFr: ["'bonjour'.isprintable()     # True", "'bonjour\\nmonde'.isprintable()  # False"],
    orderEn: ["1. If the string is empty, return True (edge case)", "2. For each character, check if it is printable (not a control character)", "3. If any character is non-printable, return False", "4. Return True"],
    orderFr: ["1. Si la cha\u00eene est vide, retourner True", "2. Pour chaque caract\u00e8re, v\u00e9rifier s'il est imprimable", "3. Si un caract\u00e8re est non-imprimable, retourner False", "4. Retourner True"],
    mistakesEn: ["''.isprintable() returns True (unlike most is* methods which return False for empty)", "isprintable() returns False for tabs (\\t) and newlines (\\n), unlike isspace()", "Surrogate characters (used in UTF-16) return False for isprintable()"],
    mistakesFr: ["''.isprintable() retourne True (contrairement \u00e0 la plupart des is*)"],
  },
  "str.islower": {
    name: "str.islower",
    type: "method",
    signature: "str.islower()",
    descriptionEn: "Returns True if at least one cased character is lowercase and no cased characters are uppercase. Non-letter characters are ignored.",
    descriptionFr: "Retourne True si au moins un caract\u00e8re est en minuscule et aucun n'est en majuscule.",
    returnType: "bool",
    examplesEn: ["'hello'.islower()   # True", "'Hello'.islower()   # False", "'hello!'.islower()  # True"],
    examplesFr: ["'bonjour'.islower()  # True"],
    orderEn: ["1. If no cased characters exist, return False", "2. Check each cased character: all must be lowercase", "3. Return the result"],
    orderFr: ["1. Si aucun caract\u00e8re avec casse n'existe, retourner False", "2. V\u00e9rifier que tous les caract\u00e8res \u00e0 casse sont en minuscule", "3. Retourner le r\u00e9sultat"],
    mistakesEn: ["''.islower() returns False (no cased characters)", "Numbers and punctuation do NOT affect islower() (they are ignored)"],
    mistakesFr: ["''.islower() retourne False"],
  },
  "str.isupper": {
    name: "str.isupper",
    type: "method",
    signature: "str.isupper()",
    descriptionEn: "Returns True if at least one cased character is uppercase and no cased characters are lowercase.",
    descriptionFr: "Retourne True si au moins un caract\u00e8re est en majuscule et aucun n'est en minuscule.",
    returnType: "bool",
    examplesEn: ["'HELLO'.isupper()   # True", "'Hello'.isupper()   # False", "'HELLO!'.isupper()  # True"],
    examplesFr: ["'BONJOUR'.isupper()  # True"],
    orderEn: ["1. If no cased characters exist, return False", "2. Check each cased character: all must be uppercase", "3. Return the result"],
    orderFr: ["1. Si aucun caract\u00e8re avec casse n'existe, retourner False", "2. V\u00e9rifier que tous les caract\u00e8res \u00e0 casse sont en majuscule", "3. Retourner le r\u00e9sultat"],
    mistakesEn: ["''.isupper() returns False (no cased characters)", "Numbers and punctuation are ignored"],
    mistakesFr: ["''.isupper() retourne False"],
  },
  "str.istitle": {
    name: "str.istitle",
    type: "method",
    signature: "str.istitle()",
    descriptionEn: "Returns True if the string is titlecased: uppercase characters follow uncased/non-letter characters, and lowercase characters follow cased (letter) characters. Non-letter characters are ignored.",
    descriptionFr: "Retourne True si la cha\u00eene est en format titre: les majuscules suivent des caract\u00e8res non-lettres, les minuscules suivent des lettres.",
    returnType: "bool",
    examplesEn: ["'Hello World'.istitle()  # True", "'Hello world'.istitle()  # False (w is lowercase after space)", "'HELLO'.istitle()     # False (all uppercase)"],
    examplesFr: ["'Bonjour Tout Le Monde'.istitle()  # True"],
    orderEn: ["1. For each cased character, check if it follows the titlecase rule", "2. Uppercase characters must follow non-letter OR uppercase characters (in titlecase sequences)", "3. Lowercase characters must follow a letter (any case)", "4. Return the result"],
    orderFr: ["1. Pour chaque caract\u00e8re \u00e0 casse, v\u00e9rifier la r\u00e8gle de titre", "2. Les majuscules doivent suivre des non-lettres ou des majuscules", "3. Les minuscules doivent suivre une lettre", "4. Retourner le r\u00e9sultat"],
    mistakesEn: ["''.istitle() returns False (no cased characters)", "istitle() is stricter than str.title() output because it checks word boundaries properly", "'Don\\'t'.istitle() may behave unexpectedly with apostrophes"],
    mistakesFr: ["''.istitle() retourne False"],
  },
  "str.partition": {
    name: "str.partition",
    type: "method",
    signature: "str.partition(sep)",
    descriptionEn: "Splits the string at the first occurrence of sep, returning a 3-tuple (head, sep, tail). If sep is not found, returns (string, '', '').",
    descriptionFr: "Divise la cha\u00eene \u00e0 la premi\u00e8re occurrence de sep, retournant un 3-uplet (t\u00eate, sep, queue).",
    returnType: "tuple of 3 str",
    examplesEn: ["'hello:world'.partition(':')  # ('hello', ':', 'world')", "'hello'.partition(':')    # ('hello', '', '')"],
    examplesFr: ["'bonjour:monde'.partition(':')  # ('bonjour', ':', 'monde')"],
    orderEn: ["1. Scan for the first occurrence of sep", "2. If found, return (before_sep, sep, after_sep)", "3. If not found, return (original_string, '', '')"],
    orderFr: ["1. Chercher la premi\u00e8re occurrence de sep", "2. Si trouv\u00e9e, retourner (avant, sep, apr\u00e8s)", "3. Si non trouv\u00e9e, retourner (original, '', '')"],
    mistakesEn: ["partition ALWAYS returns a 3-tuple (no ValueError)", "Use rpartition() to split on the LAST occurrence"],
    mistakesFr: ["partition retourne TOUJOURS un 3-uplet (pas de ValueError)"],
  },
  "str.rpartition": {
    name: "str.rpartition",
    type: "method",
    signature: "str.rpartition(sep)",
    descriptionEn: "Like partition() but splits at the LAST occurrence of sep. Returns a 3-tuple (head, sep, tail).",
    descriptionFr: "Comme partition() mais divise \u00e0 la DERNI\u00c8RE occurrence de sep.",
    returnType: "tuple of 3 str",
    examplesEn: ["'a:b:c'.rpartition(':')  # ('a:b', ':', 'c')"],
    examplesFr: ["'a:b:c'.rpartition(':')  # ('a:b', ':', 'c')"],
    orderEn: ["1. Scan from the right for the last occurrence of sep", "2. If found, return (before_last_sep, sep, after_last_sep)", "3. If not found, return ('', '', original_string)"],
    orderFr: ["1. Parcourir depuis la droite pour la derni\u00e8re occurrence", "2. Si trouv\u00e9e, retourner (avant, sep, apr\u00e8s)", "3. Si non trouv\u00e9e, retourner ('', '', original)"],
    mistakesEn: ["rpartition is useful for splitting file extensions: 'file.txt'.rpartition('.')", "Unlike rsplit, rpartition only splits ONCE"],
    mistakesFr: ["rpartition est utile pour les extensions de fichier"],
  },
  "str.rfind": {
    name: "str.rfind",
    type: "method",
    signature: "str.rfind(sub, start=0, end=len(str))",
    descriptionEn: "Returns the HIGHEST index where substring sub is found in s[start:end]. Returns -1 if not found. Like find() but searches from the right.",
    descriptionFr: "Retourne l'indice le PLUS \u00c9LEV\u00c9 de sub dans s[start:end]. Retourne -1 si non trouv\u00e9.",
    returnType: "int",
    examplesEn: ["'hello hello'.rfind('hello')  # 6"],
    examplesFr: ["'bonjour bonjour'.rfind('bonjour')  # 8"],
    orderEn: ["1. Search from the right within s[start:end]", "2. If found, return the start index of the last occurrence", "3. If not found, return -1"],
    orderFr: ["1. Chercher depuis la droite dans s[start:end]", "2. Si trouv\u00e9, retourner l'indice de la derni\u00e8re occurrence", "3. Si non trouv\u00e9, retourner -1"],
    mistakesEn: ["rfind returns -1 (not an exception) for not found", "rfind finds the LAST occurrence, find() finds the FIRST"],
    mistakesFr: ["rfind retourne -1 si non trouv\u00e9"],
  },
  "str.rindex": {
    name: "str.rindex",
    type: "method",
    signature: "str.rindex(sub, start=0, end=len(str))",
    descriptionEn: "Like rfind() but raises ValueError if sub is not found, instead of returning -1.",
    descriptionFr: "Comme rfind() mais l\u00e8ve ValueError si sub n'est pas trouv\u00e9.",
    returnType: "int",
    examplesEn: ["'hello hello'.rindex('hello')  # 6", "'hello'.rindex('xyz')  # ValueError"],
    examplesFr: ["'bonjour'.rindex('xyz')  # ValueError"],
    orderEn: ["1. Search from the right for sub", "2. If found, return the index", "3. If not found, raise ValueError"],
    orderFr: ["1. Chercher depuis la droite pour sub", "2. Si trouv\u00e9, retourner l'indice", "3. Si non trouv\u00e9, lever ValueError"],
    mistakesEn: ["rindex raises ValueError (not -1) for missing substrings"],
    mistakesFr: ["rindex l\u00e8ve ValueError"],
  },
  "str.removeprefix": {
    name: "str.removeprefix",
    type: "method",
    signature: "str.removeprefix(prefix, /)",
    descriptionEn: "If the string starts with the prefix, returns a new string with the prefix removed. Otherwise, returns a copy of the original string. Added in Python 3.9.",
    descriptionFr: "Si la cha\u00eene commence par prefix, retourne une copie sans le prefix. Sinon, retourne une copie inchang\u00e9e. Ajout\u00e9 en Python 3.9.",
    returnType: "str",
    examplesEn: ["'test.py'.removeprefix('test.')  # 'py'", "'hello'.removeprefix('xyz')  # 'hello'"],
    examplesFr: ["'test.py'.removeprefix('test.')  # 'py'"],
    orderEn: ["1. Check if the string starts with prefix", "2. If yes, return string[len(prefix):]", "3. If no, return string[:] (a copy)"],
    orderFr: ["1. V\u00e9rifier si la cha\u00eene commence par prefix", "2. Si oui, retourner string[len(prefix):]", "3. Si non, retourner une copie"],
    mistakesEn: ["removeprefix() is Python 3.9+ (will not work on older versions)", "Unlike lstrip(), removeprefix() matches an EXACT prefix string, not a character set", "removeprefix() always returns a string (never raises ValueError)"],
    mistakesFr: ["removeprefix() n\u00e9cessite Python 3.9+"],
  },
  "str.removesuffix": {
    name: "str.removesuffix",
    type: "method",
    signature: "str.removesuffix(suffix, /)",
    descriptionEn: "If the string ends with the suffix, returns a new string with the suffix removed. Otherwise, returns a copy. Added in Python 3.9.",
    descriptionFr: "Si la cha\u00eene se termine par suffix, retourne une copie sans le suffix. Python 3.9+.",
    returnType: "str",
    examplesEn: ["'hello.py'.removesuffix('.py')  # 'hello'"],
    examplesFr: ["'fichier.txt'.removesuffix('.txt')  # 'fichier'"],
    orderEn: ["1. Check if the string ends with suffix", "2. If yes, return string[:-len(suffix)]", "3. If no, return string[:] (a copy)"],
    orderFr: ["1. V\u00e9rifier si la cha\u00eene se termine par suffix", "2. Si oui, retourner string[:-len(suffix)]", "3. Si non, retourner une copie"],
    mistakesEn: ["removesuffix() is Python 3.9+", "Unlike rstrip(), removesuffix() matches an EXACT suffix string"],
    mistakesFr: ["removesuffix() n\u00e9cessite Python 3.9+"],
  },
  "str.translate": {
    name: "str.translate",
    type: "method",
    signature: "str.translate(table)",
    descriptionEn: "Returns a copy of the string where each character has been mapped through the given translation table. The table is typically created by str.maketrans().",
    descriptionFr: "Retourne une copie de la cha\u00eene o\u00f9 chaque caract\u00e8re est transform\u00e9 par la table de traduction.",
    returnType: "str",
    examplesEn: ["table = str.maketrans('aeiou', 'AEIOU')\n'hello'.translate(table)  # 'hEllO'"],
    examplesFr: ["table = str.maketrans('aeiou', 'AEIOU')\n'bonjour'.translate(table)  # 'bOnjOUr'"],
    orderEn: ["1. For each character in the string, look it up in the translation table", "2. If found, replace with the mapped character (or remove if mapped to None)", "3. If not found, keep the original character", "4. Return the new string"],
    orderFr: ["1. Pour chaque caract\u00e8re, chercher dans la table de traduction", "2. Si trouv\u00e9, remplacer (ou supprimer si None)", "3. Si non trouv\u00e9, garder l'original", "4. Retourner la nouvelle cha\u00eene"],
    mistakesEn: ["translate() is much faster than repeated replace() for single-character substitutions", "The table maps Unicode ordinals (integers), not characters directly", "Use table = str.maketrans('abc', 'xyz') to create the table"],
    mistakesFr: ["translate() est beaucoup plus rapide que replace() pour les substitutions unitaires"],
  },
  "str.maketrans": {
    name: "str.maketrans",
    type: "method",
    signature: "str.maketrans(x, y=None, z=None)",
    descriptionEn: "Returns a translation table for use with str.translate(). Three forms: (1) single dict mapping Unicode ordinals, (2) two strings of equal length mapping characters 1:1, (3) two strings plus a third string of characters to delete.",
    descriptionFr: "Retourne une table de traduction pour str.translate(). Trois formes: (1) dict ordinal->ordinal, (2) deux cha\u00eenes de m\u00eame longueur, (3) deux cha\u00eenes + une cha\u00eene de caract\u00e8res \u00e0 supprimer.",
    returnType: "dict (translation table)",
    examplesEn: ["str.maketrans('aeiou', 'AEIOU')          # {'a': 'A', 'e': 'E', ...}", "str.maketrans({'a': '1', 'b': '2'})           # from dict", "str.maketrans('ae', 'AE', 'ou')               # maps a->A, e->E, deletes o, u"],
    examplesFr: ["str.maketrans('aeiou', 'AEIOU')          # {'a': 'A', 'e': 'E', ...}"],
    orderEn: ["1. Static method (called on str, not on an instance)", "2. With one dict arg: maps ordinals to ordinals/None", "3. With two strings: pairs characters by position (must be equal length)", "4. With three strings: two strings for mapping + third for deletion (characters mapped to None)"],
    orderFr: ["1. M\u00e9thode statique (appel\u00e9e sur str, pas sur une instance)", "2. Avec un dict: mappe ordinaux vers ordinaux/None", "3. Avec deux cha\u00eenes: apparie les caract\u00e8res par position", "4. Avec trois cha\u00eenes: deux pour le mapping + une pour la suppression"],
    mistakesEn: ["maketrans is a STATIC method: str.maketrans(), not 'hello'.maketrans()", "With two-string form, strings MUST be the same length (ValueError otherwise)", "Use z (third arg) to delete characters instead of mapping them to None manually"],
    mistakesFr: ["maketrans est une m\u00e9thode STATIQUE: str.maketrans(), pas 'hello'.maketrans()"],
  },
  "set.add": {
    name: "set.add",
    type: "method",
    signature: "set.add(x)",
    descriptionEn: "Adds element x to the set. If x is already in the set, it does nothing. Modifies the set in place and returns None.",
    descriptionFr: "Ajoute l'\u00e9l\u00e9ment x \u00e0 l'ensemble. Si x est d\u00e9j\u00e0 pr\u00e9sent, ne fait rien. Modifie sur place et retourne None.",
    returnType: "None",
    examplesEn: ["s = {1, 2}\ns.add(3)\nprint(s)  # {1, 2, 3}\ns.add(1)\nprint(s)  # {1, 2, 3} (no change)"],
    examplesFr: ["s = {1, 2}\ns.add(3)\nprint(s)  # {1, 2, 3}"],
    orderEn: ["1. Hash x to find its bucket", "2. If x is not already in the set, insert it", "3. Return None"],
    orderFr: ["1. Hacher x pour trouver son emplacement", "2. Si x n'est pas d\u00e9j\u00e0 dans l'ensemble, l'ins\u00e9rer", "3. Retourner None"],
    mistakesEn: ["add() can only add hashable elements (lists and dicts will raise TypeError)", "add() takes ONE argument; use update() to add multiple elements"],
    mistakesFr: ["add() ne peut ajouter que des \u00e9l\u00e9ments hachables"],
  },
  "set.clear": {
    name: "set.clear",
    type: "method",
    signature: "set.clear()",
    descriptionEn: "Removes all elements from the set. Modifies in place and returns None.",
    descriptionFr: "Supprime tous les \u00e9l\u00e9ments de l'ensemble. Modifie sur place.",
    returnType: "None",
    examplesEn: ["s = {1, 2, 3}\ns.clear()\nprint(s)  # set()"],
    examplesFr: ["s = {1, 2, 3}\ns.clear()\nprint(s)  # set()"],
    orderEn: ["1. Remove all elements from the set", "2. The set becomes empty (length 0)", "3. Return None"],
    orderFr: ["1. Supprimer tous les \u00e9l\u00e9ments", "2. L'ensemble devient vide", "3. Retourner None"],
    mistakesEn: ["clear() affects ALL references to the same set object", "set() creates a NEW empty set; clear() empties the existing one"],
    mistakesFr: ["clear() affecte TOUTES les r\u00e9f\u00e9rences au m\u00eame ensemble"],
  },
  "set.copy": {
    name: "set.copy",
    type: "method",
    signature: "set.copy()",
    descriptionEn: "Returns a shallow copy of the set (a new set with the same elements).",
    descriptionFr: "Retourne une copie superficielle de l'ensemble.",
    returnType: "set",
    examplesEn: ["s = {1, 2, 3}\nc = s.copy()\nc.add(4)\nprint(s)  # {1, 2, 3}\nprint(c)  # {1, 2, 3, 4}"],
    examplesFr: ["s = {1, 2, 3}\nc = s.copy()\nc.add(4)\nprint(s)  # {1, 2, 3}\nprint(c)  # {1, 2, 3, 4}"],
    orderEn: ["1. Create a new set", "2. Add each element from the original to the new set", "3. Return the new set"],
    orderFr: ["1. Cr\u00e9er un nouvel ensemble", "2. Ajouter chaque \u00e9l\u00e9ment de l'original au nouveau", "3. Retourner le nouvel ensemble"],
    mistakesEn: ["copy() is SHALLOW (only the set itself is new; elements are references to the same objects)"],
    mistakesFr: ["copy() est une copie SUPERFICIELLE"],
  },
  "set.difference": {
    name: "set.difference",
    type: "method",
    signature: "set.difference(*others)",
    descriptionEn: "Returns a new set with elements in the set that are NOT in the others. Equivalent to set - other. Can take multiple sets.",
    descriptionFr: "Retourne un nouvel ensemble avec les \u00e9l\u00e9ments qui NE sont PAS dans les autres. \u00c9quivalent \u00e0 set - other.",
    returnType: "set",
    examplesEn: ["{1, 2, 3}.difference({2, 4})  # {1, 3}"],
    examplesFr: ["{1, 2, 3}.difference({2, 4})  # {1, 3}"],
    orderEn: ["1. Create a new set", "2. Add elements from the original that are not in any of the others", "3. Return the new set"],
    orderFr: ["1. Cr\u00e9er un nouvel ensemble", "2. Ajouter les \u00e9l\u00e9ments absents des autres", "3. Retourner le nouvel ensemble"],
    mistakesEn: ["difference() returns a NEW set (does NOT modify the original)", "Use difference_update() to modify in place", "Accepts multiple sets: s.difference(a, b, c)"],
    mistakesFr: ["difference() retourne un NOUVEL ensemble"],
  },
  "set.difference_update": {
    name: "set.difference_update",
    type: "method",
    signature: "set.difference_update(*others)",
    descriptionEn: "Removes all elements found in others from the set. Modifies in place and returns None.",
    descriptionFr: "Supprime tous les \u00e9l\u00e9ments pr\u00e9sents dans les autres ensembles. Modifie sur place.",
    returnType: "None",
    examplesEn: ["s = {1, 2, 3}\ns.difference_update({2, 4})\nprint(s)  # {1, 3}"],
    examplesFr: ["s = {1, 2, 3}\ns.difference_update({2, 4})\nprint(s)  # {1, 3}"],
    orderEn: ["1. For each element in others, remove it from the set if present", "2. Return None"],
    orderFr: ["1. Pour chaque \u00e9l\u00e9ment dans les autres, le supprimer de l'ensemble", "2. Retourner None"],
    mistakesEn: ["difference_update() modifies IN PLACE and returns None", "The symmetric counterpoint is intersection_update()"],
    mistakesFr: ["difference_update() modifie SUR PLACE"],
  },
  "set.discard": {
    name: "set.discard",
    type: "method",
    signature: "set.discard(x)",
    descriptionEn: "Removes element x from the set if it is present. Does NOT raise an error if x is not found (unlike remove()).",
    descriptionFr: "Supprime x de l'ensemble s'il est pr\u00e9sent. Ne l\u00e8ve PAS d'erreur si x n'existe pas.",
    returnType: "None",
    examplesEn: ["s = {1, 2}\ns.discard(1)  # s is now {2}\ns.discard(99)  # no error"],
    examplesFr: ["s = {1, 2}\ns.discard(1)  # s devient {2}\ns.discard(99)  # pas d'erreur"],
    orderEn: ["1. If x is in the set, remove it", "2. If x is not in the set, do nothing", "3. Return None"],
    orderFr: ["1. Si x est dans l'ensemble, le supprimer", "2. Si x n'est pas dans l'ensemble, ne rien faire", "3. Retourner None"],
    mistakesEn: ["discard() NEVER raises an error (unlike remove())", "For checking existence + removing, use discard() over try/except with remove()"],
    mistakesFr: ["discard() ne l\u00e8ve JAMAIS d'erreur"],
  },
  "set.intersection": {
    name: "set.intersection",
    type: "method",
    signature: "set.intersection(*others)",
    descriptionEn: "Returns a new set with elements common to the set and all others. Equivalent to set & other.",
    descriptionFr: "Retourne un nouvel ensemble avec les \u00e9l\u00e9ments communs \u00e0 tous les ensembles.",
    returnType: "set",
    examplesEn: ["{1, 2, 3}.intersection({2, 4})  # {2}"],
    examplesFr: ["{1, 2, 3}.intersection({2, 4})  # {2}"],
    orderEn: ["1. Create a new set", "2. For each element in the set, keep it only if it exists in ALL others", "3. Return the new set"],
    orderFr: ["1. Cr\u00e9er un nouvel ensemble", "2. Garder seulement les \u00e9l\u00e9ments pr\u00e9sents dans TOUS les autres", "3. Retourner le nouvel ensemble"],
    mistakesEn: ["intersection() returns a NEW set", "Use intersection_update() to modify in place", "With multiple sets: s.intersection(a, b) finds elements in s AND a AND b"],
    mistakesFr: ["intersection() retourne un NOUVEL ensemble"],
  },
  "set.intersection_update": {
    name: "set.intersection_update",
    type: "method",
    signature: "set.intersection_update(*others)",
    descriptionEn: "Keeps only elements found in the set and all others. Modifies in place and returns None.",
    descriptionFr: "Garde seulement les \u00e9l\u00e9ments pr\u00e9sents dans tous les ensembles. Modifie sur place.",
    returnType: "None",
    examplesEn: ["s = {1, 2, 3}\ns.intersection_update({2, 4})\nprint(s)  # {2}"],
    examplesFr: ["s = {1, 2, 3}\ns.intersection_update({2, 4})\nprint(s)  # {2}"],
    orderEn: ["1. Remove any element from the set not present in all others", "2. Return None"],
    orderFr: ["1. Supprimer les \u00e9l\u00e9ments absents des autres ensembles", "2. Retourner None"],
    mistakesEn: ["intersection_update() modifies IN PLACE"],
    mistakesFr: ["intersection_update() modifie SUR PLACE"],
  },
  "set.isdisjoint": {
    name: "set.isdisjoint",
    type: "method",
    signature: "set.isdisjoint(other)",
    descriptionEn: "Returns True if the set has NO elements in common with other. Two sets are disjoint if their intersection is empty.",
    descriptionFr: "Retourne True si l'ensemble n'a AUCUN \u00e9l\u00e9ment en commun avec other.",
    returnType: "bool",
    examplesEn: ["{1, 2}.isdisjoint({3, 4})  # True", "{1, 2}.isdisjoint({2, 3})  # False"],
    examplesFr: ["{1, 2}.isdisjoint({3, 4})  # True"],
    orderEn: ["1. Check if the intersection is empty", "2. Return True if disjoint, False otherwise"],
    orderFr: ["1. V\u00e9rifier si l'intersection est vide", "2. Retourner True si disjoint, False sinon"],
    mistakesEn: ["isdisjoint() is more efficient than len(intersection) == 0 (short-circuits)", "An empty set is disjoint with every set (including itself)"],
    mistakesFr: ["isdisjoint() est plus efficace que len(intersection) == 0"],
  },
  "set.issubset": {
    name: "set.issubset",
    type: "method",
    signature: "set.issubset(other)",
    descriptionEn: "Returns True if every element in the set is also in other. Equivalent to set <= other.",
    descriptionFr: "Retourne True si tous les \u00e9l\u00e9ments de l'ensemble sont dans other.",
    returnType: "bool",
    examplesEn: ["{1, 2}.issubset({1, 2, 3})  # True", "{1, 2}.issubset({1, 2})     # True (equal sets are subsets)"],
    examplesFr: ["{1, 2}.issubset({1, 2, 3})  # True"],
    orderEn: ["1. For each element in the set, check membership in other", "2. If all are present, return True; otherwise False"],
    orderFr: ["1. Pour chaque \u00e9l\u00e9ment, v\u00e9rifier sa pr\u00e9sence dans other", "2. Si tous sont pr\u00e9sents, retourner True"],
    mistakesEn: ["A set is always a subset of itself (issubset returns True)", "{} is a subset of every set", "Use < for PROPER subset (not equal)"],
    mistakesFr: ["Un ensemble est toujours un sous-ensemble de lui-m\u00eame"],
  },
  "set.issuperset": {
    name: "set.issuperset",
    type: "method",
    signature: "set.issuperset(other)",
    descriptionEn: "Returns True if every element in other is also in the set. Equivalent to set >= other.",
    descriptionFr: "Retourne True si tous les \u00e9l\u00e9ments de other sont dans l'ensemble.",
    returnType: "bool",
    examplesEn: ["{1, 2, 3}.issuperset({1, 2})  # True"],
    examplesFr: ["{1, 2, 3}.issuperset({1, 2})  # True"],
    orderEn: ["1. For each element in other, check membership in the set", "2. If all are present, return True"],
    orderFr: ["1. Pour chaque \u00e9l\u00e9ment de other, v\u00e9rifier sa pr\u00e9sence", "2. Si tous sont pr\u00e9sents, retourner True"],
    mistakesEn: ["A set is always a superset of itself (issuperset returns True)"],
    mistakesFr: ["Un ensemble est toujours un sur-ensemble de lui-m\u00eame"],
  },
  "set.pop": {
    name: "set.pop",
    type: "method",
    signature: "set.pop()",
    descriptionEn: "Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty. Since sets are unordered, the element is not predictable.",
    descriptionFr: "Supprime et retourne un \u00e9l\u00e9ment arbitraire de l'ensemble. L\u00e8ve KeyError si l'ensemble est vide.",
    returnType: "Any (the removed element)",
    examplesEn: ["s = {10, 20, 30}\nel = s.pop()\nprint(el)  # unpredictable (but will be one of 10, 20, 30)\nprint(s)   # the set without that element"],
    examplesFr: ["s = {10, 20, 30}\nel = s.pop()\nprint(el)  # impr\u00e9visible"],
    orderEn: ["1. If the set is empty, raise KeyError", "2. Pick and remove an arbitrary element", "3. Return that element"],
    orderFr: ["1. Si l'ensemble est vide, lever KeyError", "2. Choisir et supprimer un \u00e9l\u00e9ment arbitraire", "3. Retourner cet \u00e9l\u00e9ment"],
    mistakesEn: ["set.pop() removes an ARBITRARY element (not necessarily the 'first' one)", "pop() on an empty set raises KeyError (check len(s) > 0 first)", "For a predictable removal order, use collections.OrderedDict"],
    mistakesFr: ["set.pop() supprime un \u00e9l\u00e9ment ARBITRAIRE"],
  },
  "set.remove": {
    name: "set.remove",
    type: "method",
    signature: "set.remove(x)",
    descriptionEn: "Removes element x from the set. Raises KeyError if x is not found. Unlike discard(), remove() raises an error for missing elements.",
    descriptionFr: "Supprime l'\u00e9l\u00e9ment x de l'ensemble. L\u00e8ve KeyError si x n'existe pas.",
    returnType: "None",
    examplesEn: ["s = {1, 2, 3}\ns.remove(2)\nprint(s)  # {1, 3}"],
    examplesFr: ["s = {1, 2, 3}\ns.remove(2)\nprint(s)  # {1, 3}"],
    orderEn: ["1. Check if x is in the set", "2. If yes, remove it and return None", "3. If no, raise KeyError"],
    orderFr: ["1. V\u00e9rifier si x est dans l'ensemble", "2. Si oui, supprimer et retourner None", "3. Si non, lever KeyError"],
    mistakesEn: ["remove() raises KeyError for missing elements; use discard() to avoid errors", "remove() takes ONE element; use difference_update() for multiple"],
    mistakesFr: ["remove() l\u00e8ve KeyError pour les \u00e9l\u00e9ments manquants"],
  },
  "set.symmetric_difference": {
    name: "set.symmetric_difference",
    type: "method",
    signature: "set.symmetric_difference(other)",
    descriptionEn: "Returns a new set with elements in either set but NOT in both. Equivalent to set ^ other.",
    descriptionFr: "Retourne un nouvel ensemble avec les \u00e9l\u00e9ments dans l'un OU l'autre mais PAS les deux.",
    returnType: "set",
    examplesEn: ["{1, 2, 3}.symmetric_difference({3, 4})  # {1, 2, 4}"],
    examplesFr: ["{1, 2, 3}.symmetric_difference({3, 4})  # {1, 2, 4}"],
    orderEn: ["1. Create a new set", "2. Add elements from the set that are NOT in other", "3. Add elements from other that are NOT in the set", "4. Return the new set"],
    orderFr: ["1. Cr\u00e9er un nouvel ensemble", "2. Ajouter les \u00e9l\u00e9ments absents de other", "3. Ajouter les \u00e9l\u00e9ments de other absents de l'ensemble", "4. Retourner le nouvel ensemble"],
    mistakesEn: ["symmetric_difference() returns a NEW set (use symmetric_difference_update() for in-place)", "Only takes ONE other set (not multiple like union/difference)"],
    mistakesFr: ["symmetric_difference() retourne un NOUVEL ensemble"],
  },
  "set.symmetric_difference_update": {
    name: "set.symmetric_difference_update",
    type: "method",
    signature: "set.symmetric_difference_update(other)",
    descriptionEn: "Updates the set with the symmetric difference (elements in either but not both). Modifies in place.",
    descriptionFr: "Met \u00e0 jour l'ensemble avec la diff\u00e9rence sym\u00e9trique. Modifie sur place.",
    returnType: "None",
    examplesEn: ["s = {1, 2, 3}\ns.symmetric_difference_update({3, 4})\nprint(s)  # {1, 2, 4}"],
    examplesFr: ["s = {1, 2, 3}\ns.symmetric_difference_update({3, 4})\nprint(s)  # {1, 2, 4}"],
    orderEn: ["1. Compute elements in the set XOR other", "2. Replace the set with the result", "3. Return None"],
    orderFr: ["1. Calculer les \u00e9l\u00e9ments en XOR", "2. Remplacer l'ensemble par le r\u00e9sultat", "3. Retourner None"],
    mistakesEn: ["Only takes ONE other set (unlike union_update/difference_update)"],
    mistakesFr: ["Ne prend qu'UN seul autre ensemble"],
  },
  "set.union": {
    name: "set.union",
    type: "method",
    signature: "set.union(*others)",
    descriptionEn: "Returns a new set with elements from the set and all others. Equivalent to set | other. Can take multiple sets.",
    descriptionFr: "Retourne un nouvel ensemble avec les \u00e9l\u00e9ments de tous les ensembles.",
    returnType: "set",
    examplesEn: ["{1, 2}.union({3, 4}, {5, 6})  # {1, 2, 3, 4, 5, 6}"],
    examplesFr: ["{1, 2}.union({3, 4}, {5, 6})  # {1, 2, 3, 4, 5, 6}"],
    orderEn: ["1. Create a new set", "2. Add all elements from the set and all others", "3. Return the new set"],
    orderFr: ["1. Cr\u00e9er un nouvel ensemble", "2. Ajouter tous les \u00e9l\u00e9ments", "3. Retourner le nouvel ensemble"],
    mistakesEn: ["union() returns a NEW set (use update() to modify in place)", "Accepts multiple sets: s.union(a, b, c)"],
    mistakesFr: ["union() retourne un NOUVEL ensemble"],
  },
  "set.update": {
    name: "set.update",
    type: "method",
    signature: "set.update(*others)",
    descriptionEn: "Adds all elements from others to the set. Modifies in place and returns None. Equivalent to |= operator.",
    descriptionFr: "Ajoute tous les \u00e9l\u00e9ments des autres ensembles. Modifie sur place.",
    returnType: "None",
    examplesEn: ["s = {1, 2}\ns.update({3, 4}, [5, 6])\nprint(s)  # {1, 2, 3, 4, 5, 6}"],
    examplesFr: ["s = {1, 2}\ns.update({3, 4}, [5, 6])\nprint(s)  # {1, 2, 3, 4, 5, 6}"],
    orderEn: ["1. For each element in each other, add it to the set", "2. Return None"],
    orderFr: ["1. Pour chaque \u00e9l\u00e9ment de chaque other, l'ajouter \u00e0 l'ensemble", "2. Retourner None"],
    mistakesEn: ["update() accepts any iterable, not just sets (e.g., list, tuple, generator)", "update() modifies IN PLACE and returns None"],
    mistakesFr: ["update() accepte n'importe quel it\u00e9rable"],
  },
  "tuple.count": {
    name: "tuple.count",
    type: "method",
    signature: "tuple.count(x)",
    descriptionEn: "Returns the number of times x appears in the tuple.",
    descriptionFr: "Retourne le nombre d'occurrences de x dans le tuple.",
    returnType: "int",
    examplesEn: ["(1, 2, 2, 3).count(2)  # 2"],
    examplesFr: ["(1, 2, 2, 3).count(2)  # 2"],
    orderEn: ["1. Scan the tuple from left to right", "2. Count each element equal to x (using ==)", "3. Return the total count"],
    orderFr: ["1. Parcourir le tuple de gauche \u00e0 droite", "2. Compter chaque \u00e9l\u00e9ment \u00e9gal \u00e0 x", "3. Retourner le total"],
    mistakesEn: ["tuple.count scans the entire tuple (O(n))", "Tuples are immutable, so count() never modifies them"],
    mistakesFr: ["tuple.count parcourt tout le tuple (O(n))"],
  },
  "tuple.index": {
    name: "tuple.index",
    type: "method",
    signature: "tuple.index(x, start=0, end=len(tuple))",
    descriptionEn: "Returns the index of the first occurrence of x in the tuple (within optional start/end slice). Raises ValueError if not found.",
    descriptionFr: "Retourne l'indice de la premi\u00e8re occurrence de x dans le tuple. L\u00e8ve ValueError si non trouv\u00e9.",
    returnType: "int",
    examplesEn: ["(10, 20, 30).index(20)  # 1"],
    examplesFr: ["(10, 20, 30).index(20)  # 1"],
    orderEn: ["1. Scan the slice tuple[start:end] from left to right", "2. Find the first element equal to x", "3. Return its absolute index", "4. If not found, raise ValueError"],
    orderFr: ["1. Parcourir la tranche tuple[start:end]", "2. Trouver le premier \u00e9l\u00e9ment \u00e9gal \u00e0 x", "3. Retourner l'indice absolu", "4. Si non trouv\u00e9, lever ValueError"],
    mistakesEn: ["tuple.index raises ValueError (not -1) if not found"],
    mistakesFr: ["tuple.index l\u00e8ve ValueError si non trouv\u00e9"],
  },
};

export const answerPythonMethodQuery = (question: string, language: AdvancedAiLanguage): string | null => {
  const fr = language === 'fr';
  const lower = question.toLowerCase().trim();
  const cleaned = lower.replace(/[?!.]+$/g, '').trim();

  // 1. Exact match against type.method pattern
  const methodNames = Object.keys(BUILTIN_METHOD_SPECS);
  for (const dottedName of methodNames) {
    const [typeName, methodName] = dottedName.split('.');
    // Try exact: str.capitalize, list.append, etc.
    if (cleaned === dottedName || cleaned === `${dottedName}()`) {
      const spec = BUILTIN_METHOD_SPECS[dottedName];
      return formatBuiltinSpec(spec as unknown as BuiltinSpec, language);
    }
    // Try bare method name: capitalize, append, etc.
    if (cleaned === methodName || cleaned === `${methodName}()`) {
      const spec = BUILTIN_METHOD_SPECS[dottedName];
      return formatBuiltinSpec(spec as unknown as BuiltinSpec, language, [
        `**${fr ? 'M\u00e9thode' : 'Method'}: \`${dottedName}()\`**`,
      ]);
    }
    // Regex patterns
    const patterns = [
      new RegExp(`\\b${methodName}\\b`, 'i'),
      new RegExp(`what\\s+is\\s+${typeName}\\.${methodName}`, 'i'),
      new RegExp(`explain\\s+${typeName}\\.${methodName}`, 'i'),
      new RegExp(`\\b${typeName}\\.${methodName}`, 'i'),
    ];
    for (const p of patterns) {
      if (p.test(lower)) {
        const spec = BUILTIN_METHOD_SPECS[dottedName];
        return formatBuiltinSpec(spec as unknown as BuiltinSpec, language);
      }
    }
  }

  return null;
};


// Sorted list of every builtin name for disambiguation
const ALL_BUILTIN_NAMES: string[] = Object.keys(BUILTIN_SPECS).sort((a, b) => a.localeCompare(b));

export const buildGeneralAiDisambiguationList = (language: AdvancedAiLanguage): string => {
  const fr = language === 'fr';
  const headers = [
    '',
    '---',
    '',
  ];
  const byType: Record<string, string[]> = {};
  for (const name of ALL_BUILTIN_NAMES) {
    const spec = BUILTIN_SPECS[name];
    if (!spec) continue;
    const type = spec.type;
    if (!byType[type]) byType[type] = [];
    byType[type].push(name);
  }
  // Add methods grouped by type
  const methodGroups: Record<string, string[]> = {};
  for (const [dottedName] of Object.entries(BUILTIN_METHOD_SPECS)) {
    const [typeName] = dottedName.split('.');
    if (!methodGroups[typeName]) methodGroups[typeName] = [];
    methodGroups[typeName].push(dottedName);
  }

  const totalBuiltin = ALL_BUILTIN_NAMES.length;
  const totalMethods = Object.keys(BUILTIN_METHOD_SPECS).length;

  const parts: string[] = [
    `**${fr ? 'Voici ce que je peux vous expliquer' : 'Here is what I can explain'}**`,
    fr
      ? `Je ne suis pas sûr de comprendre votre question. Voici une liste de ${totalBuiltin} entrées et ${totalMethods} méthodes intégrées que je connais. Essayez d\u2019en taper une pour obtenir sa définition :`
      : `I\u2019m not sure I understood your question. Here is a list of ${totalBuiltin} entries and ${totalMethods} methods I know about. Try typing one to get its definition:`,
    ...headers,
  ];

  for (const [type, names] of Object.entries(byType).sort()) {
    parts.push(`**${type.charAt(0).toUpperCase() + type.slice(1)}**`);
    parts.push(names.map(n => `\`${n}\``).join(', '));
    parts.push('');
  }

  for (const [typeName, methods] of Object.entries(methodGroups).sort()) {
    parts.push(`**${typeName} ${fr ? 'méthodes' : 'methods'}**`);
    parts.push(methods.map(m => `\`${m}\``).join(', '));
    parts.push('');
  }

  parts.push(
    fr
      ? 'Vous pouvez aussi poser des questions comme "différence entre list et tuple", "expliquer isinstance", ou "comment utiliser zip".'
      : 'You can also ask questions like "difference between list and tuple", "explain isinstance", or "how to use zip".'
  );

  return parts.join('\n');
};

export const buildGeneralAiSmartFollowUp = (topic: string, language: AdvancedAiLanguage): string | null => {
  const relations = TOPIC_RELATIONSHIPS[topic];
  if (!relations || relations.length === 0) return null;
  const fr = language === 'fr';
  return [
    fr ? '**Suggestions pour aller plus loin**' : '**Suggested next topics**',
    ...relations.slice(0, 3).map((r, i) => `${i + 1}. \`${r.questionEn}\``),
  ].join('\n');
};
