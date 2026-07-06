# Problem AI Chat Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a problem-panel AI chat that answers user questions using current problem, code, output, and grader context.

**Architecture:** Keep the first version inside `App.tsx` using existing AI review state and offline/built-in review services. Add local chat state, a modal view, context builder, and a lightweight answer generator that uses available AI when installed and deterministic tutoring fallback otherwise.

**Tech Stack:** React state/hooks, existing `AiReviewRequest`/`AiReviewResult`, existing offline AI reviewer and built-in diagnostic reviewer, Vite build.

---

### Task 1: Add Problem AI State And Context Builder

**Files:**
- Modify: `App.tsx`

- [ ] Add `problem_ai` to `showModal` union.
- [ ] Add chat message/draft/loading state.
- [ ] Add `buildProblemAiContext()` using current exercise, active file, latest output, grader result, and solution.

### Task 2: Add Problem AI Answer Flow

**Files:**
- Modify: `App.tsx`

- [ ] Add `buildBuiltInProblemAiAnswer(question)` for deterministic fallback.
- [ ] Add `sendProblemAiQuestion(question)` that appends user message, calls available AI with a tutor-style request when possible, and appends assistant response.
- [ ] Add quick prompts: `Explain task`, `Why failed?`, `What method?`, `Show hint`.

### Task 3: Add Problem Panel AI Button And Modal

**Files:**
- Modify: `App.tsx`

- [ ] Add AI button left of Save in the problem panel.
- [ ] Add modal body for `problem_ai` with context chips, chat messages, quick prompts, input box, and send button.
- [ ] Ensure modal is scrollable and mobile-safe.

### Task 4: Verify And Commit

**Files:**
- Verify: `App.tsx`, TypeScript build, grader suite.

- [ ] Run `npm run build`.
- [ ] Run `npm run check:graders`.
- [ ] Run `git diff --check`.
- [ ] Commit and push.
