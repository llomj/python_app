import {
  getAllConceptTerms,
  lookupConcept,
  type CategoryFallback,
  type ConceptEntry,
} from './pythonConceptLibrary';
import { lookupAll, type RefEntry } from './pythonReference';
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

export const isKnowledgeFollowUpQuestion = (question: string): boolean => {
  const trimmed = question.trim();
  if (/```|(^|\n)\s*(?:def |class |for |while |if |import |from |return |yield |[A-Za-z_]\w*\s*=)/m.test(trimmed)) return false;
  return /^(?:go deeper|more detail|explain more|break it down|approfondis|plus de details?|examples?|give (?:another )?examples?|show (?:another )?examples?|simplify|explain simply|explique simplement)\b/i.test(trimmed)
    || /\b(?:it|this|that|cela|ca|il|elle)\b/i.test(trimmed);
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
  'string', 'tuple', 'type',
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
  const match = cleaned.match(/^(?:(?:please\s+)?(?:what(?:'s|\s+is|\s+are|\s+does)|define|describe|explain|tell\s+me\s+about)|can\s+you\s+(?:define|describe|explain))\s+(.+)$/i);
  if (match) return normalizeTerm(match[1].replace(/\s+(?:do|does|mean|work)$/i, ''));
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
  const localized = (value: string): string => isFrench ? localizeAiText(value, 'fr') : value;
  const frenchCategory = FRENCH_CATEGORY[record.category] || record.category.replace(/_/g, ' ');
  const summary = isFrench && record.confidence === 'categorized'
    ? (FRENCH_PRECISE_SUMMARY[record.term.toLowerCase()] || `\`${record.canonicalName}\` est un terme Python associé au domaine ${frenchCategory}.`)
    : localized(record.summary);
  const details = isFrench && record.confidence === 'categorized'
    ? `Ce terme appartient au domaine ${frenchCategory}. Son comportement exact dépend de l\'API, de la syntaxe ou de la bibliothèque indiquée par le code. La source liée ci-dessous permet de vérifier sa signature et sa version.`
    : localized(record.details);
  const returns = isFrench && record.confidence === 'categorized'
    ? 'Cela dépend de l\'API ou de l\'opération précise.'
    : localized(record.returns);
  const raises = isFrench && record.confidence === 'categorized'
    ? 'Les exceptions dépendent de l\'opération, des arguments et des valeurs utilisés.'
    : localized(record.raises);
  const version = isFrench && record.confidence === 'categorized'
    ? 'Vérifiez la disponibilité exacte dans la documentation liée pour la version utilisée.'
    : localized(record.version);
  const kind = isFrench ? (FRENCH_KIND[record.kind] || record.kind) : record.kind;
  const mutation = isFrench
    ? ({ yes: 'Oui', no: 'Non', depends: 'Cela dépend', 'not-applicable': 'Sans objet' } as const)[record.mutates]
    : ({ yes: 'Yes', no: 'No', depends: 'Depends', 'not-applicable': 'Not applicable' } as const)[record.mutates];
  const exampleText = record.examples.length
    ? record.examples.slice(0, 3).map((example, index) => `${index + 1}. ${localized(example.title)}\n\`\`\`python\n${example.code}\n\`\`\``).join('\n\n')
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

const parseComparisonPair = (question: string): [string, string] | null => {
  const cleaned = question.trim().replace(/[?!]+$/g, '');
  const patterns = [
    /(?:what(?:'s| is)?\s+)?(?:the\s+)?difference between\s+(.+?)\s+and\s+(.+)$/i,
    /(?:compare|comparison of)\s+(.+?)\s+(?:with|to|and)\s+(.+)$/i,
    /^(?:(?:what(?:'s| is)?|define|explain)\s+)?(.+?)\s+(?:vs\.?|versus)\s+(.+)$/i,
  ];
  for (const pattern of patterns) {
    const match = cleaned.match(pattern);
    if (match) return [normalizeTerm(match[1]), normalizeTerm(match[2])];
  }
  return null;
};

export const answerPythonKnowledgeComparison = (question: string, language: KnowledgeLanguage): string | null => {
  const pair = parseComparisonPair(question);
  if (!pair) return null;
  const first = resolvePythonKnowledge(pair[0]);
  const second = resolvePythonKnowledge(pair[1]);
  if (first.alternatives.length) return ambiguityAnswer(first, language);
  if (second.alternatives.length) return ambiguityAnswer(second, language);
  if (!first.record || !second.record) return null;
  const a = first.record;
  const b = second.record;
  const isFrench = language === 'fr';
  return [
    `**${a.canonicalName} ${isFrench ? 'et' : 'vs'} ${b.canonicalName}**`,
    '',
    `| ${isFrench ? 'Critère' : 'Criterion'} | ${a.canonicalName} | ${b.canonicalName} |`,
    '|---|---|---|',
    `| ${isFrench ? 'Type' : 'Kind'} | ${a.kind} | ${b.kind} |`,
    `| ${isFrench ? 'But' : 'Purpose'} | ${a.summary} | ${b.summary} |`,
    `| ${isFrench ? 'Syntaxe' : 'Syntax'} | \`${a.signature}\` | \`${b.signature}\` |`,
    `| ${isFrench ? 'Modifie l\'objet' : 'Mutates object'} | ${a.mutates} | ${b.mutates} |`,
    `| ${isFrench ? 'Retour' : 'Returns'} | ${a.returns} | ${b.returns} |`,
    `| ${isFrench ? 'Version' : 'Version'} | ${a.version} | ${b.version} |`,
    '',
    `**${isFrench ? 'Regle pratique' : 'Practical rule'}**`,
    isFrench
      ? `Choisissez \`${a.canonicalName}\` lorsque son but correspond à votre besoin ; choisissez \`${b.canonicalName}\` lorsque vous avez besoin de son comportement de retour ou de modification.`
      : `Choose \`${a.canonicalName}\` when its purpose matches the task; choose \`${b.canonicalName}\` when you need its different return or mutation behavior.`,
    '',
    `**${isFrench ? 'Sources' : 'Sources'}**\n- ${a.sourceUrl}\n- ${b.sourceUrl}`,
  ].join('\n');
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
  const directDeep = trimmed.match(/^(?:go deeper on|explain in depth|deep explanation of)\s+(.+)$/i);
  if (directDeep) return { question: `what is ${normalizeTerm(directDeep[1])}`, mode: 'deep', usedContext: true };
  const directSimple = trimmed.match(/^(?:explain simply|simple explanation of)\s+(.+)$/i);
  if (directSimple) return { question: `what is ${normalizeTerm(directSimple[1])}`, mode: 'simple', usedContext: true };
  if (!previousQuestion) return { question: trimmed, mode: currentMode, usedContext: false };
  const subject = subjectFromQuestion(previousQuestion);
  if (/^(?:go deeper|more detail|explain more|break it down|approfondis|plus de details?)\b/i.test(trimmed)) {
    return { question: previousQuestion, mode: 'deep', usedContext: true };
  }
  if (/^(?:examples?|give (?:another )?examples?|show (?:another )?examples?|donne des exemples?)\b/i.test(trimmed)) {
    return { question: previousQuestion, mode: 'examples', usedContext: true };
  }
  if (/^(?:simplify|explain simply|explain more simply|simple|explique simplement)\b/i.test(trimmed)) {
    return { question: previousQuestion, mode: 'simple', usedContext: true };
  }
  if (/\b(?:it|this|that|cela|ca|il|elle)\b/i.test(trimmed)) {
    return {
      question: trimmed.replace(/\b(?:it|this|that|cela|ca|il|elle)\b/i, subject),
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
  const calls = [...code.matchAll(/(?:\.\s*)?([A-Za-z_]\w*)\s*\(/g)]
    .map(match => match[1])
    .filter(name => !['def', 'class', 'if', 'for', 'while'].includes(name));
  const uniqueCalls = [...new Set(calls)].slice(0, 15);
  const callDetails = uniqueCalls.map(name => {
    const resolution = resolvePythonKnowledge(name);
    if (resolution.alternatives.length) return `- \`${name}()\`: ${language === 'fr' ? 'nom ambigu; precisez le type de l\'objet' : 'ambiguous name; include the object type'}`;
    return resolution.record ? `- \`${name}()\`: ${resolution.record.summary}` : `- \`${name}()\`: ${language === 'fr' ? 'fonction definie par le programme ou une bibliotheque externe' : 'defined by the program or an external library'}`;
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

export const getKnowledgeCatalogSize = (): number => getAllConceptTerms().length;
