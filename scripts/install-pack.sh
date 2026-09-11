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

# Resolve packs → skill list (union, deduped). '*' means all.
SKILLS_JSON=$(jq --argjson names "$(printf '%s\n' "${PACKS[@]}" | jq -R . | jq -s .)" '
  ($names | map(. as $n |
    (.packs // {})[$n] // ($packs_root.packs[$n]) // null
  )) as $_ |
  reduce ($names[]) as $n ([];
    . + (if $n == "all" then
           [.packs // {} | to_entries[].value.skills] | flatten
         else
           (.packs[$n] // (error("unknown pack: " + $n))).skills
         end)
  ) | unique
' "$PACKS_JSON" 2>/dev/null || true)

# Simpler resolver: shell out per pack, concatenate.
SKILLS=()
for pack in "${PACKS[@]}"; do
  if [[ "$pack" == "all" ]]; then
    while IFS= read -r s; do SKILLS+=("$s"); done < <(
      jq -r '[.packs | to_entries[] | .value.skills] | flatten | unique[]?' "$PACKS_JSON"
    )
    # 'all' also means every skill dir on disk; use the flat union as canonical.
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
