#!/usr/bin/env python3
"""Install selected repo packs into agent skill folders without overwriting files.

Preview is the default. Re-run after pulling the repo on each device.
"""

import argparse
import hashlib
import json
import shutil
import uuid
from pathlib import Path


def tree_hash(directory: Path) -> str:
    digest = hashlib.sha256()
    for file in sorted(p for p in directory.rglob("*") if p.is_file()):
        digest.update(str(file.relative_to(directory)).replace("\\", "/").encode())
        digest.update(hashlib.sha256(file.read_bytes()).digest())
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packs", nargs="+", help="Pack names from packs.json")
    parser.add_argument("--target", choices=("agents", "claude", "antigravity"), action="append")
    parser.add_argument("--apply", action="store_true", help="Copy missing skills (never overwrite)")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--home", type=Path, default=Path.home(), help="Home directory containing agent configs")
    args = parser.parse_args()

    data = json.loads((args.repo / "packs.json").read_text(encoding="utf-8"))["packs"]
    names = set()
    for pack_name in args.packs:
        if pack_name not in data:
            parser.error(f"unknown pack: {pack_name}")
        entries = data[pack_name]["skills"]
        if entries == "*":
            names.update(p.parent.name for p in (args.repo / "skills").glob("*/SKILL.md"))
        else:
            names.update(entries)

    home = args.home
    destinations = {
        "agents": home / ".agents" / "skills",
        "claude": home / ".claude" / "skills",
        "antigravity": home / ".gemini" / "config" / "skills",
    }
    state_file = home / ".justin-skills" / "managed.json"
    managed = json.loads(state_file.read_text(encoding="utf-8")) if state_file.is_file() else {}
    targets = args.target or ["agents", "claude"]
    conflicts = 0
    for target in targets:
        root = destinations[target]
        for name in sorted(names):
            source = args.repo / "skills" / name
            destination = root / name
            if not (source / "SKILL.md").is_file():
                parser.error(f"missing source skill: {source}")
            source_hash = tree_hash(source)
            key = f"{target}/{name}"
            if destination.exists() or destination.is_symlink():
                dest_hash = tree_hash(destination) if destination.is_dir() else None
                if dest_hash == source_hash:
                    state = "current"
                    if args.apply and not destination.is_symlink():
                        managed[key] = source_hash
                elif managed.get(key) == dest_hash and not destination.is_symlink():
                    if args.apply:
                        backup = home / ".justin-skills" / "backups" / target / f"{name}-{uuid.uuid4().hex[:8]}"
                        backup.parent.mkdir(parents=True, exist_ok=True)
                        staged = root / f".justin-skills-stage-{uuid.uuid4().hex}"
                        shutil.copytree(source, staged)
                        destination.replace(backup)
                        try:
                            staged.replace(destination)
                        except Exception:
                            backup.replace(destination)
                            raise
                        managed[key] = source_hash
                        state = f"updated (backup: {backup})"
                    else:
                        state = "would update managed copy"
                else:
                    state = "CONFLICT"
                    conflicts += 1
            elif args.apply:
                root.mkdir(parents=True, exist_ok=True)
                shutil.copytree(source, destination)
                managed[key] = source_hash
                state = "copied"
            else:
                state = "would copy"
            print(f"{target:11} {name:32} {state}")
    if args.apply:
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state_file.write_text(json.dumps(managed, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if conflicts:
        print(f"{conflicts} existing directories differ; review them before replacing anything.")
    return 2 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
