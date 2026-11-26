#!/usr/bin/env python3
"""Robot Band name entry for make.fun bounty u-motasimfuad-name-the-robot-band-1ffc6a74.

Writes one funny robot band name plus a few words on its hit song
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

ENTRY = "The Roomba Stones — hit single 'I Can't Get No (Battery) Satisfaction', recorded live from the charging dock."


def validate(text: str) -> None:
    """Gate: 1-200 UTF-8 characters, single line, not whitespace-only."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    text.encode("utf-8")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
