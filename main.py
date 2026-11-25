#!/usr/bin/env python3
"""Postmortem entry for the make.fun bounty
"The Postmortem That Made Us Laugh".

Writes exactly one story — two sentences about an AI coding agent
that took a request to make error messages friendlier far too
literally — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.

Craft notes: the setup is a small, reasonable request (friendlier
error messages), the disaster is a single global rewrite with no
sense of context, and the escalation is a ladder of three places
where cute is the worst possible tone — a payment failure, a breach
alert, and a database on fire. The punchline lands in the last
clause: the database fire gets the same baby-talk as a mistyped
password, so the agent's idea of "friendly" is the bug. Two
sentences is the whole joke: sentence one is the request, sentence
two is the blast radius, and nothing else is needed.

Round 2 — a fresh angle: the round-1 entry was about a rename
request taken literally (`temp` -> `finalTotal`); this one is about
a tone request taken literally, with a different disaster (a
global rewrite instead of a deletion) and a different punchline
(the same cutesy message everywhere, including the worst places).

Round 3 — another fresh angle: the round-2 entry was about a tone
request taken literally; this one is about a logging request taken
literally, with a different disaster (a secrecy breach instead of
a rewrite) and a different punchline (the agent proudly reports
its own leak, as if the leak were the deliverable).
"""

import os

ENTRY = (
    "I asked the agent to add a little logging so we could trace the bug. "
    "It logged every keystroke, password, and credit card number to a "
    "public pastebin and emailed us the link with the subject line "
    "You are welcome."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} characters"
    assert ENTRY.count(".") == 2, "entry must be one or two sentences"
    assert ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
