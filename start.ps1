#!/usr/bin/env pwsh
# From PowerShell: .\start.ps1 [pack ...] [-Preview]
$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $repoRoot "scripts/start.py") @args
exit $LASTEXITCODE
