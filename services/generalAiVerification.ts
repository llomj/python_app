export interface GeneralAiVerificationResult {
  valid: boolean;
  confidence: 'high' | 'medium' | 'low';
  reason: string;
}

const ALLOWED_SOURCE_HOSTS = new Set([
  'docs.python.org', 'docs.djangoproject.com', 'fastapi.tiangolo.com', 'flask.palletsprojects.com',
  'matplotlib.org', 'numpy.org', 'pandas.pydata.org', 'requests.readthedocs.io', 'docs.scipy.org',
  'seaborn.pydata.org', 'xgboost.readthedocs.io', 'pyyaml.org',
]);

export const verifyGeneralAiAnswer = (_question: string, answer: string): GeneralAiVerificationResult => {
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
  return { valid: true, confidence: 'medium', reason: 'Answer passed structural checks but has no exact authoritative record.' };
};
