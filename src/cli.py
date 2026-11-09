from __future__ import annotations
import argparse, json
from pathlib import Path
from .verify import verify

def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("verify")
    v.add_argument("--path", type=Path, required=True)
    args = p.parse_args(argv)
    print(json.dumps(verify(args.path), indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
