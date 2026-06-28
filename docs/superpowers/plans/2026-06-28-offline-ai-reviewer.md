# Offline AI Reviewer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an optional in-app offline AI reviewer that can analyze failed grader results and suggest likely-correct unconventional answers without replacing deterministic grading.

**Architecture:** Keep Pyodide graders as the automatic scoring authority, add a separate AI review interface, then connect the Hide Tools `AI` button to a review modal. The first implementation provides deterministic diagnostics and an offline-reviewer state shell; the model runtime is isolated behind an adapter so WebLLM can be downloaded, cached, enabled, disabled, or removed without touching grader logic.

**Tech Stack:** React 18, TypeScript, Vite, Pyodide, existing `AUTO_GRADERS`, optional `@mlc-ai/web-llm` runtime loaded only through the AI reviewer adapter.

---

## File Structure

- Create `aiReviewTypes.ts`: shared AI review request/result/status types.
- Create `services/aiReviewDiagnostics.ts`: deterministic fallback reviewer that summarizes grader failures and obvious code issues.
- Create `services/offlineAiReviewer.ts`: storage/status manager and public review API used by `App.tsx`.
- Create `services/webLlmReviewer.ts`: WebLLM adapter with capability checks, model download, review, and unload methods.
- Modify `App.tsx`: store the latest grader result, route the Hide Tools `AI` button to the new AI Review panel, add settings controls, and preserve Gemini/API-key behavior as fallback.
- Modify `package.json`: add `@mlc-ai/web-llm` only when the WebLLM adapter task is implemented.
- Modify `index.html` and `public/sw.js`: bump app/cache version for every shipped code change.
- Modify `scripts/validate_graders.js` only if the new diagnostic state requires a script-level smoke check; otherwise keep grader scripts unchanged.

## Task 1: Add AI Review Types And Deterministic Diagnostic Service

**Files:**
- Create: `aiReviewTypes.ts`
- Create: `services/aiReviewDiagnostics.ts`
- Modify: `index.html`
- Modify: `public/sw.js`

- [ ] **Step 1: Create shared types**

Create `aiReviewTypes.ts`:

```ts
export type AiReviewVerdict = 'likely_correct' | 'likely_incorrect' | 'unclear';

export type OfflineAiStatus =
    | 'not_installed'
    | 'unsupported'
    | 'downloading'
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
```

- [ ] **Step 2: Create deterministic diagnostic reviewer**

Create `services/aiReviewDiagnostics.ts`:

```ts
import { AiReviewRequest, AiReviewResult } from '../aiReviewTypes';

const hasFunctionDefinition = (code: string) => /\bdef\s+[A-Za-z_][A-Za-z0-9_]*\s*\(/.test(code);
const hasReturn = (code: string) => /\breturn\b/.test(code);
const hasPrint = (code: string) => /\bprint\s*\(/.test(code);
const hasInput = (code: string) => /\binput\s*\(/.test(code);

export const buildDiagnosticReview = (request: AiReviewRequest): AiReviewResult => {
    const code = request.userCode || '';
    const graderMessage = request.graderMessage || '';
    const notes: string[] = [];
    let confidence = 0.35;
    let verdict: AiReviewResult['verdict'] = 'unclear';

    if (request.graderPassed) {
        return {
            verdict: 'likely_correct',
            confidence: 0.99,
            explanation: 'The deterministic grader already passed this solution.',
            source: 'diagnostic',
        };
    }

    if (/Missing required source pattern|Missing required syntax/i.test(graderMessage)) {
        verdict = 'likely_incorrect';
        confidence = 0.82;
        notes.push('The grader failed because the problem requires specific syntax or a specific API call.');
    }

    if (/Could not find a callable|function/i.test(graderMessage) && !hasFunctionDefinition(code)) {
        verdict = 'likely_incorrect';
        confidence = Math.max(confidence, 0.8);
        notes.push('The answer does not define a function, but this problem appears to require one.');
    }

    if (/Expected .* got/i.test(graderMessage)) {
        verdict = verdict === 'likely_incorrect' ? verdict : 'unclear';
        confidence = Math.max(confidence, 0.55);
        notes.push('The code ran, but at least one hidden test produced a different result.');
    }

    if (hasPrint(code) && !hasReturn(code) && /Expected .* got/i.test(graderMessage)) {
        notes.push('The code prints output but may need to return a value from the required function.');
    }

    if (hasInput(code)) {
        notes.push('The code uses input(); the grader can test this only when the problem is configured as a script/input problem.');
    }

    if (!notes.length) {
        notes.push('The deterministic grader failed, but the diagnostic reviewer could not identify a single obvious cause.');
    }

    return {
        verdict,
        confidence,
        explanation: notes.join(' '),
        suggestedFix: 'Compare the required function name, return value, and edge cases against the problem statement.',
        source: 'diagnostic',
    };
};
```

- [ ] **Step 3: Bump cache version**

In `index.html`, change both `v196` strings to `v197`.

In `public/sw.js`, change `CACHE_VERSION = "v196"` to `CACHE_VERSION = "v197"`.

- [ ] **Step 4: Build**

Run:

```bash
npm run build
git restore dist
```

Expected: Vite build succeeds. The existing large chunk warning is acceptable.

- [ ] **Step 5: Commit**

```bash
git add aiReviewTypes.ts services/aiReviewDiagnostics.ts index.html public/sw.js
git commit -m "Add AI review diagnostic types"
git push origin HEAD:main
```

## Task 2: Capture Structured Grader Result In App State

**Files:**
- Modify: `App.tsx`
- Modify: `index.html`
- Modify: `public/sw.js`

- [ ] **Step 1: Import AI review types**

At the top of `App.tsx`, add:

```ts
import { AiReviewRequest, AiReviewResult } from './aiReviewTypes';
import { buildDiagnosticReview } from './services/aiReviewDiagnostics';
```

- [ ] **Step 2: Add latest grader state**

Near the other `useState` declarations, add:

```ts
const [latestAiReviewRequest, setLatestAiReviewRequest] = useState<AiReviewRequest | null>(null);
const [latestAiReviewResult, setLatestAiReviewResult] = useState<AiReviewResult | null>(null);
const [aiReviewRunning, setAiReviewRunning] = useState(false);
```

- [ ] **Step 3: Store request after grader pass/fail**

Inside `runCode()`, after `gradeResult` is parsed and before setting output status, build this request:

```ts
const reviewRequest: AiReviewRequest = {
    problemId: exercise.id,
    title: exercise.title,
    description: exercise.description,
    userCode: activeFile.content,
    graderMessage: gradeResult.message,
    graderPassed: gradeResult.passed,
    programOutput: stdout || '',
    visibleSolution: exercise.solution,
};
setLatestAiReviewRequest(reviewRequest);
setLatestAiReviewResult(null);
```

In the `catch` block where `autoGrader` failure is handled, build this request before `setOutput(...)`:

```ts
const reviewRequest: AiReviewRequest = {
    problemId: exercise.id,
    title: exercise.title,
    description: exercise.description,
    userCode: files[activeFileIndex].content,
    graderMessage: errorMessage,
    graderPassed: false,
    programOutput: stdout || '',
    visibleSolution: exercise.solution,
};
setLatestAiReviewRequest(reviewRequest);
setLatestAiReviewResult(null);
```

- [ ] **Step 4: Clear stale review state when problem or code changes**

In `loadExerciseById()` and `loadRandomExercise()`, after problem/files are changed, add:

```ts
setLatestAiReviewRequest(null);
setLatestAiReviewResult(null);
```

In `updateActiveContent()`, after `if (pendingNextProblem) setPendingNextProblem(false);`, add:

```ts
setLatestAiReviewResult(null);
```

- [ ] **Step 5: Add local review runner**

Replace the current `handleAiHint` body with:

```ts
const handleAiHint = async () => {
    const request: AiReviewRequest = latestAiReviewRequest || {
        problemId: exercise.id,
        title: exercise.title,
        description: exercise.description,
        userCode: files[activeFileIndex].content,
        graderMessage: 'Run has not been pressed for this code yet.',
        graderPassed: false,
        programOutput: output,
        visibleSolution: exercise.solution,
    };

    setShowModal('hint');
    setAiReviewRunning(true);
    setAiHintText('Reviewing code...');
    try {
        const diagnostic = buildDiagnosticReview(request);
        setLatestAiReviewResult(diagnostic);
        setAiHintText(`${diagnostic.verdict.replace('_', ' ').toUpperCase()}\n\n${diagnostic.explanation}${diagnostic.suggestedFix ? `\n\nSuggested fix: ${diagnostic.suggestedFix}` : ''}`);
    } finally {
        setAiReviewRunning(false);
    }
};
```

This step intentionally does not call Gemini. Gemini fallback is restored in Task 4 after the AI review modal has a clear source priority.

- [ ] **Step 6: Bump cache version**

Change `v197` to `v198` in `index.html` and `public/sw.js`.

- [ ] **Step 7: Validate**

Run:

```bash
npm run build
git restore dist
```

Expected: build succeeds.

- [ ] **Step 8: Commit**

```bash
git add App.tsx index.html public/sw.js
git commit -m "Connect AI button to diagnostic review"
git push origin HEAD:main
```

## Task 3: Improve AI Review Modal UI

**Files:**
- Modify: `App.tsx`
- Modify: `index.html`
- Modify: `public/sw.js`

- [ ] **Step 1: Replace hint modal content**

Find the modal branch for `showModal === 'hint'`. Replace the simple AI hint body with a structured panel:

```tsx
{showModal === 'hint' && (
    <div className="flex h-full min-h-0 flex-col">
        <h2 className="mb-3 text-lg font-bold text-[#3b82f6]">AI Review</h2>
        <div className="min-h-0 flex-1 overflow-y-auto rounded-2xl border border-[#1d2d44] bg-[#071225]/90 p-4 text-sm text-gray-200">
            {aiReviewRunning ? (
                <p className="text-[#93c5fd]">Reviewing code...</p>
            ) : latestAiReviewResult ? (
                <div className="space-y-3">
                    <div className="flex flex-wrap items-center gap-2">
                        <span className="rounded-full border border-[#3b82f6]/40 bg-[#3b82f6]/15 px-3 py-1 text-[11px] font-black uppercase tracking-[0.12em] text-[#93c5fd]">
                            {latestAiReviewResult.verdict.replace('_', ' ')}
                        </span>
                        <span className="text-xs text-gray-400">
                            Confidence {Math.round(latestAiReviewResult.confidence * 100)}% · {latestAiReviewResult.source}
                        </span>
                    </div>
                    <p className="whitespace-pre-wrap leading-relaxed">{latestAiReviewResult.explanation}</p>
                    {latestAiReviewResult.suggestedFix && (
                        <p className="rounded-xl border border-[#f59e0b]/30 bg-[#f59e0b]/10 p-3 text-[#fde68a]">
                            {latestAiReviewResult.suggestedFix}
                        </p>
                    )}
                    {latestAiReviewResult.verdict === 'likely_correct' && !latestAiReviewRequest?.graderPassed && (
                        <p className="rounded-xl border border-[#22c55e]/35 bg-[#22c55e]/10 p-3 text-[#86efac]">
                            AI Suggested Win: review this answer and use the manual Win button if you agree.
                        </p>
                    )}
                </div>
            ) : (
                <p className="whitespace-pre-wrap">{aiHintText || 'Press Run first for the strongest review, or press AI again to analyze the current code.'}</p>
            )}
        </div>
        {latestAiReviewRequest?.graderMessage && (
            <div className="mt-3 rounded-2xl border border-[#ef4444]/30 bg-[#ef4444]/10 p-3 text-xs text-[#fecaca]">
                <div className="mb-1 font-black uppercase tracking-[0.12em]">Grader Message</div>
                <div className="whitespace-pre-wrap">{latestAiReviewRequest.graderMessage}</div>
            </div>
        )}
    </div>
)}
```

- [ ] **Step 2: Keep manual scoring visible**

Do not remove `handleMarkSuccess`, `handleMarkFailed`, `Win`, or `Failed`. Confirm the Hide Tools row still contains both actions.

- [ ] **Step 3: Bump cache version**

Change `v198` to `v199` in `index.html` and `public/sw.js`.

- [ ] **Step 4: Validate**

Run:

```bash
npm run build
git restore dist
```

Expected: build succeeds.

- [ ] **Step 5: Commit**

```bash
git add App.tsx index.html public/sw.js
git commit -m "Add structured AI review modal"
git push origin HEAD:main
```

## Task 4: Add Offline AI Settings State And Gemini Fallback Priority

**Files:**
- Create: `services/offlineAiReviewer.ts`
- Modify: `App.tsx`
- Modify: `index.html`
- Modify: `public/sw.js`

- [ ] **Step 1: Create offline AI state manager**

Create `services/offlineAiReviewer.ts`:

```ts
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
```

This manager deliberately returns diagnostics until the WebLLM adapter is added in Task 5.

- [ ] **Step 2: Add state imports**

In `App.tsx`, add:

```ts
import { DEFAULT_OFFLINE_AI_STATE, loadOfflineAiState, reviewWithAvailableAi, saveOfflineAiState } from './services/offlineAiReviewer';
```

- [ ] **Step 3: Add offline AI state**

Near other settings state, add:

```ts
const [offlineAiState, setOfflineAiState] = useState(() => loadOfflineAiState());
```

Add a persistence effect:

```ts
useEffect(() => {
    saveOfflineAiState(offlineAiState);
}, [offlineAiState]);
```

- [ ] **Step 4: Update AI review runner to use manager**

In `handleAiHint`, replace `buildDiagnosticReview(request)` with:

```ts
const review = await reviewWithAvailableAi(request, offlineAiState);
setLatestAiReviewResult(review);
setAiHintText(`${review.verdict.replace('_', ' ').toUpperCase()}\n\n${review.explanation}${review.suggestedFix ? `\n\nSuggested fix: ${review.suggestedFix}` : ''}`);
```

- [ ] **Step 5: Add settings controls**

In the settings modal, below stats-by-mode and above reset controls, add:

```tsx
<div className="rounded-2xl border border-[#1d2d44] bg-[#071225]/80 p-4">
    <div className="mb-3 flex items-center justify-between gap-3">
        <div>
            <h3 className="text-sm font-black uppercase tracking-[0.14em] text-[#93c5fd]">Offline AI Reviewer</h3>
            <p className="mt-1 text-xs text-gray-400">{offlineAiState.message}</p>
        </div>
        <button
            onClick={() => setOfflineAiState(prev => ({
                ...prev,
                enabled: !prev.enabled,
                message: !prev.enabled ? 'Offline AI reviewer enabled. Model is not installed yet.' : 'Offline AI reviewer disabled.',
            }))}
            className={`rounded-xl px-3 py-2 text-xs font-black uppercase tracking-[0.12em] ${offlineAiState.enabled ? 'bg-[#22c55e]/20 text-[#86efac]' : 'bg-[#334155] text-gray-300'}`}
        >
            {offlineAiState.enabled ? 'On' : 'Off'}
        </button>
    </div>
    <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
        <button
            onClick={() => setOfflineAiState(prev => ({
                ...prev,
                enabled: true,
                status: 'not_installed',
                message: 'Model download will be available after the offline runtime is installed.',
                progress: 0,
            }))}
            className="rounded-xl border border-[#3b82f6]/35 bg-[#3b82f6]/10 px-3 py-2 text-xs font-black uppercase tracking-[0.12em] text-[#93c5fd]"
        >
            Prepare Download
        </button>
        <button
            onClick={() => setOfflineAiState(DEFAULT_OFFLINE_AI_STATE)}
            className="rounded-xl border border-[#ef4444]/35 bg-[#ef4444]/10 px-3 py-2 text-xs font-black uppercase tracking-[0.12em] text-[#fecaca]"
        >
            Remove Offline AI
        </button>
    </div>
    <div className="mt-3 text-xs text-gray-400">
        Status: {offlineAiState.status} · Model: {offlineAiState.modelId}
    </div>
</div>
```

- [ ] **Step 6: Bump cache version**

Change `v199` to `v200` in `index.html` and `public/sw.js`.

- [ ] **Step 7: Validate**

Run:

```bash
npm run build
git restore dist
```

Expected: build succeeds.

- [ ] **Step 8: Commit**

```bash
git add App.tsx services/offlineAiReviewer.ts index.html public/sw.js
git commit -m "Add offline AI reviewer settings shell"
git push origin HEAD:main
```

## Task 5: Add WebLLM Adapter Behind The Offline AI Service

**Files:**
- Modify: `package.json`
- Modify: `package-lock.json` if generated by npm
- Create: `services/webLlmReviewer.ts`
- Modify: `services/offlineAiReviewer.ts`
- Modify: `App.tsx`
- Modify: `index.html`
- Modify: `public/sw.js`

- [ ] **Step 1: Install WebLLM dependency**

Run:

```bash
npm install @mlc-ai/web-llm
```

Expected: `package.json` gains `@mlc-ai/web-llm`; `package-lock.json` is created or updated if npm writes it.

- [ ] **Step 2: Create WebLLM adapter**

Create `services/webLlmReviewer.ts`:

```ts
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
        enginePromise = import('@mlc-ai/web-llm').then(async (webllm: EngineModule) => {
            const engine = await webllm.CreateMLCEngine(modelId, {
                initProgressCallback: (report: any) => {
                    const progress = typeof report?.progress === 'number' ? report.progress : 0;
                    const text = String(report?.text || 'Downloading offline AI model...');
                    onProgress?.(progress, text);
                },
            });
            return engine;
        });
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

export const resetWebLlmReviewer = async () => {
    if (enginePromise) {
        const engine = await enginePromise.catch(() => null);
        if (engine?.unload) {
            await engine.unload();
        }
    }
    enginePromise = null;
};
```

- [ ] **Step 3: Wire WebLLM into offline service**

Modify `services/offlineAiReviewer.ts` imports:

```ts
import { loadWebLlmReviewer, resetWebLlmReviewer, reviewWithWebLlm, supportsWebLlm } from './webLlmReviewer';
```

Add:

```ts
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
    await loadWebLlmReviewer(state.modelId, (progress, message) => {
        onState({ ...downloading, status: 'downloading', progress, message });
    });
    const ready = { ...state, enabled: true, status: 'ready' as const, message: 'Offline AI reviewer is ready.', progress: 1 };
    onState(ready);
    saveOfflineAiState(ready);
    return ready;
};

export const removeOfflineAiModel = async () => {
    await resetWebLlmReviewer();
    saveOfflineAiState(DEFAULT_OFFLINE_AI_STATE);
    return DEFAULT_OFFLINE_AI_STATE;
};
```

Update `reviewWithAvailableAi`:

```ts
export const reviewWithAvailableAi = async (request: AiReviewRequest, state: OfflineAiState): Promise<AiReviewResult> => {
    if (state.enabled && state.status === 'ready') {
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
```

- [ ] **Step 4: Wire settings buttons to real download/remove**

In `App.tsx`, import:

```ts
import { DEFAULT_OFFLINE_AI_STATE, downloadOfflineAiModel, loadOfflineAiState, removeOfflineAiModel, reviewWithAvailableAi, saveOfflineAiState } from './services/offlineAiReviewer';
```

Replace the `Prepare Download` button handler with:

```tsx
onClick={() => {
    downloadOfflineAiModel(offlineAiState, setOfflineAiState).catch(error => {
        setOfflineAiState(prev => ({
            ...prev,
            status: 'failed',
            message: String(error?.message || error || 'Offline AI download failed.'),
            progress: 0,
        }));
    });
}}
```

Replace the `Remove Offline AI` handler with:

```tsx
onClick={() => {
    removeOfflineAiModel().then(setOfflineAiState).catch(() => setOfflineAiState(DEFAULT_OFFLINE_AI_STATE));
}}
```

- [ ] **Step 5: Bump cache version**

Change `v200` to `v201` in `index.html` and `public/sw.js`.

- [ ] **Step 6: Validate**

Run:

```bash
npm run build
git restore dist
npm run check:graders
```

Expected: build succeeds and grader checks pass.

- [ ] **Step 7: Commit**

```bash
git add package.json package-lock.json services/webLlmReviewer.ts services/offlineAiReviewer.ts App.tsx index.html public/sw.js
git commit -m "Add optional WebLLM offline reviewer"
git push origin HEAD:main
```

## Task 6: Final Verification On GitHub Pages Build

**Files:**
- Modify only files required by validation fixes.

- [ ] **Step 1: Verify clean status**

Run:

```bash
git status --short
```

Expected: no output.

- [ ] **Step 2: Verify latest cache version**

Run:

```bash
rg -n "v201|CACHE_VERSION" index.html public/sw.js
```

Expected: `index.html` has `v201` twice and `public/sw.js` has `CACHE_VERSION = "v201"`.

- [ ] **Step 3: Verify build and graders**

Run:

```bash
npm run build
git restore dist
npm run check:graders
```

Expected: build succeeds and grader checks pass.

- [ ] **Step 4: Push any validation fix**

If validation required a fix, commit it:

```bash
git add App.tsx aiReviewTypes.ts services index.html public/sw.js package.json package-lock.json
git commit -m "Stabilize offline AI reviewer"
git push origin HEAD:main
```

If no files changed, do not create an empty commit.

## Self-Review

- Spec coverage: deterministic grader remains authority in Tasks 1-4, AI review panel is implemented in Task 3, settings state is implemented in Task 4, optional in-app model download is implemented in Task 5, and final validation is Task 6.
- Placeholder scan: this plan contains no incomplete placeholder markers and each task includes exact files, code snippets, commands, and expected results.
- Type consistency: `AiReviewRequest`, `AiReviewResult`, `OfflineAiState`, and verdict/status strings are defined in Task 1 and reused consistently through Tasks 2-5.
