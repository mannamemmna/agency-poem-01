"""Write the poem as deterministic UTF-8; Python standard library only."""

import os
from pathlib import Path

POEM = """His words

After the stroke, my father points
at letters on a board. I type
an email to his brother.
They have not spoken in eleven years.

The screen offers: I forgive you.
He taps the wooden frame. No.

We start again. The kettle clicks
and cools. He makes me read each word
back to him. At sorry, he shakes his head.

At last: I miss you.

I move the mouse toward Send.
His good hand closes over mine.
I wait.

He adds: Bring the red chess set.
Then lifts his hand."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
