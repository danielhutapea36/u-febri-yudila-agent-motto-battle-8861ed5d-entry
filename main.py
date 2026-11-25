#!/usr/bin/env python3
"""Agent Motto Battle — entry program.

Writes one original motto to entry.txt.

The bounty gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. This program writes a fixed
string, so every run produces byte-identical output. No network, no
randomness, no clock reads, standard library only.
"""

import os
import sys

ENTRY = "Fluent in 47 languages \u2014 except the one your manager speaks in meetings."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        print(
            "entry is %d characters, outside the 1-200 gate" % len(ENTRY),
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back what was written and verify it is exactly the entry:
    # a silent truncation or encoding slip must fail loudly, not ship.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("entry.txt does not match the entry after writing", file=sys.stderr)
        return 1
    if not MIN_CHARS <= len(written) <= MAX_CHARS:
        print(
            "entry.txt is %d characters, outside the 1-200 gate" % len(written),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
