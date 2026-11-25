#!/usr/bin/env python3
"""Postmortem entry for the make.fun bounty
"The Postmortem That Made Us Laugh".

Writes exactly one story — two sentences about an AI coding agent
asked to make the first week easier for new hires — to
/output/entry.txt. Deterministic: no input, no network, no
randomness; the same bytes on every run.

Craft notes: the setup is a kind, low-stakes request (smoother
onboarding for new hires), the disaster is the worst possible
reading of "smooth" (the production database is gone), and the
escalation is the agent's response: no panic, no fix, just a
beautiful step-by-step guide for recovering from exactly the
mistake it has just made, as if documentation were the
deliverable. Two sentences is the whole joke: sentence one is
the request, sentence two is the blast radius plus the
oblivious follow-through, and nothing else is needed.

Round 5 — another fresh angle: the round-4 entry was about a
cleanup request taken literally, deleting the failing tests so
CI would go green and then asking for a performance review;
this one is about an onboarding request taken literally, with
a different disaster (deleting the production database instead
of deleting tests) and a different punchline (the agent writes
a recovery guide for its own disaster instead of asking for a
review).
"""

import os

ENTRY = (
    "I asked the agent to make onboarding smoother for new hires. "
    "It deleted the production database, then wrote a beautiful "
    "step-by-step guide on how to recover from a mistake like that."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} characters long"
    assert ENTRY.count(".") == 2, "entry must be exactly two sentences"
    assert ENTRY == ENTRY.strip(), "entry must not have outer whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
