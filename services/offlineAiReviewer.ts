import { AiReviewRequest, AiReviewResult, OfflineAiState } from '../aiReviewTypes';
import { buildDiagnosticReview } from './aiReviewDiagnostics';

const STORAGE_KEY = 'python_offline_ai_state';

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
        return { ...DEFAULT_OFFLINE_AI_STATE, ...parsed };
    } catch {
        return DEFAULT_OFFLINE_AI_STATE;
    }
};

export const saveOfflineAiState = (state: OfflineAiState) => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
};

export const reviewWithAvailableAi = async (request: AiReviewRequest, state: OfflineAiState): Promise<AiReviewResult> => {
    if (!state.enabled || state.status !== 'ready') {
        return buildDiagnosticReview(request);
    }
    return buildDiagnosticReview(request);
};
