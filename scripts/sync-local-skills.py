#!/usr/bin/env python3
"""Sync selected skill packs from this checkout into one shared local copy.

Preview is the default. Re-run after ``git pull`` on each device.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import uuid
from pathlib import Path


def tree_hash(directory: Path) -> str:
    digest = hashlib.sha256()
    for file in sorted(p for p in directory.rglob("*") if p.is_file()):
        digest.update(str(file.relative_to(directory)).replace("\\", "/").encode())
        digest.update(hashlib.sha256(file.read_bytes()).digest())
    return digest.hexdigest()


def is_link(path: Path) -> bool:
    return path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction())


def exists(path: Path) -> bool:
    return path.exists() or is_link(path)


def same_link(path: Path, target: Path) -> bool:
    return is_link(path) and path.resolve() == target.resolve()


def make_directory_link(path: Path, target: Path) -> None:
    """Use a junction on Windows so Claude can follow it without developer mode."""
    if os.name == "nt":
        environment = os.environ.copy()
        environment["JUSTIN_SKILLS_LINK_PATH"] = str(path)
        environment["JUSTIN_SKILLS_LINK_TARGET"] = str(target)
        subprocess.run(
            [
                "powershell", "-NoProfile", "-NonInteractive", "-Command",
                "$ErrorActionPreference = 'Stop'; "
                "New-Item -ItemType Junction -Path $env:JUSTIN_SKILLS_LINK_PATH "
                "-Target $env:JUSTIN_SKILLS_LINK_TARGET | Out-Null",
            ],
            env=environment,
            check=True,
        )
    else:
        path.symlink_to(target, target_is_directory=True)


def backup_path(home: Path, target: str, name: str) -> Path:
    return home / ".justin-skills" / "backups" / target / f"{name}-{uuid.uuid4().hex[:8]}"


def discovered_elsewhere(home: Path) -> dict[str, list[Path]]:
    """Find skill folders outside the canonical top-level shared directory."""
    found: dict[str, list[Path]] = {}
    for root in (home / ".agents" / "skills", home / ".codex" / "skills"):
        if not root.is_dir():
            continue
        for skill_file in root.rglob("SKILL.md"):
            folder = skill_file.parent
            if folder == root / folder.name and root.name == "skills" and root.parent.name == ".agents":
                continue
            found.setdefault(folder.name, []).append(folder)
    return found


def sync_shared(source: Path, destination: Path, other_paths: dict[str, list[Path]], managed: dict,
                home: Path, name: str, apply: bool) -> tuple[str, bool]:
    source_hash = tree_hash(source)
    key = f"agents/{name}"
    if exists(destination):
        if is_link(destination):
            return "CONFLICT (shared path is a link)", True
        dest_hash = tree_hash(destination) if destination.is_dir() else None
        if dest_hash == source_hash:
            if apply:
                managed[key] = source_hash
            return "current", False
        if managed.get(key) != dest_hash:
            return "CONFLICT (local content differs)", True
        if not apply:
            return "would update managed copy", False
        backup = backup_path(home, "agents", name)
        backup.parent.mkdir(parents=True, exist_ok=True)
        staged = destination.parent / f".justin-skills-stage-{uuid.uuid4().hex}"
        shutil.copytree(source, staged)
        destination.replace(backup)
        try:
            staged.replace(destination)
        except Exception:
            backup.replace(destination)
            raise
        managed[key] = source_hash
        return f"updated (backup: {backup})", False
    if name in other_paths:
        return f"CONFLICT (same skill already at {other_paths[name][0]})", True
    if not apply:
        return "would copy", False
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    managed[key] = source_hash
    return "copied", False


def sync_link(shared: Path, destination: Path, home: Path, target: str,
              name: str, apply: bool) -> tuple[str, bool]:
    if same_link(destination, shared):
        return "linked", False
    if exists(destination):
        if is_link(destination) or not destination.is_dir():
            return "CONFLICT (different link or file exists)", True
        if tree_hash(destination) != tree_hash(shared):
            return "CONFLICT (local content differs)", True
        if not apply:
            return "would link identical copy", False
        backup = backup_path(home, target, name)
        backup.parent.mkdir(parents=True, exist_ok=True)
        destination.replace(backup)
        try:
            make_directory_link(destination, shared)
        except Exception:
            backup.replace(destination)
            raise
        return f"linked (old copy: {backup})", False
    if not apply:
        return "would link", False
    destination.parent.mkdir(parents=True, exist_ok=True)
    make_directory_link(destination, shared)
    return "linked", False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packs", nargs="+", help="Pack names from packs.json")
    parser.add_argument("--target", choices=("agents", "claude", "antigravity"), action="append")
    parser.add_argument("--apply", action="store_true", help="Apply the previewed copies, updates, and links")
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
    other_paths = discovered_elsewhere(home)
    targets = set(args.target or ["agents", "claude"])
    # Every requested agent reads the one shared installation. Other roots link to it.
    targets.add("agents")
    conflicts = 0
    for name in sorted(names):
        source = args.repo / "skills" / name
        if not (source / "SKILL.md").is_file():
            parser.error(f"missing source skill: {source}")
        shared = destinations["agents"] / name
        state, conflict = sync_shared(source, shared, other_paths,
                                      managed, home, name, args.apply)
        print(f"{'agents':11} {name:32} {state}")
        conflicts += conflict
        if conflict:
            continue
        for target in ("claude", "antigravity"):
            if target not in targets:
                continue
            # In preview, a missing shared copy is represented by its source.
            link_source = shared if shared.exists() else source
            state, conflict = sync_link(link_source, destinations[target] / name,
                                        home, target, name, args.apply)
            print(f"{target:11} {name:32} {state}")
            conflicts += conflict
    if args.apply:
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state_file.write_text(json.dumps(managed, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if conflicts:
        print(f"{conflicts} existing skill paths need review; nothing at those paths was replaced.")
    return 2 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
