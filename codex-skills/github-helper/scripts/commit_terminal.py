#!/usr/bin/env python3
"""
Commit terminal-helper to GitHub Terminal repo
"""

import os
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

HOME = Path.home()
TERMINAL_REPO_LOCAL = HOME / "Terminal"
TERMINAL_REPO_URL = "https://github.com/llomj/Terminal.git"


def run_cmd(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout, result.stderr


def commit_terminal():
    print("=== Commit Terminal to GitHub ===\n")

    if not TERMINAL_REPO_LOCAL.exists():
        print("Cloning Terminal repo...")
        code, out, err = run_cmd(f"git clone {TERMINAL_REPO_URL} {TERMINAL_REPO_LOCAL}")
        if code != 0:
            print(f"Error cloning: {err}")
            return

    terminal_helper = HOME / ".codex/skills/terminal-helper"
    if not terminal_helper.exists():
        print("Error: terminal-helper skill not found")
        return

    print(f"Copying terminal-helper to {TERMINAL_REPO_LOCAL}...")
    for item in terminal_helper.iterdir():
        dest = TERMINAL_REPO_LOCAL / item.name
        if dest.exists():
            if dest.is_dir():
                shutil.rmtree(dest)
            else:
                dest.unlink()

        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)
        print(f"  Copied: {item.name}")

    os.chdir(TERMINAL_REPO_LOCAL)

    code, out, err = run_cmd("git status")
    print(out)

    code, out, err = run_cmd("git add .")
    if code != 0:
        print(f"Error adding files: {err}")
        return

    msg = f"Update terminal-helper - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    code, out, err = run_cmd(f'git commit -m "{msg}"')
    if code != 0:
        print("Nothing to commit")
    else:
        print(f"Committed: {msg}")

    code, out, err = run_cmd("git push")
    if code == 0:
        print("✅ Pushed to GitHub!")
    else:
        print(f"Push error: {err}")


if __name__ == "__main__":
    commit_terminal()
