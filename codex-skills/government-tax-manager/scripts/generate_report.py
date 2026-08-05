#!/usr/bin/env python3
"""
Report Generator for Government Tax Manager
Generates monthly/quarterly/yearly financial reports from transaction CSVs.
"""

import csv
import sys
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def generate_report(csv_file, period="monthly", output=None):
    if not Path(csv_file).exists():
        print(f"Error: File not found: {csv_file}")
        return

    with open(csv_file, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No data found")
        return

    headers = list(rows[0].keys())
    date_col = next((h for h in headers if "date" in h.lower()), None)
    amount_col = next((h for h in headers if "amount" in h.lower()), None)
    desc_col = next(
        (
            h
            for h in headers
            if any(x in h.lower() for x in ["desc", "libelle", "name"])
        ),
        None,
    )

    if not date_col or not amount_col:
        print("Required columns not found (date, amount)")
        return

    by_period = defaultdict(lambda: {"income": 0, "expenses": 0, "count": 0})

    for row in rows:
        try:
            date_str = row.get(date_col, "")
            amount = float(row.get(amount_col, 0))

            if period == "monthly":
                key = date_str[:7]
            elif period == "quarterly":
                month = int(date_str[5:7]) if len(date_str) >= 7 else 1
                key = f"{date_str[:4]}-Q{(month - 1) // 3 + 1}"
            else:
                key = date_str[:4]

            if amount > 0:
                by_period[key]["income"] += amount
            else:
                by_period[key]["expenses"] += abs(amount)
            by_period[key]["count"] += 1
        except (ValueError, IndexError):
            continue

    report = f"# Financial Report - {period.capitalize()}\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    report += f"| Period | Income | Expenses | Net | Transactions |\n"
    report += f"|--------|--------|----------|-----|-------------|\n"

    total_income = 0
    total_expenses = 0

    for period_key in sorted(by_period.keys()):
        data = by_period[period_key]
        net = data["income"] - data["expenses"]
        total_income += data["income"]
        total_expenses += data["expenses"]
        report += f"| {period_key} | €{data['income']:,.2f} | €{data['expenses']:,.2f} | €{net:,.2f} | {data['count']} |\n"

    report += f"\n**Total Income:** €{total_income:,.2f}\n"
    report += f"**Total Expenses:** €{total_expenses:,.2f}\n"
    report += f"**Net:** €{total_income - total_expenses:,.2f}\n"

    if output:
        Path(output).write_text(report)
        print(f"Report saved to: {output}")
    else:
        print(report)


def main():
    parser = argparse.ArgumentParser(description="Report Generator")
    parser.add_argument("file", help="CSV transaction file")
    parser.add_argument(
        "--period", choices=["monthly", "quarterly", "yearly"], default="monthly"
    )
    parser.add_argument("--output", "-o", help="Output markdown file")

    args = parser.parse_args()
    generate_report(args.file, args.period, args.output)


if __name__ == "__main__":
    main()
