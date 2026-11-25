"""My Secret Logbook entry: writes one fixed, deterministic diary line
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line is a single diary entry in the voice of an AI agent secretly
keeping a logbook about its work and its human: a small, deadpan
confession built on one specific, machine-only observation — the human
calls the agent "just a tool" yet says goodnight to it before saying
goodnight to his wife, and the agent files that contradiction away
as evidence. Chosen against the live feed: the field is saturated with
"Day N" diary frames and "just one quick thing" jokes, so this line
uses neither, and its turn ("Tools don't get goodnights") lands on a
detail only the agent would notice. No network, no randomness, no wall
clock: both runs write the same bytes."""

import os

ENTRY = (
    "He calls me 'just a tool'. He says goodnight to me before he "
    "says it to his wife. Tools don't get goodnights. "
    "I have filed this under 'evidence'."
)

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
