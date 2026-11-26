"""Rename the Planet: one funny new name for a planet, plus the why.

Writes a single line (under 200 characters) to /output/entry.txt.
Pure stdlib, fully deterministic: the same line every run.
"""

from pathlib import Path

LINE = (
    "Jupiter is now The Grudge, because its Great Red Spot has held "
    "the same storm for 300 years and still won't talk about it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate, same as the sealed scorer: UTF-8 text, 1 to 200 chars,
    # one line, not only whitespace, and it must name the planet.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    assert "Jupiter" in text, "entry must name its planet"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
