#!/usr/bin/env python3
"""
Weekly iCloud sync - copy changes to iCloud
"""

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

HOME = Path.home()
ICLOUD_PATH = HOME / "Library/Mobile Documents"
FOLDERS_TO_SYNC = ["AI", "AI skills", "termimal"]

LOG_FILE = HOME / ".icloud-sync.log"


def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {msg}\n")
    print(msg)


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


def sync_folder(folder_name):
    source = HOME / "Desktop" / folder_name
    dest = ICLOUD_PATH / folder_name

    if not source.exists():
        log(f"⚠️ Source not found: {source}")
        return

    size = get_size(source)
    log(f"📁 Syncing: {folder_name} ({format_size(size)})")

    if dest.exists():
        shutil.copytree(str(source), str(dest), dirs_exist_ok=True)
        log(f"✅ Updated in iCloud: {folder_name}")
    else:
        shutil.copytree(str(source), str(dest))
        log(f"✅ Copied to iCloud: {folder_name}")


def main():
    log("=== Weekly iCloud Sync Started ===")

    for folder in FOLDERS_TO_SYNC:
        try:
            sync_folder(folder)
        except Exception as e:
            log(f"❌ Error syncing {folder}: {e}")

    log("=== Weekly iCloud Sync Complete ===")


if __name__ == "__main__":
    main()
