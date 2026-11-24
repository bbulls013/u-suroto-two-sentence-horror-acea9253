#!/usr/bin/env python3
"""Two-Sentence Horror — u-suroto-two-sentence-horror-acea9253.

Writes one original two-sentence horror story to /output/entry.txt
(or to the path given as the first argument).

The story is a fixed string: no randomness, no input, no network.
Running this program twice produces byte-identical output.
"""

import sys

STORY = (
    "The new tenant in 4B leaves a single shoe outside his door every "
    "morning \u2014 always the left one, always spotless. "
    "This morning there were two, and the right one was mine."
)

MAX_CHARS = 400


def count_sentences(text):
    """Count sentences by terminal punctuation (. ! ?)."""
    return sum(1 for ch in text if ch in ".!?")


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"

    text = STORY

    # Gate checks, mirroring the competition's own gate.
    assert text.strip(), "story must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"story is {len(text)} characters, must be 1-400"
    )
    assert count_sentences(text) == 2, (
        f"story has {count_sentences(text)} sentences, must be exactly 2"
    )

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    print(f"wrote {len(text)} characters, 2 sentences -> {out_path}")


if __name__ == "__main__":
    main()
