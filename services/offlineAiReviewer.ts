import { AiReviewRequest, AiReviewResult, OfflineAiState } from '../aiReviewTypes';
import { buildDiagnosticReview } from './aiReviewDiagnostics';
import { loadWebLlmReviewer, resetWebLlmReviewer, reviewWithWebLlm, supportsWebLlm, testWebLlmReviewer, verifyWebLlmSupport } from './webLlmReviewer';
import { hasGeminiKey, reviewWithGemini } from './geminiService';
import { isOllamaRunning, findAvailableCodeModel, reviewWithOllama } from './ollamaService';

const STORAGE_KEY = 'python_offline_ai_state';
const DEFAULT_MODEL_ID = 'Qwen2.5-Coder-0.5B-Instruct-q4f16_1-MLC';
const FALLBACK_MODEL_IDS = [
    'Qwen2.5-0.5B-Instruct-q4f16_1-MLC',
    'SmolLM2-360M-Instruct-q4f16_1-MLC',
];
const OFFLINE_AI_DOWNLOAD_TIMEOUT_MS = 180000;
const OFFLINE_AI_DOWNLOAD_STALL_TIMEOUT_MS = 30000;
const OFFLINE_AI_HEALTH_CHECK_TIMEOUT_MS = 30000;
const OFFLINE_AI_REVIEW_TIMEOUT_MS = 45000;
const LEGACY_MODEL_IDS = new Set([
    'SmolLM2-135M-Instruct-q0f16-MLC',
    'SmolLM2-135M-Instruct-q0f32-MLC',
    'SmolLM2-360M-Instruct-q0f16-MLC',
    'SmolLM2-360M-Instruct-q0f32-MLC',
    'SmolLM2-360M-Instruct-q4f32_1-MLC',
    'Llama-3.2-1B-Instruct-q4f16_1-MLC',
    'Llama-3.2-1B-Instruct-q4f32_1-MLC',
]);

const withTimeout = async <T,>(promise: Promise<T>, timeoutMs: number, message: string): Promise<T> => {
    let timeoutId: ReturnType<typeof setTimeout> | undefined;
    const timeout = new Promise<never>((_, reject) => {
        timeoutId = setTimeout(() => reject(new Error(message)), timeoutMs);
    });
    try {
        return await Promise.race([promise, timeout]);
    } finally {
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
    }
};

const withActivityTimeout = async <T,>(
    promise: Promise<T>,
    getActivityKey: () => string,
    stallTimeoutMs: number,
    totalTimeoutMs: number,
    stallMessage: string,
    totalMessage: string,
): Promise<T> => {
    let monitorId: ReturnType<typeof setInterval> | undefined;
    let totalId: ReturnType<typeof setTimeout> | undefined;
    let lastActivityKey = getActivityKey();
    let lastActivityAt = Date.now();

    const timeout = new Promise<never>((_, reject) => {
        monitorId = setInterval(() => {
            const nextActivityKey = getActivityKey();
            if (nextActivityKey !== lastActivityKey) {
                lastActivityKey = nextActivityKey;
                lastActivityAt = Date.now();
            }
            if (Date.now() - lastActivityAt >= stallTimeoutMs) {
                reject(new Error(stallMessage));
            }
        }, 1000);
        totalId = setTimeout(() => reject(new Error(totalMessage)), totalTimeoutMs);
    });

    try {
        return await Promise.race([promise, timeout]);
    } finally {
        if (monitorId) clearInterval(monitorId);
        if (totalId) clearTimeout(totalId);
    }
};

const formatOfflineAiError = (error: unknown) => {
    const message = String((error as { message?: unknown })?.message || error || 'Offline AI setup failed.');
    if (/importing a module script failed|failed to fetch dynamically imported module|error loading dynamically imported module|load failed/i.test(message)) {
        return 'Offline model is unavailable in this browser/app. Built-in offline review is active.';
    }
    if (/webgpu|gpu/i.test(message)) {
        return 'This browser does not expose WebGPU for the offline model. Built-in offline review is active.';
    }
    if (/progress|taking too long|did not answer/i.test(message)) {
        return message;
    }
    return message;
};

const isUnsupportedOfflineAiError = (error: unknown) => {
    const message = String((error as { message?: unknown })?.message || error || '');
    return /importing a module script failed|failed to fetch dynamically imported module|error loading dynamically imported module|load failed|webgpu|gpu/i.test(message);
};

const getInstallCandidateModelIds = (state: OfflineAiState) => {
    const modelIds = [
        LEGACY_MODEL_IDS.has(String(state.modelId)) ? DEFAULT_MODEL_ID : state.modelId,
        DEFAULT_MODEL_ID,
        ...FALLBACK_MODEL_IDS,
    ];
    return Array.from(new Set(modelIds.filter(Boolean)));
};

const getModelLabel = (modelId: string) => {
    if (modelId === DEFAULT_MODEL_ID) return 'coding model';
    if (modelId.includes('Qwen2.5-0.5B')) return 'compatible Qwen model';
    if (modelId.includes('SmolLM2-360M')) return 'fast fallback model';
    return 'offline model';
};

const extractReviewSignals = (request: AiReviewRequest) => {
    const signals = new Set<string>();
    const addWords = (text: string, minLength = 4) => {
        for (const word of text.match(/\b[A-Za-z_][A-Za-z0-9_]*\b/g) || []) {
            if (word.length >= minLength && !/^(this|that|with|from|your|code|problem|python|return|value|output|expected|actual|line|function|student)$/i.test(word)) {
                signals.add(word.toLowerCase());
            }
        }
    };

    addWords(request.title || '');
    addWords(request.description || '');
    addWords(request.graderMessage || '');
    addWords(request.programOutput || '', 2);
    for (const match of request.userCode.matchAll(/\b(?:def\s+([A-Za-z_][A-Za-z0-9_]*)|([A-Za-z_][A-Za-z0-9_]*)\s*=|([A-Za-z_][A-Za-z0-9_]*)\s*\()/g)) {
        const value = match[1] || match[2] || match[3];
        if (value && !/^(if|for|while|print|return|input|range|len|str|int|float|list|dict|set)$/i.test(value)) {
            signals.add(value.toLowerCase());
        }
    }
    return Array.from(signals).slice(0, 30);
};

const isSpecificModelReview = (review: AiReviewResult, request: AiReviewRequest) => {
    const explanation = `${review.explanation || ''}\n${review.suggestedFix || ''}`.toLowerCase();
    if (review.verdict === 'unclear' || explanation.length < 120) return false;
    if (/generic answer|cannot determine|not enough information|unable to/i.test(explanation)) return false;

    const signals = extractReviewSignals(request);
    const signalHits = signals.filter(signal => explanation.includes(signal)).length;
    const hasLineReference = /\bline\s+\d+\b/.test(explanation);
    const hasGraderReference = /(grader|expected|got|passed|failed|output|return|none|missing)/i.test(explanation);
    return signalHits >= 2 && (hasLineReference || hasGraderReference);
};

export const DEFAULT_OFFLINE_AI_STATE: OfflineAiState = {
    enabled: false,
    status: 'not_installed',
    modelId: DEFAULT_MODEL_ID,
    message: 'Offline AI reviewer is not installed.',
    progress: 0,
    startedAt: undefined,
};

export const loadOfflineAiState = (): OfflineAiState => {
    try {
        const parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
        const persisted = { ...DEFAULT_OFFLINE_AI_STATE, ...parsed };

        if (LEGACY_MODEL_IDS.has(String(persisted.modelId))) {
            return {
                ...DEFAULT_OFFLINE_AI_STATE,
                message: 'Offline AI was switched to the coding model. Press Prepare Download to install it.',
            };
        }

        if (persisted.status === 'downloading') {
            return {
                ...persisted,
                enabled: false,
                status: 'failed',
                message: 'Previous offline AI download was interrupted. Start the download again to finish setup.',
                progress: 0,
                startedAt: undefined,
            };
        }

        if (persisted.status === 'removing') {
            return {
                ...persisted,
                enabled: false,
                status: 'failed',
                message: 'Previous offline AI removal was interrupted. Retry removal or download the model again.',
                progress: 0,
                startedAt: undefined,
            };
        }

        if (persisted.status !== 'ready' && persisted.enabled) {
            return {
                ...persisted,
                enabled: false,
            };
        }

        return persisted;
    } catch {
        return DEFAULT_OFFLINE_AI_STATE;
    }
};

export const saveOfflineAiState = (state: OfflineAiState) => {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch {
        // Ignore storage failures; offline AI can still use in-memory state.
    }
};

export const downloadOfflineAiModel = async (
    state: OfflineAiState,
    onState: (next: OfflineAiState) => void,
) => {
    if (!supportsWebLlm()) {
        const next = { ...state, enabled: false, status: 'unsupported' as const, message: 'This browser does not expose WebGPU for the offline model. Built-in offline review is active.', progress: 0, startedAt: undefined };
        onState(next);
        saveOfflineAiState(next);
        return next;
    }
    try {
        await verifyWebLlmSupport();
    } catch (error) {
        const next = { ...state, enabled: false, status: 'unsupported' as const, message: formatOfflineAiError(error), progress: 0, startedAt: undefined };
        onState(next);
        saveOfflineAiState(next);
        return next;
    }

    const candidates = getInstallCandidateModelIds(state);
    let lastError: unknown;
    let lastModelId = candidates[0] || DEFAULT_MODEL_ID;

    const startedAt = Date.now();

    for (let index = 0; index < candidates.length; index += 1) {
        const modelId = candidates[index];
        lastModelId = modelId;
        const modelLabel = getModelLabel(modelId);
        const downloading = {
            ...state,
            modelId,
            enabled: false,
            status: 'downloading' as const,
            message: `Preparing ${modelLabel}${index > 0 ? ' after the previous model failed' : ''}. Built-in offline review still works while this downloads.`,
            progress: 0,
            startedAt,
        };
        onState(downloading);
        saveOfflineAiState(downloading);

        let acceptProgress = true;
        let latestProgress = 0;
        let latestMessage = downloading.message;

        try {
            await withActivityTimeout(
                loadWebLlmReviewer(modelId, (progress, message) => {
                    latestProgress = progress;
                    latestMessage = message;
                    if (acceptProgress) {
                        onState({
                            ...downloading,
                            status: 'downloading',
                            progress,
                            message: `${getModelLabel(modelId)}: ${message}`,
                        });
                    }
                }),
                () => `${modelId}:${Math.round(latestProgress * 1000)}:${latestMessage}`,
                OFFLINE_AI_DOWNLOAD_STALL_TIMEOUT_MS,
                OFFLINE_AI_DOWNLOAD_TIMEOUT_MS,
                `${modelLabel} made no visible progress for 30 seconds.`,
                `${modelLabel} setup is taking too long.`,
            );
            if (acceptProgress) {
                onState({ ...downloading, status: 'downloading', progress: Math.max(downloading.progress, 0.96), message: `Testing ${modelLabel} response...` });
            }
            await withTimeout(
                testWebLlmReviewer(modelId),
                OFFLINE_AI_HEALTH_CHECK_TIMEOUT_MS,
                `${modelLabel} loaded but did not answer the test prompt in time.`,
            );
            acceptProgress = false;
            const ready = { ...state, modelId, enabled: true, status: 'ready' as const, message: `${modelLabel} installed and tested. Model review is on.`, progress: 1, startedAt: undefined };
            onState(ready);
            saveOfflineAiState(ready);
            return ready;
        } catch (error) {
            acceptProgress = false;
            lastError = error;
            await resetWebLlmReviewer(modelId).catch(() => undefined);

            if (isUnsupportedOfflineAiError(error)) {
                break;
            }

            if (index < candidates.length - 1) {
                const nextModelId = candidates[index + 1];
                const fallingBack = {
                    ...state,
                    modelId: nextModelId,
                    enabled: false,
                    status: 'downloading' as const,
                    message: `${modelLabel} failed: ${formatOfflineAiError(error)} Trying ${getModelLabel(nextModelId)} now.`,
                    progress: 0,
                    startedAt,
                };
                onState(fallingBack);
                saveOfflineAiState(fallingBack);
                continue;
            }
        }
    }

    const failed = {
        ...state,
        modelId: lastModelId,
        enabled: false,
        status: isUnsupportedOfflineAiError(lastError) ? 'unsupported' as const : 'failed' as const,
        message: `${formatOfflineAiError(lastError)} Built-in offline review is still active.`,
        progress: 0,
        startedAt: undefined,
    };
    onState(failed);
    saveOfflineAiState(failed);
    return failed;
};

export const removeOfflineAiModel = async (modelId = DEFAULT_OFFLINE_AI_STATE.modelId) => {
    await resetWebLlmReviewer(modelId);
    saveOfflineAiState(DEFAULT_OFFLINE_AI_STATE);
    return DEFAULT_OFFLINE_AI_STATE;
};

export const reviewWithAvailableAi = async (request: AiReviewRequest, state: OfflineAiState): Promise<AiReviewResult> => {
    const diagnostic = buildDiagnosticReview(request);

    if (state.enabled && state.status === 'ready') {
        if (!supportsWebLlm()) {
            return {
                ...diagnostic,
                explanation: `Offline model is marked ready, but this browser does not expose WebGPU. Built-in offline review was used instead.\n\n${diagnostic.explanation}`,
            };
        }
        try {
            const offlineResult = await withTimeout(
                reviewWithWebLlm(request, state.modelId),
                OFFLINE_AI_REVIEW_TIMEOUT_MS,
                'Offline AI review timed out.',
            );
            if (isSpecificModelReview(offlineResult, request)) {
                return {
                    ...offlineResult,
                    confidence: Math.max(offlineResult.confidence, diagnostic.confidence),
                    explanation: `${offlineResult.explanation}\n\n---\nBuilt-in analysis: ${diagnostic.explanation}`,
                    suggestedFix: offlineResult.suggestedFix || diagnostic.suggestedFix,
                    source: 'offline_model',
                };
            }
            return {
                ...diagnostic,
                explanation: `The local model response was too generic for this problem, so it was rejected. Specific built-in analysis: ${diagnostic.explanation}`,
            };
        } catch {
            return diagnostic;
        }
    }

    const ollamaOnline = await isOllamaRunning();
    if (ollamaOnline) {
        const ollamaModel = await findAvailableCodeModel();
        if (ollamaModel) {
            try {
                const ollamaResult = await reviewWithOllama(request, ollamaModel);
                if (ollamaResult.verdict !== 'unclear' && ollamaResult.explanation.length > 20) {
                    return ollamaResult;
                }
            } catch {
                // Ollama failed, fall through
            }
        }
    }

    if (hasGeminiKey()) {
        try {
            const geminiResult = await reviewWithGemini(request);
            if (geminiResult.verdict !== 'unclear' || geminiResult.explanation.length > 20) {
                return {
                    ...geminiResult,
                    confidence: Math.max(geminiResult.confidence, diagnostic.confidence),
                };
            }
        } catch {
            // Gemini failed, fall through
        }
    }

    return diagnostic;
};
