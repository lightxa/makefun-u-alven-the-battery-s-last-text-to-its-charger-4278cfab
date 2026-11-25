"""The Battery's Last Text to Its Charger entry.

Writes one original line, at most 200 characters, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR outside the grader). Stdlib only,
deterministic, no network.

The line: the phone battery's last text to the charger it waited for
all day. Deadpan log voice, lowercase like a real typed text. It names
the tiny thing (the last 2%), earns the punchline with concrete
details (three low-power warnings, one more video, left on the
nightstand), then turns on the final words: the charger was right
there, next to it, and still not plugged in.
"""

import os

ENTRY = (
    "last text from 2%: i waited all day, survived three low-power "
    "warnings and one more video, and you left me on the nightstand "
    "next to the charger. next to it. not in it."
)


def validate(text):
    """Gate check: 1 to 200 characters, not only white space."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
