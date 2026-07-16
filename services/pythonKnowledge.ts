import {
  getAllConceptTerms,
  lookupConcept,
  type CategoryFallback,
  type ConceptEntry,
} from './pythonConceptLibrary';
import { allBuiltins, allDictMethods, allListMethods, allReferenceEntries, allSetMethods, allStringMethods, allTupleMethods, answerGeneralPythonQuestion, lookupAll, type RefEntry } from './pythonReference';
import type { GeneralAiResponseMode } from './generalAiMode';
import { localizeAiText } from './aiLocalization';

export type KnowledgeLanguage = 'en' | 'fr';
export type KnowledgeConfidence = 'authoritative' | 'curated' | 'categorized';

export interface PythonKnowledgeRecord {
  term: string;
  canonicalName: string;
  kind: string;
  category: string;
  summary: string;
  details: string;
  signature: string;
  returns: string;
  mutates: 'yes' | 'no' | 'depends' | 'not-applicable';
  raises: string;
  examples: Array<{ title: string; code: string }>;
  related: string[];
  version: string;
  sourceLabel: string;
  sourceUrl: string;
  confidence: KnowledgeConfidence;
}

export interface KnowledgeResolution {
  term: string;
  record: PythonKnowledgeRecord | null;
  alternatives: PythonKnowledgeRecord[];
}

export interface KnowledgeFollowUpResolution {
  question: string;
  mode: GeneralAiResponseMode;
  usedContext: boolean;
}

export const getPythonReferenceCounts = () => ({
  builtin: allBuiltins().length,
  dict: allDictMethods().length,
  list: allListMethods().length,
  set: allSetMethods().length,
  str: allStringMethods().length,
  tuple: allTupleMethods().length,
});

export const answerPythonReferenceQuestion = (question: string): string | null => answerGeneralPythonQuestion(question);

const catalogEntriesForType = (type: string): RefEntry[] => {
  const seen = new Set<string>();
  return allReferenceEntries()
    .filter(entry => entry.type === type)
    .sort((left, right) => left.name.localeCompare(right.name))
    .filter(entry => {
      const key = `${entry.type}:${entry.signature}`;
      if (seen.has(key)) return false;
      seen.add(key);
      return true;
    });
};

const formatCatalogEntries = (entries: RefEntry[], language: KnowledgeLanguage, start = 1): string => entries
  .map((entry, index) => `${index + start}. \`${entry.signature}\` — ${language === 'fr' ? localizeAiText(entry.desc, 'fr') : entry.desc}`)
  .join('\n\n');

export const answerPythonCatalogQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const q = question.toLowerCase().replace(/[?!.]+$/g, '').trim();
  const asksForCatalog = /\b(?:show|give|name|display|all|every|how many|number of|count of|montre|donne|tous|toutes|combien|nombre de)\b/i.test(q)
    || /^(?:please\s+)?(?:list|liste|lister)\s+(?:all|every|the|methods?|functions?|keywords?|operators?|types?|built-ins?|toutes?|les|des|m[eé]thodes?|fonctions?|mots?[- ]cl[eé]s?|op[eé]rateurs?|types?)\b/i.test(q);
  if (!asksForCatalog) return null;
  const fr = language === 'fr';
  const typeMatch = q.match(/\b(string|str|list|dict|dictionary|set|tuple)\s+methods?\b|\bmethods?\s+(?:of|for|on)\s+(?:a\s+)?(string|str|list|dict|dictionary|set|tuple)\b/i);
  const methodType = (typeMatch?.[1] || typeMatch?.[2] || '').replace('string', 'str').replace('dictionary', 'dict');

  if (/\bmethods?\b|\bm[eé]thodes?\b/i.test(q)) {
    if (methodType) {
      const entries = catalogEntriesForType(methodType);
      return [
        `**${fr ? 'Catalogue Python' : 'Python catalog'}: ${methodType} ${fr ? 'méthodes' : 'methods'} (${entries.length})**`,
        fr ? `Voici les ${entries.length} méthodes référencées avec leur signature complète :` : `Here are all ${entries.length} referenced methods with their complete signatures:`,
        formatCatalogEntries(entries, language),
        fr ? 'Demandez ensuite une méthode précise pour obtenir des exemples, l’ordre des arguments et les erreurs fréquentes.' : 'Ask about any specific method for examples, argument order, and common mistakes.',
      ].join('\n\n');
    }
    const groups = ['str', 'list', 'dict', 'set', 'tuple'];
    const grouped = groups.map(type => ({ type, entries: catalogEntriesForType(type) }));
    const total = grouped.reduce((sum, group) => sum + group.entries.length, 0);
    return [
      `**${fr ? 'Catalogue Python' : 'Python catalog'}: ${fr ? 'toutes les méthodes intégrées principales' : 'all core built-in-type methods'} (${total})**`,
      fr ? 'Les méthodes sont regroupées par type. Un même nom peut appartenir à plusieurs types.' : 'Methods are grouped by owner type. The same method name may exist on several types.',
      ...grouped.map(group => [
        `**${group.type} ${fr ? 'méthodes' : 'methods'} (${group.entries.length})**`,
        formatCatalogEntries(group.entries, language),
      ].join('\n\n')),
    ].join('\n\n');
  }

  if (/\b(?:built.?ins?|built.?in functions?|fonctions? int[eé]gr[eé]es?)\b/i.test(q) && !/\b(?:data types?|types? de donn[eé]es)\b/i.test(q)) {
    const entries = catalogEntriesForType('builtin');
    return [
      `**${fr ? 'Catalogue Python' : 'Python catalog'}: ${fr ? 'fonctions intégrées' : 'built-in functions'} (${entries.length})**`,
      fr ? 'Ces fonctions sont disponibles sans importer de bibliothèque :' : 'These functions are available without importing a library:',
      formatCatalogEntries(entries, language),
      fr ? 'Demandez une fonction précise pour connaître son nombre d’arguments, leur ordre, son retour et des exemples.' : 'Ask about any function for its argument count, argument order, return value, and examples.',
    ].join('\n\n');
  }

  if (/\bkeywords?\b|\bmots?[- ]cl[eé]s?\b/i.test(q)) {
    const entries = catalogEntriesForType('keyword');
    return [`**${fr ? 'Catalogue Python' : 'Python catalog'}: ${fr ? 'mots-clés' : 'keywords'} (${entries.length})**`, formatCatalogEntries(entries, language)].join('\n\n');
  }

  if (/\b(?:data types?|types? de donn[eé]es)\b/i.test(q)) {
    const types = [
      ['bool', 'boolean truth value'], ['int', 'integer number'], ['float', 'decimal number'], ['complex', 'complex number'],
      ['str', 'text sequence'], ['list', 'mutable sequence'], ['tuple', 'immutable sequence'], ['range', 'integer sequence'],
      ['dict', 'key-value mapping'], ['set', 'mutable unique collection'], ['frozenset', 'immutable unique collection'],
      ['bytes', 'immutable bytes'], ['bytearray', 'mutable bytes'], ['memoryview', 'zero-copy binary view'], ['None', 'absence of a value'],
    ];
    return [`**${fr ? 'Catalogue Python' : 'Python catalog'}: ${fr ? 'types de données intégrés' : 'built-in data types'} (${types.length})**`, ...types.map(([name, description], index) => `${index + 1}. \`${name}\` — ${description}`)].join('\n\n');
  }

  if (/\boperators?\b|\bop[eé]rateurs?\b/i.test(q)) {
    const operators = ['+ addition', '- subtraction', '* multiplication', '/ true division', '// floor division', '% remainder', '** exponentiation', '== equality', '!= inequality', '< <= > >= ordering', 'and boolean AND', 'or boolean OR', 'not boolean negation', 'is identity', 'in membership', '& | ^ set/bitwise operations', '<< >> bit shifts', ':= assignment expression'];
    return [`**${fr ? 'Catalogue Python' : 'Python catalog'}: ${fr ? 'opérateurs principaux' : 'core operators'} (${operators.length})**`, ...operators.map((operator, index) => `${index + 1}. \`${operator.split(' ')[0]}\` — ${operator.split(' ').slice(1).join(' ')}`)].join('\n\n');
  }

  if (/\bcomprehensions?\b|\bcompr[eé]hensions?\b/i.test(q)) {
    const forms = [
      ['[expression for item in iterable]', 'list comprehension'],
      ['{expression for item in iterable}', 'set comprehension'],
      ['{key: value for item in iterable}', 'dictionary comprehension'],
      ['(expression for item in iterable)', 'generator expression'],
    ];
    return [`**${fr ? 'Catalogue Python' : 'Python catalog'}: ${fr ? 'formes de compréhension' : 'comprehension forms'} (${forms.length})**`, ...forms.map(([signature, description], index) => `${index + 1}. \`${signature}\` — ${description}`)].join('\n\n');
  }

  if (/\bfunctions?\b|\bfonctions?\b/i.test(q) && /\b(?:how many|number of|count|combien|nombre)\b/i.test(q)) {
    const count = catalogEntriesForType('builtin').length;
    return [
      `**${fr ? 'Nombre de fonctions Python' : 'Python function count'}**`,
      fr ? `Les utilisateurs et bibliothèques peuvent définir un nombre illimité de fonctions. Cette application référence **${count} fonctions intégrées**.` : `Users and libraries can define unlimited functions. This app references **${count} built-in functions**.`,
      fr ? 'Demandez « liste toutes les fonctions intégrées » pour afficher la liste numérotée complète.' : 'Ask “list all built-in functions” to display the complete numbered catalog.',
    ].join('\n\n');
  }

  return null;
};

export const answerPythonContractSearch = (question: string, language: KnowledgeLanguage): string | null => {
  if (!/\b(?:find|which|show|list|search|what|trouve|quels?|montre|liste|cherche)\b/i.test(question)) return null;
  const q = question.toLowerCase();
  const wantsMethods = /\bmethods?\b|\bm[eé]thodes?\b/.test(q);
  const wantsFunctions = /\bfunctions?\b|\bfonctions?\b/.test(q);
  const hasContractFilter = /\b(?:return(?:s|ing)?|accept(?:s|ing)?|argument|iterable|mutat|modify|in place|remove|delete|sort|copy|none|renvoie|accepte|it[eé]rable|modifie|supprime|trie|copie|aucun)\b/i.test(q);
  if ((!wantsMethods && !wantsFunctions) || !hasContractFilter) return null;
  const records = allReferenceEntries().filter(entry => wantsMethods ? !['builtin', 'keyword', 'concept'].includes(entry.type) : entry.type === 'builtin');
  const matches = records.filter(entry => {
    const text = `${entry.name} ${entry.signature} ${entry.desc}`.toLowerCase();
    if (/\b(?:iterable|it[eé]rable)\b/.test(q) && !/iterable|sequence|collection/.test(text)) return false;
    if (/\b(?:remove|delete|supprime|efface)\b/.test(q) && !/remove|delete|discard|pop|clear/.test(text)) return false;
    if (/\b(?:sort|trie|tri)\b/.test(q) && !/sort|order/.test(text)) return false;
    if (/\b(?:copy|copie)\b/.test(q) && !/copy|new/.test(text)) return false;
    if (/\b(?:return(?:s|ing)? none|renvoie (?:none|aucun)|in place|mutat|modify|modifie)\b/.test(q) && !/in place|modif|adds item|removes|updates|none/.test(text)) return false;
    return true;
  });
  if (!matches.length) return null;
  const fr = language === 'fr';
  const limited = matches.slice(0, 40);
  const mutationSummary = /\b(?:return(?:s|ing)? none|renvoie (?:none|aucun)|in place|mutat|modify|modifie)\b/.test(q)
    ? (fr ? 'Contrat recherché : ces opérations modifient généralement l’objet sur place et renvoient `None`.' : 'Requested contract: these operations generally mutate the object in place and return `None`.')
    : '';
  return [
    `**${fr ? 'Recherche dans les contrats Python' : 'Python contract search'} (${matches.length})**`,
    fr ? 'Résultats classés à partir des signatures et descriptions vérifiées :' : 'Matches from verified signatures and API descriptions:',
    mutationSummary,
    formatCatalogEntries(limited, language),
    matches.length > limited.length ? (fr ? `${matches.length - limited.length} autres résultats existent ; précisez le type ou le comportement.` : `${matches.length - limited.length} more results exist; narrow the owner type or behavior.`) : '',
  ].filter(Boolean).join('\n\n');
};

const splitSignatureParameters = (signature: string): { parameters: string[]; required: number; variadic: boolean } | null => {
  const open = signature.indexOf('(');
  const close = signature.lastIndexOf(')');
  if (open < 0 || close < open) return null;
  const raw = signature.slice(open + 1, close).trim();
  if (!raw) return { parameters: [], required: 0, variadic: false };
  const optionalStart = raw.indexOf('[');
  const flattened = raw.replace(/[\[\]]/g, '');
  const parameters = flattened.split(',').map(value => value.trim()).filter(Boolean);
  const required = parameters.filter(parameter => {
    const position = raw.indexOf(parameter);
    return parameter !== '...' && !parameter.startsWith('*') && !parameter.includes('=') && (optionalStart < 0 || position < optionalStart);
  }).length;
  return { parameters, required, variadic: parameters.some(parameter => parameter === '...' || parameter.startsWith('*')) };
};

export const answerPythonCallableSignatureQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  if (!/\b(?:how many|number of|order|arguments?|parameters?|takes?|accepts?|combien|nombre|ordre|arguments?|param[eè]tres?|prend|accepte)\b/i.test(question)) return null;
  const explicitCalls = [...question.matchAll(/\b([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)?)\s*\(\s*\)/g)].map(match => match[1]);
  const dottedNames = [...question.matchAll(/\b([A-Za-z_]\w*\.[A-Za-z_]\w*)\b/g)].map(match => match[1]);
  const explicitSubjects = [
    ...question.matchAll(/\b(?:does|do)\s+([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)?)\s+(?:take|accept)/gi),
    ...question.matchAll(/\b(?:arguments?|parameters?)\s+(?:of|for|in|de|des|pour)\s+([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)?)/gi),
    ...question.matchAll(/\b(?:prend|accepte)\s+([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)?)/gi),
  ].map(match => match[1]);
  const stopWords = new Set(['how', 'many', 'number', 'of', 'arguments', 'argument', 'parameters', 'parameter', 'does', 'do', 'take', 'takes', 'accept', 'accepts', 'what', 'is', 'the', 'order', 'in', 'for', 'first', 'combien', 'nombre', 'de', 'des', 'ordre', 'prend', 'accepte']);
  const plainNames = [...question.matchAll(/\b([A-Za-z_]\w*)\b/g)].map(match => match[1]).filter(value => !stopWords.has(value.toLowerCase()));
  const candidates = [...new Set([...explicitCalls, ...dottedNames, ...explicitSubjects, ...plainNames])];
  const subject = candidates.find(candidate => {
    const candidateResolution = resolvePythonKnowledge(candidate, typeFromPrefix(candidate));
    const records = candidateResolution.record ? [candidateResolution.record] : candidateResolution.alternatives;
    return records.some(record => (
      (record.kind === 'builtin' || ['str', 'list', 'dict', 'set', 'tuple'].includes(record.kind))
      && /\([^)]*\)/.test(record.signature)
    ));
  });
  if (!subject) return null;
  const resolution = resolvePythonKnowledge(subject, typeFromPrefix(subject));
  if (!resolution.record) {
    if (!resolution.alternatives.length) return null;
    const fr = language === 'fr';
    return [
      fr ? `**Précisez le type pour \`${subject}\`**` : `**Specify the owner type for \`${subject}\`**`,
      fr ? 'Plusieurs API portent ce nom :' : 'Several Python APIs use this name:',
      ...resolution.alternatives.slice(0, 8).map((record, index) => `${index + 1}. \`${record.signature}\``),
    ].join('\n\n');
  }
  const record = resolution.record;
  const parsed = splitSignatureParameters(record.signature);
  if (!parsed) return null;
  const fr = language === 'fr';
  const optional = Math.max(0, parsed.parameters.filter(parameter => parameter !== '...' && !parameter.startsWith('*')).length - parsed.required);
  const countText = parsed.variadic
    ? (fr ? `au moins ${parsed.required}, puis des arguments supplémentaires` : `at least ${parsed.required}, with additional arguments allowed`)
    : optional > 0
      ? (fr ? `${parsed.required} obligatoire(s) et ${optional} facultatif(s)` : `${parsed.required} required and ${optional} optional`)
      : (fr ? `exactement ${parsed.required}` : `exactly ${parsed.required}`);
  return [
    `**${fr ? 'Signature et nombre d’arguments' : 'Signature and argument count'}: ${record.canonicalName}**`,
    `\`${record.signature}\``,
    `${fr ? 'Nombre accepté' : 'Accepted count'}: **${countText}**.`,
    `**${fr ? 'Ordre des arguments' : 'Argument order'}**`,
    ...(parsed.parameters.length
      ? parsed.parameters.map((parameter, index) => `${index + 1}. \`${parameter}\`${parameter === '...' ? (fr ? ' — autres itérables/arguments positionnels' : ' — additional iterables/positional arguments') : ''}`)
      : [fr ? 'Aucun argument.' : 'No arguments.']),
    `**${fr ? 'Règle pratique' : 'Practical rule'}**\n${record.canonicalName === 'map'
      ? (fr ? 'Passez d’abord la fonction, puis un ou plusieurs itérables. La fonction reçoit un élément de chaque itérable à chaque étape.' : 'Pass the function first, then one or more iterables. The function receives one item from each iterable per step.')
      : localizedKnowledgeSummary(record, language)}`,
  ].join('\n\n');
};

export const answerPythonEvaluationAndScopeQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const fr = language === 'fr';
  if (/\b(?:scope|global|local|nonlocal|legb|variable resolution|which variable|port[eé]e|globale?|locale?|r[eé]solution des noms)\b/i.test(question)) {
    return [
      fr ? '**Résolution des variables : règle LEGB**' : '**Variable resolution: the LEGB rule**',
      fr ? 'Python cherche un nom dans cet ordre :' : 'Python looks up a name in this order:',
      `1. **Local** — ${fr ? 'paramètres et affectations de la fonction courante' : 'parameters and assignments in the current function'}.`,
      `2. **Enclosing** — ${fr ? 'fonctions englobantes, important pour les fermetures' : 'enclosing functions, important for closures'}.`,
      `3. **Global** — ${fr ? 'espace de noms du module' : 'the module namespace'}.`,
      `4. **Built-ins** — \`len\`, \`sum\`, \`print\`, ${fr ? 'etc.' : 'and so on'}.`,
      fr ? '`global name` permet d’affecter le nom du module ; `nonlocal name` permet d’affecter le nom d’une fonction englobante. Sans ces mots-clés, une affectation crée normalement un nom local.' : '`global name` allows assignment to the module name; `nonlocal name` allows assignment to an enclosing-function name. Without them, assignment normally creates a local name.',
    ].join('\n\n');
  }
  if (!/\b(?:order of (?:operations|evaluation|execution)|evaluation order|execution order|lambda|list comprehension|dict comprehension|set comprehension|default arguments?|default parameters?|mutable defaults?|decorators?|generator execution|import execution|short[- ]?circuit|function calls?|call order|argument evaluation|ordre d['’](?:op[eé]rations|ex[eé]cution|[eé]valuation)|compr[eé]hension|arguments? par d[eé]faut|param[eè]tres? par d[eé]faut|d[eé]corateurs?|g[eé]n[eé]rateur|importation|court-circuit|appel de fonction)\b/i.test(question)) return null;
  if (/\b(?:default arguments?|default parameters?|mutable defaults?|arguments? par d[eé]faut|param[eè]tres? par d[eé]faut)\b/i.test(question)) {
    return [
      fr ? '**Moment d’évaluation des arguments par défaut**' : '**Default-argument evaluation timing**',
      `1. ${fr ? 'Python évalue chaque expression par défaut une seule fois, lorsque l’instruction `def` s’exécute.' : 'Python evaluates each default expression once, when the `def` statement executes.'}`,
      `2. ${fr ? 'L’objet obtenu est stocké dans la fonction et réutilisé lors des appels qui omettent cet argument.' : 'The resulting object is stored on the function and reused by calls that omit that argument.'}`,
      `3. ${fr ? 'Un défaut mutable peut donc conserver les modifications entre les appels.' : 'A mutable default can therefore retain changes across calls.'}`,
      '```python\ndef collect(value, items=None):\n    if items is None:\n        items = []\n    items.append(value)\n    return items\n```',
      fr ? 'Utilisez `None`, puis créez l’objet mutable dans le corps lorsque chaque appel doit recevoir une nouvelle valeur.' : 'Use `None`, then create the mutable object in the body when each call needs a fresh value.',
    ].join('\n\n');
  }
  if (/\b(?:decorators?|d[eé]corateurs?)\b/i.test(question)) {
    return [
      fr ? '**Ordre d’évaluation des décorateurs**' : '**Decorator evaluation and application order**',
      `1. ${fr ? 'Les expressions de décorateur sont évaluées de haut en bas lorsque `def` ou `class` s’exécute.' : 'Decorator expressions are evaluated top to bottom when the `def` or `class` statement executes.'}`,
      `2. ${fr ? 'Le corps de la fonction n’est pas exécuté ; un objet fonction est créé.' : 'The function body does not run; a function object is created.'}`,
      `3. ${fr ? 'Les décorateurs sont ensuite appliqués de bas en haut.' : 'The decorators are then applied bottom to top.'}`,
      '```python\n@outer\n@inner\ndef work():\n    pass\n\n# Equivalent to:\nwork = outer(inner(work))\n```',
    ].join('\n\n');
  }
  if (/\b(?:generator|yield|g[eé]n[eé]rateur)\b/i.test(question)) {
    return [
      fr ? '**Modèle d’exécution d’un générateur**' : '**Generator execution model**',
      `1. ${fr ? 'Appeler une fonction contenant `yield` crée un générateur sans exécuter son corps.' : 'Calling a function containing `yield` creates a generator without running its body.'}`,
      `2. ${fr ? '`next()` démarre ou reprend le corps jusqu’au prochain `yield`.' : '`next()` starts or resumes the body until the next `yield`.'}`,
      `3. ${fr ? 'La valeur est produite et l’état local est suspendu.' : 'The value is produced and local state is suspended.'}`,
      `4. ${fr ? 'Un `return` ou la fin du corps déclenche `StopIteration`.' : 'A `return` or reaching the end raises `StopIteration`.'}`,
      '```python\ndef numbers():\n    yield 1\n    yield 2\n\ngen = numbers()  # body has not run\nfirst = next(gen) # runs through yield 1\n```',
    ].join('\n\n');
  }
  if (/\b(?:import|module|importation)\b/i.test(question)) {
    return [
      fr ? '**Ordre d’exécution d’une importation**' : '**Import execution order**',
      `1. ${fr ? 'Python cherche d’abord le nom dans `sys.modules`.' : 'Python first checks the name in `sys.modules`.'}`,
      `2. ${fr ? 'S’il est absent, le système d’importation trouve et crée le module.' : 'If absent, the import system locates and creates the module.'}`,
      `3. ${fr ? 'Le code de niveau module s’exécute de haut en bas une fois pour cette instance de module.' : 'Module-level code executes top to bottom once for that module instance.'}`,
      `4. ${fr ? 'Le module est mis en cache ; une importation ultérieure réutilise normalement le même objet.' : 'The module is cached; a later import normally reuses the same object.'}`,
      fr ? 'Une importation circulaire peut observer un module seulement partiellement initialisé.' : 'A circular import can observe a module that is only partially initialized.',
    ].join('\n\n');
  }
  if (/\b(?:short[- ]?circuit|\band\b|\bor\b|court-circuit)\b/i.test(question)) {
    return [
      fr ? '**Évaluation booléenne avec court-circuit**' : '**Boolean short-circuit evaluation**',
      `1. ${fr ? 'Python évalue les opérandes de gauche à droite.' : 'Python evaluates operands left to right.'}`,
      `2. \`a and b\` ${fr ? 'renvoie `a` s’il est faux ; sinon il évalue et renvoie `b`.' : 'returns `a` when it is falsy; otherwise it evaluates and returns `b`.'}`,
      `3. \`a or b\` ${fr ? 'renvoie `a` s’il est vrai ; sinon il évalue et renvoie `b`.' : 'returns `a` when it is truthy; otherwise it evaluates and returns `b`.'}`,
      `4. ${fr ? 'Ces opérateurs renvoient un opérande, pas nécessairement un `bool`.' : 'These operators return an operand, not necessarily a `bool`.'}`,
      '```python\nname = supplied_name or "Guest"\nvalid = value is not None and value > 0\n```',
    ].join('\n\n');
  }
  if (/\b(?:function calls?|call order|argument evaluation|appel de fonction|ordre des arguments?)\b/i.test(question)) {
    return [
      fr ? '**Ordre d’un appel de fonction**' : '**Function-call execution order**',
      `1. ${fr ? 'Évaluer l’expression qui produit l’objet appelable.' : 'Evaluate the expression that produces the callable.'}`,
      `2. ${fr ? 'Évaluer les arguments de gauche à droite, y compris les déballages `*` et `**`.' : 'Evaluate arguments left to right, including `*` and `**` unpacking.'}`,
      `3. ${fr ? 'Associer les valeurs aux paramètres positionnels, nommés, variadiques et par défaut.' : 'Bind values to positional, keyword, variadic, and default parameters.'}`,
      `4. ${fr ? 'Exécuter le corps jusqu’à `return`, une exception ou la fin.' : 'Execute the body until `return`, an exception, or the end.'}`,
      `5. ${fr ? 'La fin sans `return` explicite produit `None`.' : 'Reaching the end without explicit `return` produces `None`.'}`,
    ].join('\n\n');
  }
  if (/\blambda\b/i.test(question)) {
    return [
      fr ? '**Ordre d’évaluation d’une lambda**' : '**Lambda evaluation order**',
      `1. ${fr ? 'Python crée la fonction sans exécuter son expression.' : 'Python creates the function without running its expression.'}`,
      `2. ${fr ? 'Lors de l’appel, les expressions des arguments sont évaluées de gauche à droite.' : 'At call time, argument expressions are evaluated left to right.'}`,
      `3. ${fr ? 'Les paramètres reçoivent les valeurs, puis l’unique expression après `:` est évaluée.' : 'Parameters receive the values, then the single expression after `:` is evaluated.'}`,
      `4. ${fr ? 'Le résultat de cette expression est renvoyé automatiquement.' : 'That expression result is returned automatically.'}`,
      '```python\ndouble = lambda number: number * 2\nresult = double(5)  # 10\n```',
    ].join('\n\n');
  }
  return [
    fr ? '**Ordre d’une compréhension**' : '**Comprehension evaluation order**',
    `1. ${fr ? 'Évaluez l’itérable du premier `for`.' : 'Evaluate the first `for` iterable.'}`,
    `2. ${fr ? 'Liez la variable de boucle à chaque élément.' : 'Bind the loop variable to each item.'}`,
    `3. ${fr ? 'Évaluez les clauses `for` suivantes puis les filtres `if`, de gauche à droite.' : 'Evaluate later `for` clauses and then `if` filters, left to right.'}`,
    `4. ${fr ? 'Si les filtres réussissent, évaluez l’expression de sortie (ou la paire clé/valeur).' : 'When filters pass, evaluate the output expression (or key/value pair).'}`,
    '```python\nsquares = [number ** 2 for number in range(6) if number % 2 == 0]\n# [0, 4, 16]\n```',
  ].join('\n\n');
};

const classificationSubject = (question: string): string | null => {
  const cleaned = question.replace(/[`"']/g, '').replace(/[?!]+$/g, '').trim();
  const patterns = [
    /\bis\s+(.+?)\s+(?:a|an)\s+(?:(?:string|str|list|dict|dictionary|set|tuple|built[- ]?in)\s+)?(?:function|method|keyword|operator|type|class|protocol|expression|statement)\b/i,
    /\bwhat\s+(?:kind|type|category)\s+of\s+(?:python\s+)?(?:thing|object|construct)\s+is\s+(.+)$/i,
    /\bclassify\s+(.+)$/i,
    /\best-ce que\s+(.+?)\s+est\s+(?:un|une)\b/i,
    /\bquel(?:le)?\s+(?:type|cat[eé]gorie).+?\s+est\s+(.+)$/i,
    /\bclasse\s+(.+)$/i,
  ];
  for (const pattern of patterns) {
    const match = cleaned.match(pattern);
    if (match?.[1]) return normalizeTerm(match[1].replace(/\(\)$/g, ''));
  }
  return null;
};

const SPECIAL_CLASSIFICATIONS: Record<string, { kind: string; behavior: string; syntax: string; distinction: string }> = {
  yield: { kind: 'keyword and expression', behavior: 'Suspends a generator and produces a value to its caller.', syntax: 'yield value', distinction: 'Using `yield` makes the enclosing function a generator function; it is not a normal function call.' },
  lambda: { kind: 'keyword that starts a lambda expression', behavior: 'Creates an anonymous function whose single expression is returned automatically.', syntax: 'lambda parameters: expression', distinction: 'A lambda is an expression, while `def` is a statement.' },
  range: { kind: 'built-in immutable sequence type', behavior: 'Calling it constructs a lazy arithmetic sequence object.', syntax: 'range(stop) or range(start, stop, step)', distinction: '`range` is technically a type/class, not a regular user-defined function.' },
  list: { kind: 'built-in mutable sequence type', behavior: 'Stores ordered values and supports indexed mutation.', syntax: 'list(iterable) or [items]', distinction: '`list` is a type; `list()` constructs an instance and `[]` is a list display.' },
  dict: { kind: 'built-in mutable mapping type', behavior: 'Maps unique hashable keys to values.', syntax: 'dict(...) or {key: value}', distinction: '`dict` is a type; methods such as `dict.get` belong to its instances.' },
  print: { kind: 'built-in function', behavior: 'Writes textual representations to a stream and returns `None`.', syntax: 'print(*objects, sep=" ", end="\\n", file=None, flush=False)', distinction: 'It displays values; it does not return the displayed value.' },
};

export const answerPythonClassificationQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const subject = classificationSubject(question);
  if (!subject) return null;
  const fr = language === 'fr';
  const special = SPECIAL_CLASSIFICATIONS[subject.toLowerCase()];
  const resolution = resolvePythonKnowledge(subject, typeFromPrefix(subject));
  if (!special && !resolution.record && !resolution.alternatives.length) return null;
  if (resolution.alternatives.length) {
    return [
      fr ? `**Classification ambiguë : \`${subject}\`**` : `**Ambiguous classification: \`${subject}\`**`,
      fr ? 'Ce nom a plusieurs classifications selon son propriétaire :' : 'This name has multiple classifications depending on its owner:',
      ...resolution.alternatives.map((record, index) => `${index + 1}. \`${record.signature}\` — ${record.kind === 'builtin' ? (fr ? 'fonction intégrée' : 'built-in function') : `${record.kind} ${fr ? 'méthode' : 'method'}`}`),
      fr ? `Précisez le propriétaire, par exemple \`str.${subject}\` ou \`list.${subject}\`.` : `Specify the owner, for example \`str.${subject}\` or \`list.${subject}\`.`,
    ].join('\n\n');
  }
  const record = resolution.record;
  const kind = special?.kind || (record?.kind === 'builtin' ? 'built-in function' : record?.kind === 'keyword' ? 'keyword' : record?.kind === 'concept' ? 'Python concept' : `${record?.kind} method`);
  const behavior = special?.behavior || record?.summary || '';
  const syntax = special?.syntax || record?.signature || subject;
  const distinction = special?.distinction || (record?.kind && !['builtin', 'keyword', 'concept'].includes(record.kind)
    ? `It must be accessed through a ${record.kind} object (or through the owner type); it is not a standalone built-in function.`
    : 'Its classification determines where it can appear and how Python invokes it.');
  return [
    fr ? `**Classification Python : \`${subject}\`**` : `**Python classification: \`${subject}\`**`,
    `1. **${fr ? 'Classification exacte' : 'Exact classification'}**\n${fr ? localizeAiText(kind, 'fr') : kind}.`,
    `2. **${fr ? 'Pourquoi' : 'Why'}**\n${fr ? localizeAiText(behavior, 'fr') : behavior}`,
    `3. **${fr ? 'Forme correcte' : 'Correct form'}**\n\`${syntax}\``,
    `4. **${fr ? 'Distinction importante' : 'Important distinction'}**\n${fr ? localizeAiText(distinction, 'fr') : distinction}`,
    record?.sourceUrl ? `5. **${fr ? 'Source' : 'Source'}**\n${record.sourceUrl}` : '',
  ].filter(Boolean).join('\n\n');
};

type ProtocolRecord = { definition: string; methods: string; examples: string; relation: string; check: string };
const PROTOCOLS: Record<string, ProtocolRecord> = {
  iterable: { definition: 'An object that can produce an iterator.', methods: '`__iter__()` or sequence-style `__getitem__()`', examples: '`list`, `tuple`, `str`, `dict`, `set`, `range`, generators', relation: 'Every iterator is iterable, but a reusable iterable is not necessarily an iterator.', check: 'isinstance(value, collections.abc.Iterable)' },
  iterator: { definition: 'A stateful, single-pass object that produces the next value.', methods: '`__iter__()` returning itself and `__next__()`', examples: '`iter([1, 2])`, `enumerate(...)`, `zip(...)`, generator objects', relation: 'An iterator is also iterable. Exhaustion is reported with `StopIteration`.', check: 'isinstance(value, collections.abc.Iterator)' },
  generator: { definition: 'An iterator created by a generator function or generator expression.', methods: '`__iter__()`, `__next__()`, `send()`, `throw()`, `close()`', examples: '`(x * 2 for x in values)` or a function containing `yield`', relation: 'Every generator object is an iterator and iterable; a generator function is a callable that creates one.', check: 'isinstance(value, types.GeneratorType)' },
  sequence: { definition: 'An ordered collection supporting integer indexing and usually slicing.', methods: '`__len__()`, `__getitem__()`, plus sequence operations', examples: '`list`, `tuple`, `str`, `range`, `bytes`', relation: 'Sequences are iterable, but sets, mappings, and generators are iterable without being sequences.', check: 'isinstance(value, collections.abc.Sequence)' },
  mapping: { definition: 'An object that associates hashable keys with values.', methods: '`__getitem__(key)`, `__iter__()`, `__len__()`', examples: '`dict`, `collections.defaultdict`, `collections.ChainMap`', relation: 'A mapping iterates over keys by default and is not a positional sequence.', check: 'isinstance(value, collections.abc.Mapping)' },
  hashable: { definition: 'An object with a stable hash value that can participate in equality comparisons.', methods: '`__hash__()` and compatible `__eq__()` behavior', examples: 'numbers, strings, bytes, and tuples whose elements are hashable', relation: 'Hashable objects can be dictionary keys and set elements. Mutable containers are normally unhashable.', check: 'isinstance(value, collections.abc.Hashable)' },
  mutable: { definition: 'An object whose observable state or contents can change without replacing the object.', methods: 'No universal mutable protocol; each type exposes its own mutating operations.', examples: '`list`, `dict`, `set`, `bytearray`, and most user-defined instances', relation: 'Mutability is an object property, not the same as variable reassignment. Mutable built-in containers are normally unhashable.', check: 'Check the concrete type contract; Python has no universal Mutable ABC.' },
  immutable: { definition: 'An object whose value cannot be changed after construction.', methods: 'No universal immutable protocol; operations create or return other objects.', examples: '`int`, `float`, `bool`, `str`, `bytes`, `tuple`, `frozenset`, `range`', relation: 'An immutable container is hashable only when all values participating in its hash are hashable.', check: 'Check the concrete type contract; Python has no universal Immutable ABC.' },
  callable: { definition: 'An object that Python can invoke with call syntax.', methods: '`__call__()`', examples: 'functions, classes, bound methods, and instances defining `__call__`', relation: 'A callable is not necessarily a function; classes and callable instances are separate kinds.', check: 'callable(value)' },
  descriptor: { definition: 'An object that controls attribute lookup, assignment, or deletion on another class.', methods: '`__get__()`, `__set__()`, and/or `__delete__()`', examples: '`property`, functions stored on classes, `classmethod`, `staticmethod`', relation: 'Data descriptors outrank instance attributes; non-data descriptors can be shadowed by them.', check: 'hasattr(type(value), "__get__")' },
  'context manager': { definition: 'An object that establishes and reliably cleans up a runtime context.', methods: '`__enter__()` and `__exit__()` (or async variants)', examples: 'files, locks, database transactions, `contextlib` managers', relation: 'The `with` statement invokes the protocol and calls cleanup even when the body raises.', check: 'hasattr(value, "__enter__") and hasattr(value, "__exit__")' },
  awaitable: { definition: 'An object whose completion can be suspended on with `await`.', methods: '`__await__()`', examples: 'coroutine objects, `asyncio.Task`, `asyncio.Future`', relation: 'Coroutine objects are awaitable, but an arbitrary awaitable need not be a coroutine.', check: 'isinstance(value, collections.abc.Awaitable)' },
  'async iterable': { definition: 'An object that can create an asynchronous iterator.', methods: '`__aiter__()`', examples: 'asynchronous streams and objects used by `async for`', relation: 'An async iterable is consumed with `async for`, not ordinary `for` unless it also implements the synchronous protocol.', check: 'isinstance(value, collections.abc.AsyncIterable)' },
  'async iterator': { definition: 'A stateful object that asynchronously produces its next value.', methods: '`__aiter__()` returning itself and `__anext__()` returning an awaitable', examples: 'asynchronous generator objects', relation: 'Every async iterator is an async iterable; exhaustion is reported with `StopAsyncIteration`.', check: 'isinstance(value, collections.abc.AsyncIterator)' },
};

const PROTOCOL_ALIASES: Record<string, string> = { 'it[eé]rable': 'iterable', 'it[eé]rateur': 'iterator', 'g[eé]n[eé]rateur': 'generator', 's[eé]quence': 'sequence', mappage: 'mapping', 'hac?chable': 'hashable', appelable: 'callable', descripteur: 'descriptor', 'gestionnaire de contexte': 'context manager' };

const findProtocol = (question: string): string | null => Object.keys(PROTOCOLS)
  .sort((left, right) => right.length - left.length)
  .find(name => new RegExp(`\\b${name.replace(' ', '[- ]')}s?\\b`, 'i').test(question))
  || Object.entries(PROTOCOL_ALIASES).find(([alias]) => new RegExp(`\\b${alias}s?\\b`, 'i').test(question))?.[1]
  || null;

export const answerPythonProtocolQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const name = findProtocol(question);
  if (!name) return null;
  const fr = language === 'fr';
  const item = PROTOCOLS[name];
  return [
    fr ? `**Taxonomie et protocole : ${localizeAiText(name, 'fr')}**` : `**Python taxonomy and protocol: ${name}**`,
    `1. **${fr ? 'Définition' : 'Definition'}**\n${fr ? localizeAiText(item.definition, 'fr') : item.definition}`,
    `2. **${fr ? 'Contrat minimal' : 'Minimum contract'}**\n${item.methods}`,
    `3. **${fr ? 'Exemples' : 'Examples'}**\n${item.examples}`,
    `4. **${fr ? 'Relation et limite' : 'Relationship and boundary'}**\n${fr ? localizeAiText(item.relation, 'fr') : item.relation}`,
    `5. **${fr ? 'Vérification pratique' : 'Practical check'}**\n\`${item.check}\``,
  ].join('\n\n');
};

const SYNTAX_ROLES: Record<string, string[]> = {
  '*': ['multiplication: `left * right`', 'iterable unpacking: `[*items]` or `func(*args)`', 'collecting positional arguments: `def func(*args)`', 'keyword-only separator in a signature: `def func(value, *, option=False)`'],
  '**': ['exponentiation: `base ** power`', 'mapping unpacking: `{**mapping}` or `func(**kwargs)`', 'collecting keyword arguments: `def func(**kwargs)`'],
  '/': ['true division: `left / right`', 'positional-only separator inside a function signature'],
  '//': ['floor division: `left // right`'],
  ':=': ['assignment expression (walrus): assign a value while an expression is being evaluated'],
  '->': ['return annotation in a function definition; it documents a type and is not runtime return control'],
  '@': ['matrix multiplication operator', 'decorator prefix above a function or class'],
  ':': ['starts an indented suite after statements such as `if`, `for`, `def`, and `class`', 'separates keys from values in dictionaries', 'separates slice bounds', 'separates parameters from the expression in a lambda'],
  '.': ['attribute or method access: `object.name`', 'decimal point in a numeric literal', 'relative-import level when used in `from . import name`'],
  ',': ['separates items or arguments', 'creates a tuple through comma syntax: `value,`'],
  '[]': ['list display: `[1, 2]`', 'subscription/indexing: `items[0]`', 'slicing: `items[start:stop:step]`', 'generic type parameters: `list[int]`'],
  '{}': ['dictionary display when it contains key-value pairs', 'set display when it contains values', 'replacement fields in format strings'],
  '()': ['function or callable invocation', 'grouping to control precedence', 'tuple display when commas are present', 'generator expression delimiters'],
  '_': ['ordinary identifier character', 'conventional throwaway name', 'previous result in the interactive interpreter', 'wildcard in structural pattern matching'],
};

export const answerPythonSyntaxRoleQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const token = Object.keys(SYNTAX_ROLES).sort((a, b) => b.length - a.length).find(candidate => question.includes(`\`${candidate}\``) || question.includes(`"${candidate}"`) || question.includes(`'${candidate}'`));
  if (!token) return null;
  const fr = language === 'fr';
  const roles = SYNTAX_ROLES[token];
  return [
    fr ? `**Rôles syntaxiques de \`${token}\`**` : `**Syntax roles of \`${token}\`**`,
    fr ? 'Ce symbole dépend de son contexte. Python détermine son rôle à partir de l’endroit où il apparaît :' : 'This symbol is context-sensitive. Python determines its role from where it appears:',
    ...roles.map((role, index) => `${index + 1}. ${fr ? localizeAiText(role, 'fr') : role}.`),
    fr ? 'Pour une réponse exacte sur une ligne particulière, fournissez cette ligne de code.' : 'For an exact answer about a particular line, provide that line of code.',
  ].join('\n\n');
};

export const isKnowledgeFollowUpQuestion = (question: string): boolean => {
  const trimmed = question.trim();
  if (/```|(^|\n)\s*(?:def |class |for |while |if |import |from |return |yield |[A-Za-z_]\w*\s*=)/m.test(trimmed)) return false;
  return /^(?:go deeper|more detail|explain more|break it down|approfondis|plus de details?|examples?|give (?:another )?examples?|show (?:another )?examples?|simplify|explain simply|explique simplement)\b/i.test(trimmed)
    || /\b(?:it|this|that|them|those|cela|ca|ceci|il|elle|eux)\b/i.test(trimmed);
};

export const selectKnowledgeContextQuestion = (newestFirstQuestions: string[]): string => (
  newestFirstQuestions.find(question => !isKnowledgeFollowUpQuestion(question))
  || newestFirstQuestions[0]
  || ''
);

const PYTHON_DOCS = 'https://docs.python.org/3';

const CATEGORY_DOCS: Record<string, string> = {
  abstract_syntax_trees: `${PYTHON_DOCS}/library/ast.html`,
  asynchronous_programming: `${PYTHON_DOCS}/library/asyncio.html`,
  built_in_data_types: `${PYTHON_DOCS}/library/stdtypes.html`,
  classes_and_oop: `${PYTHON_DOCS}/tutorial/classes.html`,
  closures: `${PYTHON_DOCS}/reference/executionmodel.html#binding-of-names`,
  collections_module: `${PYTHON_DOCS}/library/collections.html`,
  comprehensions: `${PYTHON_DOCS}/tutorial/datastructures.html#list-comprehensions`,
  context_managers: `${PYTHON_DOCS}/reference/datamodel.html#context-managers`,
  control_flow: `${PYTHON_DOCS}/tutorial/controlflow.html`,
  dataclasses: `${PYTHON_DOCS}/library/dataclasses.html`,
  date_and_time: `${PYTHON_DOCS}/library/datetime.html`,
  debugging: `${PYTHON_DOCS}/library/debug.html`,
  decorators: `${PYTHON_DOCS}/glossary.html#term-decorator`,
  descriptors: `${PYTHON_DOCS}/howto/descriptor.html`,
  docstrings: `${PYTHON_DOCS}/glossary.html#term-docstring`,
  exceptions: `${PYTHON_DOCS}/library/exceptions.html`,
  file_handling: `${PYTHON_DOCS}/tutorial/inputoutput.html#reading-and-writing-files`,
  functools: `${PYTHON_DOCS}/library/functools.html`,
  functions: `${PYTHON_DOCS}/reference/compound_stmts.html#function-definitions`,
  generators: `${PYTHON_DOCS}/glossary.html#term-generator`,
  introspection_and_reflection: `${PYTHON_DOCS}/library/inspect.html`,
  iteration: `${PYTHON_DOCS}/glossary.html#term-iterator`,
  itertools: `${PYTHON_DOCS}/library/itertools.html`,
  logging: `${PYTHON_DOCS}/library/logging.html`,
  memory_management: `${PYTHON_DOCS}/c-api/memory.html`,
  metaclasses: `${PYTHON_DOCS}/reference/datamodel.html#metaclasses`,
  modules_and_imports: `${PYTHON_DOCS}/reference/import.html`,
  multiprocessing: `${PYTHON_DOCS}/library/multiprocessing.html`,
  numbers: `${PYTHON_DOCS}/library/stdtypes.html#numeric-types-int-float-complex`,
  objects_and_object_model: `${PYTHON_DOCS}/reference/datamodel.html`,
  operators: `${PYTHON_DOCS}/reference/expressions.html`,
  packages_and_project_structure: `${PYTHON_DOCS}/tutorial/modules.html#packages`,
  pathlib: `${PYTHON_DOCS}/library/pathlib.html`,
  performance: `${PYTHON_DOCS}/library/profile.html`,
  protocols_and_abstract_base_classes: `${PYTHON_DOCS}/library/abc.html`,
  python_fundamentals: `${PYTHON_DOCS}/tutorial/`,
  regular_expressions: `${PYTHON_DOCS}/library/re.html`,
  security: `${PYTHON_DOCS}/library/security_warnings.html`,
  serialization: `${PYTHON_DOCS}/library/persistence.html`,
  special_methods: `${PYTHON_DOCS}/reference/datamodel.html#special-method-names`,
  strings: `${PYTHON_DOCS}/library/stdtypes.html#text-sequence-type-str`,
  testing: `${PYTHON_DOCS}/library/development.html#testing`,
  threading: `${PYTHON_DOCS}/library/threading.html`,
  type_hints: `${PYTHON_DOCS}/library/typing.html`,
  variables_and_names: `${PYTHON_DOCS}/reference/executionmodel.html#naming-and-binding`,
};

const THIRD_PARTY_SOURCES: Record<string, [string, string]> = {
  django: ['Django documentation', 'https://docs.djangoproject.com/'],
  fastapi: ['FastAPI documentation', 'https://fastapi.tiangolo.com/'],
  flask: ['Flask documentation', 'https://flask.palletsprojects.com/'],
  matplotlib: ['Matplotlib documentation', 'https://matplotlib.org/stable/'],
  numpy: ['NumPy documentation', 'https://numpy.org/doc/stable/'],
  pandas: ['pandas documentation', 'https://pandas.pydata.org/docs/'],
  requests: ['Requests documentation', 'https://requests.readthedocs.io/'],
  scipy: ['SciPy documentation', 'https://docs.scipy.org/doc/scipy/'],
  seaborn: ['seaborn documentation', 'https://seaborn.pydata.org/'],
  sys: ['Official Python sys module documentation', `${PYTHON_DOCS}/library/sys.html`],
  xgboost: ['XGBoost documentation', 'https://xgboost.readthedocs.io/'],
  yaml: ['PyYAML documentation', 'https://pyyaml.org/wiki/PyYAMLDocumentation'],
};

const VERSION_NOTES: Record<string, string> = {
  '@dataclass': 'Added in Python 3.7.',
  'asyncio': 'The asyncio package was added in Python 3.4; async/await syntax was added in Python 3.5.',
  'async/await': 'The async and await syntax was added in Python 3.5.',
  'breakpoint': 'Added in Python 3.7.',
  'dataclass': 'Added in Python 3.7.',
  'exceptiongroup': 'Added in Python 3.11.',
  'f-string': 'Added in Python 3.6.',
  'match': 'Structural pattern matching was added in Python 3.10.',
  'match statement': 'Structural pattern matching was added in Python 3.10.',
  'removeprefix': 'Added in Python 3.9.',
  'removesuffix': 'Added in Python 3.9.',
  'tomllib': 'Added in Python 3.11.',
  'type statement': 'Added in Python 3.12.',
  'walrus': 'Assignment expressions were added in Python 3.8.',
  'walrus operator': 'Assignment expressions were added in Python 3.8.',
  'zoneinfo': 'Added in Python 3.9.',
};

const CONCEPT_FIRST_TERMS = new Set([
  'bool', 'boolean', 'bytearray', 'bytes', 'class', 'complex', 'dict', 'dictionary',
  'float', 'function', 'int', 'integer', 'list', 'none', 'object', 'set', 'str',
  'string', 'sys', 'tuple', 'type',
]);

const FRENCH_KIND: Record<string, string> = {
  builtin: 'fonction intégrée',
  concept: 'concept Python',
  dict: 'méthode de dictionnaire',
  keyword: 'mot-clé Python',
  list: 'méthode de liste',
  set: 'méthode d\'ensemble',
  str: 'méthode de chaîne',
  tuple: 'méthode de tuple',
};

const FRENCH_CATEGORY: Record<string, string> = {
  abstract_syntax_trees: 'arbres syntaxiques abstraits',
  asynchronous_programming: 'programmation asynchrone',
  built_in_data_types: 'types de données intégrés',
  classes_and_oop: 'classes et programmation orientée objet',
  closures: 'fermetures',
  collections_module: 'collections specialisees',
  comprehensions: 'comprehensions',
  context_managers: 'gestionnaires de contexte',
  control_flow: 'controle du flux',
  dataclasses: 'classes de donnees',
  date_and_time: 'dates et heures',
  debugging: 'débogage',
  decorators: 'décorateurs',
  descriptors: 'descripteurs',
  docstrings: 'chaînes de documentation',
  exceptions: 'exceptions',
  file_handling: 'gestion des fichiers',
  functools: 'outils de fonctions',
  functions: 'fonctions',
  generators: 'generateurs',
  introspection_and_reflection: 'introspection et reflexion',
  iteration: 'itération',
  itertools: 'outils d\'itération',
  logging: 'journalisation',
  memory_management: 'gestion de la mémoire',
  metaclasses: 'métaclasses',
  modules_and_imports: 'modules et importations',
  multiprocessing: 'multiprocessus',
  numbers: 'nombres',
  objects_and_object_model: 'objets et modèle objet',
  operators: 'opérateurs',
  packages_and_project_structure: 'paquets et structure de projet',
  pathlib: 'chemins de fichiers',
  performance: 'performances',
  protocols_and_abstract_base_classes: 'protocoles et classes abstraites',
  python_fundamentals: 'fondamentaux de Python',
  regular_expressions: 'expressions régulières',
  security: 'sécurité',
  serialization: 'sérialisation',
  special_methods: 'méthodes spéciales',
  strings: 'chaînes de caractères',
  testing: 'tests',
  threading: 'threads',
  type_hints: 'annotations de type',
  variables_and_names: 'variables et noms',
};

const FRENCH_PRECISE_SUMMARY: Record<string, string> = {
  boolean: 'Un booléen représente une valeur logique : `True` ou `False`. Il est utilisé dans les conditions, les comparaisons et les décisions du programme.',
  class: 'Une classe est un modèle qui définit les données et les comportements partagés par les objets créés à partir de cette classe.',
  closure: 'Une fermeture est une fonction interne qui conserve l’accès aux variables de sa portée englobante, même après la fin de la fonction externe.',
  comprehension: 'Une compréhension construit une collection avec une expression, une ou plusieurs boucles et éventuellement une condition de filtrage.',
  dict: 'Un dictionnaire stocke des paires clé-valeur. Chaque clé unique permet de retrouver sa valeur sans utiliser une position numérique.',
  dictionary: 'Un dictionnaire stocke des paires clé-valeur. Chaque clé unique permet de retrouver sa valeur sans utiliser une position numérique.',
  function: 'Une fonction est un bloc de code réutilisable défini avec `def`. Elle peut recevoir des arguments et renvoyer une valeur avec `return`.',
  lambda: 'Une expression `lambda` crée une petite fonction anonyme limitée à une seule expression.',
  list: 'Une liste est une collection ordonnée et modifiable. Elle utilise des crochets, par exemple `[1, 2, 3]`, et peut contenir différents types de valeurs.',
  method: 'Une méthode est une fonction attachée à une classe ou à un objet et appelée avec la notation pointée, par exemple `objet.methode()`.',
  object: 'Un objet est une instance concrète d’une classe. Il possède une identité, un type, des attributs et éventuellement des méthodes.',
  set: 'Un ensemble est une collection non ordonnée de valeurs uniques. Il élimine les doublons et prend en charge l’union, l’intersection et la différence.',
  str: 'Une chaîne représente du texte sous forme d’une séquence Unicode immuable, écrite entre guillemets simples ou doubles.',
  string: 'Une chaîne représente du texte sous forme d’une séquence Unicode immuable, écrite entre guillemets simples ou doubles.',
  sys: 'Le module `sys` donne accès à l’interpréteur Python en cours d’exécution, aux arguments de ligne de commande, aux chemins d’importation, aux modules chargés et aux flux standard.',
  tuple: 'Un tuple est une collection ordonnée et immuable. Il utilise généralement des parenthèses, par exemple `(1, 2, 3)`.',
  asyncio: '`asyncio` est le cadre de la bibliothèque standard pour les entrées-sorties asynchrones, les coroutines, les tâches et les boucles d\'événements.',
  csv: '`csv` est le module de la bibliothèque standard qui lit et écrit des données tabulaires séparées par des délimiteurs, notamment les fichiers CSV.',
  django: 'Django est un framework web Python complet avec routage, modèles, formulaires, authentification et ORM.',
  fastapi: 'FastAPI est un framework Python pour construire des API HTTP typées avec validation et documentation OpenAPI automatique.',
  flask: 'Flask est un framework web Python léger qui fournit le routage, les requêtes, les réponses et un système d\'extensions.',
  matplotlib: 'Matplotlib est une bibliothèque Python qui crée des graphiques et des figures statiques, animés ou interactifs.',
  numpy: 'NumPy est une bibliothèque de calcul numérique centrée sur les tableaux multidimensionnels et les opérations vectorisées.',
  pandas: 'pandas est une bibliothèque d\'analyse de données centrée sur les objets `Series` et `DataFrame`.',
  pathlib: '`pathlib` est le module de la bibliothèque standard pour manipuler les chemins de fichiers sous forme d\'objets.',
  requests: 'Requests est une bibliothèque cliente HTTP pour envoyer des requêtes et traiter les réponses, sessions, en-têtes et cookies.',
  threading: '`threading` est le module de la bibliothèque standard pour créer et coordonner des threads qui partagent la mémoire d\'un processus.',
  xgboost: 'XGBoost est une bibliothèque d\'apprentissage automatique qui implémente des arbres de décision optimisés par gradient boosting.',
};

const localizedKnowledgeSummary = (record: PythonKnowledgeRecord, language: KnowledgeLanguage): string => {
  if (language !== 'fr') return record.summary;
  const precise = FRENCH_PRECISE_SUMMARY[record.term.toLowerCase()]
    || FRENCH_PRECISE_SUMMARY[record.canonicalName.toLowerCase()];
  if (precise) return precise;
  const translated = localizeAiText(record.summary, 'fr');
  const category = FRENCH_CATEGORY[record.category] || record.category.replace(/_/g, ' ');
  if (translated !== record.summary && !/\b(?:is|the|returns|creates|used|with|from|and|this|that|library)\b/i.test(translated)) return translated;
  return `\`${record.canonicalName}\` est un terme Python du domaine ${category}. Sa définition exacte et sa syntaxe sont vérifiées dans la source indiquée.`;
};

const normalizeTerm = (value: string): string => {
  const raw = value.trim();
  const withoutQuestionMark = /^[?!]+$/.test(raw) ? raw : raw.replace(/[?!]+$/g, '');
  return withoutQuestionMark
    .replace(/^(?:a|an|the)\s+/i, '')
    .replace(/\s+in python$/i, '')
    .replace(/^([A-Za-z_]\w*)\(\)$/, '$1')
    .trim();
};

const typeFromPrefix = (term: string): string | undefined => {
  const match = term.toLowerCase().match(/^(str|string|list|dict|dictionary|set|tuple)\./);
  return match?.[1].replace('string', 'str').replace('dictionary', 'dict');
};

const sourceForCategory = (category: string, term: string): [string, string] => {
  const thirdParty = THIRD_PARTY_SOURCES[term.toLowerCase()];
  if (thirdParty) return thirdParty;
  return ['Official Python documentation', CATEGORY_DOCS[category] || `${PYTHON_DOCS}/`];
};

const inferMutation = (entry: RefEntry): PythonKnowledgeRecord['mutates'] => {
  const text = `${entry.desc} ${entry.example}`.toLowerCase();
  if (/modif(?:y|ies|ied)|in place|adds item|removes all|extends the list|updates the/.test(text)) return 'yes';
  if (entry.type === 'builtin') return ['delattr', 'exec', 'setattr'].includes(entry.name) ? 'depends' : 'no';
  if (entry.type === 'str' || entry.type === 'tuple') return 'no';
  if (/returns? (?:a |an |the )?(?:copy|new|iterator|value|number|string|list|tuple|set|dictionary|boolean)/.test(text)) return 'no';
  return entry.type === 'keyword' || entry.type === 'concept' ? 'not-applicable' : 'depends';
};

const inferRaises = (description: string): string => {
  const matches = [...description.matchAll(/raises?\s+([A-Z][A-Za-z]+Error)/g)].map(match => match[1]);
  return matches.length ? [...new Set(matches)].join(', ') : 'No specific exception is guaranteed; invalid types or values may still raise an exception.';
};

const recordFromReference = (term: string, entry: RefEntry): PythonKnowledgeRecord => {
  const category = entry.type === 'builtin' ? 'built_in_data_types'
    : entry.type === 'keyword' ? 'python_fundamentals'
      : entry.type === 'concept' ? 'python_fundamentals'
        : entry.type === 'str' ? 'strings'
          : 'built_in_data_types';
  const [sourceLabel, sourceUrl] = entry.type === 'builtin'
    ? ['Official Python built-in functions', `${PYTHON_DOCS}/library/functions.html#${entry.name}`]
    : entry.type === 'keyword'
      ? ['Official Python language reference', `${PYTHON_DOCS}/reference/lexical_analysis.html#keywords`]
      : sourceForCategory(category, term);
  const mutates = inferMutation(entry);
  return {
    term,
    canonicalName: entry.name,
    kind: entry.type,
    category,
    summary: entry.desc,
    details: entry.desc,
    signature: entry.signature,
    returns: mutates === 'yes' ? 'Usually `None` when the operation mutates the object in place.' : entry.desc,
    mutates,
    raises: inferRaises(entry.desc),
    examples: [{ title: 'Verified API example', code: entry.example }],
    related: [],
    version: VERSION_NOTES[entry.name.toLowerCase()] || 'See the linked current Python 3 documentation for version-specific behavior.',
    sourceLabel,
    sourceUrl,
    confidence: 'authoritative',
  };
};

const recordFromConceptEntry = (term: string, entry: ConceptEntry): PythonKnowledgeRecord => {
  const [sourceLabel, sourceUrl] = sourceForCategory(entry.category, entry.name);
  return {
    term,
    canonicalName: entry.name,
    kind: 'concept',
    category: entry.category,
    summary: entry.easy,
    details: `${entry.intermediate}\n\n${entry.advanced}`,
    signature: entry.examples[0]?.code.split('\n')[0] || entry.name,
    returns: 'Depends on the operation shown in the concept.',
    mutates: 'not-applicable',
    raises: entry.commonMistakes.join('; ') || 'Depends on the operation and input values.',
    examples: entry.examples,
    related: entry.related,
    version: VERSION_NOTES[entry.name.toLowerCase()] || 'Documented for current Python 3 unless the linked source states otherwise.',
    sourceLabel,
    sourceUrl,
    confidence: 'curated',
  };
};

const recordFromCategory = (term: string, fallback: CategoryFallback): PythonKnowledgeRecord => {
  const [sourceLabel, sourceUrl] = sourceForCategory(fallback.category, term);
  return {
    term,
    canonicalName: term,
    kind: 'concept',
    category: fallback.category,
    summary: fallback.summary,
    details: `${fallback.intermediate}\n\n${fallback.advanced}`,
    signature: term,
    returns: 'Depends on the specific API, syntax form, or library represented by this term.',
    mutates: 'depends',
    raises: 'Depends on the specific operation and input values.',
    examples: [],
    related: [],
    version: VERSION_NOTES[term.toLowerCase()] || 'Verify exact availability in the linked documentation for the Python or library version in use.',
    sourceLabel,
    sourceUrl,
    confidence: 'categorized',
  };
};

export const resolvePythonKnowledge = (rawTerm: string, preferredType?: string): KnowledgeResolution => {
  const term = normalizeTerm(rawTerm);
  const prefixType = typeFromPrefix(term);
  const effectiveType = preferredType || prefixType;
  const concept = lookupConcept(term);
  if (!effectiveType && concept.entry && CONCEPT_FIRST_TERMS.has(term.toLowerCase())) {
    return { term, record: recordFromConceptEntry(term, concept.entry), alternatives: [] };
  }
  const referenceMatches = lookupAll(term);
  const filteredMatches = effectiveType ? referenceMatches.filter(entry => entry.type === effectiveType) : referenceMatches;
  if (filteredMatches.length === 1) {
    return { term, record: recordFromReference(term, filteredMatches[0]), alternatives: [] };
  }
  if (!effectiveType && referenceMatches.length > 1) {
    return { term, record: null, alternatives: referenceMatches.map(entry => recordFromReference(term, entry)) };
  }

  if (concept.entry) return { term, record: recordFromConceptEntry(term, concept.entry), alternatives: [] };
  if (concept.categoryFallback.found) return { term, record: recordFromCategory(term, concept.categoryFallback), alternatives: [] };
  return { term, record: null, alternatives: [] };
};

export const extractKnowledgeTerm = (question: string): string | null => {
  const cleaned = question.trim().replace(/[?!]+$/g, '').trim();
  if (!cleaned || /\b(?:difference between|compare|versus|\bvs\.?\b)\b/i.test(cleaned)) return null;
  const match = cleaned.match(/^(?:(?:please\s+)?(?:what(?:'s|\s+is|\s+are|\s+does)|define|describe|explain|tell\s+me\s+about|d[eé]finis?|explique|d[eé]cris|parle-moi\s+de)|can\s+you\s+(?:define|describe|explain))\s+(.+)$/i);
  if (match) return normalizeTerm(match[1].replace(/\s+(?:do|does|mean|work|to\s+me|in\s+python|en\s+python)$/i, ''));
  return cleaned.split(/\s+/).length <= 4 ? normalizeTerm(cleaned) : null;
};

const ambiguityAnswer = (resolution: KnowledgeResolution, language: KnowledgeLanguage): string => {
  const choices = resolution.alternatives.map((record, index) => {
    const label = language === 'fr' ? (FRENCH_KIND[record.kind] || record.kind) : record.kind;
    return `${index + 1}. \`${record.signature}\` - ${label}`;
  }).join('\n');
  return language === 'fr'
    ? `**Précision nécessaire pour \`${resolution.term}\`**\n\nCe nom correspond à plusieurs API Python :\n${choices}\n\nIndiquez le type, par exemple \`list.${resolution.term}\` ou \`str.${resolution.term}\`.`
    : `**Clarification needed for \`${resolution.term}\`**\n\nThis name matches several Python APIs:\n${choices}\n\nInclude the type, for example \`list.${resolution.term}\` or \`str.${resolution.term}\`.`;
};

export const formatPythonKnowledgeRecord = (record: PythonKnowledgeRecord, language: KnowledgeLanguage): string => {
  const isFrench = language === 'fr';
  const localizedOr = (value: string, fallback: string): string => {
    if (!isFrench) return value;
    const translated = localizeAiText(value, 'fr');
    return translated === value ? fallback : translated;
  };
  const frenchCategory = FRENCH_CATEGORY[record.category] || record.category.replace(/_/g, ' ');
  const summary = isFrench && record.confidence === 'categorized'
    ? (FRENCH_PRECISE_SUMMARY[record.term.toLowerCase()] || `\`${record.canonicalName}\` est un terme Python associé au domaine ${frenchCategory}.`)
    : localizedKnowledgeSummary(record, language);
  const details = isFrench && record.confidence === 'categorized'
    ? `Ce terme appartient au domaine ${frenchCategory}. Son comportement exact dépend de l\'API, de la syntaxe ou de la bibliothèque indiquée par le code. La source liée ci-dessous permet de vérifier sa signature et sa version.`
    : localizedOr(record.details, `Ce concept relève du domaine ${frenchCategory}. Son fonctionnement dépend de la syntaxe et des valeurs utilisées ; l’exemple et la source ci-dessous montrent son usage vérifié.`);
  const returns = isFrench && record.confidence === 'categorized'
    ? 'Cela dépend de l\'API ou de l\'opération précise.'
    : localizedOr(record.returns, 'La valeur renvoyée dépend de l’opération précise présentée par la signature et l’exemple.');
  const raises = isFrench && record.confidence === 'categorized'
    ? 'Les exceptions dépendent de l\'opération, des arguments et des valeurs utilisés.'
    : localizedOr(record.raises, 'Les erreurs possibles dépendent des types, des arguments et des valeurs fournis.');
  const version = isFrench && record.confidence === 'categorized'
    ? 'Vérifiez la disponibilité exacte dans la documentation liée pour la version utilisée.'
    : localizedOr(record.version, 'Consultez la source liée pour vérifier la disponibilité et le comportement de la version Python utilisée.');
  const kind = isFrench ? (FRENCH_KIND[record.kind] || record.kind) : record.kind;
  const mutation = isFrench
    ? ({ yes: 'Oui', no: 'Non', depends: 'Cela dépend', 'not-applicable': 'Sans objet' } as const)[record.mutates]
    : ({ yes: 'Yes', no: 'No', depends: 'Depends', 'not-applicable': 'Not applicable' } as const)[record.mutates];
  const exampleText = record.examples.length
    ? record.examples.slice(0, 3).map((example, index) => {
      const title = isFrench ? localizedOr(example.title, `Exemple ${index + 1}`) : example.title;
      return `${index + 1}. ${title}\n\`\`\`python\n${example.code}\n\`\`\``;
    }).join('\n\n')
    : (isFrench ? 'Aucun exemple générique n\'est inventé. Demandez un exemple avec le contexte ou le module exact.' : 'No generic example is invented. Ask with the exact module or code context for a precise example.');
  const confidence = isFrench
    ? ({ authoritative: 'source officielle', curated: 'définition vérifiée', categorized: 'définition catégorisée' } as const)[record.confidence]
    : ({ authoritative: 'official source', curated: 'curated definition', categorized: 'categorized definition' } as const)[record.confidence];

  return [
    `**${record.canonicalName}**`,
    '',
    `1. **${isFrench ? 'Définition' : 'Definition'}**\n${summary}`,
    '',
    `2. **${isFrench ? 'Type et syntaxe' : 'Kind and syntax'}**\n${kind}: \`${record.signature}\``,
    '',
    `3. **${isFrench ? 'Fonctionnement' : 'Behavior'}**\n${details}`,
    '',
    `4. **${isFrench ? 'Retour et modification' : 'Return and mutation'}**\n${isFrench ? 'Retour' : 'Returns'}: ${returns}\n${isFrench ? 'Modifie une valeur existante' : 'Mutates an existing value'}: ${mutation}`,
    '',
    `5. **${isFrench ? 'Erreurs possibles' : 'Possible errors'}**\n${raises}`,
    '',
    `6. **${isFrench ? 'Version' : 'Version'}**\n${version}`,
    '',
    `7. **${isFrench ? 'Exemples' : 'Examples'}**\n${exampleText}`,
    '',
    `8. **${isFrench ? 'Source et confiance' : 'Source and confidence'}**\n${record.sourceLabel}: ${record.sourceUrl}\n${isFrench ? 'Niveau' : 'Level'}: ${confidence}`,
  ].join('\n');
};

export const answerPythonKnowledgeQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const term = extractKnowledgeTerm(question);
  if (!term) return null;
  const preferredType = /\b(?:string|str)\b/i.test(question) ? 'str'
    : /\blist\b/i.test(question) ? 'list'
      : /\b(?:dict|dictionary)\b/i.test(question) ? 'dict'
        : /\bset\b/i.test(question) ? 'set'
          : /\btuple\b/i.test(question) ? 'tuple'
            : undefined;
  const resolution = resolvePythonKnowledge(term, preferredType);
  if (resolution.alternatives.length) return ambiguityAnswer(resolution, language);
  return resolution.record ? formatPythonKnowledgeRecord(resolution.record, language) : null;
};

export type PythonExplanationLevel = 'beginner' | 'intermediate' | 'expert';

const editDistance = (left: string, right: string): number => {
  if (left === right) return 0;
  if (!left.length) return right.length;
  if (!right.length) return left.length;
  const previous = Array.from({ length: right.length + 1 }, (_, index) => index);
  for (let row = 1; row <= left.length; row += 1) {
    let diagonal = previous[0];
    previous[0] = row;
    for (let column = 1; column <= right.length; column += 1) {
      const above = previous[column];
      previous[column] = Math.min(
        previous[column] + 1,
        previous[column - 1] + 1,
        diagonal + (left[row - 1] === right[column - 1] ? 0 : 1),
      );
      diagonal = above;
    }
  }
  return previous[right.length];
};

export const resolveFuzzyPythonTerm = (rawTerm: string): { term: string; distance: number } | null => {
  const normalized = normalizeTerm(rawTerm).toLowerCase();
  if (!/^[a-z_][a-z0-9_.-]{1,39}$/.test(normalized)) return null;
  const exact = resolvePythonKnowledge(normalized);
  if (exact.record || exact.alternatives.length) return { term: normalized, distance: 0 };
  const candidates = getAllConceptTerms()
    .filter(term => /^[a-z_][a-z0-9_.-]+$/i.test(term) && Math.abs(term.length - normalized.length) <= 2)
    .map(term => ({ term, distance: editDistance(normalized, term.toLowerCase()) }))
    .filter(candidate => candidate.distance <= (normalized.length <= 4 ? 1 : 2))
    .sort((a, b) => a.distance - b.distance || a.term.length - b.term.length || a.term.localeCompare(b.term));
  if (!candidates.length) return null;
  if (candidates[1] && candidates[1].distance === candidates[0].distance && candidates[1].term.length === candidates[0].term.length) return null;
  return candidates[0];
};

export const answerPythonBareOrFuzzyQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const value = question.trim().replace(/[?!]+$/g, '');
  if (!/^[A-Za-z_][A-Za-z0-9_.-]*(?:\(\))?$/.test(value)) return null;
  const normalized = normalizeTerm(value);
  const exact = resolvePythonKnowledge(normalized, typeFromPrefix(normalized));
  if (exact.alternatives.length) return ambiguityAnswer(exact, language);
  if (exact.record) return formatPythonKnowledgeRecord(exact.record, language);
  const fuzzy = resolveFuzzyPythonTerm(normalized);
  if (!fuzzy || fuzzy.distance === 0) return null;
  const resolution = resolvePythonKnowledge(fuzzy.term, typeFromPrefix(fuzzy.term));
  if (!resolution.record) return null;
  const prefix = language === 'fr'
    ? `**Correction probable**\nJ’ai interprété \`${value}\` comme \`${fuzzy.term}\`.`
    : `**Likely correction**\nI interpreted \`${value}\` as \`${fuzzy.term}\`.`;
  return `${prefix}\n\n${formatPythonKnowledgeRecord(resolution.record, language)}`;
};

export const answerPythonAtLevel = (question: string, language: KnowledgeLanguage, level: PythonExplanationLevel): string | null => {
  const term = extractKnowledgeTerm(question) || normalizeTerm(question);
  const fuzzy = resolveFuzzyPythonTerm(term);
  let resolution = resolvePythonKnowledge(fuzzy?.term || term, typeFromPrefix(fuzzy?.term || term));
  if (!resolution.record && !resolution.alternatives.length) {
    const semantic = searchPythonKnowledge(term, 1)[0];
    if (semantic && semantic.score >= 8) resolution = { term: semantic.matchedTerm, record: semantic.record, alternatives: [] };
  }
  if (resolution.alternatives.length) return ambiguityAnswer(resolution, language);
  if (!resolution.record) return null;
  const record = resolution.record;
  const fr = language === 'fr';
  const summary = localizedKnowledgeSummary(record, language);
  const example = record.examples[0]?.code || '';
  const frenchOr = (value: string, fallback: string): string => {
    if (!fr) return value;
    const translated = localizeAiText(value, 'fr');
    return translated !== value && !/\b(?:is|the|returns|creates|used|with|from|and|this|that|library)\b/i.test(translated) ? translated : fallback;
  };
  const mutation = fr
    ? ({ yes: 'oui', no: 'non', depends: 'cela dépend', 'not-applicable': 'sans objet' } as const)[record.mutates]
    : record.mutates;
  if (level === 'beginner') {
    return [
      `**${record.canonicalName} — ${fr ? 'niveau débutant' : 'beginner level'}**`,
      summary,
      `${fr ? 'Syntaxe de départ' : 'Starting syntax'}: \`${record.signature}\``,
      example ? `**${fr ? 'Petit exemple' : 'Tiny example'}**\n\`\`\`python\n${example}\n\`\`\`` : '',
      fr ? '**À retenir**\nComprenez d’abord son rôle et essayez le petit exemple avant d’ajouter des cas complexes.' : '**Key point**\nUnderstand its purpose first and run the tiny example before adding complex cases.',
    ].filter(Boolean).join('\n\n');
  }
  if (level === 'intermediate') {
    return [
      `**${record.canonicalName} — ${fr ? 'niveau intermédiaire' : 'intermediate level'}**`,
      summary,
      `**${fr ? 'Fonctionnement' : 'How it works'}**\n${language === 'fr' ? localizedKnowledgeSummary({ ...record, term: record.canonicalName }, language) : record.details}`,
      `**${fr ? 'Retour et modification' : 'Return and mutation'}**\n${fr ? 'Modification' : 'Mutation'}: ${mutation}. ${fr ? 'Retour' : 'Return'}: ${frenchOr(record.returns, 'La valeur renvoyée dépend de l’opération et des arguments indiqués par la signature.')}`,
      `**${fr ? 'Erreurs à surveiller' : 'Mistakes to watch'}**\n${frenchOr(record.raises, 'Vérifiez les types, le nombre d’arguments, les valeurs limites et les éléments absents.')}`,
      example ? `\`\`\`python\n${example}\n\`\`\`` : '',
    ].filter(Boolean).join('\n\n');
  }
  return [
    `**${record.canonicalName} — ${fr ? 'niveau expert' : 'expert level'}**`,
    summary,
    `**${fr ? 'Mécanisme et contrat' : 'Mechanics and contract'}**\n${fr ? `Analysez la signature \`${record.signature}\`, la mutabilité (${record.mutates}) et le contrat de retour. Consultez la source pour les détails d’implémentation propres à la version.` : record.details}`,
    `**${fr ? 'Cas limites et erreurs' : 'Edge cases and errors'}**\n${fr ? 'Vérifiez les entrées vides, les types incompatibles, la mutabilité, la portée, les itérateurs épuisés et les coûts de matérialisation.' : record.raises}`,
    `**${fr ? 'Version et source' : 'Version and source'}**\n${frenchOr(record.version, 'Consultez la source officielle pour vérifier les différences entre versions.')}\n${record.sourceUrl}`,
    record.related.length ? `**${fr ? 'Concepts liés' : 'Related concepts'}**\n${record.related.map((item, index) => `${index + 1}. ${item}`).join('\n')}` : '',
    buildPythonKnowledgeDeepSupplement(`what is ${record.term}`, language),
    example ? `\`\`\`python\n${example}\n\`\`\`` : '',
  ].filter(Boolean).join('\n\n');
};

const complexityForRecord = (record: PythonKnowledgeRecord): string => {
  const key = `${record.kind}.${record.canonicalName}`.toLowerCase();
  if (key === 'builtin.len') return 'Built-in containers normally store their size, so `len()` is O(1); a custom `__len__()` controls its own cost.';
  if (/^(?:list|tuple)\.count$/.test(key)) return '`count()` scans the sequence and compares each item with `==`, so its runtime is O(n).';
  if (key === 'str.count') return '`str.count()` scans the selected string range for non-overlapping matches, so runtime grows with the searched text.';
  if (key === 'list.append') return '`append()` is amortized O(1); occasional list resizing makes an individual append more expensive.';
  if (key === 'list.sort' || key === 'builtin.sorted') return 'Python uses Timsort; typical and worst-case sorting cost is O(n log n), with O(n) best cases for existing ordered runs.';
  if (key === 'list.reverse' || key === 'builtin.reversed') return '`list.reverse()` touches the list items in O(n); `reversed()` creates an iterator in O(1) and produces items lazily.';
  if (/^(?:dict|get|set)/.test(key)) return 'Hash-table lookup is O(1) on average but can degrade with heavy collisions.';
  return 'Complexity depends on the concrete type, input size, implementation, and whether the operation is lazy or materializes a result.';
};

export const buildPythonKnowledgeDeepSupplement = (question: string, language: KnowledgeLanguage): string => {
  const term = extractKnowledgeTerm(question);
  if (!term) return '';
  const resolution = resolvePythonKnowledge(term, typeFromPrefix(term));
  if (!resolution.record) return '';
  const record = resolution.record;
  const complexity = complexityForRecord(record);
  if (language === 'fr') {
    return [
      '**Mécanique approfondie**',
      `1. Python résout d\'abord \`${record.signature}\` sur le type ou le module concerné.`,
      `2. Il vérifie les arguments, puis exécute l\'implémentation correspondant à ${record.kind}.`,
      `3. Modification : ${record.mutates}. Retour : ${localizeAiText(record.returns, 'fr')}`,
      `4. Coût : ${localizeAiText(complexity, 'fr')}`,
      `5. Cas limites : ${localizeAiText(record.raises, 'fr')}`,
      `6. Vérification : ${record.sourceUrl}`,
    ].join('\n');
  }
  return [
    '**Deep mechanics**',
    `1. Python first resolves \`${record.signature}\` on the relevant type or module.`,
    `2. It validates the arguments, then runs the implementation for this ${record.kind}.`,
    `3. Mutation: ${record.mutates}. Return behavior: ${record.returns}`,
    `4. Complexity: ${complexity}`,
    `5. Edge cases: ${record.raises}`,
    `6. Verification source: ${record.sourceUrl}`,
  ].join('\n');
};

const EXTRA_EXAMPLES: Record<string, string[]> = {
  'builtin.len': [
    'word = "Python"\nprint(len(word))       # 6\nprint(len({"a": 1})) # 1',
    'class Box:\n    def __init__(self, items):\n        self.items = items\n    def __len__(self):\n        return len(self.items)\n\nprint(len(Box([1, 2, 3])))  # 3',
  ],
  'list.append': [
    'names = ["Ana"]\nnames.append("Bo")\nprint(names)  # ["Ana", "Bo"]',
    'rows = []\nfor number in range(3):\n    rows.append(number ** 2)\nprint(rows)  # [0, 1, 4]',
  ],
  'list.count': [
    'letters = ["a", "b", "a", "c"]\nprint(letters.count("a"))  # 2',
    'values = []\nprint(values.count(10))  # 0',
  ],
  'str.count': [
    'text = "banana"\nprint(text.count("an"))  # 2',
    'text = "aaaa"\nprint(text.count("aa"))  # 2 (non-overlapping)',
  ],
  'tuple.count': [
    'point_history = (1, 2, 1, 3)\nprint(point_history.count(1))  # 2',
  ],
  'list.sort': [
    'numbers = [3, 1, 2]\nresult = numbers.sort()\nprint(numbers)  # [1, 2, 3]\nprint(result)   # None',
    'names = ["Ada", "Christopher", "Bo"]\nnames.sort(key=len)\nprint(names)  # ["Bo", "Ada", "Christopher"]',
  ],
  'builtin.sorted': [
    'numbers = [3, 1, 2]\nordered = sorted(numbers)\nprint(numbers)  # [3, 1, 2]\nprint(ordered)  # [1, 2, 3]',
  ],
  'list.reverse': [
    'items = [1, 2, 3]\nresult = items.reverse()\nprint(items)   # [3, 2, 1]\nprint(result)  # None',
  ],
  'builtin.reversed': [
    'items = [1, 2, 3]\niterator = reversed(items)\nprint(items)           # [1, 2, 3]\nprint(list(iterator))  # [3, 2, 1]',
  ],
};

export const buildPythonKnowledgeExampleSupplement = (question: string, language: KnowledgeLanguage): string => {
  const term = extractKnowledgeTerm(question);
  if (!term) return '';
  const resolution = resolvePythonKnowledge(term, typeFromPrefix(term));
  if (!resolution.record) return '';
  const record = resolution.record;
  const key = `${record.kind}.${record.canonicalName}`.toLowerCase();
  const examples = EXTRA_EXAMPLES[key] || [];
  if (!examples.length) return '';
  return examples.map((code, index) => `${index + 1}. ${language === 'fr' ? 'Exemple ciblé' : 'Targeted example'}\n\`\`\`python\n${code}\n\`\`\``).join('\n\n');
};

export const answerPythonProgressiveExamples = (question: string, language: KnowledgeLanguage): string | null => {
  const cleaned = question.replace(/\b(?:give|show|another|examples?|of|for|donne|montre|des|exemples?|de|pour)\b/gi, ' ').replace(/\s+/g, ' ').trim();
  const term = /\b(?:examples?|exemples?)\b/i.test(question) ? cleaned : (extractKnowledgeTerm(question) || cleaned);
  const fuzzy = resolveFuzzyPythonTerm(term);
  const resolution = resolvePythonKnowledge(fuzzy?.term || term, typeFromPrefix(fuzzy?.term || term));
  if (resolution.alternatives.length) return ambiguityAnswer(resolution, language);
  if (!resolution.record) return null;
  const record = resolution.record;
  const key = `${record.kind}.${record.canonicalName}`.toLowerCase();
  const examples = [...record.examples.map(example => example.code), ...(EXTRA_EXAMPLES[key] || [])]
    .filter((code, index, all) => code.trim() && all.indexOf(code) === index)
    .slice(0, 4);
  const fr = language === 'fr';
  const blocks = examples.map((code, index) => {
    const level = index === 0 ? (fr ? 'Débutant' : 'Beginner')
      : index === 1 ? (fr ? 'Intermédiaire' : 'Intermediate')
        : (fr ? 'Expert' : 'Expert');
    return `${index + 1}. **${level}**\n\`\`\`python\n${code}\n\`\`\``;
  });
  return [
    `**${fr ? 'Exemples progressifs' : 'Progressive examples'}: ${record.canonicalName}**`,
    localizedKnowledgeSummary(record, language),
    ...blocks,
    blocks.length === 0 ? `**${fr ? 'Syntaxe vérifiée' : 'Verified syntax'}**\n\`\`\`python\n${record.signature}\n\`\`\`` : '',
    `**${fr ? 'Progression conseillée' : 'Suggested progression'}**`,
    fr
      ? '1. Exécutez l’exemple avec les valeurs fournies.\n2. Remplacez une entrée et prédisez le résultat.\n3. Testez un cas vide ou limite.\n4. Expliquez le type renvoyé, la mutabilité et les erreurs possibles.'
      : '1. Run the example with its original values.\n2. Replace one input and predict the result.\n3. Test an empty or boundary case.\n4. Explain the return type, mutation behavior, and possible errors.',
  ].filter(Boolean).join('\n\n');
};

const parseComparisonPair = (question: string): [string, string] | null => {
  const cleaned = question.trim().replace(/[?!]+$/g, '');
  const patterns = [
    /(?:what(?:'s| is)?\s+)?(?:the\s+)?difference between\s+(.+?)\s+and\s+(.+)$/i,
    /(?:compare|comparison of)\s+(.+?)\s+(?:with|to|and)\s+(.+)$/i,
    /^(?:(?:what(?:'s| is)?|define|explain|compare)\s+)?(.+?)\s+(?:vs\.?|versus)\s+(.+)$/i,
    /(?:compare|compar(?:e|er))\s+(.+?)\s+(?:avec|with|to|and|et)\s+(.+)$/i,
  ];
  for (const pattern of patterns) {
    const match = cleaned.match(pattern);
    if (match) return [normalizeTerm(match[1]), normalizeTerm(match[2])];
  }
  return null;
};

type ComparisonTrait = {
  meaning: string;
  access: string;
  order: string;
  duplicates: string;
  choose: string;
  literal: string;
};

const CORE_COMPARISON_TRAITS: Record<string, ComparisonTrait> = {
  list: {
    meaning: 'An ordered, mutable sequence of values.',
    access: 'Use an integer position such as `items[0]`.',
    order: 'Keeps item order.',
    duplicates: 'Allows duplicate values.',
    choose: 'Choose it for an ordered collection that you will index, loop over, or modify.',
    literal: 'items = ["Ada", "Lin", "Ada"]\nprint(items[0])  # Ada',
  },
  dict: {
    meaning: 'A mutable mapping from unique, hashable keys to values.',
    access: 'Use a key such as `person["name"]`.',
    order: 'Keeps insertion order in current Python.',
    duplicates: 'Keys are unique; values may repeat.',
    choose: 'Choose it when each value needs a meaningful key or label.',
    literal: 'person = {"name": "Ada", "age": 36}\nprint(person["name"])  # Ada',
  },
  dictionary: {
    meaning: 'A mutable mapping from unique, hashable keys to values.',
    access: 'Use a key such as `person["name"]`.',
    order: 'Keeps insertion order in current Python.',
    duplicates: 'Keys are unique; values may repeat.',
    choose: 'Choose it when each value needs a meaningful key or label.',
    literal: 'person = {"name": "Ada", "age": 36}\nprint(person["name"])  # Ada',
  },
  tuple: {
    meaning: 'An ordered sequence that cannot be changed after creation.',
    access: 'Use an integer position such as `point[0]`.',
    order: 'Keeps item order.',
    duplicates: 'Allows duplicate values.',
    choose: 'Choose it for a fixed record or group of values that should not change.',
    literal: 'point = (10, 20)\nprint(point[0])  # 10',
  },
  set: {
    meaning: 'A mutable collection of unique, hashable values.',
    access: 'Test membership with `value in items`; sets have no positional indexing.',
    order: 'Do not rely on a stable positional order.',
    duplicates: 'Automatically removes duplicates.',
    choose: 'Choose it for uniqueness, fast membership checks, union, intersection, or difference.',
    literal: 'tags = {"python", "web", "python"}\nprint(tags)  # two unique values',
  },
  frozenset: {
    meaning: 'An immutable set of unique, hashable values.',
    access: 'Test membership; there is no positional indexing.',
    order: 'Do not rely on a stable positional order.',
    duplicates: 'Automatically removes duplicates.',
    choose: 'Choose it when set behavior is needed but the collection must be hashable and immutable.',
    literal: 'permissions = frozenset({"read", "write"})\nprint("read" in permissions)  # True',
  },
  str: {
    meaning: 'An immutable sequence of Unicode characters.',
    access: 'Use integer indexes or slices such as `text[0]` and `text[1:3]`.',
    order: 'Keeps character order.',
    duplicates: 'Allows repeated characters.',
    choose: 'Choose it for human-readable text.',
    literal: 'text = "python"\nprint(text[0])  # p',
  },
  bytes: {
    meaning: 'An immutable sequence of byte values from 0 to 255.',
    access: 'Indexing returns an integer byte; slicing returns `bytes`.',
    order: 'Keeps byte order.',
    duplicates: 'Allows repeated bytes.',
    choose: 'Choose it for encoded text, files, network data, or binary protocols.',
    literal: 'data = b"ABC"\nprint(data[0])  # 65',
  },
  bytearray: {
    meaning: 'A mutable sequence of byte values from 0 to 255.',
    access: 'Indexing returns an integer byte and indexed values can be replaced.',
    order: 'Keeps byte order.',
    duplicates: 'Allows repeated bytes.',
    choose: 'Choose it when binary data must be edited in place.',
    literal: 'data = bytearray(b"ABC")\ndata[0] = 90\nprint(data)  # bytearray(b"ZBC")',
  },
  range: {
    meaning: 'An immutable, lazy arithmetic sequence of integers.',
    access: 'Index, slice, iterate, or test membership without storing every integer.',
    order: 'Follows start, stop, and step.',
    duplicates: 'A valid nonzero step does not repeat values.',
    choose: 'Choose it for counted loops or compact integer sequences.',
    literal: 'numbers = range(1, 6, 2)\nprint(list(numbers))  # [1, 3, 5]',
  },
};

const comparisonTraitFor = (record: PythonKnowledgeRecord): ComparisonTrait => {
  const key = record.canonicalName.toLowerCase().replace(/\(\)$/, '');
  return CORE_COMPARISON_TRAITS[key] || CORE_COMPARISON_TRAITS[record.term.toLowerCase()] || {
    meaning: record.summary,
    access: `Use its documented form: \`${record.signature}\`.`,
    order: 'Order or evaluation behavior depends on this API’s documented contract.',
    duplicates: 'Duplicate behavior depends on the values and operation.',
    choose: `Choose it when this purpose matches the task: ${record.summary}`,
    literal: record.examples[0]?.code || record.signature,
  };
};

const COMPARISON_TERM_ALIASES: Record<string, string> = {
  array: 'list',
  boolean: 'bool',
  dic: 'dict',
  dictionaries: 'dict',
  dictionary: 'dict',
  integer: 'int',
  integers: 'int',
  lst: 'list',
  mapping: 'dict',
  string: 'str',
  strings: 'str',
  tup: 'tuple',
};

const resolveComparisonSide = (term: string): KnowledgeResolution => {
  const normalized = normalizeTerm(term).toLowerCase();
  const canonicalTerm = COMPARISON_TERM_ALIASES[normalized] || normalized;
  const exact = resolvePythonKnowledge(canonicalTerm, typeFromPrefix(canonicalTerm));
  if (exact.record || exact.alternatives.length) return exact;
  const fuzzy = resolveFuzzyPythonTerm(canonicalTerm);
  if (fuzzy) return resolvePythonKnowledge(fuzzy.term, typeFromPrefix(fuzzy.term));
  const semantic = searchPythonKnowledge(canonicalTerm, 1)[0];
  return semantic && semantic.score >= 10
    ? { term: semantic.matchedTerm, record: semantic.record, alternatives: [] }
    : exact;
};

const localizedComparisonTrait = (text: string, language: KnowledgeLanguage): string => {
  if (language === 'en') return text;
  const translated = localizeAiText(text, 'fr');
  return translated === text ? text : translated;
};

const comparisonExampleBlock = (record: PythonKnowledgeRecord, trait: ComparisonTrait, language: KnowledgeLanguage) => {
  const code = trait.literal || record.examples[0]?.code || record.signature;
  return `**${record.canonicalName}**\n\`\`\`python\n${code}\n\`\`\``;
};

export const answerPythonKnowledgeComparisonAtLevel = (
  question: string,
  language: KnowledgeLanguage,
  mode: GeneralAiResponseMode = 'normal',
): string | null => {
  const pair = parseComparisonPair(question);
  if (!pair) return null;
  const first = resolveComparisonSide(pair[0]);
  const second = resolveComparisonSide(pair[1]);
  if (first.alternatives.length) return ambiguityAnswer(first, language);
  if (second.alternatives.length) return ambiguityAnswer(second, language);
  if (!first.record || !second.record) return null;
  const a = first.record;
  const b = second.record;
  const traitA = comparisonTraitFor(a);
  const traitB = comparisonTraitFor(b);
  const fr = language === 'fr';
  const titleLevel = mode === 'simple' ? (fr ? 'comparaison débutant' : 'beginner comparison')
    : mode === 'deep' ? (fr ? 'comparaison expert' : 'expert comparison')
      : mode === 'examples' ? (fr ? 'comparaison par exemples' : 'examples comparison')
        : (fr ? 'comparaison intermédiaire' : 'intermediate comparison');
  const biggestDifference = fr
    ? `\`${a.canonicalName}\` : ${localizedComparisonTrait(traitA.access, language)} \`${b.canonicalName}\` : ${localizedComparisonTrait(traitB.access, language)}`
    : `\`${a.canonicalName}\`: ${traitA.access} \`${b.canonicalName}\`: ${traitB.access}`;
  const basicTable = [
    `| ${fr ? 'Critère' : 'Criterion'} | ${a.canonicalName} | ${b.canonicalName} |`,
    '|---|---|---|',
    `| ${fr ? 'Signification' : 'Meaning'} | ${fr ? localizedKnowledgeSummary(a, language) : traitA.meaning} | ${fr ? localizedKnowledgeSummary(b, language) : traitB.meaning} |`,
    `| ${fr ? 'But' : 'Purpose'} | ${localizedKnowledgeSummary(a, language)} | ${localizedKnowledgeSummary(b, language)} |`,
    `| ${fr ? 'Accès' : 'Access'} | ${localizedComparisonTrait(traitA.access, language)} | ${localizedComparisonTrait(traitB.access, language)} |`,
    `| ${fr ? 'Syntaxe' : 'Syntax'} | \`${a.signature}\` | \`${b.signature}\` |`,
  ].join('\n');
  const header = `**${a.canonicalName} vs ${b.canonicalName} — ${titleLevel}**`;

  if (mode === 'simple') {
    return [
      header,
      `**1. ${fr ? 'En termes simples' : 'In plain language'}**\n${localizedComparisonTrait(traitA.meaning, language)}\n\n${localizedComparisonTrait(traitB.meaning, language)}`,
      `**2. ${fr ? 'La plus grande différence' : 'Biggest difference'}**\n${biggestDifference}`,
      basicTable,
      `**3. ${fr ? 'Petit exemple' : 'Tiny example'}**\n\`\`\`python\n${traitA.literal}\n\n${traitB.literal}\n\`\`\``,
      `**4. ${fr ? 'Règle simple' : 'Simple rule'}**\n${localizedComparisonTrait(traitA.choose, language)}\n${localizedComparisonTrait(traitB.choose, language)}`,
    ].join('\n\n');
  }

  const behaviorTable = [
    basicTable,
    `| ${fr ? 'Ordre' : 'Order'} | ${localizedComparisonTrait(traitA.order, language)} | ${localizedComparisonTrait(traitB.order, language)} |`,
    `| ${fr ? 'Doublons' : 'Duplicates'} | ${localizedComparisonTrait(traitA.duplicates, language)} | ${localizedComparisonTrait(traitB.duplicates, language)} |`,
    `| ${fr ? 'Type' : 'Kind'} | ${a.kind} | ${b.kind} |`,
    `| ${fr ? 'Modifie l’objet' : 'Mutates object'} | ${a.mutates} | ${b.mutates} |`,
    `| ${fr ? 'Retour' : 'Returns'} | ${a.returns} | ${b.returns} |`,
    `| ${fr ? 'Version' : 'Version'} | ${a.version} | ${b.version} |`,
  ].join('\n');

  if (mode === 'examples') {
    const exampleA = a.examples[0]?.code || traitA.literal;
    const exampleB = b.examples[0]?.code || traitB.literal;
    return [
      header,
      `**1. ${fr ? 'Différence à observer' : 'Difference to watch'}**\n${biggestDifference}`,
      behaviorTable,
      `**2. ${fr ? 'Exemple débutant côte à côte' : 'Beginner side-by-side example'}**\n\`\`\`python\n${traitA.literal}\n\n${traitB.literal}\n\`\`\``,
      `**3. ${fr ? `Exemple avec ${a.canonicalName}` : `${a.canonicalName} example`}**\n\`\`\`python\n${exampleA}\n\`\`\``,
      `**4. ${fr ? `Exemple avec ${b.canonicalName}` : `${b.canonicalName} example`}**\n\`\`\`python\n${exampleB}\n\`\`\``,
      `**5. ${fr ? 'À vous' : 'Try it'}**\n${fr ? `Représentez les mêmes données une fois avec \`${a.canonicalName}\` et une fois avec \`${b.canonicalName}\`, puis comparez la façon d’accéder à une valeur.` : `Represent the same information once with ${a.canonicalName} and once with ${b.canonicalName}, then compare how one value is accessed.`}`,
    ].join('\n\n');
  }

  const intermediate = [
    header,
    `**1. ${fr ? 'Différence principale' : 'Core difference'}**\n${biggestDifference}`,
    `**2. ${fr ? 'Comparaison du comportement' : 'Behavior comparison'}**\n${behaviorTable}`,
    `**3. ${fr ? 'Exemples côte à côte' : 'Side-by-side examples'}**\n${comparisonExampleBlock(a, traitA, language)}\n\n${comparisonExampleBlock(b, traitB, language)}`,
    `**4. ${fr ? 'Quand choisir chacun' : 'When to choose each'}**\n- **${a.canonicalName}:** ${localizedComparisonTrait(traitA.choose, language)}\n- **${b.canonicalName}:** ${localizedComparisonTrait(traitB.choose, language)}`,
    `**5. ${fr ? 'Erreurs fréquentes' : 'Common mistakes'}**\n- **${a.canonicalName}:** ${language === 'fr' ? localizeAiText(a.raises, 'fr') : a.raises}\n- **${b.canonicalName}:** ${language === 'fr' ? localizeAiText(b.raises, 'fr') : b.raises}`,
    `**6. ${fr ? 'Sources' : 'Sources'}**\n- ${a.sourceUrl}\n- ${b.sourceUrl}`,
  ];
  if (mode === 'normal') return intermediate.join('\n\n');

  return [
    ...intermediate,
    `**7. ${fr ? 'Mécanismes internes et compromis' : 'Internals and tradeoffs'}**\n**${a.canonicalName}:** ${language === 'fr' ? localizeAiText(a.details, 'fr') : a.details}\n\n**${b.canonicalName}:** ${language === 'fr' ? localizeAiText(b.details, 'fr') : b.details}`,
    `**8. ${fr ? 'Contrats et cas limites' : 'Contracts and edge cases'}**\n- **${a.canonicalName}:** kind=${a.kind}, mutation=${a.mutates}, returns=${a.returns}\n- **${b.canonicalName}:** kind=${b.kind}, mutation=${b.mutates}, returns=${b.returns}`,
    `**9. ${fr ? 'Versions et sources officielles' : 'Versions and official sources'}**\n- **${a.canonicalName}:** ${a.version} — ${a.sourceUrl}\n- **${b.canonicalName}:** ${b.version} — ${b.sourceUrl}`,
  ].join('\n\n');
};

export const answerPythonKnowledgeComparison = (question: string, language: KnowledgeLanguage): string | null => {
  return answerPythonKnowledgeComparisonAtLevel(question, language, 'normal');
};

export const answerPythonVersionQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const cleaned = question.trim().replace(/[?!]+$/g, '');
  const patterns = [
    /(?:when|what python version)\s+(?:was|were|did|is|are)?\s*(.+?)\s+(?:added|introduced|available|released|supported)$/i,
    /(?:what|which)\s+(?:python\s+)?version\s+(?:was|were|did)?\s*(.+?)\s+(?:added|introduced|available|released|supported)$/i,
    /what python version (?:added|introduced|supports?)\s+(.+)$/i,
  ];
  let term = '';
  for (const pattern of patterns) {
    const match = cleaned.match(pattern);
    if (match) {
      term = normalizeTerm(match[1]);
      break;
    }
  }
  if (!term) return null;
  const resolution = resolvePythonKnowledge(term);
  if (resolution.alternatives.length) return ambiguityAnswer(resolution, language);
  if (!resolution.record) return null;
  const record = resolution.record;
  return language === 'fr'
    ? `**Version de ${record.canonicalName}**\n\n${record.version}\n\nSource : ${record.sourceUrl}`
    : `**${record.canonicalName} version information**\n\n${record.version}\n\nSource: ${record.sourceUrl}`;
};

const subjectFromQuestion = (question: string): string => {
  const term = extractKnowledgeTerm(question);
  if (term) return term;
  const pair = parseComparisonPair(question);
  return pair ? `${pair[0]} and ${pair[1]}` : question;
};

export const resolveKnowledgeFollowUp = (
  question: string,
  previousQuestion: string,
  currentMode: GeneralAiResponseMode,
): KnowledgeFollowUpResolution => {
  const trimmed = question.trim();
  if (/```|(^|\n)\s*(?:def |class |for |while |if |import |from |return |yield |[A-Za-z_]\w*\s*=)/m.test(trimmed)) {
    return { question: trimmed, mode: currentMode, usedContext: false };
  }
  const directExamples = trimmed.match(/^(?:show|give)\s+(?:me\s+)?(?:another\s+)?examples?\s+(?:of|for)\s+(.+)$/i);
  if (directExamples) return { question: `what is ${normalizeTerm(directExamples[1])}`, mode: 'examples', usedContext: true };
  const directFrenchExamples = trimmed.match(/^(?:donne|montre)(?:-moi)?\s+(?:un autre |des )?exemples?\s+(?:de|des|pour)\s+(.+)$/i);
  if (directFrenchExamples) return { question: `what is ${normalizeTerm(directFrenchExamples[1])}`, mode: 'examples', usedContext: true };
  const directDeep = trimmed.match(/^(?:go deeper on|explain in depth|deep explanation of)\s+(.+)$/i);
  if (directDeep) return { question: `what is ${normalizeTerm(directDeep[1])}`, mode: 'deep', usedContext: true };
  const directFrenchDeep = trimmed.match(/^(?:approfondis|explique en d[eé]tail)\s+(.+)$/i);
  if (directFrenchDeep) return { question: `what is ${normalizeTerm(directFrenchDeep[1])}`, mode: 'deep', usedContext: true };
  const directSimple = trimmed.match(/^(?:explain simply|simple explanation of)\s+(.+)$/i);
  if (directSimple) return { question: `what is ${normalizeTerm(directSimple[1])}`, mode: 'simple', usedContext: true };
  const directFrenchSimple = trimmed.match(/^(?:explique simplement|explication simple de)\s+(.+)$/i);
  if (directFrenchSimple) return { question: `what is ${normalizeTerm(directFrenchSimple[1])}`, mode: 'simple', usedContext: true };
  if (!previousQuestion) return { question: trimmed, mode: currentMode, usedContext: false };
  const subject = subjectFromQuestion(previousQuestion);
  if (/^(?:simplify|make (?:it|this|that) simpler|explain simply|explain more simply|simple|simplifie|rends? (?:cela|ca|ceci) plus simple|explique simplement)\b/i.test(trimmed)) {
    return { question: previousQuestion, mode: 'simple', usedContext: true };
  }
  if (/^(?:go deeper|make (?:it|this|that) more detailed|more detail|explain more|break it down|approfondis|plus de d[eé]tails?|rends? (?:cela|ca|ceci) plus d[eé]taill[eé])\b/i.test(trimmed)) {
    return { question: previousQuestion, mode: 'deep', usedContext: true };
  }
  if (/^(?:another example|harder example|simpler example|examples?|give (?:me )?(?:a )?(?:another |harder |simpler )?examples?|show (?:me )?(?:a )?(?:another |harder |simpler )?examples?|donne (?:un autre |des )?exemples?)\b/i.test(trimmed)) {
    return { question: previousQuestion, mode: 'examples', usedContext: true };
  }
  const contextualComparison = trimmed.match(/^(?:compare|difference between|how (?:is|does))\s+(?:it|this|that|cela|ca|ceci)\s+(?:with|to|and|different from|et|avec|de)\s+(.+?)[?.!]*$/i);
  if (contextualComparison) {
    return { question: `difference between ${subject} and ${normalizeTerm(contextualComparison[1])}`, mode: currentMode, usedContext: true };
  }
  const newSubject = trimmed.match(/^(?:what about|how about|et|et pour)\s+(.+?)[?.!]*$/i);
  if (newSubject) return { question: `what is ${normalizeTerm(newSubject[1])}`, mode: currentMode, usedContext: true };
  if (/\b(?:it|this|that|them|those|cela|ca|ceci|il|elle|eux)\b/i.test(trimmed)) {
    return {
      question: trimmed.replace(/\b(?:it|this|that|them|those|cela|ca|ceci|il|elle|eux)\b/i, subject),
      mode: currentMode,
      usedContext: true,
    };
  }
  return { question: trimmed, mode: currentMode, usedContext: false };
};

const extractCode = (question: string): string | null => {
  const fenced = question.match(/```(?:python)?\s*([\s\S]*?)```/i)?.[1]?.trim();
  if (fenced) return fenced;
  const looksLikeCode = /(^|\n)\s*(?:def |class |for |while |if |elif |else:|try:|except |with |import |from |return |yield |print\(|[A-Za-z_]\w*\s*=)/m.test(question);
  return looksLikeCode ? question.trim() : null;
};

const explainCodeLine = (line: string, language: KnowledgeLanguage): string => {
  const text = line.trim();
  const fr = language === 'fr';
  if (!text) return fr ? 'Ligne vide qui separe visuellement les blocs.' : 'Blank line used to separate blocks visually.';
  if (text.startsWith('#')) return fr ? 'Commentaire: Python ne l\'execute pas.' : 'Comment: Python does not execute it.';
  if (/^(?:from\s+\S+\s+)?import\b/.test(text)) return fr ? 'Importe un module ou un nom avant son utilisation.' : 'Imports a module or name before it is used.';
  if (/^def\s+/.test(text)) return fr ? 'Definit une fonction; son corps s\'execute seulement lors d\'un appel.' : 'Defines a function; its body runs only when the function is called.';
  if (/^class\s+/.test(text)) return fr ? 'Cree une classe et execute son corps pour construire l\'objet classe.' : 'Creates a class and executes its body to build the class object.';
  if (/^(?:for|while)\b/.test(text)) return fr ? 'Demarre une boucle et repete son bloc indente.' : 'Starts a loop and repeats its indented block.';
  if (/^(?:if|elif|else)\b/.test(text)) return fr ? 'Controle quelle branche indentee sera executee.' : 'Controls which indented branch will execute.';
  if (/^(?:try|except|finally|raise)\b/.test(text)) return fr ? 'Participe au controle et au traitement des exceptions.' : 'Participates in exception control and handling.';
  if (/^return\b/.test(text)) return fr ? 'Termine la fonction et renvoie une valeur a l\'appelant.' : 'Ends the function and sends a value back to the caller.';
  if (/^yield\b/.test(text)) return fr ? 'Suspend le generateur et produit une valeur paresseusement.' : 'Suspends the generator and produces one value lazily.';
  if (/^with\b/.test(text)) return fr ? 'Entre dans un gestionnaire de contexte et garantit le nettoyage.' : 'Enters a context manager and guarantees cleanup.';
  if (/^[A-Za-z_]\w*(?:\[[^\]]+\])?\s*=/.test(text)) return fr ? 'Calcule la partie droite puis affecte le resultat a gauche.' : 'Evaluates the right side, then assigns the result on the left.';
  if (/\w+\s*\(/.test(text)) return fr ? 'Appelle une fonction ou une methode avec les arguments indiques.' : 'Calls a function or method with the supplied arguments.';
  return fr ? 'Expression Python evaluee selon la priorite des operateurs et le contexte.' : 'Python expression evaluated according to operator precedence and context.';
};

export const answerPythonCodeQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  const code = extractCode(question);
  if (!code) return null;
  const lines = code.split('\n').slice(0, 80);
  const explanations = lines.map((line, index) => `${index + 1}. \`${line || ' '}\`\n   ${explainCodeLine(line, language)}`);
  const variableTypes = new Map<string, string>();
  for (const match of code.matchAll(/^\s*([A-Za-z_]\w*)\s*=\s*(.+)$/gm)) {
    const value = match[2].trim();
    const type = value.startsWith('[') ? 'list'
      : value.startsWith('{') && value.includes(':') ? 'dict'
        : value.startsWith('{') ? 'set'
          : value.startsWith('(') ? 'tuple'
            : /^['"]/.test(value) ? 'str'
              : '';
    if (type) variableTypes.set(match[1], type);
  }
  const calls = [...code.matchAll(/\b(?:(\w+)\.)?([A-Za-z_]\w*)\s*\(/g)]
    .map(match => ({ owner: match[1] || '', name: match[2] }))
    .filter(call => !['def', 'class', 'if', 'for', 'while'].includes(call.name));
  const uniqueCalls = calls.filter((call, index, all) => all.findIndex(other => other.owner === call.owner && other.name === call.name) === index).slice(0, 15);
  const callDetails = uniqueCalls.map(call => {
    const ownerType = variableTypes.get(call.owner);
    const term = ownerType ? `${ownerType}.${call.name}` : call.name;
    const resolution = resolvePythonKnowledge(term, ownerType);
    const label = call.owner ? `${call.owner}.${call.name}()` : `${call.name}()`;
    if (resolution.alternatives.length) return `- \`${label}\`: ${language === 'fr' ? 'nom ambigu; precisez le type de l\'objet' : 'ambiguous name; include the object type'}`;
    return resolution.record ? `- \`${label}\`: ${localizedKnowledgeSummary(resolution.record, language)}` : `- \`${label}\`: ${language === 'fr' ? 'fonction definie par le programme ou une bibliotheque externe' : 'defined by the program or an external library'}`;
  });
  const syntaxFindings: string[] = [];
  if (/\[[^\]]*:[^\]]*\]/.test(code)) syntaxFindings.push(language === 'fr' ? '- `start:stop:step` est un decoupage; `stop` est exclu.' : '- `start:stop:step` is slicing; the `stop` position is excluded.');
  if (/\[\s*-1\s*\]/.test(code)) syntaxFindings.push(language === 'fr' ? '- `[-1]` selectionne le dernier element de la sequence.' : '- `[-1]` selects the last item in a sequence.');
  if (/\[[^\]]+\]/.test(code)) syntaxFindings.push(language === 'fr' ? '- Les crochets creent une liste ou accedent a un element selon leur position.' : '- Square brackets create a list or access an item, depending on their position.');
  if (/\{[^}]*:[^}]*\}/.test(code)) syntaxFindings.push(language === 'fr' ? '- Les accolades avec `cle: valeur` creent un dictionnaire.' : '- Curly braces containing `key: value` create a dictionary.');
  if (/\bfor\b[^\n]+\bin\b[^\n]+\]/.test(code)) syntaxFindings.push(language === 'fr' ? '- La comprehension construit une collection a partir d\'une iteration.' : '- The comprehension constructs a collection from an iteration.');
  if (/\blambda\b/.test(code)) syntaxFindings.push(language === 'fr' ? '- `lambda` cree une petite fonction limitee a une expression.' : '- `lambda` creates a small function limited to one expression.');
  if (/\bf["']/.test(code)) syntaxFindings.push(language === 'fr' ? '- Une f-string evalue les expressions placees entre accolades.' : '- An f-string evaluates expressions placed inside braces.');
  if (/\*\*|\/\/|<<|>>/.test(code)) syntaxFindings.push(language === 'fr' ? '- Les operateurs suivent leur priorite; utilisez des parentheses lorsque le groupement doit etre explicite.' : '- Operators follow precedence rules; use parentheses when grouping must be explicit.');
  return [
    language === 'fr' ? '**Analyse du code ligne par ligne**' : '**Line-by-line code analysis**',
    '',
    explanations.join('\n\n'),
    '',
    language === 'fr' ? '**Ordre d\'execution**' : '**Execution flow**',
    language === 'fr'
      ? 'Python charge les imports, cree les definitions, puis execute les instructions de niveau module de haut en bas. Les corps de fonctions s\'executent seulement lorsqu\'ils sont appeles.'
      : 'Python loads imports, creates definitions, then executes module-level statements from top to bottom. Function bodies run only when called.',
    '',
    language === 'fr' ? '**Appels detectes**' : '**Detected calls**',
    callDetails.join('\n') || (language === 'fr' ? 'Aucun appel detecte.' : 'No calls detected.'),
    '',
    language === 'fr' ? '**Syntaxe detectee**' : '**Detected syntax**',
    syntaxFindings.join('\n') || (language === 'fr' ? 'Aucune syntaxe speciale detectee.' : 'No special syntax detected.'),
  ].join('\n');
};

export interface PythonKnowledgeSearchResult {
  matchedTerm: string;
  score: number;
  record: PythonKnowledgeRecord;
}

const SEARCH_STOP_WORDS = new Set([
  'a', 'about', 'an', 'and', 'are', 'de', 'des', 'documentation', 'docs', 'du', 'for',
  'in', 'is', 'la', 'le', 'les', 'of', 'official', 'python', 'reference', 'sur', 'the',
  'what', 'with', 'une', 'un',
]);

const SEARCH_SYNONYMS: Record<string, string[]> = {
  anonymous: ['lambda'],
  array: ['list'],
  mapping: ['dict', 'dictionary'],
  pairs: ['dict', 'dictionary', 'key', 'value'],
  duplicate: ['set', 'unique'],
  duplicates: ['set', 'unique'],
  deduplicate: ['set', 'unique'],
  unique: ['set'],
  unordered: ['set'],
  immutable: ['tuple', 'frozenset', 'string'],
  text: ['string', 'str'],
  loop: ['iteration', 'for', 'while'],
  errors: ['exceptions', 'traceback'],
  fichier: ['file'],
  dictionnaire: ['dict', 'dictionary'],
  liste: ['list'],
  ensemble: ['set'],
  chaine: ['string', 'str'],
  boucle: ['loop', 'iteration'],
};

interface SearchIndexItem {
  term: string;
  text: string;
}

let knowledgeSearchIndex: SearchIndexItem[] | null = null;

const tokenizeSearchText = (value: string): string[] => {
  const base = value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9_+.]+/g, ' ')
    .split(/\s+/)
    .filter(token => token.length > 1 && !SEARCH_STOP_WORDS.has(token));
  return [...new Set(base.flatMap(token => [token, ...(SEARCH_SYNONYMS[token] || [])]))];
};

const getKnowledgeSearchIndex = (): SearchIndexItem[] => {
  if (knowledgeSearchIndex) return knowledgeSearchIndex;
  const terms = [...new Set([...getAllConceptTerms(), ...allReferenceEntries().map(entry => entry.name)])];
  knowledgeSearchIndex = terms.map(term => {
    const concept = lookupConcept(term);
    const text = [
      term,
      concept.entry?.name,
      ...(concept.entry?.aliases || []),
      concept.entry?.easy,
      concept.entry?.intermediate,
      concept.categoryFallback.summary,
      concept.categoryFallback.label,
    ].filter(Boolean).join(' ').toLowerCase();
    return { term, text };
  });
  return knowledgeSearchIndex;
};

export const searchPythonKnowledge = (query: string, limit = 5): PythonKnowledgeSearchResult[] => {
  const normalizedQuery = normalizeTerm(query).toLowerCase();
  const tokens = tokenizeSearchText(normalizedQuery);
  if (!tokens.length) return [];
  const scored = getKnowledgeSearchIndex().map(item => {
    let score = item.term.toLowerCase() === normalizedQuery ? 100 : 0;
    if (item.term.toLowerCase().startsWith(normalizedQuery)) score += 35;
    for (const token of tokens) {
      if (item.term.toLowerCase() === token) score += 30;
      else if (item.term.toLowerCase().includes(token)) score += 12;
      if (item.text.includes(` ${token} `) || item.text.startsWith(`${token} `)) score += 5;
      else if (item.text.includes(token)) score += 2;
    }
    return { term: item.term, score };
  }).filter(item => item.score > 0).sort((a, b) => b.score - a.score || a.term.localeCompare(b.term));

  const results: PythonKnowledgeSearchResult[] = [];
  const seen = new Set<string>();
  for (const item of scored) {
    const resolution = resolvePythonKnowledge(item.term);
    if (!resolution.record) continue;
    const key = `${resolution.record.kind}:${resolution.record.canonicalName}`.toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    results.push({ matchedTerm: item.term, score: item.score, record: resolution.record });
    if (results.length >= limit) break;
  }
  return results;
};

export const answerPythonDocumentationQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  if (!/\b(?:documentation|official docs?|reference|docs? for|documentation officielle|r[eé]f[eé]rence)\b/i.test(question)) return null;
  const subject = question
    .replace(/\b(?:find|show|give|open|cherche|montre|donne)\b/gi, ' ')
    .replace(/\b(?:me|moi|the|la|les|official|officielle|python|documentation|docs?|reference|r[eé]f[eé]rence|for|pour|about|sur)\b/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  const results = searchPythonKnowledge(subject || question, 3).filter(result => result.score >= 7);
  if (!results.length) return null;
  const fr = language === 'fr';
  return [
    fr ? '**Documentation Python correspondante**' : '**Matching Python documentation**',
    ...results.flatMap((result, index) => [
      '',
      `${index + 1}. **${result.record.canonicalName}** — ${localizedKnowledgeSummary(result.record, language)}`,
      `${fr ? 'Syntaxe' : 'Syntax'}: \`${result.record.signature}\``,
      `${fr ? 'Source vérifiée' : 'Verified source'}: ${result.record.sourceUrl}`,
    ]),
  ].join('\n');
};

export const answerPythonSemanticSuggestion = (question: string, language: KnowledgeLanguage): string | null => {
  const results = searchPythonKnowledge(question, 3).filter(result => result.score >= 12);
  if (!results.length) return null;
  const fr = language === 'fr';
  return [
    fr ? '**Précision nécessaire**' : '**Clarification needed**',
    fr
      ? 'Je ne peux pas relier cette formulation à un seul concept avec suffisamment de certitude. Vouliez-vous parler de :'
      : 'I cannot connect that wording to one concept with enough confidence. Did you mean:',
    ...results.map((result, index) => `${index + 1}. \`${result.record.canonicalName}\` — ${localizedKnowledgeSummary(result.record, language)}`),
  ].join('\n\n');
};

export const answerPythonPurposeQuestion = (question: string, language: KnowledgeLanguage): string | null => {
  if (!/\b(?:how can i|what should i use|which (?:method|function|type|tool)|best way to|comment (?:puis-je|faire)|que dois-je utiliser)\b/i.test(question)) return null;
  const recipes: Array<[RegExp, string[]]> = [
    [/\b(?:remove|avoid|without|supprimer|[eé]viter).*(?:duplicate|duplicates|doublons?)|\b(?:deduplicate|unique values?|valeurs uniques)\b/i, ['set', 'dict.fromkeys', 'list comprehension']],
    [/\b(?:sort|order|trier|ordonner).*(?:without|copy|new|sans modifier|nouvelle)\b/i, ['sorted', 'list.sort']],
    [/\b(?:read|open|load|lire|ouvrir|charger).*(?:file|fichier)\b/i, ['open', 'pathlib']],
    [/\b(?:length|size|number of items|longueur|taille|nombre d.ele?ments)\b/i, ['len']],
    [/\b(?:reverse|reversed|inverser|renverser).*(?:without|copy|new|sans modifier|nouvelle)\b/i, ['reversed', 'list.reverse', 'slicing']],
  ];
  const recipe = recipes.find(([pattern]) => pattern.test(question));
  const recipeResults = recipe?.[1].flatMap(term => {
    const resolution = resolvePythonKnowledge(term, typeFromPrefix(term));
    return resolution.record ? [{ matchedTerm: term, score: 100, record: resolution.record }] : [];
  }) || [];
  const results = recipeResults.length ? recipeResults : searchPythonKnowledge(question, 4).filter(result => result.score >= 8);
  if (!results.length) return null;
  const fr = language === 'fr';
  return [
    fr ? '**Outils Python correspondant au besoin**' : '**Python tools matching the goal**',
    fr ? 'Voici les options les plus proches, classées par pertinence :' : 'These are the closest verified options, ranked by relevance:',
    ...results.map((result, index) => [
      `${index + 1}. **${result.record.canonicalName}** — ${localizedKnowledgeSummary(result.record, language)}`,
      `${fr ? 'Syntaxe' : 'Syntax'}: \`${result.record.signature}\``,
      `${fr ? 'Modification' : 'Mutation'}: ${result.record.mutates}`,
    ].join('\n')),
    fr ? 'Si plusieurs options conviennent, précisez le type de données, la sortie attendue et si l’objet d’origine doit être modifié.' : 'If several options fit, specify the input type, expected output, and whether the original object may be modified.',
  ].join('\n\n');
};

export const answerPythonRelationships = (question: string, language: KnowledgeLanguage): string | null => {
  if (!/\b(?:related concepts?|concepts? (?:are )?related|what next|learn next|connected to|goes with|concepts? li[eé]s?|apprendre ensuite)\b/i.test(question)) return null;
  const stripped = question.replace(/\b(?:what|which|are|is|the|related|concepts?|to|learn|next|connected|goes|with|quels?|sont|les|li[eé]s?|apprendre|ensuite|à|de)\b/gi, ' ').replace(/\s+/g, ' ').trim();
  const direct = resolvePythonKnowledge(stripped);
  const record = direct.record || searchPythonKnowledge(stripped || question, 1)[0]?.record;
  if (!record) return null;
  const related = record.related.length ? record.related : searchPythonKnowledge(`${record.category} ${record.canonicalName}`, 6)
    .map(result => result.record.canonicalName)
    .filter(name => name.toLowerCase() !== record.canonicalName.toLowerCase())
    .slice(0, 5);
  const fr = language === 'fr';
  return [
    `**${fr ? 'Carte de concepts' : 'Concept map'}: ${record.canonicalName}**`,
    localizedKnowledgeSummary(record, language),
    `**${fr ? 'À apprendre ensuite' : 'Learn next'}**`,
    ...(related.length ? related.map((item, index) => `${index + 1}. \`${item}\``) : [fr ? 'Aucun lien précis n’est enregistré.' : 'No precise relationships are recorded.']),
    `**${fr ? 'Parcours conseillé' : 'Suggested path'}**\n${fr ? 'Commencez par la syntaxe, puis le comportement, les erreurs fréquentes et enfin les mécanismes internes.' : 'Start with syntax, then behavior, common mistakes, and finally internal mechanics.'}`,
  ].join('\n\n');
};

export const getKnowledgeCatalogSize = (): number => getAllConceptTerms().length;
