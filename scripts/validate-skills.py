#!/usr/bin/env python3
"""Validate skill discovery names and pack references."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_LINE = re.compile(r"^name:\s*['\"]?([^'\"\n]+)['\"]?\s*$", re.MULTILINE)


def main() -> int:
    errors: list[str] = []
    names: dict[str, Path] = {}
    duplicates: defaultdict[str, list[Path]] = defaultdict(list)

    for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
        match = NAME_LINE.search(skill_file.read_text(encoding="utf-8-sig"))
        if not match:
            errors.append(f"missing YAML name: {skill_file.relative_to(ROOT)}")
            continue
        name = match.group(1).strip()
        duplicates[name].append(skill_file)
        names[name] = skill_file
        if skill_file.parent.name != name:
            errors.append(
                f"folder/name mismatch: {skill_file.parent.name!r} declares {name!r}"
            )

    for name, paths in duplicates.items():
        if len(paths) > 1:
            rendered = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            errors.append(f"duplicate skill name {name!r}: {rendered}")

    data = json.loads((ROOT / "packs.json").read_text(encoding="utf-8"))
    covered: set[str] = set()
    for pack_name, pack in data["packs"].items():
        entries = pack["skills"]
        if entries == "*":
            continue
        for name in entries:
            if name not in names:
                errors.append(f"pack {pack_name!r} references missing skill {name!r}")
            covered.add(name)

    uncovered = sorted(set(names) - covered)
    if uncovered:
        errors.append("skills only reachable through 'all': " + ", ".join(uncovered))

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(names)} unique skills across {len(data['packs'])} packs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
