#!/usr/bin/env python3
"""
Organize home folder - move loose files to proper locations
"""

import os
import shutil
from pathlib import Path
import argparse

HOME = Path.home()

RECOMMENDED_MOVES = [
    # Loose files -> suggested locations
    ("package.json", "~/Clean/projects/"),
    ("package-lock.json", "~/Clean/projects/"),
    ("node_modules", "~/Clean/projects/"),
    ("index.js", "~/Clean/scripts/"),
    ("index.html", "~/Clean/scripts/"),
    ("index.tsx", "~/Clean/projects/"),
    ("components/", "~/Clean/projects/"),
    ("services/", "~/Clean/projects/"),
    ("node/", "~/Clean/archives/"),
    ("bin/", "~/Clean/scripts/"),
    ("go/", "~/Clean/projects/"),
    ("llm-env/", "~/Clean/projects/"),
    ("ollama_uncensored/", "~/Clean/archives/"),
    ("discord-telegram-bridge/", "~/Clean/projects/"),
    ("constants.ts", "~/Clean/projects/"),
    ("logicEngine.ts", "~/Clean/projects/"),
    ("knowledgeBase.ts", "~/Clean/projects/"),
    ("translations.ts", "~/Clean/projects/"),
    ("types.ts", "~/Clean/projects/"),
    ("fallacyData.ts", "~/Clean/projects/"),
    ("metadata.json", "~/Clean/archives/"),
    ("ps.md", "~/Clean/scripts/"),
]


def create_folders():
    folders = [
        HOME / "Clean" / "projects",
        HOME / "Clean" / "scripts",
        HOME / "Clean" / "archives",
    ]
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
    print("Created: Clean/projects, Clean/scripts, Clean/archives")


def organize_files(dry_run=True):
    print(f"\n=== Organize Files ({'DRY RUN' if dry_run else 'FOR REAL'}) ===\n")
    print("WARNING: This only MOVES files, does NOT delete anything.\n")

    for filename, dest in RECOMMENDED_MOVES:
        source = HOME / filename
        dest_path = Path(dest).expanduser()

        if source.exists():
            action = "Would move" if dry_run else "Moving"
            print(f"{action}: {filename} -> {dest}")
            if not dry_run:
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(source), str(dest_path))
        else:
            print(f"Skip: {filename} (not found)")

    print("\n=== Summary ===")
    print("Files are MOVED, not deleted. You can always move them back.")


def main():
    parser = argparse.ArgumentParser(description="Organize home folder")
    parser.add_argument(
        "--dry-run", action="store_true", default=True, help="Show what would happen"
    )
    parser.add_argument("--execute", action="store_true", help="Actually move files")

    args = parser.parse_args()

    create_folders()
    organize_files(dry_run=not args.execute)


if __name__ == "__main__":
    main()
