import { classifyGeneralAiIntent, type GeneralAiIntent, type GeneralAiIntentResult } from './generalAiIntent';
import type { GeneralAiResponseMode } from './generalAiMode';
import {
  resolveFuzzyPythonTerm,
  resolvePythonKnowledge,
  searchPythonKnowledge,
  type PythonKnowledgeRecord,
} from './pythonKnowledge';

export type GeneralAiPlannerLanguage = 'en' | 'fr';

export interface GeneralAiPlanEntity {
  raw: string;
  canonical: string;
  kind: string;
  confidence: number;
  alternatives: string[];
  record: PythonKnowledgeRecord | null;
}

export interface GeneralAiConversationContext {
  subjects: string[];
  previousQuestion: string;
  previousCode: string;
  unresolvedAlternatives: string[];
  selectedDepth: GeneralAiResponseMode;
  turns: number;
}

export interface GeneralAiQueryPlan {
  originalQuestion: string;
  normalizedQuestion: string;
  primary: GeneralAiIntentResult;
  intents: GeneralAiIntentResult[];
  entities: GeneralAiPlanEntity[];
  codeBlocks: string[];
  requestedDepth: GeneralAiResponseMode;
  requests: {
    comparison: boolean;
    examples: boolean;
    performance: boolean;
    executionOrder: boolean;
    internals: boolean;
    mistakes: boolean;
    sources: boolean;
    workflow: boolean;
  };
  confidence: number;
  needsClarification: boolean;
  clarification: string;
  usedConversationContext: boolean;
  groundingContext: string;
}

type PlannerMessage = { role: 'user' | 'assistant'; text: string };

const ENTITY_ALIASES: Record<string, string> = {
  arr: 'list',
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

const OWNER_REQUIRED_METHODS: Record<string, string[]> = {
  append: ['list.append', 'bytearray.append'],
  clear: ['list.clear', 'dict.clear', 'set.clear', 'bytearray.clear'],
  copy: ['list.copy', 'dict.copy', 'set.copy', 'bytearray.copy'],
  count: ['str.count', 'list.count', 'tuple.count', 'bytes.count', 'bytearray.count'],
  find: ['str.find', 'bytes.find', 'bytearray.find'],
  index: ['str.index', 'list.index', 'tuple.index', 'bytes.index', 'bytearray.index', 'range.index'],
  pop: ['list.pop', 'dict.pop', 'set.pop', 'bytearray.pop'],
  remove: ['list.remove', 'set.remove', 'bytearray.remove'],
  reverse: ['list.reverse', 'bytearray.reverse'],
};

const VERIFIED_PERFORMANCE_FACTS: Record<string, { en: string; fr: string }> = {
  list: {
    en: 'Index access is O(1), membership search is O(n), and append is amortized O(1). Inserting or removing near the front is O(n) because later references shift.',
    fr: 'L’accès par index est O(1), la recherche d’appartenance est O(n) et append est O(1) amorti. Insérer ou supprimer près du début est O(n), car les références suivantes sont décalées.',
  },
  tuple: {
    en: 'Index access is O(1) and membership search is O(n). A tuple is fixed-size and usually has less overhead than an equivalent list, but changing it requires a new tuple.',
    fr: 'L’accès par index est O(1) et la recherche d’appartenance est O(n). Un tuple a une taille fixe et généralement moins de surcharge qu’une liste équivalente, mais toute modification crée un nouveau tuple.',
  },
  dict: {
    en: 'Key lookup, insertion, and deletion are O(1) on average and O(n) in the pathological worst case. Dictionaries trade additional memory for hash-table lookup speed.',
    fr: 'La recherche, l’insertion et la suppression par clé sont O(1) en moyenne et O(n) dans le pire cas pathologique. Les dictionnaires utilisent plus de mémoire pour accélérer les recherches par table de hachage.',
  },
  set: {
    en: 'Membership, insertion, and deletion are O(1) on average and O(n) in the pathological worst case. Sets use hash-table storage and do not provide positional indexing.',
    fr: 'L’appartenance, l’insertion et la suppression sont O(1) en moyenne et O(n) dans le pire cas pathologique. Les ensembles utilisent une table de hachage et ne proposent pas d’indexation positionnelle.',
  },
  str: {
    en: 'Index access is O(1), searching is generally O(n), and strings are immutable. Repeated concatenation can copy growing strings; collect pieces and use join for large workloads.',
    fr: 'L’accès par index est O(1), la recherche est généralement O(n) et les chaînes sont immuables. Les concaténations répétées peuvent recopier des chaînes croissantes ; pour de gros volumes, collectez les morceaux puis utilisez join.',
  },
  bytes: {
    en: 'Index access is O(1) and searching is generally O(n). bytes is immutable, so transformations allocate a new bytes object.',
    fr: 'L’accès par index est O(1) et la recherche est généralement O(n). bytes est immuable : les transformations allouent donc un nouvel objet bytes.',
  },
  generator: {
    en: 'A generator produces values lazily, normally using O(1) additional state instead of storing every result. Total runtime still depends on the work performed for each yielded value.',
    fr: 'Un générateur produit les valeurs paresseusement et utilise normalement O(1) d’état supplémentaire au lieu de stocker tous les résultats. Le temps total dépend toutefois du travail effectué pour chaque valeur produite.',
  },
  iterator: {
    en: 'An iterator returns one item at a time and avoids materializing the entire input. Calling next is typically O(1), but the underlying iterator controls the actual cost.',
    fr: 'Un itérateur renvoie un élément à la fois et évite de matérialiser toute l’entrée. Un appel à next est généralement O(1), mais l’itérateur sous-jacent détermine le coût réel.',
  },
};

const ENTITY_STOP_WORDS = new Set([
  'about', 'again', 'also', 'and', 'answer', 'any', 'are', 'between', 'better', 'can', 'code', 'compare',
  'comparison', 'could', 'difference', 'does', 'example', 'examples', 'explain', 'for', 'from', 'give', 'how',
  'into', 'more', 'of', 'please', 'python', 'question', 'show', 'than', 'that', 'the', 'their', 'them', 'then',
  'this', 'use', 'using', 'versus', 'what', 'when', 'which', 'why', 'with', 'would',
  'avec', 'ceci', 'cela', 'comment', 'dans', 'des', 'différence', 'donne', 'entre', 'est', 'exemple', 'exemples',
  'explique', 'les', 'montre', 'plus', 'pour', 'pourquoi', 'quel', 'quelle', 'sont', 'une',
]);

const MULTIWORD_CONCEPTS = [
  'assignment expression', 'async iterator', 'context manager', 'dictionary comprehension', 'generator expression',
  'keyword argument', 'list comprehension', 'object oriented programming', 'positional argument', 'set comprehension',
  'type hint', 'variable scope',
];

const INTENT_RULES: Array<{ intent: GeneralAiIntent; confidence: number; pattern: RegExp }> = [
  { intent: 'comparison', confidence: 0.98, pattern: /\b(?:compare|difference between|different from|versus|vs\.?)\b/i },
  { intent: 'examples', confidence: 0.94, pattern: /\b(?:examples?|sample code|show (?:me )?(?:code|how)|exemples?|montre.*code)\b/i },
  { intent: 'performance', confidence: 0.93, pattern: /\b(?:performance|complexity|big[- ]?o|faster|slower|memory|speed|complexité|mémoire|rapide|lent)\b/i },
  { intent: 'execution_model', confidence: 0.95, pattern: /\b(?:execution order|evaluation order|what happens first|workflow|step by step|ordre d['’](?:exécution|évaluation)|étape par étape)\b/i },
  { intent: 'documentation', confidence: 0.93, pattern: /\b(?:official (?:docs|documentation)|documentation|source|reference|docs officielles?|référence)\b/i },
  { intent: 'error_help', confidence: 0.92, pattern: /\b(?:error|exception|traceback|fails?|wrong|erreur|exception|échoue|incorrect)\b/i },
  { intent: 'relationships', confidence: 0.90, pattern: /\b(?:related|relationship|learn next|connects? to|lié|relation|apprendre ensuite)\b/i },
  { intent: 'mechanism', confidence: 0.92, pattern: /\b(?:how (?:does|do|is)|internals?|under the hood|mechanism|fonctionnement|en interne|mécanisme)\b/i },
  { intent: 'count', confidence: 0.94, pattern: /\b(?:how many|number of|count of|combien|nombre de)\b/i },
  { intent: 'quiz', confidence: 0.95, pattern: /\b(?:quiz|test me|question me|interroge-moi)\b/i },
];

const codeBlocksFromQuestion = (question: string): string[] => {
  const fenced = [...question.matchAll(/```(?:python)?\s*\n?([\s\S]*?)```/gi)]
    .map(match => match[1].trim())
    .filter(Boolean);
  if (fenced.length) return fenced;
  if (/(^|\n)\s*(?:def |class |for |while |if |from |import |return |yield |print\(|[A-Za-z_]\w*\s*=)/m.test(question)) {
    return [question.split('\n').filter(line => !/^\s*(?:explain|analyse|analyze|debug|why|what does)\b/i.test(line)).join('\n').trim()];
  }
  return [];
};

const comparisonTerms = (question: string): string[] => {
  const cleaned = question.trim().replace(/[?!]+$/g, '');
  const patterns = [
    /difference between\s+(.+?)\s+and\s+(.+)$/i,
    /compare\s+(.+?)\s+(?:with|to|and)\s+(.+)$/i,
    /^(.+?)\s+(?:vs\.?|versus)\s+(.+)$/i,
    /différence entre\s+(.+?)\s+et\s+(.+)$/i,
    /compare\s+(.+?)\s+(?:avec|et)\s+(.+)$/i,
  ];
  for (const pattern of patterns) {
    const match = cleaned.match(pattern);
    if (match) return [match[1], match[2]].map(value => value.replace(/\b(?:and|with|including|show|explain|examples?|performance).*$/i, '').trim());
  }
  return [];
};

const candidateTerms = (question: string): string[] => {
  const withoutCode = question.replace(/```[\s\S]*?```/g, ' ');
  const catalogCommand = /^\s*(?:list|show|name)\s+(?:all|the|every)\b/i.test(withoutCode);
  const values = new Set<string>();
  comparisonTerms(withoutCode).forEach(value => values.add(value));
  for (const match of withoutCode.matchAll(/`([^`]{1,60})`/g)) values.add(match[1]);
  for (const match of withoutCode.matchAll(/\b([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)?)\s*\(/g)) values.add(match[1]);
  for (const match of withoutCode.matchAll(/\b([A-Za-z_]\w*\.[A-Za-z_]\w*)\b/g)) values.add(match[1]);
  const lower = withoutCode.toLowerCase();
  MULTIWORD_CONCEPTS.filter(concept => lower.includes(concept)).forEach(concept => values.add(concept));
  for (const word of withoutCode.match(/[A-Za-z_][A-Za-z0-9_.-]*/g) || []) {
    if (catalogCommand && /^(?:list|show|name|all|the|every)$/i.test(word)) continue;
    if (word.length > 1 && !ENTITY_STOP_WORDS.has(word.toLowerCase())) values.add(word);
  }
  return [...values].slice(0, 48);
};

const resolveEntities = (question: string): GeneralAiPlanEntity[] => {
  const entities: GeneralAiPlanEntity[] = [];
  const seen = new Set<string>();
  for (const rawValue of candidateTerms(question)) {
    const raw = rawValue.trim().replace(/\(\)$/, '');
    const alias = ENTITY_ALIASES[raw.toLowerCase()] || raw;
    const ownerAlternatives = !alias.includes('.') ? OWNER_REQUIRED_METHODS[alias.toLowerCase()] : undefined;
    if (ownerAlternatives) {
      const key = `ambiguous:${alias}`;
      if (!seen.has(key)) {
        seen.add(key);
        entities.push({ raw, canonical: alias, kind: 'ambiguous', confidence: 0.99, alternatives: ownerAlternatives, record: null });
      }
      continue;
    }
    let resolution = resolvePythonKnowledge(alias);
    let confidence = 0.98;
    if (!resolution.record && !resolution.alternatives.length && !alias.includes(' ')) {
      const fuzzy = resolveFuzzyPythonTerm(alias);
      if (fuzzy && fuzzy.distance > 0) {
        resolution = resolvePythonKnowledge(fuzzy.term);
        confidence = Math.max(0.72, 0.9 - fuzzy.distance * 0.08);
      }
    }
    const record = resolution.record;
    const alternatives = resolution.alternatives.map(item => `${item.kind}:${item.canonicalName}`);
    if (!record && !alternatives.length) continue;
    const canonical = record?.canonicalName || resolution.term;
    const key = `${record?.kind || 'ambiguous'}:${canonical}`.toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    entities.push({ raw, canonical, kind: record?.kind || 'ambiguous', confidence, alternatives, record });
  }
  if (!entities.length) {
    const semantic = searchPythonKnowledge(question, 1)[0];
    if (semantic && semantic.score >= 12) {
      entities.push({
        raw: semantic.matchedTerm,
        canonical: semantic.record.canonicalName,
        kind: semantic.record.kind,
        confidence: Math.min(0.82, 0.58 + semantic.score / 100),
        alternatives: [],
        record: semantic.record,
      });
    }
  }
  return entities.slice(0, 8);
};

const requestedDepthFromQuestion = (question: string, selected: GeneralAiResponseMode): GeneralAiResponseMode => {
  if (/\b(?:simple|simply|beginner|basic|short|easy|simplement|débutant|facile|court)\b/i.test(question)) return 'simple';
  if (/\b(?:expert|deep|deeper|go deeper|in depth|internals?|under the hood|advanced|approfondi|approfondis|en profondeur|interne|avancé)\b/i.test(question)) return 'deep';
  if (/\b(?:examples only|mostly examples|several examples|progressive examples|exemples seulement|plusieurs exemples)\b/i.test(question)) return 'examples';
  if (/\b(?:intermediate|normal detail|intermédiaire)\b/i.test(question)) return 'normal';
  return selected;
};

const intentCandidates = (question: string, primary: GeneralAiIntentResult): GeneralAiIntentResult[] => {
  const candidates: GeneralAiIntentResult[] = [primary];
  for (const rule of INTENT_RULES) {
    if (rule.intent !== primary.intent && rule.pattern.test(question)) {
      candidates.push({ intent: rule.intent, confidence: rule.confidence, reason: 'Secondary request detected by the structured planner' });
    }
  }
  const seen = new Set<GeneralAiIntent>();
  return candidates.filter(candidate => {
    if (seen.has(candidate.intent)) return false;
    seen.add(candidate.intent);
    return true;
  });
};

const groundingForEntities = (entities: GeneralAiPlanEntity[], language: GeneralAiPlannerLanguage): string => {
  const records = entities.map(entity => entity.record).filter((record): record is PythonKnowledgeRecord => Boolean(record)).slice(0, 4);
  if (!records.length) return '';
  const fr = language === 'fr';
  return [
    fr ? 'RÉFÉRENCES PYTHON HORS LIGNE VÉRIFIÉES' : 'VERIFIED OFFLINE PYTHON REFERENCES',
    ...records.map(record => [
      `[${record.canonicalName}]`,
      `${fr ? 'Type' : 'Kind'}: ${record.kind}`,
      `${fr ? 'Résumé' : 'Summary'}: ${record.summary}`,
      `${fr ? 'Syntaxe' : 'Signature'}: ${record.signature}`,
      `${fr ? 'Retour' : 'Returns'}: ${record.returns}`,
      `${fr ? 'Modification' : 'Mutates'}: ${record.mutates}`,
      `${fr ? 'Erreurs' : 'Raises'}: ${record.raises}`,
      `${fr ? 'Version' : 'Version'}: ${record.version}`,
      `${fr ? 'Source' : 'Source'}: ${record.sourceUrl}`,
    ].join('\n')),
  ].join('\n\n');
};

export const buildGeneralAiConversationContext = (
  messages: PlannerMessage[],
  language: GeneralAiPlannerLanguage,
  selectedDepth: GeneralAiResponseMode,
): GeneralAiConversationContext => {
  const userMessages = messages.filter(message => message.role === 'user').slice(-8);
  const previousQuestion = userMessages.at(-1)?.text || '';
  const previousCode = [...userMessages].reverse().flatMap(message => codeBlocksFromQuestion(message.text))[0] || '';
  const subjects: string[] = [];
  for (const message of [...userMessages].reverse()) {
    for (const entity of resolveEntities(message.text)) {
      if (!subjects.includes(entity.canonical)) subjects.push(entity.canonical);
      if (subjects.length >= 4) break;
    }
    if (subjects.length >= 4) break;
  }
  const previousAssistant = [...messages].reverse().find(message => message.role === 'assistant')?.text || '';
  const unresolvedAlternatives = [...previousAssistant.matchAll(/`([^`]+)`/g)].map(match => match[1]).slice(0, 8);
  return { subjects, previousQuestion, previousCode, unresolvedAlternatives, selectedDepth, turns: userMessages.length };
};

const clarificationForPlan = (
  primary: GeneralAiIntentResult,
  entities: GeneralAiPlanEntity[],
  requestsComparison: boolean,
  language: GeneralAiPlannerLanguage,
): string => {
  const fr = language === 'fr';
  const ambiguous = entities.find(entity => entity.alternatives.length > 1);
  if (ambiguous) {
    return [
      `**${fr ? 'Précision nécessaire' : 'Clarification needed'}**`,
      fr ? `Le nom \`${ambiguous.raw}\` correspond à plusieurs API. Laquelle voulez-vous ?` : `The name \`${ambiguous.raw}\` matches several APIs. Which one do you mean?`,
      ...ambiguous.alternatives.map((item, index) => `${index + 1}. \`${item}\``),
    ].join('\n\n');
  }
  if (requestsComparison && entities.length < 2) {
    return fr
      ? '**Précision nécessaire**\n\nIndiquez les deux concepts Python à comparer, par exemple `list vs dict`.'
      : '**Clarification needed**\n\nName both Python concepts to compare, for example `list vs dict`.';
  }
  if (primary.intent === 'unknown') {
    return fr
      ? '**Précision nécessaire**\n\nJe ne peux pas identifier avec certitude la question Python. Indiquez le concept, le code ou l’erreur concerné.'
      : '**Clarification needed**\n\nI cannot identify the Python question confidently. Name the concept, paste the code, or include the exact error.';
  }
  return '';
};

export const planGeneralAiQuestion = (
  question: string,
  language: GeneralAiPlannerLanguage,
  selectedDepth: GeneralAiResponseMode,
  context?: GeneralAiConversationContext,
): GeneralAiQueryPlan => {
  const normalizedQuestion = question.trim().replace(/\s+/g, ' ');
  const primary = classifyGeneralAiIntent(question);
  const intents = intentCandidates(question, primary);
  let entities = resolveEntities(question);
  const vagueFollowUp = /^(?:it|this|that|why|how|more|go deeper|another example|examples?|cela|ça|pourquoi|comment|plus|approfondis)\b/i.test(normalizedQuestion);
  let usedConversationContext = false;
  if ((!entities.length || vagueFollowUp) && context?.subjects.length) {
    const contextualEntities = context.subjects.map(subject => resolveEntities(subject)[0]).filter(Boolean);
    if (contextualEntities.length) {
      entities = [...entities, ...contextualEntities].filter((entity, index, all) => all.findIndex(item => item.canonical === entity.canonical && item.kind === entity.kind) === index);
      usedConversationContext = true;
    }
  }
  const requestedDepth = requestedDepthFromQuestion(question, selectedDepth);
  const requests = {
    comparison: intents.some(item => item.intent === 'comparison'),
    examples: intents.some(item => item.intent === 'examples') || requestedDepth === 'examples',
    performance: intents.some(item => ['performance', 'complexity_analysis', 'profiling'].includes(item.intent)),
    executionOrder: intents.some(item => item.intent === 'execution_model'),
    internals: requestedDepth === 'deep' || /\b(?:internals?|under the hood|implementation|en interne)\b/i.test(question),
    mistakes: /\b(?:mistakes?|pitfalls?|errors?|wrong|erreurs?|pièges?)\b/i.test(question) || ['normal', 'deep'].includes(requestedDepth),
    sources: intents.some(item => item.intent === 'documentation') || requestedDepth === 'deep',
    workflow: /\b(?:workflow|steps?|how (?:does|to)|process|étapes?|fonctionnement)\b/i.test(question) || ['normal', 'deep'].includes(requestedDepth),
  };
  const clarification = clarificationForPlan(primary, entities, requests.comparison, language);
  const entityConfidence = entities.length ? entities.reduce((total, entity) => total + entity.confidence, 0) / entities.length : primary.confidence;
  const confidence = Math.max(0, Math.min(1, primary.confidence * 0.65 + entityConfidence * 0.35));
  return {
    originalQuestion: question,
    normalizedQuestion,
    primary,
    intents,
    entities,
    codeBlocks: codeBlocksFromQuestion(question),
    requestedDepth,
    requests,
    confidence,
    needsClarification: Boolean(clarification),
    clarification,
    usedConversationContext,
    groundingContext: groundingForEntities(entities, language),
  };
};

const progressiveExamples = (entities: GeneralAiPlanEntity[], language: GeneralAiPlannerLanguage): string => {
  const examples = entities.flatMap(entity => (entity.record?.examples || []).map(example => ({ entity, example }))).slice(0, 4);
  if (!examples.length) return '';
  const fr = language === 'fr';
  return [
    `**${fr ? 'Exemples vérifiés progressifs' : 'Verified progressive examples'}**`,
    ...examples.map(({ entity, example }, index) => `${index + 1}. **${entity.canonical}: ${example.title}**\n\`\`\`python\n${example.code}\n\`\`\``),
  ].join('\n\n');
};

export const enrichGeneralAiAnswerFromPlan = (
  answer: string,
  plan: GeneralAiQueryPlan,
  language: GeneralAiPlannerLanguage,
): string => {
  if (plan.needsClarification || plan.requestedDepth === 'simple') return answer;
  const fr = language === 'fr';
  const additions: string[] = [];
  const records = plan.entities.map(entity => entity.record).filter((record): record is PythonKnowledgeRecord => Boolean(record));
  if (plan.requests.examples && !/```python/i.test(answer)) {
    const examples = progressiveExamples(plan.entities, language);
    if (examples) additions.push(examples);
  }
  if ((plan.requests.executionOrder || plan.requests.workflow) && records.length && !/\*\*(?:Workflow|Déroulement|Execution|Exécution)/i.test(answer)) {
    additions.push([
      `**${fr ? 'Contrats vérifiés' : 'Verified contracts'}**`,
      ...records.slice(0, 4).map((record, index) => `${index + 1}. \`${record.signature}\` — ${fr ? 'renvoie' : 'returns'} ${record.returns}; ${fr ? 'modifie' : 'mutates'}: ${record.mutates}.`),
    ].join('\n'));
  }
  if (plan.requests.performance) {
    const verifiedFacts = plan.entities.flatMap(entity => {
      const fact = VERIFIED_PERFORMANCE_FACTS[entity.canonical.toLowerCase()];
      return fact ? [`- **${entity.canonical}:** ${fact[language]}`] : [];
    });
    const recordNotes = records.flatMap(record => record.details.split(/(?<=[.!?])\s+/)
      .filter(sentence => /\b(?:O\(|complexity|performance|memory|linear|constant|quadratic|lazy|complexité|mémoire|linéaire|constant)\b/i.test(sentence))
      .slice(0, 2)
      .map(sentence => `- **${record.canonicalName}:** ${sentence}`));
    const performanceNotes = [...new Set([...verifiedFacts, ...recordNotes])];
    if (performanceNotes.length && !/\*\*(?:Performance|Complexité)/i.test(answer)) {
      additions.push(`**${fr ? 'Performance vérifiée' : 'Verified performance notes'}**\n${performanceNotes.join('\n')}`);
    }
  }
  if (plan.requests.internals && records.length && !/\*\*(?:Internals|Mécanismes internes|In-depth|Analyse approfondie)/i.test(answer)) {
    additions.push([
      `**${fr ? 'Mécanismes et cas limites' : 'Mechanics and edge cases'}**`,
      ...records.slice(0, 3).map(record => `- **${record.canonicalName}:** ${record.details}\n  ${fr ? 'Erreurs' : 'Raises'}: ${record.raises}`),
    ].join('\n'));
  }
  if (plan.requests.sources && records.length && !/https?:\/\//.test(answer)) {
    additions.push([
      `**${fr ? 'Sources Python vérifiées' : 'Verified Python sources'}**`,
      ...records.slice(0, 4).map(record => `- **${record.canonicalName}:** ${record.sourceUrl} (${record.version})`),
    ].join('\n'));
  }
  return [answer, ...additions].filter(Boolean).join('\n\n');
};

export const buildGroundedGeneralAiModelQuestion = (plan: GeneralAiQueryPlan): string => {
  if (!plan.groundingContext) return plan.originalQuestion;
  return [
    plan.originalQuestion,
    '',
    'Use the verified offline references below as factual constraints. Do not contradict them. If they do not answer the question, state what remains uncertain.',
    plan.groundingContext,
  ].join('\n');
};

export const recordGeneralAiCoverageGap = (plan: GeneralAiQueryPlan, reason: string): void => {
  if (typeof localStorage === 'undefined') return;
  try {
    if (localStorage.getItem('python_general_ai_local_learning_enabled') !== 'true') return;
    const key = 'python_general_ai_coverage_gaps';
    const existing = JSON.parse(localStorage.getItem(key) || '[]');
    const events = Array.isArray(existing) ? existing : [];
    events.push({
      time: new Date().toISOString(),
      question: plan.normalizedQuestion.slice(0, 500),
      intents: plan.intents.map(item => item.intent),
      entities: plan.entities.map(entity => entity.canonical),
      confidence: Number(plan.confidence.toFixed(3)),
      reason,
    });
    localStorage.setItem(key, JSON.stringify(events.slice(-100)));
  } catch {
    // Coverage logging is local-only and must never block an answer.
  }
};

export const assessGeneralAiDepthContract = (answer: string, mode: GeneralAiResponseMode): { valid: boolean; missing: string[] } => {
  const missing: string[] = [];
  if (mode === 'simple' && answer.length > 2200) missing.push('concise answer');
  if (mode === 'normal' && !/(?:workflow|steps?|common mistakes|déroulement|étapes?|erreurs fréquentes)/i.test(answer)) missing.push('workflow or common mistakes');
  if (mode === 'deep' && !/(?:internals?|mechanics|edge cases?|tradeoffs?|mécanismes?|cas limites?|compromis)/i.test(answer)) missing.push('internals and edge cases');
  if (mode === 'examples' && (answer.match(/```python/g) || []).length < 2) missing.push('multiple Python examples');
  return { valid: missing.length === 0, missing };
};
