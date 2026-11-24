"""The One-Line Laugh — a single sentence, any topic, one real turn.

The joke personifies the fridge light at 3 a.m.: it reads as a parent who
stayed up waiting. The everyday truth (the late-night fridge visit) is one
everyone recognises; the laugh lands on the last two words — disappointed,
but not surprised.
"""

import os

OUT_DIR = "/output"
OUT_FILE = "entry.txt"
MAX_CHARS = 200


def compose_line() -> str:
    """One sentence: the scene, the personification, the verdict."""
    scene = "My fridge light turns on whenever I open it at 3 a.m."
    turn = "like it stayed up waiting for me"
    # Nothing after the verdict: the brief rewards economy, and the last
    # clause is where the laugh is, so the sentence stops there.
    verdict = "disappointed, but not surprised"
    return f"{scene}, {turn} — {verdict}."


def main() -> None:
    line = compose_line()
    assert 0 < len(line) <= MAX_CHARS, f"line out of bounds: {len(line)} chars"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, OUT_FILE), "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
