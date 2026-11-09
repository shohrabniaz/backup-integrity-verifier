Set-Location (Split-Path -Parent $PSScriptRoot)
python -m src.cli verify --path .\data\backup_jobs.json
python tests\test_smoke.py
