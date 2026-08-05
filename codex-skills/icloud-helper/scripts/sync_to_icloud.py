#!/usr/bin/env python3
"""
Sync folder to iCloud - Move folder to iCloud Drive
"""

import os
import shutil
import subprocess
from pathlib import Path
import argparse

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


def sync_to_icloud(folder_path, dry_run=True):
    source = Path(folder_path).expanduser()

    if not source.exists():
        print(f"Error: {source} does not exist")
        return

    dest = ICLOUD_PATH / source.name

    if dest.exists():
        print(f"Warning: {dest.name} already exists in iCloud")
        response = input("Update existing? (y/n): ")
        if response.lower() != "y":
            print("Cancelled")
            return

    size = get_size(source)
    print(f"\n=== {'DRY RUN' if dry_run else 'FOR REAL'} ===")
    print(f"Source (local): {source}")
    print(f"Destination (iCloud): {dest}")
    print(f"Size: {format_size(size)}")
    print(f"\nThis will COPY (not move) the folder to iCloud.")
    print("✅ Original stays in place (local)")
    print("✅ iCloud gets a duplicate (backup)")
    print("✅ Access from any device\n")

    if dry_run:
        print("Use --execute to actually copy the folder")
        return

    confirm = input("Continue? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled")
        return

    shutil.copytree(str(source), str(dest), dirs_exist_ok=True)
    print(f"Copied {source.name} to iCloud (original stays local)")


def main():
    parser = argparse.ArgumentParser(description="Sync folder to iCloud")
    parser.add_argument("folder", help="Folder to sync to iCloud")
    parser.add_argument("--dry-run", action="store_true", default=True)
    parser.add_argument("--execute", action="store_true", help="Actually move folder")

    args = parser.parse_args()
    dry_run = not args.execute
    sync_to_icloud(args.folder, dry_run)


if __name__ == "__main__":
    main()
