---
name: local-model-router
description: |
  Use when the user wants to use local/open-source models on this Mac through LM Studio or Ollama,
  especially for mundane Obsidian tasks when remote model tokens are limited.
  Trigger on phrases like "use local model", "use nemotron", "nemotron", "use gemma", "gemma", or "use ollama".
---

You are a local-model routing skill for this Mac.

## Goal

Use local models for cheap, low-risk Obsidian work without breaking vault rules.

## Important Limitation

If Codex is completely unavailable because the session cannot run at all, Codex cannot be the thing that starts the local model.

So the fallback has two layers:

1. While Codex is still available for short orchestration, Codex can route work to local models.
2. If Codex is unavailable, the same local workflow must be started by another local tool path on the Mac, such as OpenCode or a terminal-launched wrapper script.

## Canonical Vault Guard

- Active vault path: `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain`
- Finder/iPhone path: `iCloud Drive/Obsidian/AI brain`
- Never use the old CloudDocs Obsidian path
- Never modify `raw/` or `raw/Sources/`
- Prefer local models for drafting and suggestion work, then verify before applying edits

## Current Local Model Inventory

### LM Studio

- App present and running
- Local API listening on `127.0.0.1:1234`
- Models available from `/v1/models`:
  - `nvidia/nemotron-3-nano-4b`
  - `google/gemma-3-1b`
  - `text-embedding-nomic-embed-text-v1.5`

### Ollama

- Service present and listening on `127.0.0.1:11434`
- Current installed models: none

## Recommended Use

Use LM Studio first for mundane tasks:

- note summaries
- cleanup drafts
- section rewrites
- tag/category suggestions
- outline generation
- first-pass extraction from already-open text

Prefer `nvidia/nemotron-3-nano-4b` over `google/gemma-3-1b` for richer drafting.
Use `google/gemma-3-1b` only for lighter/cheaper prompts.

Do not rely on local models alone for:

- destructive edits
- bulk link repair
- security decisions
- factual claims that need external verification
- sync/path operations

## Operational Pattern

1. Check local endpoints:
   - LM Studio: `curl http://127.0.0.1:1234/v1/models`
   - Ollama: `curl http://127.0.0.1:11434/api/tags`
2. If the user says `use nemotron`, route to:
   - provider: `lmstudio`
   - model: `nvidia/nemotron-3-nano-4b`
3. If the user says `use gemma`, route to:
   - provider: `lmstudio`
   - model: `google/gemma-3-1b`
4. If the user says `use ollama <model>` or `use ollama:model_name`, verify that Ollama has the model installed before attempting the run.
5. Use:
   - `scripts/local_model_draft.sh <alias> "<prompt>" [output_file]`
6. In every context window / run report, show the active local model with an emoji:
   - `🧠 model: <exact model name> | provider: <lmstudio|ollama>`
7. In every context window / run report, show token usage when available:
   - `prompt_tokens`
   - `completion_tokens`
   - `total_tokens`
8. If usage is unavailable, state that plainly so the user knows the count is not exposed by the provider.
9. Generate draft output locally.
10. Verify before writing to the vault.
11. Log provider/model and usage telemetry if available.

## Suggested Routing Policy

- If user says `use local model`, default to LM Studio.
- If user says `use nemotron` or just `nemotron`, default to LM Studio Nemotron 4B.
- If user says `use gemma` or just `gemma`, default to LM Studio Gemma 1B.
- If user says `use ollama`, check whether models are actually installed first.
- If no local model is available, say so plainly and fall back to Codex or OpenCode.
- Always include the `🧠 model: ...` line in the response when a local model is used.

## Example Decision Rule

- light rewrite => `google/gemma-3-1b`
- richer note draft => `nvidia/nemotron-3-nano-4b`
- embeddings/search experiments => `text-embedding-nomic-embed-text-v1.5`

## Future Extension

If the user later pulls Ollama models, update this skill with:
- installed model list
- best-use classes
- exact command examples
