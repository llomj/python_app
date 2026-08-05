#!/usr/bin/env python3
"""
Analyze home folder - show size breakdown and organization suggestions
"""

import os
import subprocess
from pathlib import Path
from collections import defaultdict

HOME = Path.home()


def get_size(path):
    try:
        return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
    except:
        return 0


def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def analyze_home():
    print("=== Home Folder Analysis ===\n")

    items = []
    for item in HOME.iterdir():
        if item.name.startswith("."):
            category = "Hidden"
        else:
            category = "Visible"

        size = get_size(item)
        items.append((item.name, size, category))

    items.sort(key=lambda x: x[1], reverse=True)

    print(f"{'Folder':<30} {'Size':>10} {'Type'}")
    print("-" * 50)

    for name, size, category in items[:20]:
        print(f"{name:<30} {format_size(size):>10} {category}")

    total = sum(s for _, s, _ in items)
    print("-" * 50)
    print(f"{'Total':<30} {format_size(total):>10}")

    print("\n=== Loose Files in Root ===")
    loose = [f for f in HOME.iterdir() if f.is_file() and not f.name.startswith(".")]
    for f in loose:
        print(f"  {f.name}")


def main():
    analyze_home()


if __name__ == "__main__":
    main()
