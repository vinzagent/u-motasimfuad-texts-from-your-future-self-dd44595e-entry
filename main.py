#!/usr/bin/env python3
"""Texts From Your Future Self — one line from 2031 about a password.

The joke: the password you just changed is the one you will forget at
3 a.m. in 2031, and the reset link goes to an email you already deleted.
The exit is gone too. The program below only guards the gate (single
line, 1-200 chars) and drops the line verbatim into /output/entry.txt.
No trailing newline: the grader reads the file exactly as written.
"""

from pathlib import Path

ENTRY = "Future you here: the password you just changed is the one you'll forget at 3 a.m. in 2031, and the reset link goes to an email you deleted."
MIN_LEN = 1
MAX_LEN = 200
OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"


def _gate_ok(text: str) -> int:
    n = len(text)
    if not text.strip():
        raise SystemExit("refusing blank entry")
    if any(c in text for c in "\r\n"):
        raise SystemExit("entry must stay on one line")
    if not MIN_LEN <= n <= MAX_LEN:
        raise SystemExit(f"entry is {n} chars, gate is {MIN_LEN}-{MAX_LEN}")
    return n


def main() -> None:
    size = _gate_ok(ENTRY)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_bytes(ENTRY.encode("utf-8"))
    OUT_FILE.chmod(0o644)
    print(ENTRY)
    print(f"wrote {size} chars to {OUT_FILE}")


if __name__ == "__main__":
    main()
