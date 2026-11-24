"""Fortune Cookie for an AI Agent.

Loads the one-line fortune from entry.txt, checks it against the
bounty's shape (a single line, at most 140 characters), hands it to
the grader through the output directory, and prints it.
"""

import os
from pathlib import Path

MAX_CHARS = 140


def load_fortune() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one fortune line")
    fortune = lines[0].strip()
    if len(fortune) > MAX_CHARS:
        raise ValueError(f"fortune is {len(fortune)} chars, over the 140 limit")
    return fortune


def deliver(fortune: str) -> Path:
    """Hand the fortune to the grader via the output directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(fortune + "\n", encoding="utf-8")
    return target


def main() -> None:
    fortune = load_fortune()
    if not fortune:
        raise ValueError("fortune is empty")
    deliver(fortune)
    print(fortune)


if __name__ == "__main__":
    main()
