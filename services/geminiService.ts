import { AiReviewRequest, AiReviewResult } from '../aiReviewTypes';
import type { GeneralAiResponseMode } from './generalAiMode';

const REVIEW_TIMEOUT_MS = 15000;

export type OnlineAiProvider = 'gemini' | 'openai_compatible';

export interface OnlineAiConfig {
    provider: OnlineAiProvider;
    apiKey: string;
    endpoint: string;
    model: string;
}

export const loadOnlineAiConfig = (): OnlineAiConfig => {
    const legacyKey = localStorage.getItem('gemini_api_key') || '';
    const provider = localStorage.getItem('online_ai_provider') === 'openai_compatible' ? 'openai_compatible' : 'gemini';
    return {
        provider,
        apiKey: localStorage.getItem('online_ai_api_key') || legacyKey,
        endpoint: localStorage.getItem('online_ai_endpoint') || 'https://api.openai.com/v1',
        model: localStorage.getItem('online_ai_model') || (provider === 'gemini' ? 'gemini-2.0-flash' : 'gpt-4o-mini'),
    };
};

export const saveOnlineAiConfig = (config: OnlineAiConfig): void => {
    localStorage.setItem('online_ai_provider', config.provider);
    localStorage.setItem('online_ai_api_key', config.apiKey.trim());
    localStorage.setItem('online_ai_endpoint', config.endpoint.trim());
    localStorage.setItem('online_ai_model', config.model.trim());
    if (config.provider === 'gemini') localStorage.setItem('gemini_api_key', config.apiKey.trim());
};

export const hasOnlineAiKey = (): boolean => {
    try {
        return loadOnlineAiConfig().apiKey.trim().length > 10;
    } catch {
        return false;
    }
};

const withTimeout = async <T>(promise: Promise<T>): Promise<T> => {
    let timeoutId = 0;
    const timeout = new Promise<never>((_, reject) => {
        timeoutId = window.setTimeout(() => reject(new Error('Online AI timed out after 15 seconds.')), REVIEW_TIMEOUT_MS);
    });
    try {
        return await Promise.race([promise, timeout]);
    } finally {
        window.clearTimeout(timeoutId);
    }
};

const generateOnlineText = async (messages: Array<{ role: 'system' | 'user' | 'assistant'; content: string }>, maxTokens = 1000): Promise<string> => {
    const config = loadOnlineAiConfig();
    if (!config.apiKey) throw new Error('No AI API key is configured.');
    if (config.provider === 'gemini') {
        const { GoogleGenAI } = await import('@google/genai');
        const ai = new GoogleGenAI({ apiKey: config.apiKey });
        const prompt = messages.map(message => `${message.role.toUpperCase()}: ${message.content}`).join('\n\n');
        const response = await withTimeout(ai.models.generateContent({
            model: config.model || 'gemini-2.0-flash',
            contents: prompt,
            config: { temperature: 0.2, maxOutputTokens: maxTokens },
        }));
        return String((response as any).text || '').trim();
    }
    const endpoint = `${config.endpoint.replace(/\/+$/, '')}/chat/completions`;
    const response = await withTimeout(fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${config.apiKey}` },
        body: JSON.stringify({ model: config.model, messages, temperature: 0.2, max_tokens: maxTokens }),
    }));
    if (!response.ok) throw new Error(`AI API returned HTTP ${response.status}.`);
    const payload = await response.json();
    return String(payload?.choices?.[0]?.message?.content || '').trim();
};

export const reviewWithOnlineAi = async (request: AiReviewRequest): Promise<AiReviewResult> => {
    const prompt = `Problem ${request.problemId}: ${request.title || ''}\n${request.description || ''}\n\nStudent code:\n${request.userCode || '(empty)'}\n\nGrader result: ${request.graderMessage || 'none'}\nProgram output: ${request.programOutput || 'none'}\n\nJudge the logic against the problem, not against literal names or sample values. Return JSON only: {"verdict":"likely_correct|likely_incorrect|unclear","confidence":0.0,"explanation":"specific reasoning","suggestedFix":"optional fix"}. Never mark code correct if it has a syntax/runtime error.`;
    try {
        const text = await generateOnlineText([
            { role: 'system', content: 'You are a precise Python code grader. Test semantics and accept equivalent implementations.' },
            { role: 'user', content: prompt },
        ], 900);
        const parsed = JSON.parse(text.replace(/```json|```/g, '').trim());
        const verdict = ['likely_correct', 'likely_incorrect', 'unclear'].includes(parsed.verdict) ? parsed.verdict : 'unclear';
        return {
            verdict,
            confidence: Math.max(0, Math.min(1, Number(parsed.confidence) || 0)),
            explanation: String(parsed.explanation || 'The AI API returned no explanation.'),
            suggestedFix: parsed.suggestedFix ? String(parsed.suggestedFix) : undefined,
            source: 'online_api',
        };
    } catch (error: any) {
        return { verdict: 'unclear', confidence: 0, explanation: `AI API review failed: ${error?.message || 'Unknown error'}`, source: 'online_api' };
    }
};

export const answerGeneralPythonWithOnlineAi = async (
    question: string,
    history: Array<{ role: 'system' | 'user' | 'assistant'; content: string }>,
    language: 'en' | 'fr',
    mode: GeneralAiResponseMode,
): Promise<string | null> => {
    if (!hasOnlineAiKey()) return null;
    const answer = await generateOnlineText([
        {
            role: 'system',
            content: `You are an interactive Python tutor. Answer in ${language === 'fr' ? 'French' : 'English'} at ${mode} depth. Plain prose is white; put Python code only in fenced python blocks. Be accurate, state uncertainty, preserve follow-up context, and explain argument order, evaluation order, scope, and edge cases when relevant.`,
        },
        ...history,
        { role: 'user', content: question },
    ], 1400);
    return answer.length >= 20 ? answer : null;
};

// Backward-compatible exports for older callers and stored Gemini keys.
export const hasGeminiKey = hasOnlineAiKey;
export const reviewWithGemini = reviewWithOnlineAi;
