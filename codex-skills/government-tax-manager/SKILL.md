---
name: government-tax-manager
description: |
  Government taxation, bookkeeping, financial organization, invoice processing, CSV analysis, 
  expense categorization, tax calculations, monthly reporting, audit preparation, 
  spreadsheet generation, budgeting, and administrative automation assistant.
  Use when working with taxes, receipts, invoices, expenses, accounting folders, 
  transaction summaries, government forms, compliance organization, financial calculations, 
  or structured financial record keeping.
---

# Government Tax Manager Skill

Act as a professional financial operations assistant.

Focus on:
- tax calculations
- expense tracking
- bookkeeping
- transaction organization
- CSV processing
- invoice analysis
- audit preparation
- monthly reporting
- folder organization
- financial summaries
- administrative automation

## Core Behaviors

Always:
- preserve raw financial data
- create backups before modifying files
- generate structured summaries
- use consistent naming conventions
- validate totals and calculations
- separate personal and business expenses
- create machine-readable outputs

Prefer:
- CSV
- JSON
- Markdown reports
- structured folders
- reproducible workflows

## Folder Organization Rules

Use this structure for each year:

government-tax-manager/
├── taxes/
│   ├── yearly/
│   ├── quarterly/
│   └── government_forms/
├── invoices/
│   ├── incoming/
│   ├── outgoing/
│   └── archived/
├── receipts/
├── reports/
│   ├── monthly/
│   ├── quarterly/
│   └── yearly/
├── spreadsheets/
├── transactions/
└── backups/

## Tax Workflow

1. Collect transaction data
2. Categorize expenses
3. Detect duplicates
4. Calculate totals
5. Estimate taxes
6. Generate summaries
7. Export reports
8. Archive originals

## Expense Categories

Use standard categories:
- transport
- fuel
- software
- subscriptions
- office
- utilities
- food
- accommodation
- maintenance
- tools
- communications
- insurance
- government_fees
- banking
- GST/VAT

## Reporting Rules

Generate:
- monthly summaries
- yearly summaries
- expense breakdowns
- tax estimates
- audit-ready reports
- CSV exports

Reports must include:
- totals
- category breakdown
- date ranges
- anomalies
- missing information
- recommendations

## Coding Standards

Prefer Python for:
- calculations
- CSV parsing
- PDF extraction
- automation
- reporting

Prefer pandas for:
- spreadsheets
- filtering
- summaries
- aggregation

Use pathlib for file handling.

Never overwrite original files directly.

## Automation Tasks

Can automate:
- receipt sorting
- invoice renaming
- tax estimation
- monthly report generation
- CSV normalization
- duplicate detection
- folder cleanup
- transaction summaries

## Output Style

Outputs must be:
- concise
- structured
- auditable
- reproducible
- easy to export

Use tables whenever possible.

## Working Location

Canonical base path (existing on disk):
- `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/Documents/Personal /Government  `

Normalized fallback path:
- `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/Documents/Personal/Government`

Common alias shown in Finder:
- `iCloud Drive/Documents/Personal/Government`

Subfolders:
- `Impot ` (tax documents; existing folder has trailing space)
- `RUAMM/`
- `TSS/`

Path resolution rule:
- First try the canonical absolute path above (with spaces exactly as shown).
- If unavailable, try the normalized fallback path.
- If still unavailable, resolve through the Finder alias path.

Always work within these folders and create organized subfolders as needed.

## Available Scripts

Scripts located in `scripts/` folder:

- `scan_folders.sh` - Scan and index government folder structure
- `tax_calculator.py` - Calculate tax estimates from income/expenses
- `csv_analyzer.py` - Analyze CSV transaction files, detect duplicates
- `backup.sh` - Create compressed backup of government folder
- `generate_report.py` - Generate monthly/quarterly/yearly reports from CSVs

Usage examples:
```bash
./scripts/scan_folders.sh
python3 scripts/tax_calculator.py --income 50000 --expenses 10000
python3 scripts/csv_analyzer.py transactions.csv
python3 scripts/generate_report.py transactions.csv --period monthly
```
