#!/usr/bin/env python3
"""
CSV Analyzer for Government Tax Manager
Analyzes CSV transaction files, detects duplicates, categorizes expenses.
"""

import csv
import argparse
from pathlib import Path


def find_duplicates(rows, key):
    seen = {}
    dups = []
    for i, row in enumerate(rows):
        val = row.get(key, "").strip().lower()
        if val and val in seen:
            dups.append(f"Row {i + 1}: {val}")
        seen[val] = i
    return dups


def analyze_csv(filepath, date_col=None, amount_col=None, desc_col=None):
    if not Path(filepath).exists():
        print(f"Error: File not found: {filepath}")
        return

    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No data found in CSV")
        return

    headers = list(rows[0].keys())
    print(f"=== CSV Analysis: {Path(filepath).name} ===")
    print(f"Total rows: {len(rows)}")
    print(f"Columns: {', '.join(headers)}")

    amounts = None
    if amount_col:
        amounts = [float(row.get(amount_col, 0)) for row in rows if row.get(amount_col)]
        print(f"\nAmount Stats:")
        print(f"  Total: €{sum(amounts):,.2f}")
        print(f"  Average: €{sum(amounts) / len(amounts):,.2f}")
        print(f"  Min: €{min(amounts):,.2f}")
        print(f"  Max: €{max(amounts):,.2f}")

    if amount_col == "amount" and amounts:
        income = sum(a for a in amounts if a > 0)
        expenses = sum(a for a in amounts if a < 0)
        print(f"\n  Income: €{income:,.2f}")
        print(f"  Expenses: €{abs(expenses):,.2f}")

    duplicates = find_duplicates(rows, desc_col or "description")
    if duplicates:
        print(f"\nPotential duplicates: {len(duplicates)}")
        for dup in duplicates[:5]:
            print(f"  - {dup}")


def main():
    parser = argparse.ArgumentParser(description="CSV Analyzer")
    parser.add_argument("file", help="CSV file to analyze")
    parser.add_argument("--date", help="Date column name")
    parser.add_argument("--amount", help="Amount column name")
    parser.add_argument("--desc", help="Description column name")

    args = parser.parse_args()
    analyze_csv(args.file, args.date, args.amount, args.desc)


if __name__ == "__main__":
    main()
