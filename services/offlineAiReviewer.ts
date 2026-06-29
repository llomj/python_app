import { AiReviewRequest, AiReviewResult, OfflineAiState } from '../aiReviewTypes';
import { buildDiagnosticReview } from './aiReviewDiagnostics';
import { loadWebLlmReviewer, resetWebLlmReviewer, reviewWithWebLlm, supportsWebLlm, testWebLlmReviewer } from './webLlmReviewer';
import { hasGeminiKey, reviewWithGemini } from './geminiService';

const STORAGE_KEY = 'python_offline_ai_state';
const DEFAULT_MODEL_ID = 'SmolLM2-135M-Instruct-q0f16-MLC';
const OFFLINE_AI_DOWNLOAD_TIMEOUT_MS = 180000;
const OFFLINE_AI_DOWNLOAD_STALL_TIMEOUT_MS = 60000;
const OFFLINE_AI_HEALTH_CHECK_TIMEOUT_MS = 30000;
const OFFLINE_AI_REVIEW_TIMEOUT_MS = 8000;
const LEGACY_MODEL_IDS = new Set([
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
                message: 'Offline AI was switched to the lightweight phone model. Press Prepare Download to install it.',
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
    const downloading = { ...state, enabled: false, status: 'downloading' as const, message: 'Preparing offline model. Built-in offline review still works while this downloads.', progress: 0, startedAt: Date.now() };
    onState(downloading);
    let acceptProgress = true;
    let latestProgress = 0;
    let latestMessage = downloading.message;
    try {
        await withActivityTimeout(
            loadWebLlmReviewer(state.modelId, (progress, message) => {
                latestProgress = progress;
                latestMessage = message;
                if (acceptProgress) {
                    onState({ ...downloading, status: 'downloading', progress, message });
                }
            }),
            () => `${Math.round(latestProgress * 1000)}:${latestMessage}`,
            OFFLINE_AI_DOWNLOAD_STALL_TIMEOUT_MS,
            OFFLINE_AI_DOWNLOAD_TIMEOUT_MS,
            'Offline model download made no visible progress for 60 seconds. Built-in offline review is active; try again on Wi-Fi.',
            'Offline model setup is taking too long. Built-in offline review is active; try Prepare Download again on Wi-Fi.',
        );
        if (acceptProgress) {
            onState({ ...downloading, status: 'downloading', progress: Math.max(downloading.progress, 0.96), message: 'Testing offline model response...' });
        }
        await withTimeout(
            testWebLlmReviewer(state.modelId),
            OFFLINE_AI_HEALTH_CHECK_TIMEOUT_MS,
            'Offline model loaded but did not answer the test prompt in time. Built-in offline review is active.',
        );
        acceptProgress = false;
        const ready = { ...state, enabled: true, status: 'ready' as const, message: 'Offline model installed and tested. Model review is on.', progress: 1, startedAt: undefined };
        onState(ready);
        saveOfflineAiState(ready);
        return ready;
    } catch (error) {
        acceptProgress = false;
        await resetWebLlmReviewer(state.modelId).catch(() => undefined);
        const failed = {
            ...state,
            enabled: false,
            status: isUnsupportedOfflineAiError(error) ? 'unsupported' as const : 'failed' as const,
            message: formatOfflineAiError(error),
            progress: 0,
            startedAt: undefined,
        };
        onState(failed);
        saveOfflineAiState(failed);
        return failed;
    }
};

export const removeOfflineAiModel = async (modelId = DEFAULT_OFFLINE_AI_STATE.modelId) => {
    await resetWebLlmReviewer(modelId);
    saveOfflineAiState(DEFAULT_OFFLINE_AI_STATE);
    return DEFAULT_OFFLINE_AI_STATE;
};

export const reviewWithAvailableAi = async (request: AiReviewRequest, state: OfflineAiState): Promise<AiReviewResult> => {
    const diagnostic = buildDiagnosticReview(request);

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
            if (offlineResult.verdict !== 'unclear' && offlineResult.explanation.length > 20) {
                return {
                    ...diagnostic,
                    confidence: Math.max(diagnostic.confidence, offlineResult.confidence),
                    explanation: `${offlineResult.explanation}\n\n---\nBuilt-in analysis: ${diagnostic.explanation}`,
                    suggestedFix: offlineResult.suggestedFix || diagnostic.suggestedFix,
                    source: diagnostic.source,
                };
            }
            return diagnostic;
        } catch {
            return diagnostic;
        }
    }
    return diagnostic;
};
