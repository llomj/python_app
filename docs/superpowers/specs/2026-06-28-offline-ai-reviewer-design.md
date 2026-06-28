# Offline AI Reviewer Design

## Purpose

The AI task adds an optional in-app offline reviewer that helps evaluate unconventional Python solutions without replacing the deterministic grader. The feature must work inside the existing web app, not as a separate app. The app stays lightweight by default, and the model is downloaded only when the user enables offline AI.

## Goals

- Keep the deterministic Pyodide grader as the main source of automatic wins.
- Let users enable an optional background offline AI reviewer from settings.
- Use the AI reviewer when the grader fails or when the user presses the AI tool.
- Help detect potentially correct unconventional solutions and explain likely grader limitations.
- Preserve manual `Win` and `Failed` controls.
- Avoid requiring an API key or internet after the model is installed.

## Non-Goals

- Do not make a local model a separate application.
- Do not bundle a large model into the default app load.
- Do not let AI freely award points without deterministic support by default.
- Do not remove Gemini/API-key support unless a later task explicitly replaces it.

## User Flow

1. User opens settings and turns on `Offline AI Reviewer`.
2. App downloads the selected small reviewer model in the background.
3. App shows status: `Not installed`, `Downloading`, `Ready offline`, or `Failed`.
4. User writes code and presses `Run`.
5. Deterministic grader runs first.
6. If the grader passes, the app awards an automatic win.
7. If the grader fails, the user can press `AI`.
8. AI reviewer analyzes the problem, user code, grader tests, and grader failure.
9. AI returns one of: `Likely correct`, `Likely incorrect`, or `Unclear`, with a short explanation.
10. If AI says `Likely correct`, the UI shows `AI Suggested Win`; the user can still press manual `Win`.

## Scoring Rule

Automatic scoring remains deterministic:

- `AUTO WIN`: deterministic grader passes.
- `AUTO FAILED`: deterministic grader fails.
- `AI Suggested Win`: AI reviewer thinks the answer may be correct, but the grader failed.

The first implementation must not auto-award points from AI alone. A later setting may allow high-confidence AI auto-wins, but that setting must default off.

## Architecture

### Deterministic Grader

The current Pyodide grader remains the authority. It should continue to improve through broader tests, better script handling, better function discovery, and more precise source requirements only when a problem explicitly requires specific syntax.

### AI Review Service

Add a client-side AI review service with a stable interface:

```ts
type AiReviewVerdict = 'likely_correct' | 'likely_incorrect' | 'unclear';

interface AiReviewRequest {
  problemId: number;
  description: string;
  userCode: string;
  graderMessage: string;
  graderPassed: boolean;
  visibleSolution?: string;
}

interface AiReviewResult {
  verdict: AiReviewVerdict;
  confidence: number;
  explanation: string;
  suggestedFix?: string;
}
```

The UI should call this interface, not a model runtime directly. This keeps the app flexible if the runtime changes from Transformers.js to WebLLM or another browser runtime.

### Offline Model Runtime

Use an optional browser runtime loaded only when the user enables the feature. Candidate runtimes:

- Transformers.js for smaller ONNX/browser models.
- WebLLM for browser WebGPU LLMs if iPhone support and memory are acceptable.

The first implementation should include runtime capability checks before download. If the phone cannot support the model, show `Device not supported` or `Download failed` without breaking the main app.

### Storage

Store model assets through browser cache or IndexedDB, depending on the selected runtime. Add settings controls:

- `Offline AI Reviewer` on/off.
- `Download reviewer model`.
- `Remove offline model`.
- `Reviewer status`.
- `Use AI when grader fails`.

The app should never clear progress, stats, saved code, or settings when removing the model.

## UI Changes

### Hide Tools AI Button

The `AI` button should open an `AI Review` panel:

- If offline reviewer is ready, run local review.
- If reviewer is not installed, show setup instructions and the existing API/Gemini fallback if available.
- If grader failed, show grader failure beside AI feedback.
- If AI says `Likely correct`, show a clear `AI Suggested Win` state, not `AUTO WIN`.

### Settings

Settings should include an `Offline AI Reviewer` section. It must be scrollable on phone and show download/removal controls without hiding reset or other existing settings.

## Error Handling

- If model download fails, keep the deterministic grader usable.
- If model inference fails, show a short error and keep manual controls.
- If the reviewer times out, return `Unclear`.
- If storage is unavailable, disable offline model installation.
- If the model is not ready, `AI` should still show deterministic diagnostics.

## Testing

- Build must pass with the AI reviewer disabled.
- Existing grader validation must continue to pass.
- Settings must persist reviewer enablement and model status.
- AI panel must work when model is not installed.
- Removing the model must not remove user progress, stats, saved files, or customization.
- Grader pass must still award automatic points without AI.
- Grader fail plus AI likely-correct must not auto-award points in the first implementation.

## Implementation Stages

1. Add deterministic `AI Review` panel and structured grader diagnostics without adding a model runtime.
2. Add offline reviewer settings and status state, still with no model download.
3. Add a runtime adapter and choose the smallest viable in-browser code reviewer model after device compatibility testing.
4. Add optional model download/remove flow.
5. Connect the ready offline reviewer to the `AI` button.
6. Continue improving deterministic graders in parallel.

