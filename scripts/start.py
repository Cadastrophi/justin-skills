#!/usr/bin/env python3
"""Pull this checkout and sync selected skills into the shared agent folder."""

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packs", nargs="*", default=["all"],
                        help="Packs to sync (default: all repo skills)")
    parser.add_argument("--preview", action="store_true", help="Pull and show planned changes only")
    parser.add_argument("--antigravity", action="store_true",
                        help="Also link Antigravity when it does not already scan .agents/skills")
    parser.add_argument("--home", type=Path, help="Agent configuration home (mainly for testing)")
    parser.add_argument("--no-pull", action="store_true",
                        help="Use the current checkout when offline")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    if not args.no_pull:
        pull = subprocess.run(["git", "-C", str(repo), "pull", "--ff-only"], check=False)
        if pull.returncode:
            print("Git pull failed; no skills were changed.", file=sys.stderr)
            return pull.returncode

    command = [sys.executable, str(repo / "scripts" / "sync-local-skills.py"),
               *args.packs, "--repo", str(repo)]
    if not args.preview:
        command.append("--apply")
    if args.antigravity:
        command.extend(["--target", "agents", "--target", "claude",
                        "--target", "antigravity"])
    if args.home:
        command.extend(["--home", str(args.home)])
    print(f"Syncing packs: {', '.join(args.packs)}", flush=True)
    return subprocess.run(command, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
