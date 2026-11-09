# Backup integrity verifier

**Author:** Md Shohrab Hossen Niaz

Verify backup job exports for 3-2-1 coverage signals: success rate, offline/immutable copy, and restore-test evidence.

```powershell
python -m src.cli verify --path .\data\backup_jobs.json
```
