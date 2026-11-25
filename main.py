#!/usr/bin/env python3
"""One-line crypto trading joke: check the fixed entry, then write it out.

A trader sells at the bottom, buys back higher, and calls the whole
mess dollar-cost averaging -- until the accountant calls it something
else. This program never accepts outside text: it holds exactly one
joke, proves that joke is well formed, and saves it to a file. There
is no input, no network access, no clock, and no randomness anywhere
in here.
"""

import sys

ENTRY = "I sold at the bottom to buy back higher. I call it dollar-cost averaging. My accountant calls it a cry for help."
CHAR_LIMIT = 200
DESTINATION = "/output/entry.txt"
ENDERS = (".", "!", "?")
FILLER = set(".,!?;:'\"-() ")


def fail(problem):
    """Print why the entry was refused and stop without writing."""
    print(f"refused: {problem}", file=sys.stderr)
    raise SystemExit(1)


def guard_nonempty(text):
    return bool(text and text.strip())


def guard_short_enough(text):
    return len(text) <= CHAR_LIMIT


def guard_no_controls(text):
    return all(ord(letter) >= 32 for letter in text)


def guard_tidy_spacing(text):
    stripped = text.strip()
    return text == stripped and "  " not in text and "\t" not in text


def guard_has_letters(text):
    return any(letter.isalpha() for letter in text)


def guard_not_only_marks(text):
    return not all(letter in FILLER for letter in text)


def guard_not_only_digits(text):
    return not text.strip().isdigit()


def guard_ends_with_mark(text):
    return text.rstrip().endswith(ENDERS)


def guard_names_strategy(text):
    return "dollar-cost" in text.lower()


def guard_no_doubled_ender(text):
    # Two bangs or two question marks in a row reads as shouting.
    return "!!" not in text and "??" not in text


def guard_no_tripled_letter(text):
    # Three identical characters in a row is a keyboard stutter.
    return all(a != b or b != c for a, b, c in zip(text, text[1:], text[2:]))


# Every guard is listed with the complaint shown when it trips. The
# checker runs them in this order and stops at the first failure, so a
# bad entry never reaches the file.
RULES = [
    ("entry must mention dollar-cost averaging", guard_names_strategy),
    ("entry must not shout with doubled punctuation", guard_no_doubled_ender),
    ("entry must not repeat a character three times in a row", guard_no_tripled_letter),
    ("entry is empty", guard_nonempty),
    ("entry is longer than the 200 character limit", guard_short_enough),
    ("entry contains control characters", guard_no_controls),
    ("entry has ragged spacing or a tab", guard_tidy_spacing),
    ("entry contains no letters", guard_has_letters),
    ("entry is punctuation only", guard_not_only_marks),
    ("entry is digits only", guard_not_only_digits),
    ("entry does not end with punctuation", guard_ends_with_mark),
]


def check_entry(text):
    for problem, guard in RULES:
        if not guard(text):
            fail(problem)


def main():
    check_entry(ENTRY)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
