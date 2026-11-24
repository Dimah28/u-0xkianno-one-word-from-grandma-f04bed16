#!/usr/bin/env python3
"""One Word From Grandma (make.fun bounty u-0xkianno-one-word-from-grandma-f04bed16).

Writes exactly one word to /output/entry.txt: the word a grandma would
text about AI.

The word is "robit": her warm, baffled typo for "robot" -- the way a
grandma actually types it to a grandchild. One word, instantly readable,
tied to robots/machines, funny without any caption or context, and fresh
because it is her misspelling, not the obvious correct word.

Deterministic: the word is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

WORD = "robit"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(word: str) -> None:
    """Enforce the competition's gate before writing: exactly one word,
    1-30 characters, not only white space. Fail loudly instead of
    writing an entry the gate would refuse."""
    if not 1 <= len(word) <= 30:
        raise SystemExit(f"word is {len(word)} characters, must be 1-30")
    if not any(not ch.isspace() for ch in word):
        raise SystemExit("word must contain a non-whitespace character")
    if len(word.split()) != 1:
        raise SystemExit(f"word must be exactly one word, got: {word!r}")
    if not word.isalpha():
        raise SystemExit(f"word must be letters only, got: {word!r}")


def main() -> None:
    validate(WORD)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the word: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(WORD, encoding="utf-8")
    # Read-back verification: the file on disk must contain exactly the
    # word, byte for byte. Fail loudly instead of shipping a bad entry.
    written = output_path.read_text(encoding="utf-8")
    if written != WORD:
        raise SystemExit(f"read-back mismatch: wrote {WORD!r}, file has {written!r}")


if __name__ == "__main__":
    main()
