#!/usr/bin/env python3
"""
Check iCloud sync status for a folder
"""

import os
from pathlib import Path

HOME = Path.home()
ICLOUD_PATH = HOME / "Library/Mobile Documents"


def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def get_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total += os.path.getsize(fp)
            except:
                pass
    return total


def check_sync(folder_name):
    local_path = HOME / folder_name
    icloud_path = ICLOUD_PATH / folder_name

    print(f"=== Sync Status: {folder_name} ===\n")

    local_exists = local_path.exists()
    icloud_exists = icloud_path.exists()

    print(
        f"Local:   {'✅ ' + format_size(get_size(local_path)) if local_exists else '❌ Not found'}"
    )
    print(
        f"iCloud:  {'✅ ' + format_size(get_size(icloud_path)) if icloud_exists else '❌ Not found'}"
    )

    if local_exists and icloud_exists:
        print(f"\nStatus: 🔄 SYNCED (duplicate in both)")
    elif local_exists and not icloud_exists:
        print(f"\nStatus: 📱 Local only (not in iCloud)")
    elif not local_exists and icloud_exists:
        print(f"\nStatus: ☁️ iCloud only (not local)")
    else:
        print(f"\nStatus: ❌ Neither exists")


def list_icloud():
    print("=== iCloud Drive Contents ===\n")
    if not ICLOUD_PATH.exists():
        print("Error: iCloud Drive not accessible")
        return

    items = []
    for item in ICLOUD_PATH.iterdir():
        size = get_size(item)
        items.append((item.name, size))

    items.sort(key=lambda x: x[1], reverse=True)

    for name, size in items:
        print(f"  {name:<40} {format_size(size)}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="iCloud sync status")
    parser.add_argument(
        "folder", nargs="?", help="Folder to check (leave empty to list all)"
    )
    parser.add_argument("--list", action="store_true", help="List all iCloud folders")

    args = parser.parse_args()

    if args.list:
        list_icloud()
    elif args.folder:
        check_sync(args.folder)
    else:
        print("Usage: check_status.py [folder_name] or check_status.py --list")


if __name__ == "__main__":
    main()
