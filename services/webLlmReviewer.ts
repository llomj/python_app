import { AiReviewRequest, AiReviewResult } from '../aiReviewTypes';

type EngineModule = typeof import('@mlc-ai/web-llm');

let enginePromise: Promise<any> | null = null;

export const isAppleMobileBrowser = () => {
    if (typeof navigator === 'undefined') {
        return false;
    }
    const userAgent = navigator.userAgent || '';
    const platform = navigator.platform || '';
    return (
        /iPad|iPhone|iPod/i.test(userAgent)
        || (platform === 'MacIntel' && navigator.maxTouchPoints > 1)
    );
};

export const supportsWebLlm = () => {
    if (typeof navigator === 'undefined') {
        return false;
    }
    const nav = navigator as Navigator & { gpu?: { requestAdapter?: unknown } };
    return Boolean(nav.gpu && typeof nav.gpu.requestAdapter === 'function');
};

const clampText = (text: string, maxLength: number) => (
    text.length > maxLength ? `${text.slice(0, maxLength)}...` : text
);

const buildPrompt = (request: AiReviewRequest) => `
Review this beginner Python answer against the exact problem, grader result, and program output.
Return JSON only:
{"verdict":"likely_correct|likely_incorrect|unclear","confidence":0.0,"explanation":"specific review","suggestedFix":"specific fix or empty"}

Rules:
- If the grader passed, explain why the code satisfies the prompt.
- If the grader failed, identify the exact mismatch between prompt, code, output, and expected behavior.
- Mention missing return values, wrong function names, wrong parameters, forbidden APIs, and edge cases when relevant.
- Put corrected Python code in suggestedFix when useful.

Problem ${request.problemId}
Title: ${clampText(request.title, 300)}
Description: ${clampText(request.description, 1200)}
Grader passed: ${request.graderPassed ? 'yes' : 'no'}
Grader message: ${clampText(request.graderMessage, 500)}
Output: ${clampText(request.programOutput || '', 500)}
User code:
${clampText(request.userCode, 1800)}
${request.visibleSolution ? `Expected solution:\n${clampText(request.visibleSolution, 600)}` : ''}
`;

const parseReviewJson = (text: string): AiReviewResult => {
    try {
        const cleaned = text.replace(/```json|```/g, '').trim();
        const jsonMatch = cleaned.match(/\{[\s\S]*\}/);
        const parsed = JSON.parse(jsonMatch ? jsonMatch[0] : cleaned);
        const verdict = parsed.verdict === 'likely_correct' || parsed.verdict === 'likely_incorrect' || parsed.verdict === 'unclear'
            ? parsed.verdict
            : 'unclear';
        const confidence = Number.isFinite(Number(parsed.confidence))
            ? Math.max(0, Math.min(1, Number(parsed.confidence)))
            : 0.5;
        return {
            verdict,
            confidence,
            explanation: String(parsed.explanation || 'The offline reviewer returned no explanation.'),
            suggestedFix: parsed.suggestedFix ? String(parsed.suggestedFix) : undefined,
            source: 'offline_model',
        };
    } catch {
        return {
            verdict: 'unclear',
            confidence: 0.4,
            explanation: text.slice(0, 1200) || 'The offline reviewer returned an unreadable response.',
            source: 'offline_model',
        };
    }
};

export const loadWebLlmReviewer = async (modelId: string, onProgress?: (progress: number, message: string) => void) => {
    if (!supportsWebLlm()) {
        throw new Error('WebGPU is not available on this device/browser.');
    }
    if (!enginePromise) {
        const loadPromise = import('@mlc-ai/web-llm').then(async (webllm: EngineModule) => {
            const engine = await webllm.CreateMLCEngine(modelId, {
                initProgressCallback: (report: any) => {
                    const progress = typeof report?.progress === 'number' ? report.progress : 0;
                    const text = String(report?.text || 'Downloading offline AI model...');
                    onProgress?.(progress, text);
                },
            });
            return engine;
        });
        const guardedPromise = loadPromise.catch(error => {
            if (enginePromise === guardedPromise) {
                enginePromise = null;
            }
            throw error;
        });
        enginePromise = guardedPromise;
    }
    return enginePromise;
};

export const reviewWithWebLlm = async (request: AiReviewRequest, modelId: string): Promise<AiReviewResult> => {
    const engine = await loadWebLlmReviewer(modelId);
    const response = await engine.chat.completions.create({
        messages: [
            { role: 'system', content: 'You are a precise Python tutor and code reviewer. Return valid JSON only.' },
            { role: 'user', content: buildPrompt(request) },
        ],
        temperature: 0.1,
        max_tokens: 420,
    });
    return parseReviewJson(response?.choices?.[0]?.message?.content || '');
};

export const testWebLlmReviewer = async (modelId: string) => {
    const engine = await loadWebLlmReviewer(modelId);
    const response = await engine.chat.completions.create({
        messages: [
            { role: 'system', content: 'Return only the word ready.' },
            { role: 'user', content: 'Health check.' },
        ],
        temperature: 0,
        max_tokens: 8,
    });
    const text = String(response?.choices?.[0]?.message?.content || '').trim();
    if (!text) {
        throw new Error('Offline model loaded but did not return a test response.');
    }
    return text;
};

export const resetWebLlmReviewer = async (modelId?: string) => {
    const pendingEngine = enginePromise;
    enginePromise = null;

    if (pendingEngine) {
        pendingEngine
            .then(engine => engine?.unload?.())
            .catch(() => undefined);
    }

    if (modelId && supportsWebLlm()) {
        const webllm = await import('@mlc-ai/web-llm');
        if (typeof webllm.deleteModelAllInfoInCache === 'function') {
            await webllm.deleteModelAllInfoInCache(modelId);
        }
    }
};
