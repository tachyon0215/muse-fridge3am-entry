#!/usr/bin/env python3
"""Entry program for the make.fun contest 'The 3AM Fridge Text'.

Three candidate texts were drafted and scored against the judge brief.
The brief rewards a fresh angle over the obvious milk, ice and door jokes,
in the voice of a machine with an opinion and no shame. The selected draft
has the fridge talk its owner out of a snack, and the punchline is the
fridge describing itself as literally full of snacks. This program emits
that single line.
"""

import os
import sys

ENTRY_TEXT = "You don't need me. You need sleep and a glass of water. I say this as someone who is literally full of snacks."
CHAR_LIMIT = 140


def check_text(text):
    if not text or not text.strip():
        raise ValueError("entry text is empty")
    if len(text) > CHAR_LIMIT:
        raise ValueError("entry text exceeds the character limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    return text


def emit(text, directory):
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return target


def run():
    # Validate first, so a malformed entry never reaches the output file.
    text = check_text(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    emit(text, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(run())
