export interface GeneralAiVerificationResult {
  valid: boolean;
  confidence: 'high' | 'medium' | 'low';
  reason: string;
}

export type GeneralAiEvidenceKind = 'runtime' | 'documentation' | 'static' | 'model';

export const formatGeneralAiEvidenceLabel = (kind: GeneralAiEvidenceKind, language: 'en' | 'fr'): string => {
  const fr = language === 'fr';
  const labels = {
    runtime: fr ? ['Exécution locale vérifiée', 'élevée', 'Le code ou les assertions ont été exécutés dans le moteur Python local borné.'] : ['Runtime verified', 'high', 'The code or assertions ran in the bounded local Python engine.'],
    documentation: fr ? ['Documentation vérifiée', 'élevée', 'La réponse contient une source appartenant à une documentation approuvée.'] : ['Documentation verified', 'high', 'The answer contains a source from an approved documentation host.'],
    static: fr ? ['Analyse statique', 'moyenne', 'La conclusion est déduite du code ou des données structurées sans exécuter tous les chemins.'] : ['Static analysis', 'medium', 'The conclusion is inferred from code or structured data without executing every path.'],
    model: fr ? ['Réponse du modèle', 'à vérifier', 'La réponse a passé les contrôles de structure, mais elle doit être confirmée par des tests ou la documentation.'] : ['Model-generated answer', 'requires verification', 'The answer passed structural checks but should be confirmed with tests or documentation.'],
  } as const;
  const [evidence, confidence, detail] = labels[kind];
  return `**${fr ? 'Preuve et confiance' : 'Evidence and confidence'}**\n${fr ? 'Preuve' : 'Evidence'}: **${evidence}** · ${fr ? 'Confiance' : 'Confidence'}: **${confidence}**\n${detail}`;
};

const ALLOWED_SOURCE_HOSTS = new Set([
  'docs.python.org', 'docs.djangoproject.com', 'fastapi.tiangolo.com', 'flask.palletsprojects.com',
  'matplotlib.org', 'numpy.org', 'pandas.pydata.org', 'requests.readthedocs.io', 'docs.scipy.org',
  'seaborn.pydata.org', 'xgboost.readthedocs.io', 'pyyaml.org',
]);

const QUESTION_STOP_WORDS = new Set([
  'a', 'an', 'and', 'about', 'can', 'could', 'does', 'explain', 'for', 'how', 'i', 'in', 'is', 'it',
  'me', 'of', 'on', 'please', 'python', 'the', 'this', 'to', 'what', 'which', 'why', 'with', 'you',
  'comment', 'dans', 'de', 'des', 'du', 'est', 'explique', 'la', 'le', 'les', 'pour', 'que', 'quel', 'quelle', 'un', 'une',
]);

const questionSubjects = (question: string): string[] => [...new Set(
  question.toLowerCase().match(/[a-z_][a-z0-9_.]{2,}/g) || [],
)].filter(token => !QUESTION_STOP_WORDS.has(token));

export const verifyGeneralAiAnswer = (question: string, answer: string): GeneralAiVerificationResult => {
  const value = answer.trim();
  if (value.length < 20) return { valid: false, confidence: 'low', reason: 'Answer is too short to be useful.' };
  if ((value.match(/```/g) || []).length % 2 !== 0) return { valid: false, confidence: 'low', reason: 'Answer contains an unclosed code block.' };
  if (/\b(?:as an ai|i think maybe|probably exists|invented example|placeholder answer)\b/i.test(value)) {
    return { valid: false, confidence: 'low', reason: 'Answer contains uncertain or placeholder wording.' };
  }
  const urls = [...value.matchAll(/https?:\/\/[^\s)]+/g)].map(match => match[0]);
  for (const url of urls) {
    try {
      if (!ALLOWED_SOURCE_HOSTS.has(new URL(url).hostname)) {
        return { valid: false, confidence: 'low', reason: `Unverified documentation host: ${new URL(url).hostname}` };
      }
    } catch {
      return { valid: false, confidence: 'low', reason: 'Answer contains an invalid source URL.' };
    }
  }
  if (urls.length > 0) return { valid: true, confidence: 'high', reason: 'Answer cites a verified documentation host.' };
  if (/\*\*(?:Source and confidence|Source et confiance)\*\*/i.test(value)) {
    return { valid: true, confidence: 'high', reason: 'Answer contains structured source and confidence metadata.' };
  }
  const requiresGrounding = /\b(?:what is|define|difference between|compare|how many|what does|qu['’]est-ce|définis|différence entre|compare|combien)\b/i.test(question);
  const subjects = questionSubjects(question);
  if (requiresGrounding && subjects.length && !subjects.some(subject => value.toLowerCase().includes(subject))) {
    return { valid: false, confidence: 'low', reason: 'Answer does not address the identifiable subject in the question.' };
  }
  return { valid: true, confidence: 'medium', reason: 'Answer passed structural checks but has no exact authoritative record.' };
};
