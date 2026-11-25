#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. The rant is capped at 400 characters by the
competition gate, so the punch has to come fast.

Rant angle: the "Resealable" shredded-cheese bag whose tear notch
always rips diagonally through the zipper track. First-person voice,
one concrete detail, twist at the end. Written fresh for this entry.
"""

import os

RANT = (
    "The person who prints 'Resealable' on shredded cheese bags is running "
    "a psychological operation on me. I pull the little tear notch and it rips "
    "diagonally straight through the zipper track, every single time, like the "
    "bag was designed by someone who personally hates me. Now half my fridge "
    "is limp mozzarella pouches held shut by binder clips and prayers."
)


def main() -> None:
    text = RANT
    assert 1 <= len(text) <= 400, f"rant must be 1-400 chars, got {len(text)}"
    assert text.strip(), "rant must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Small log line so a test run shows the gate-relevant size at a glance.
    print(f"wrote /output/entry.txt: {len(text)} chars, {len(text.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
