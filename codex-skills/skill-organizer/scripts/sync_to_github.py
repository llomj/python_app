#!/usr/bin/env python3
"""Mirror user-authored Codex skills to Git and push the resulting commit."""

from __future__ import annotations

import argparse
import filecmp
import fcntl
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


SOURCE = Path("/Users/moll/.codex/skills")
REPO = Path("/Users/moll/.codex/github-sync/python_app")
DESTINATION = REPO / "codex-skills"
EXPECTED_REMOTE = "https://github.com/llomj/python_app.git"
LOCK_FILE = Path("/tmp/com.user.skill-sync.lock")
EXCLUDED_SKILLS = {".system", "user-codex-skills"}
IGNORED_NAMES = {".DS_Store", "__pycache__"}
SECRET_PATTERNS = {
    "GitHub token": re.compile(rb"(?:ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})"),
    "OpenAI API key": re.compile(rb"sk-[A-Za-z0-9_-]{20,}"),
    "AWS access key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "private key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def run_git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["/usr/bin/git", "-C", str(REPO), *args],
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def skill_directories() -> list[Path]:
    return sorted(
        path
        for path in SOURCE.iterdir()
        if path.name not in EXCLUDED_SKILLS
        and path.is_dir()
        and not path.is_symlink()
        and (path / "SKILL.md").is_file()
    )


def ignored(_directory: str, names: list[str]) -> set[str]:
    return {
        name
        for name in names
        if name in IGNORED_NAMES or name.endswith((".pyc", ".pyo"))
    }


def scan_for_secrets(skills: list[Path]) -> list[str]:
    findings: list[str] = []
    for skill in skills:
        for path in skill.rglob("*"):
            if not path.is_file() or path.is_symlink() or path.stat().st_size > 5_000_000:
                continue
            data = path.read_bytes()
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(data):
                    findings.append(f"{label}: {path}")
    return findings


def same_tree(left: Path, right: Path) -> bool:
    if not left.is_dir() or not right.is_dir():
        return False
    comparison = filecmp.dircmp(left, right, ignore=list(IGNORED_NAMES))
    if comparison.left_only or comparison.right_only or comparison.diff_files or comparison.funny_files:
        return False
    return all(same_tree(left / name, right / name) for name in comparison.common_dirs)


def build_snapshot(skills: list[Path], root: Path) -> None:
    for skill in skills:
        shutil.copytree(skill, root / skill.name, symlinks=True, ignore=ignored)


def replace_mirror(snapshot: Path) -> None:
    DESTINATION.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["/usr/bin/rsync", "-a", "--delete", f"{snapshot}/", f"{DESTINATION}/"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "rsync failed")


def verify_repository() -> None:
    if not (REPO / ".git").is_dir():
        REPO.parent.mkdir(parents=True, exist_ok=True)
        cloned = subprocess.run(
            [
                "/usr/bin/git",
                "clone",
                "--depth",
                "1",
                "--branch",
                "main",
                "--single-branch",
                EXPECTED_REMOTE,
                str(REPO),
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if cloned.returncode:
            raise RuntimeError(f"Could not create automation checkout: {cloned.stderr.strip()}")
    if not (REPO / ".git").is_dir():
        raise RuntimeError(f"Git repository not found: {REPO}")
    remote = run_git("remote", "get-url", "origin").stdout.strip()
    if remote.removesuffix(".git") != EXPECTED_REMOTE.removesuffix(".git"):
        raise RuntimeError(f"Unexpected origin remote: {remote}")
    branch = run_git("branch", "--show-current").stdout.strip()
    if branch != "main":
        raise RuntimeError(f"Expected main branch, found: {branch or 'detached HEAD'}")


def fetch_and_check_divergence() -> int:
    fetched = run_git("fetch", "origin", check=False)
    if fetched.returncode:
        raise RuntimeError(f"Could not fetch origin: {fetched.stderr.strip()}")
    counts = run_git("rev-list", "--left-right", "--count", "HEAD...origin/main").stdout.split()
    ahead, behind = (int(value) for value in counts)
    if ahead and behind:
        raise RuntimeError("automation checkout and origin/main have diverged")
    if behind:
        run_git("merge", "--ff-only", "origin/main")
    if ahead:
        subjects = run_git("log", "--format=%s", "origin/main..HEAD").stdout.splitlines()
        if any(not subject.startswith("chore(skills): automated sync") for subject in subjects):
            raise RuntimeError("local main has non-automation commits; refusing to push them automatically")
    return ahead


def commit_and_push(push: bool) -> str:
    run_git("add", "--all", "--", "codex-skills")
    changed = run_git("diff", "--cached", "--quiet", "--", "codex-skills", check=False)
    if changed.returncode not in (0, 1):
        raise RuntimeError(changed.stderr.strip() or "Could not inspect staged skill changes")
    if changed.returncode == 1:
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        run_git("commit", "-m", f"chore(skills): automated sync {stamp}", "--", "codex-skills")
    if not push:
        return "committed locally" if changed.returncode == 1 else "already current locally"
    ahead = int(run_git("rev-list", "--count", "origin/main..HEAD").stdout.strip())
    if ahead:
        pushed = run_git("push", "origin", "HEAD:main", check=False)
        if pushed.returncode:
            raise RuntimeError(f"Push failed: {pushed.stderr.strip()}")
        return f"pushed {ahead} commit(s)"
    return "GitHub already current"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Report whether the mirror differs")
    parser.add_argument("--no-push", action="store_true", help="Commit locally without pushing")
    args = parser.parse_args()

    LOCK_FILE.touch(exist_ok=True)
    with LOCK_FILE.open("r+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Another skill sync is already running")
            return 0

        verify_repository()
        skills = skill_directories()
        if not skills:
            raise RuntimeError(f"No user-authored skills found in {SOURCE}")
        findings = scan_for_secrets(skills)
        if findings:
            raise RuntimeError("Potential secrets found; sync stopped:\n" + "\n".join(findings))

        if not args.dry_run:
            fetch_and_check_divergence()

        with tempfile.TemporaryDirectory(prefix="codex-skill-sync-") as temp:
            snapshot = Path(temp)
            build_snapshot(skills, snapshot)
            current = same_tree(snapshot, DESTINATION)
            if args.dry_run:
                print(f"Skills found: {len(skills)}")
                print("Mirror status: current" if current else "Mirror status: update needed")
                return 0 if current else 1
            if not current:
                replace_mirror(snapshot)
            result = commit_and_push(not args.no_push)

        print(f"Skills mirrored: {len(skills)}")
        print(f"Repository result: {result}")
        return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"Skill sync failed: {error}", file=sys.stderr)
        raise SystemExit(1)
