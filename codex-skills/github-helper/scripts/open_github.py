#!/usr/bin/env python3
"""
Open GitHub in default browser
"""

import subprocess
import argparse

GITHUB_USER = "llomj"
GITHUB_BASE = "https://github.com"


def open_url(url):
    subprocess.run(["open", url])
    print(f"Opened: {url}")


def main():
    parser = argparse.ArgumentParser(description="Open GitHub")
    parser.add_argument(
        "target", nargs="?", default="home", help="Target: home, profile, or repo name"
    )

    args = parser.parse_args()

    if args.target == "home":
        open_url(GITHUB_BASE)
    elif args.target == "profile":
        open_url(f"{GITHUB_BASE}/{GITHUB_USER}")
    else:
        open_url(f"{GITHUB_BASE}/{GITHUB_USER}/{args.target}")


if __name__ == "__main__":
    main()
