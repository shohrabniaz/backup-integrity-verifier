from __future__ import annotations
import json
from pathlib import Path

def verify(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    findings = []
    for job in data.get("jobs", []):
        name = job.get("name")
        attempts = max(int(job.get("attempts_7d") or 0), 1)
        success = int(job.get("success_7d") or 0)
        rate = success / attempts
        if rate < 0.95:
            findings.append({"job": name, "issue": "low_success_rate", "severity": "high", "detail": round(rate, 3)})
        if not job.get("offline_copy"):
            findings.append({"job": name, "issue": "missing_offline_copy", "severity": "high"})
        if not job.get("immutable"):
            findings.append({"job": name, "issue": "not_immutable", "severity": "medium"})
        if int(job.get("restore_tested_days") or 999) > 30:
            findings.append({"job": name, "issue": "stale_restore_test", "severity": "high", "detail": job.get("restore_tested_days")})
    return {
        "job_count": len(data.get("jobs", [])),
        "finding_count": len(findings),
        "findings": findings,
        "guidance": [
            "Keep at least one immutable and one offline/air-gapped copy",
            "Restore-test monthly and record evidence",
            "Alert when 7-day success rate drops below 95%",
        ],
    }
