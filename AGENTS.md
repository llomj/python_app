# Rules

1. Black/Yellow theme
2. Gemini-3-flash-preview for scoring
3. **Full offline support** – The app must work when there is no internet. Users can access and use the app entirely offline (exercises, editor, Python execution). AI scoring requires network; show a clear "offline" message when unavailable.
4. User-authored Codex skills live in `~/.codex/skills/`. The repo root `codex-skills/` folder is their automated, non-destructive GitHub backup. Add and update skills, but preserve older GitHub content if a local source disappears. Keep the backup committed and pushed; exclude Codex-managed `.system/` content and the recursive `user-codex-skills` symlink.
5. Never delete a folder from this repository. Preserve missing or obsolete content. Any requested deletion must follow the global two-warning `🛑 ⚠️` confirmation sequence, and permanent deletion must be performed manually by Jono.
