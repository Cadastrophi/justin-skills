#!/usr/bin/env bash
# Install one or more skill packs from Cadastrophi/justin-skills into the
# current repo (default) or globally (--global).
#
# Usage:
#   scripts/install-pack.sh <pack> [<pack>...] [--global] [--yes]
#   scripts/install-pack.sh --list
#
# Requires: node/npx (for `npx skills add`), jq (for reading packs.json).
#
# Examples:
#   scripts/install-pack.sh design
#   scripts/install-pack.sh slides swe --global --yes
#   scripts/install-pack.sh all --global

set -euo pipefail

REPO_SLUG="Cadastrophi/justin-skills"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKS_JSON="$SCRIPT_DIR/../packs.json"

die() { echo "error: $*" >&2; exit 1; }

command -v jq >/dev/null 2>&1 || die "jq is required (brew install jq / apt install jq / winget install jqlang.jq)"
command -v npx >/dev/null 2>&1 || die "npx is required (install Node.js)"

if [[ "${1:-}" == "--list" || "${1:-}" == "-l" ]]; then
  jq -r '.packs | to_entries[] | "\(.key)\t\(.value.title) — \(.value.summary)"' "$PACKS_JSON" | column -ts $'\t'
  exit 0
fi

if [[ $# -eq 0 ]]; then
  echo "Usage: scripts/install-pack.sh <pack> [<pack>...] [--global] [--yes]"
  echo "       scripts/install-pack.sh --list"
  exit 1
fi

PACKS=()
FLAGS=()

for arg in "$@"; do
  case "$arg" in
    --global|-g) FLAGS+=("--global") ;;
    --yes|-y)    FLAGS+=("--yes") ;;
    --*)         FLAGS+=("$arg") ;;
    *)           PACKS+=("$arg") ;;
  esac
done

[[ ${#PACKS[@]} -gt 0 ]] || die "no pack names provided (try --list)"

SKILLS=()
for pack in "${PACKS[@]}"; do
  if [[ "$pack" == "all" ]]; then
    while IFS= read -r s; do SKILLS+=("$s"); done < <(
      find "$SCRIPT_DIR/../skills" -mindepth 2 -maxdepth 2 -type f -name SKILL.md \
        -exec dirname {} \; | xargs -n1 basename | sort
    )
    continue
  fi
  exists=$(jq --arg p "$pack" '.packs[$p]' "$PACKS_JSON")
  [[ "$exists" != "null" ]] || die "unknown pack '$pack' (try --list)"
  while IFS= read -r s; do SKILLS+=("$s"); done < <(
    jq -r --arg p "$pack" '.packs[$p].skills[]' "$PACKS_JSON"
  )
done

# Dedupe
IFS=$'\n' UNIQ=($(printf '%s\n' "${SKILLS[@]}" | awk '!seen[$0]++'))
unset IFS

echo "Installing ${#UNIQ[@]} skills from $REPO_SLUG:"
printf '  - %s\n' "${UNIQ[@]}"
echo ""

npx --yes skills add "$REPO_SLUG" --skill "${UNIQ[@]}" "${FLAGS[@]}"
