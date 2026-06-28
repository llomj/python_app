import { AiReviewRequest, AiReviewResult } from '../aiReviewTypes';

type EngineModule = typeof import('@mlc-ai/web-llm');

let enginePromise: Promise<any> | null = null;

export const supportsWebLlm = () => {
    return typeof navigator !== 'undefined' && 'gpu' in navigator;
};

const buildPrompt = (request: AiReviewRequest) => `
You are an offline Python code reviewer inside a learning app.
Return only JSON with keys: verdict, confidence, explanation, suggestedFix.
Allowed verdict values: likely_correct, likely_incorrect, unclear.
Do not award points. Do not claim certainty.

Problem ${request.problemId}: ${request.title}
Description: ${request.description}
Grader passed: ${request.graderPassed}
Grader message: ${request.graderMessage}
Program output: ${request.programOutput || ''}
User code:
\`\`\`python
${request.userCode}
\`\`\`
`;

const parseReviewJson = (text: string): AiReviewResult => {
    try {
        const parsed = JSON.parse(text);
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
            { role: 'system', content: 'You review beginner Python code and return strict JSON only.' },
            { role: 'user', content: buildPrompt(request) },
        ],
        temperature: 0.1,
        max_tokens: 350,
        response_format: { type: 'json_object' },
    });
    return parseReviewJson(response?.choices?.[0]?.message?.content || '');
};

export const resetWebLlmReviewer = async (modelId?: string) => {
    const pendingEngine = enginePromise;
    enginePromise = null;

    if (pendingEngine) {
        const engine = await pendingEngine.catch(() => null);
        if (engine?.unload) {
            await engine.unload();
        }
    }

    if (modelId) {
        const webllm = await import('@mlc-ai/web-llm');
        if (typeof webllm.deleteModelAllInfoInCache === 'function') {
            await webllm.deleteModelAllInfoInCache(modelId);
        }
    }
};
