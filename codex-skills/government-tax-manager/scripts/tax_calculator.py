#!/usr/bin/env python3
"""
Tax Calculator for Government Tax Manager
Calculates tax estimates based on income and expenses.
"""

import sys
import argparse
from pathlib import Path

DEFAULT_RATE = 0.20
DEFAULT_YEAR = 2024


def calculate_taxable(income, expenses):
    return max(0, income - expenses)


def calculate_tax(amount, rate=DEFAULT_RATE):
    return amount * rate


def categorize_expenses(expenses, categories):
    result = {}
    for cat, amount in categories.items():
        result[cat] = amount
    return result


def main():
    parser = argparse.ArgumentParser(description="Tax Calculator")
    parser.add_argument("--income", type=float, required=True, help="Total income")
    parser.add_argument(
        "--expenses", type=float, default=0, help="Total deductible expenses"
    )
    parser.add_argument(
        "--rate", type=float, default=DEFAULT_RATE, help="Tax rate (default: 0.20)"
    )
    parser.add_argument("--year", type=int, default=DEFAULT_YEAR, help="Tax year")
    parser.add_argument("--csv", type=str, help="CSV file with transactions")

    args = parser.parse_args()

    if args.csv and Path(args.csv).exists():
        import csv

        total_expenses = 0
        with open(args.csv, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "amount" in row:
                    total_expenses += abs(float(row.get("amount", 0)))
        expenses = total_expenses
    else:
        expenses = args.expenses

    taxable = calculate_taxable(args.income, expenses)
    tax = calculate_tax(taxable, args.rate)
    net = args.income - tax

    print(f"=== Tax Calculation {args.year} ===")
    print(f"Income:        €{args.income:,.2f}")
    print(f"Expenses:      €{expenses:,.2f}")
    print(f"Taxable:       €{taxable:,.2f}")
    print(f"Tax ({args.rate * 100}%):    €{tax:,.2f}")
    print(f"Net Income:    €{net:,.2f}")
    print(f"Effective Rate:{(tax / args.income) * 100:.1f}%")


if __name__ == "__main__":
    main()
