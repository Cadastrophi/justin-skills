#!/usr/bin/env python3
"""Compare a justin-skills checkout with local agent skill directories.

Read-only. Prints a JSON inventory suitable for reviewing before a sync.
"""

import argparse
import hashlib
import json
from pathlib import Path


def skills_at(root: Path) -> dict[str, dict[str, str]]:
    if not root.is_dir():
        return {}
    found = {}
    for directory in sorted(root.iterdir()):
        skill_file = directory / "SKILL.md"
        if not directory.is_dir() or not skill_file.is_file():
            continue
        tree_hash = hashlib.sha256()
        for file in sorted(p for p in directory.rglob("*") if p.is_file()):
            tree_hash.update(str(file.relative_to(directory)).replace("\\", "/").encode())
            tree_hash.update(hashlib.sha256(file.read_bytes()).digest())
        found[directory.name] = {
            "path": str(directory),
            "sha256": hashlib.sha256(skill_file.read_bytes()).hexdigest(),
            "tree_sha256": tree_hash.hexdigest(),
            "link": directory.is_symlink() or (hasattr(directory, "is_junction") and directory.is_junction()),
        }
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--root", action="append", nargs=2, metavar=("NAME", "PATH"))
    args = parser.parse_args()

    home = Path.home()
    roots = args.root or [
        ("codex", str(home / ".codex" / "skills")),
        ("agents", str(home / ".agents" / "skills")),
        ("claude", str(home / ".claude" / "skills")),
        ("antigravity", str(home / ".gemini" / "config" / "skills")),
    ]
    catalogs = {"repo": skills_at(args.repo / "skills")}
    catalogs.update({name: skills_at(Path(path)) for name, path in roots})
    names = sorted(set().union(*(set(c) for c in catalogs.values())))
    overlap = []
    for name in names:
        present = {source: catalog[name]["sha256"] for source, catalog in catalogs.items() if name in catalog}
        if len(present) > 1:
            overlap.append({"name": name, "copies": list(present), "identical": len(set(present.values())) == 1})

    report = {
        "roots": {name: {"path": str(args.repo / "skills") if name == "repo" else dict(roots)[name], "count": len(catalog)} for name, catalog in catalogs.items()},
        "overlap": overlap,
        "repo_missing_locally": [name for name in catalogs["repo"] if not any(name in catalogs[r] for r in catalogs if r != "repo")],
        "local_missing_from_repo": [name for name in names if name not in catalogs["repo"]],
        "entries": {name: {source: catalog[name] for source, catalog in catalogs.items() if name in catalog} for name in names},
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
