import { AiReviewRequest, AiReviewResult } from "../aiReviewTypes";

const OLLAMA_HOST = 'http://localhost:11434';
const OLLAMA_TIMEOUT_MS = 30000;
const PREFERRED_MODELS = ['qwen2.5-coder:1.5b', 'qwen2.5-coder:0.5b', 'llama3.2:3b', 'phi3:mini', 'codellama:7b'];
const REVIEW_TIMEOUT_MS = 25000;

let cachedAvailableModel: string | null = null;
let lastModelCheck = 0;

const withTimeout = async <T>(promise: Promise<T>, ms: number, msg: string): Promise<T> => {
    let id: ReturnType<typeof setTimeout> | undefined;
    const timeout = new Promise<never>((_, reject) => {
        id = setTimeout(() => reject(new Error(msg)), ms);
    });
    try {
        return await Promise.race([promise, timeout]);
    } finally {
        if (id) clearTimeout(id);
    }
};

export const isOllamaRunning = async (): Promise<boolean> => {
    try {
        const res = await withTimeout(
            fetch(`${OLLAMA_HOST}/api/tags`, { method: 'GET' }),
            2000,
            'Ollama not reachable',
        );
        return res.ok;
    } catch {
        return false;
    }
};

export const findAvailableCodeModel = async (): Promise<string | null> => {
    const now = Date.now();
    if (cachedAvailableModel && now - lastModelCheck < 30000) {
        return cachedAvailableModel;
    }
    try {
        const res = await withTimeout(
            fetch(`${OLLAMA_HOST}/api/tags`, { method: 'GET' }),
            3000,
            'Ollama not reachable',
        );
        if (!res.ok) return null;
        const data = await res.json();
        const installed: string[] = (data.models || []).map((m: any) => m.name);

        for (const preferred of PREFERRED_MODELS) {
            const match = installed.find(i => i.startsWith(preferred.replace(/:.*$/, '')));
            if (match) {
                cachedAvailableModel = match;
                lastModelCheck = now;
                return match;
            }
        }
        return null;
    } catch {
        return null;
    }
};

export const reviewWithOllama = async (request: AiReviewRequest, modelName: string): Promise<AiReviewResult> => {
    const prompt = `You are a Python tutor reviewing a student's code. Be specific and step-by-step.

Problem ${request.problemId}: ${request.title || ''}
${request.description || ''}

Student's code:
${request.userCode || '(empty)'}

${request.visibleSolution ? `Expected solution:
${request.visibleSolution}` : ''}

${request.graderMessage ? `Grader result: ${request.graderMessage}` : ''}
${request.programOutput ? `Program output: ${request.programOutput}` : ''}

Return JSON only (no markdown, no code fences):
{"verdict":"likely_correct","confidence":0.95,"explanation":"step-by-step analysis...","suggestedFix":"concise fix..."}

verdict: likely_correct | likely_incorrect | unclear
confidence: 0.0 to 1.0
explanation: restate the problem, then analyze the student's code step by step
suggestedFix: if incorrect, give the correct code or specific changes`;

    try {
        const res = await withTimeout(
            fetch(`${OLLAMA_HOST}/api/generate`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    model: modelName,
                    prompt: prompt,
                    stream: false,
                    options: { temperature: 0.1, num_predict: 800 },
                }),
            }),
            REVIEW_TIMEOUT_MS,
            'Ollama review timed out.',
        );
        if (!res.ok) {
            return {
                verdict: 'unclear',
                confidence: 0,
                explanation: `Ollama error: ${res.status} ${res.statusText}`,
                source: 'ollama',
            };
        }
        const data = await res.json();
        const text = String(data.response || '').trim();

        try {
            const cleaned = text.replace(/```json|```/g, '').trim();
            const parsed = JSON.parse(cleaned);
            const verdict = parsed.verdict === 'likely_correct' || parsed.verdict === 'likely_incorrect' || parsed.verdict === 'unclear'
                ? parsed.verdict : 'unclear';
            const confidence = Number.isFinite(Number(parsed.confidence))
                ? Math.max(0, Math.min(1, Number(parsed.confidence))) : 0.5;
            return {
                verdict,
                confidence,
                explanation: String(parsed.explanation || 'No explanation returned.'),
                suggestedFix: parsed.suggestedFix ? String(parsed.suggestedFix) : undefined,
                source: 'ollama',
            };
        } catch {
            return {
                verdict: 'unclear',
                confidence: 0.3,
                explanation: text.slice(0, 1500) || 'Model returned an unreadable response.',
                source: 'ollama',
            };
        }
    } catch (e: any) {
        return {
            verdict: 'unclear',
            confidence: 0,
            explanation: `Ollama review failed: ${e?.message || 'Unknown error'}`,
            source: 'ollama',
        };
    }
};
