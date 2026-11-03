"""Optimize a knitout file with KODA.

Usage: python3 koda_cli.py infile.k outfile.k

With the versions pinned in requirements.txt, the input must not use negative
needle indices, `x-` extension lines, or drops.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from koda_knitout import koda_optimizer  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Optimize a knitout file with KODA.")
    parser.add_argument("infile", help="knitout file to optimize")
    parser.add_argument("outfile", help="path to write the optimized knitout to")
    args = parser.parse_args()
    try:
        koda_optimizer.optimize_knitout_file(args.infile, args.outfile, visualize=False)
    except Exception as e:
        message = f"{type(e).__name__}: {e}".splitlines()[0]
        print(f"koda_cli: {message}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
