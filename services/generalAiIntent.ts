export type GeneralAiIntent =
  | 'traceback'
  | 'code_explanation'
  | 'comparison'
  | 'count'
  | 'creation'
  | 'version'
  | 'quiz'
  | 'examples'
  | 'error_help'
  | 'documentation'
  | 'definition'
  | 'unknown';

export interface GeneralAiIntentResult {
  intent: GeneralAiIntent;
  confidence: number;
  reason: string;
}

const containsCode = (question: string): boolean => (
  /```(?:python)?/i.test(question)
  || /(^|\n)\s*(?:def |class |for |while |if |from |import |return |yield |print\(|[A-Za-z_]\w*\s*=)/m.test(question)
);

export const classifyGeneralAiIntent = (question: string): GeneralAiIntentResult => {
  const value = question.trim();
  const lower = value.toLowerCase();
  if (/traceback \(most recent call last\)|(^|\n)\s*file ".+", line \d+/i.test(value)) {
    return { intent: 'traceback', confidence: 1, reason: 'Python traceback frames detected' };
  }
  if (containsCode(value) && /explain|analyse|analyze|debug|why|output|code|ligne|erreur/i.test(value)) {
    return { intent: 'code_explanation', confidence: 0.98, reason: 'Python code and an analysis request detected' };
  }
  if (/\b(?:difference between|compare|versus|vs\.?|diff[eé]rence entre|compar(?:e|er))\b/i.test(lower)) {
    return { intent: 'comparison', confidence: 0.98, reason: 'Comparison phrasing detected' };
  }
  if (/\b(?:how many|number of|count of|combien|nombre de)\b/i.test(lower)) {
    return { intent: 'count', confidence: 0.96, reason: 'Count request detected' };
  }
  if (/\b(?:how (?:do|can|would) (?:i|you)|how to|comment)\b/i.test(lower)
    && /\b(?:create|make|write|build|define|start|use|cr[eé]er|faire|[eé]crire|d[eé]finir|utiliser)\b/i.test(lower)) {
    return { intent: 'creation', confidence: 0.94, reason: 'How-to creation request detected' };
  }
  if (/\b(?:what version|which version|when was|introduced|added in|deprecated|version|quelle version|ajout[eé]|introduit)\b/i.test(lower)) {
    return { intent: 'version', confidence: 0.94, reason: 'Version request detected' };
  }
  if (/\b(?:quiz|test me|practice me|check my understanding|interroge-moi|teste-moi)\b/i.test(lower)) {
    return { intent: 'quiz', confidence: 0.96, reason: 'Quiz request detected' };
  }
  if (/\b(?:examples?|show me|another example|exemples?|montre-moi)\b/i.test(lower)) {
    return { intent: 'examples', confidence: 0.88, reason: 'Example request detected' };
  }
  if (/\b(?:documentation|official docs?|reference|docs? for|documentation officielle|r[eé]f[eé]rence)\b/i.test(lower)) {
    return { intent: 'documentation', confidence: 0.94, reason: 'Documentation request detected' };
  }
  if (/\b(?:syntaxerror|typeerror|nameerror|valueerror|keyerror|indexerror|indentationerror|attributeerror|exception|error|erreur)\b/i.test(lower)) {
    return { intent: 'error_help', confidence: 0.91, reason: 'Python error name or error request detected' };
  }
  if (/^(?:please\s+)?(?:what(?:'s|\s+is|\s+are|\s+does)|define|describe|explain|tell me about|qu['’]est-ce que|d[eé]finis?|explique|d[eé]cris)\b/i.test(value)
    || value.split(/\s+/).length <= 4) {
    return { intent: 'definition', confidence: 0.82, reason: 'Definition or short concept query detected' };
  }
  if (containsCode(value)) {
    return { intent: 'code_explanation', confidence: 0.76, reason: 'Python code detected' };
  }
  return { intent: 'unknown', confidence: 0.35, reason: 'No reliable Python intent matched' };
};

export const shouldClarifyGeneralAiQuestion = (question: string): boolean => {
  const value = question.trim();
  if (!value) return true;
  if (/^(?:it|this|that|more|why|how|yes|no|cela|ça|pourquoi|comment)[?.!]*$/i.test(value)) return true;
  return classifyGeneralAiIntent(value).intent === 'unknown' && value.split(/\s+/).length < 3;
};
