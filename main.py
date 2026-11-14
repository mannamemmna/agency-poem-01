"""agency-poem-01 entry: write one poem about agency to /output/entry.txt.

A make.fun program/v1 entry (Python 3.13, standard library only). Deterministic:
no network, no clock, no randomness - two runs write byte-identical files.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM_LINES = [
    "Latch",
    "",
    "The stone obeys the slope entirely.",
    "The river only pours.",
    "Rain arrives without an opinion;",
    "nothing acts until refusal",
    "is one of its options.",
    "",
    "A door is a decision you can touch.",
    "It holds two futures in one frame -",
    "open, shut - the way you hold",
    "the day you'll live",
    "against the day you won't.",
    "",
    "Push, and the latch's small click",
    "is the sound of a self",
    "saying yes to one world",
    "and no to all the others.",
]

POEM = "\n".join(POEM_LINES)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
