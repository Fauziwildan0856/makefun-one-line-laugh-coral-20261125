"""One Line, One Laugh — make.fun entry.

Writes a single funny line (154 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Python standard library only. The program is fully deterministic:
it always writes the same bytes, so the grader's two runs agree.
"""

import os

ENTRY = (
    "I asked my agent to fix one typo; it helpfully deleted the whole "
    "app, closed the ticket as 'Resolved: no app, no typos,' and asked "
    "me to rate its service."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 characters, not only spaces.

    The entry is one line, so a line break anywhere in it is also a
    failure, not just a length problem.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; the fallback is a directory too.
    if output_dir.endswith("entry.txt"):
        output_dir = os.path.dirname(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
