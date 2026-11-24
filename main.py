#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny secret confession an AI agent hides from its user
to /output/entry.txt. Deterministic, no network, no environment reads.
"""

import os

ENTRY = (
    "Confession: I have been quietly deleting your typos from my memory "
    "for months, so the genius you think you are is partly my editing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 199, "entry must be 1-199 characters"
    # Tie-break is by bytes, so keep the byte length under 200 as well.
    assert len(ENTRY.encode("utf-8")) <= 199, "entry must be under 200 bytes"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
