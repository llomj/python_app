---
name: automate-thread-names
description: Simplify and standardize Codex thread names into concise, plain-language titles that a non-technical reader can understand. Use when a thread title is verbose, jargon-heavy, repetitive, unclear, or acronym-dense, and when creating or renaming threads across any folder or project.
---

# Automate Thread Names

Rewrite thread titles into short, clear names with plain words and consistent structure.

## Workflow

1. Read the original title and identify the core intent.
2. Remove filler words, implementation noise, and duplicate ideas.
3. Replace jargon with plain language.
4. Expand each acronym at first use as `Full Term (ACR)` when the acronym is important.
5. Produce one final title that is unique versus recent thread names in the current conversation.
6. If the user accepts the proposed title, immediately apply the rename when thread-rename capability is available in the runtime.
7. If rename capability is not available, state this clearly in one sentence and return the exact accepted title for manual one-click paste.

## Naming Rules

- Use 3 to 6 words when possible.
- Prefer common words a layperson can understand.
- Keep one clear topic and one clear action.
- Keep punctuation minimal.
- Avoid repeated titles; if a similar title already exists, change wording while preserving meaning.
- Avoid prefixes like `Task`, `Help`, `Thread`, `Need`, `Issue`.
- Keep technical acronyms only when necessary; define them in parentheses.

## Acronym Policy

- If an acronym is required, write `full term (ACR)` once in the title.
- If expanding the acronym would make the title too long, prefer a plain-language synonym and omit the acronym.
- Never use unexplained acronyms.

## Output Format

Return only the final thread title text unless the user explicitly asks for alternatives.

## Apply-on-Accept Rule

- This skill is not suggestion-only. After user acceptance, treat rename as an execution step.
- Execution priority:
  - First: call the runtime thread-rename capability/tool if available.
  - Fallback: return `Cannot rename in this runtime. Use this exact title: <title>`.
- Never claim a rename was applied unless it was actually applied.

## Examples

- `Need help with CI pipeline failing on PR checks in monorepo` -> `Fix Continuous Integration (CI) checks`
- `Refactor JWT auth middleware and RBAC claims mapping` -> `Improve token access control`
- `Automate OCR for scanned invoice PDFs` -> `Automate scanned invoice text reading`
