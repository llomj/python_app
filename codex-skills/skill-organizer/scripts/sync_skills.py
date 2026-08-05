#!/usr/bin/env python3
"""Safely align user-authored skills across local agent runtimes."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


VAULT = Path("/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain")
CANONICAL = VAULT / "AI skills/codex-skills"
USER_MIRROR = CANONICAL / "user-codex-skills"
CURSOR_LIVE = Path.home() / ".cursor/skills-cursor"
CURSOR_MIRROR = VAULT / "AI skills/cursor-skills"

RUNTIME_TARGETS = {
    "codex": Path.home() / ".codex/skills",
    "agents": Path.home() / ".agents/skills",
    "opencode": Path.home() / ".config/opencode/skills",
    "opencode-mirror": VAULT / "AI skills/opencode-skills",
    "user-codex-mirror": USER_MIRROR,
}


def skill_dirs(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir()
        and path.name != "user-codex-skills"
        and (path / "SKILL.md").is_file()
    )


def same_tree(source: Path, target: Path) -> bool:
    if not target.is_dir():
        return False
    comparison = filecmp.dircmp(source, target)
    if comparison.left_only or comparison.right_only or comparison.diff_files or comparison.funny_files:
        return False
    return all(
        same_tree(source / name, target / name)
        for name in comparison.common_dirs
    )


def copy_skill(source: Path, target_root: Path, apply: bool) -> str:
    target = target_root / source.name
    if same_tree(source, target):
        return "current"
    if not apply:
        return "update-needed"
    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)
    return "updated"


def sync_group(label: str, sources: list[Path], target: Path, apply: bool) -> int:
    changes = 0
    print(f"\n{label}: {target}")
    for source in sources:
        status = copy_skill(source, target, apply)
        changes += status != "current"
        print(f"  {status:13} {source.name}")
    return changes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply updates. Without this option the command performs a dry run.",
    )
    args = parser.parse_args()

    if not CANONICAL.is_dir():
        raise SystemExit(f"Canonical skill folder missing: {CANONICAL}")

    canonical_skills = skill_dirs(CANONICAL)
    cursor_skills = skill_dirs(CURSOR_LIVE)
    changes = 0

    print(f"Canonical skills: {CANONICAL}")
    print(f"Mode: {'apply' if args.apply else 'dry-run'}")
    for label, target in RUNTIME_TARGETS.items():
        changes += sync_group(label, canonical_skills, target, args.apply)
    changes += sync_group("cursor-mirror", cursor_skills, CURSOR_MIRROR, args.apply)

    print(f"\nChanges {'applied' if args.apply else 'needed'}: {changes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
