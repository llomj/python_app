# User display preferences

## Financial values

- Render USD-denominated values in accessible green (`#16a34a`) across Codex dashboards, tables, and financial reports when supported.
- When color is unavailable, use `🟢` or `💵` while retaining the `$`/`USD` label.
- Render adjacent unit and denomination labels in accessible pink (`#be185d`). Example: `$0.002868` is green and `/HEX` is pink.
- When color is unavailable, prefix the unit with `🩷` and retain the written unit label.
- Never encode meaning through color alone.
- Do not alter raw data, calculations, CSV, JSON, code, source excerpts, or machine interfaces to force color.

The global runtime rule is also recorded in `/Users/moll/.codex/AGENTS.md` so individual skills inherit it without duplicating the policy in every skill folder.
