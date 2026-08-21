# PulseChain Market Analyst integration

## Skill link

- Display name: PulseChain Market Analyst
- Invocation: `$analyze-pulsechain-markets`
- Codex path: `/Users/moll/.codex/skills/analyze-pulsechain-markets`
- Canonical iCloud path: `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/AI/Pulsechain/analyze-pulsechain-markets`
- Canonical Obsidian data folder: `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain/raw/files/pulsechain`
- Canonical visible overview folder: `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain/raw/Pulsechain ` (the existing filesystem name includes a trailing space; preserve it and never create a duplicate without the space)

Use the market skill for live collection and quantitative analysis. Use Obsidian Helper to find prior research, synthesize multiple dated observations, and publish human-readable knowledge notes.

When the user says `dashboard`, route to the market skill's emoji dashboard. It includes live indexed markets, ratios, confidence, DEX liquidity, broad-crypto Fear & Greed, alerts, and sanitized upcoming stake endings.

## Routing rules

- Treat unqualified `HEX` as HEX on PulseChain.
- Treat `HEX on Ethereum`, `Ethereum HEX`, or `eHEX` as HEX on Ethereum.
- Refresh live data before answering current-market questions.
- Preserve the UTC observation time, source health, and coverage limitations.
- Never present a stored Obsidian note as live market data.
- Never store wallet addresses, seed phrases, private keys, authentication secrets, or browser-local wallet data in the vault.
- For Richard Heart questions, start with `wiki/hubs/richard-heart-hub.md`, `wiki/entities/richard-heart.md`, `wiki/sources/richard-heart-source-index.md`, the timeline, claim registry, theses, positions, worldview, and track record. Verify current tweets and time-sensitive claims against current primary sources.
- Separate Richard Heart's stated view, Obsidian synthesis, current factual verification, and unresolved disputes.

## Vault publication

Write only when the user explicitly asks to save, remember, publish, or update research.

- Put dated market reports in `wiki/sources/`.
- Put durable token definitions, terminology, and methodologies in `wiki/concepts/`.
- Link related pages with Obsidian wikilinks.
- Follow the vault frontmatter format.
- Update `index.md` and append the action to `log.md`.
- Cite the skill snapshot path and external market sources used.
- Never modify `raw/`.

Stable automated entry points are `wiki/sources/pulsechain-market-daily.md` and `wiki/sources/pulsechain-market-weekly.md`. Update those canonical files instead of creating dated duplicates.

The user-designated visible overview is `raw/Pulsechain /pulsechain-overview.md`. This is an explicit exception to the normal raw-folder synthesis rule. Generated PulseChain CSV and JSON data belongs only in `raw/files/pulsechain/` and uses stable `*-latest` filenames. Never scatter PulseChain data exports elsewhere in the vault.

HEX Daily Stats is a canonical two-chain cross-check in this folder. Maintain `hex-daily-stats-latest.csv` and `hex-daily-stats-latest.json` with explicit `HEX (PulseChain)` and `HEX on Ethereum` labels, source URLs, collection time, and the source record date. Treat its price fields as secondary cross-checks; use refreshed DEX market data for the live dashboard price.

Keep machine snapshots in the PulseChain skill. Store concise conclusions and source links in Obsidian rather than duplicating complete JSON snapshots.
