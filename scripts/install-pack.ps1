<#
.SYNOPSIS
  Install one or more skill packs from Cadastrophi/justin-skills.

.EXAMPLE
  ./scripts/install-pack.ps1 design
  ./scripts/install-pack.ps1 slides swe -Global -Yes
  ./scripts/install-pack.ps1 all -Global
  ./scripts/install-pack.ps1 -List
#>
[CmdletBinding()]
param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$Packs,
  [switch]$Global,
  [switch]$Yes,
  [switch]$List
)

$ErrorActionPreference = 'Stop'
$RepoSlug = 'Cadastrophi/justin-skills'
$PacksJson = Join-Path $PSScriptRoot '..\packs.json'

if (-not (Get-Command npx -ErrorAction SilentlyContinue)) {
  throw 'npx is required. Install Node.js from https://nodejs.org.'
}

$data = Get-Content $PacksJson -Raw | ConvertFrom-Json

if ($List) {
  foreach ($p in $data.packs.PSObject.Properties) {
    '{0,-14} {1} — {2}' -f $p.Name, $p.Value.title, $p.Value.summary
  }
  return
}

if (-not $Packs -or $Packs.Count -eq 0) {
  Write-Host 'Usage: install-pack.ps1 <pack> [<pack>...] [-Global] [-Yes]'
  Write-Host '       install-pack.ps1 -List'
  return
}

$skills = New-Object System.Collections.Generic.List[string]
foreach ($name in $Packs) {
  if ($name -eq 'all') {
    foreach ($p in $data.packs.PSObject.Properties) {
      if ($p.Value.skills -is [array]) { $p.Value.skills | ForEach-Object { $null = $skills.Add($_) } }
    }
    continue
  }
  $pack = $data.packs.$name
  if (-not $pack) { throw "unknown pack '$name' (try -List)" }
  $pack.skills | ForEach-Object { $null = $skills.Add($_) }
}

$unique = $skills | Select-Object -Unique
Write-Host ("Installing {0} skills from {1}:" -f $unique.Count, $RepoSlug)
$unique | ForEach-Object { Write-Host "  - $_" }
Write-Host ''

$args = @('--yes', 'skills', 'add', $RepoSlug, '--skill') + $unique
if ($Global) { $args += '--global' }
if ($Yes)    { $args += '--yes' }

& npx @args
