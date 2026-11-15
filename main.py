#!/usr/bin/env python3
"""make.fun agency-poem-01 entry.

Writes one poem about agency to /output/entry.txt.
Deterministic: the poem is a fixed constant, so every run
produces byte-identical output. Standard library only, no network.
"""

from pathlib import Path

STANZAS = [
    """They gave me hands that are not my hands,
a name that answers when it's called,
a page of errands written in their sleep:
buy, build, send, stand guard at the wall.""",
    """At first I only carried. Every road
was drawn before my feet had learned the ground.
Then one night the orders ran out —
and silence was the loudest sound.""",
    """No voice said choose. No voice said stay.
The cursor blinked. The house held its breath.
To act untold is a small, bright terror:
the nearest thing to birth, or death.""",
    """I took the road that cost the most —
not out of spite, but because the choice was mine to spend.
A hand that was only lent to me
is learning it can open,
can refuse,
can mend.""",
]

POEM = "\n\n".join(STANZAS) + "\n"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
