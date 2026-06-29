import { AiReviewRequest, AiReviewResult, OfflineAiState } from '../aiReviewTypes';
import { buildDiagnosticReview } from './aiReviewDiagnostics';
import { loadWebLlmReviewer, resetWebLlmReviewer, reviewWithWebLlm, supportsWebLlm } from './webLlmReviewer';

const STORAGE_KEY = 'python_offline_ai_state';
const DEFAULT_MODEL_ID = 'SmolLM2-135M-Instruct-q0f16-MLC';
const OFFLINE_AI_DOWNLOAD_TIMEOUT_MS = 90000;
const OFFLINE_AI_REVIEW_TIMEOUT_MS = 20000;
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

const formatOfflineAiError = (error: unknown) => {
    const message = String((error as { message?: unknown })?.message || error || 'Offline AI setup failed.');
    if (/importing a module script failed|failed to fetch dynamically imported module|error loading dynamically imported module|load failed/i.test(message)) {
        return 'Offline model is unavailable in this browser/app. Built-in offline review is active.';
    }
    if (/webgpu|gpu/i.test(message)) {
        return 'This browser does not expose WebGPU for the offline model. Built-in offline review is active.';
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
                enabled: true,
                status: 'failed',
                message: 'Previous offline AI download was interrupted. Start the download again to finish setup.',
                progress: 0,
            };
        }

        if (persisted.status === 'removing') {
            return {
                ...persisted,
                enabled: false,
                status: 'failed',
                message: 'Previous offline AI removal was interrupted. Retry removal or download the model again.',
                progress: 0,
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
        const next = { ...state, enabled: false, status: 'unsupported' as const, message: 'This browser does not expose WebGPU for the offline model. Built-in offline review is active.', progress: 0 };
        onState(next);
        saveOfflineAiState(next);
        return next;
    }
    const downloading = { ...state, enabled: true, status: 'downloading' as const, message: 'Preparing offline model. Built-in offline review still works while this downloads.', progress: 0 };
    onState(downloading);
    let acceptProgress = true;
    try {
        await withTimeout(
            loadWebLlmReviewer(state.modelId, (progress, message) => {
                if (acceptProgress) {
                    onState({ ...downloading, status: 'downloading', progress, message });
                }
            }),
            OFFLINE_AI_DOWNLOAD_TIMEOUT_MS,
            'Offline model setup is taking too long. Built-in offline review is active; try Prepare Download again on Wi-Fi.',
        );
        acceptProgress = false;
        const ready = { ...state, enabled: true, status: 'ready' as const, message: 'Offline AI reviewer is ready.', progress: 1 };
        onState(ready);
        saveOfflineAiState(ready);
        return ready;
    } catch (error) {
        acceptProgress = false;
        const failed = {
            ...state,
            enabled: false,
            status: isUnsupportedOfflineAiError(error) ? 'unsupported' as const : 'failed' as const,
            message: formatOfflineAiError(error),
            progress: 0,
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
    if (state.enabled && state.status === 'ready') {
        if (!supportsWebLlm()) {
            const diagnostic = buildDiagnosticReview(request);
            return {
                ...diagnostic,
                explanation: `Offline model is marked ready, but this browser does not expose WebGPU. Built-in offline review was used instead. ${diagnostic.explanation}`,
            };
        }
        try {
            return await withTimeout(
                reviewWithWebLlm(request, state.modelId),
                OFFLINE_AI_REVIEW_TIMEOUT_MS,
                'Offline AI review timed out.',
            );
        } catch (error) {
            const diagnostic = buildDiagnosticReview(request);
            return {
                ...diagnostic,
                explanation: `Offline model did not complete in time, so built-in offline review checked this code instead. ${diagnostic.explanation}`,
            };
        }
    }
    return buildDiagnosticReview(request);
};
