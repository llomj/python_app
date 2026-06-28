export type AiReviewVerdict = 'likely_correct' | 'likely_incorrect' | 'unclear';

export type OfflineAiStatus =
    | 'not_installed'
    | 'unsupported'
    | 'downloading'
    | 'removing'
    | 'ready'
    | 'failed'
    | 'disabled';

export interface AiReviewRequest {
    problemId: number;
    title: string;
    description: string;
    userCode: string;
    graderMessage: string;
    graderPassed: boolean;
    programOutput?: string;
    visibleSolution?: string;
}

export interface AiReviewResult {
    verdict: AiReviewVerdict;
    confidence: number;
    explanation: string;
    suggestedFix?: string;
    source: 'diagnostic' | 'offline_model' | 'gemini';
}

export interface OfflineAiState {
    enabled: boolean;
    status: OfflineAiStatus;
    modelId: string;
    message: string;
    progress: number;
}
