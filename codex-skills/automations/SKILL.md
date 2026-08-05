# Automations

Use this skill when the user asks to schedule reminders/follow-ups/automations in Codex.

## Modes

- `plan-only`: Create reminder + checklist only.
- `execute-on-confirm`: On trigger date, run checks and request explicit confirmation before actions.

## Safety Tiers

- `low`: read-only verification.
- `medium`: archive/move (reversible).
- `high`: delete/reset (irreversible, requires strict confirmation).

## Hard Safety Rules

1. Never auto-run destructive actions from automation.
2. For `high` tier actions, require explicit confirmation with exact prompt:
   - `Type YES to proceed.`
3. Always run preflight checks before execution.

## Preflight Contract

- Verify target paths exist.
- Verify canonical vault path is active.
- Show before-counts/sizes where relevant.
- Abort if path mismatch is detected.

## Required Execution Prompt

`🛑 Confirmation required: I verified targets and preflight checks. Type YES to proceed with this action.`

## Logging

Write a structured log block to:
- `logs/automations.md`

Append summary lines to:
- `ps.md`
- `track.md`

## Emoji UI Style

Use emojis in reminders/summaries (not command logic):
- `🗓️` schedule
- `📍` targets
- `✅` passed checks
- `⚠️` warnings
- `🧹` cleanup action
- `🛑` confirmation required
- `📝` log written

## Reminder Template (Archive Review)

- Title: `🗓️ Review hidden iCloud archives`
- Message:
  - `📍 Targets:`
    - `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/.ARCHIVE_AI_2_20260525`
    - `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/.ARCHIVE_Obsidian_2_20260525`
  - `⚠️ Do not auto-delete.`
  - `🛑 Ask for explicit confirmation before any deletion.`

## Tool Availability Rule

- If automation scheduling tool is unavailable in current session:
  - clearly state scheduling cannot be executed automatically,
  - provide a ready-to-paste reminder payload,
  - do not claim the automation was created.

## Idempotency

- If an equivalent pending reminder exists (same target/date/action), update/merge instead of duplicating.
