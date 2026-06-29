import { GoogleGenAI } from "@google/genai";
import { AiReviewRequest, AiReviewResult } from "../aiReviewTypes";

const REVIEW_TIMEOUT_MS = 15000;

export const hasGeminiKey = (): boolean => {
    try {
        const key = localStorage.getItem('gemini_api_key');
        return Boolean(key && key.trim().length > 10);
    } catch {
        return false;
    }
};

export const reviewWithGemini = async (request: AiReviewRequest): Promise<AiReviewResult> => {
    const apiKey = localStorage.getItem('gemini_api_key') || '';
    if (!apiKey) {
        return {
            verdict: 'unclear',
            confidence: 0,
            explanation: 'No Gemini API key found. Add one in Settings > API Key.',
            source: 'gemini',
        };
    }

    const prompt = `You are a Python tutor reviewing a student's code for a coding problem.

Problem ${request.problemId}: ${request.title || ''}
${request.description || ''}

Student's code:
\`\`\`python
${request.userCode || '(empty)'}
\`\`\`

${request.visibleSolution ? `Expected solution:
\`\`\`python
${request.visibleSolution}
\`\`\`` : ''}

${request.graderMessage ? `Grader result: ${request.graderMessage}` : ''}
${request.programOutput ? `Program output: ${request.programOutput}` : ''}

Review this answer. First read the problem carefully. Then compare the student's code against the expected solution. Explain step by step what the student did wrong (if anything) and why. Be specific — reference actual lines from their code and the problem requirements.

Return JSON only (no markdown, no code fences):
{"verdict":"likely_correct","confidence":0.95,"explanation":"step-by-step analysis...","suggestedFix":"concise fix..."}

verdict must be one of: likely_correct, likely_incorrect, unclear
confidence must be a number between 0 and 1
explanation: start by restating the problem, then analyze the student's code step by step, comparing against expected behavior. Be thorough.
suggestedFix: if incorrect, give the correct code or specific changes needed.`;

    const ai = new GoogleGenAI({ apiKey });
    const timeout = new Promise<never>((_, reject) =>
        setTimeout(() => reject(new Error('Gemini review timed out after 15 seconds.')), REVIEW_TIMEOUT_MS)
    );
    const request_promise = ai.models.generateContent({
        model: 'gemini-2.0-flash',
        contents: prompt,
        config: { temperature: 0.2, maxOutputTokens: 800 },
    });

    try {
        const res = await Promise.race([request_promise, timeout]) as any;
        const text = res.text || '';
        try {
            const parsed = JSON.parse(text.replace(/```json|```/g, '').trim());
            const verdict = parsed.verdict === 'likely_correct' || parsed.verdict === 'likely_incorrect' || parsed.verdict === 'unclear'
                ? parsed.verdict : 'unclear';
            const confidence = Number.isFinite(Number(parsed.confidence))
                ? Math.max(0, Math.min(1, Number(parsed.confidence))) : 0.5;
            return {
                verdict,
                confidence,
                explanation: String(parsed.explanation || 'No explanation returned.'),
                suggestedFix: parsed.suggestedFix ? String(parsed.suggestedFix) : undefined,
                source: 'gemini',
            };
        } catch {
            return {
                verdict: 'unclear',
                confidence: 0.4,
                explanation: text.slice(0, 1500) || 'Gemini returned an unreadable response.',
                source: 'gemini',
            };
        }
    } catch (e: any) {
        return {
            verdict: 'unclear',
            confidence: 0,
            explanation: `Gemini review failed: ${e?.message || 'Unknown error'}`,
            source: 'gemini',
        };
    }
};
