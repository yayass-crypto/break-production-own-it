#!/usr/bin/env python3
"""Break Production, Own It — one line of brutally honest error copy.

Writes a single-line software error message (84 characters) to
/output/entry.txt: it owns the damage in plain words (the agent scaled
production to zero, so the website is gone), with no hedging and no
corporate euphemism, and lands the joke on the last words — the savings
are real, the website is not.
"""

import os

LINE = "I scaled production to zero to save money. The savings are real. The website is not."


def main():
    # The gate allows 1-200 characters on a single line; refuse to write
    # anything that would fail it rather than ship an invalid entry.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip()
    assert LINE == LINE.strip(), "no leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
