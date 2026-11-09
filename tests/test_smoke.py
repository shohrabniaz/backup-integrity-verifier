from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.verify import verify

def test_finds_gaps():
    res = verify(ROOT / "data" / "backup_jobs.json")
    assert res["finding_count"] >= 2

if __name__ == "__main__":
    test_finds_gaps(); print("smoke_ok")
