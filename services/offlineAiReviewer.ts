import { AiReviewRequest, AiReviewResult, OfflineAiState } from '../aiReviewTypes';
import { buildDiagnosticReview } from './aiReviewDiagnostics';
import { loadWebLlmReviewer, resetWebLlmReviewer, reviewWithWebLlm, supportsWebLlm } from './webLlmReviewer';

const STORAGE_KEY = 'python_offline_ai_state';

const formatOfflineAiError = (error: unknown) => {
    const message = String((error as { message?: unknown })?.message || error || 'Offline AI setup failed.');
    if (/importing a module script failed|failed to fetch dynamically imported module|error loading dynamically imported module|load failed/i.test(message)) {
        return 'Offline AI runtime could not load in this browser/app. Built-in AI review still works; refresh after the update or try a browser with WebGPU support.';
    }
    if (/webgpu|gpu/i.test(message)) {
        return 'This browser does not expose WebGPU for offline AI. Built-in AI review will still work.';
    }
    return message;
};

export const DEFAULT_OFFLINE_AI_STATE: OfflineAiState = {
    enabled: false,
    status: 'not_installed',
    modelId: 'Llama-3.2-1B-Instruct-q4f16_1-MLC',
    message: 'Offline AI reviewer is not installed.',
    progress: 0,
};

export const loadOfflineAiState = (): OfflineAiState => {
    try {
        const parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
        const persisted = { ...DEFAULT_OFFLINE_AI_STATE, ...parsed };

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
        const next = { ...state, enabled: false, status: 'unsupported' as const, message: 'This browser does not expose WebGPU for offline AI.', progress: 0 };
        onState(next);
        saveOfflineAiState(next);
        return next;
    }
    const downloading = { ...state, enabled: true, status: 'downloading' as const, message: 'Downloading offline AI model...', progress: 0 };
    onState(downloading);
    try {
        await loadWebLlmReviewer(state.modelId, (progress, message) => {
            onState({ ...downloading, status: 'downloading', progress, message });
        });
        const ready = { ...state, enabled: true, status: 'ready' as const, message: 'Offline AI reviewer is ready.', progress: 1 };
        onState(ready);
        saveOfflineAiState(ready);
        return ready;
    } catch (error) {
        const failed = {
            ...state,
            enabled: false,
            status: 'failed' as const,
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
                explanation: `Offline AI is marked ready, but this browser does not expose WebGPU. Diagnostic review was used instead. ${diagnostic.explanation}`,
            };
        }
        try {
            return await reviewWithWebLlm(request, state.modelId);
        } catch (error) {
            const diagnostic = buildDiagnosticReview(request);
            return {
                ...diagnostic,
                explanation: `Offline AI failed, so diagnostic review was used. ${diagnostic.explanation}`,
            };
        }
    }
    return buildDiagnosticReview(request);
};
