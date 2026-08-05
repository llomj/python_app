#!/usr/bin/env python3
"""
Find largest files in home folder
"""

import os
from pathlib import Path

HOME = Path.home()


def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def find_large_files(top=20):
    files = []
    for root, dirs, filenames in os.walk(HOME):
        for f in filenames:
            try:
                path = Path(root) / f
                size = path.stat().st_size
                if size > 10 * 1024 * 1024:  # > 10MB
                    files.append((str(path), size))
            except:
                pass

    files.sort(key=lambda x: x[1], reverse=True)

    print(f"=== Largest Files in Home Folder ===\n")
    print(f"{'Size':>10} {'Path'}")
    print("-" * 70)

    for path, size in files[:top]:
        print(f"{format_size(size):>10} {path}")


def main():
    find_large_files()


if __name__ == "__main__":
    main()
