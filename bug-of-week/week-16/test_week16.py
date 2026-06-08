# test_week16.py
# CAPSTONE UNIT TESTS — Week 16
#
# HOW TO RUN:
#   python -m pytest test_week16.py -v
#   python -m pytest test_week16.py --cov=morse_stats --cov-report=term-missing
#
# This file, morse_stats.py, and your Morse project modules
# (morse_encoder.py, morse_codebook.py) must all be in the SAME folder.
#
# ============================================================
# WHAT THIS SUITE IS FOR
#
# This is the test half of your audit. The worked tests pass against the
# starting code. The stubs and the from-scratch test do the real work:
#   - one stub COVERS the untested branch that hides a bug (it fails until
#     you fix classify_message)
#   - one stub catches the DRY drift in the timing functions
#   - one stub uses pytest.raises to demand input validation
#
# As you fix morse_stats.py, every test here should end up green AND coverage
# should reach 100%.
#
# RUNNING TEST CASE CATEGORIES (the whole semester's vocabulary):
#   first | middle | last | missing | edge | boundary | empty
#   | stateful | exception | PATH | consistency
# ============================================================

import pytest
from morse_stats import (
    classify_message,
    estimate_ms,
    longest_letter_ms,
    summarize,
)


# ============================================================
# WORKED TESTS — fully written. They pass against the starting code.
# ============================================================

def test_classify_short():
    """A 3-letter word is SHORT."""
    assert classify_message("SOS") == "SHORT"

def test_estimate_single_dot():
    """One dot = dot (100) + symbol gap (100) + letter gap (300) = 500 ms."""
    assert estimate_ms(["."]) == 500

def test_estimate_word_gap():
    """A space in the pattern list is a 700 ms word gap."""
    assert estimate_ms([" "]) == 700


# ============================================================
# STUB 1 — Your turn: cover the untested SHORT_NUMERIC branch (catches the bug)
#
# Run coverage. classify_message has a branch for a short, all-DIGITS message
# that no other test reaches. It is SUPPOSED to return "SHORT_NUMERIC", but the
# starting code returns "SHORT". Write a test for a short numeric message
# (e.g. "12") and assert it equals "SHORT_NUMERIC".
#
# This test FAILS against the starting code — that failure is the bug coverage
# pointed you to. After you fix classify_message, it passes.
#
# Test case category: PATH (the branch the obvious tests skipped)
# ============================================================
def test_classify_short_numeric():
    """A short, all-digit message should be SHORT_NUMERIC."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# STUB 2 — Your turn: catch the DRY drift in the timing functions
#
# estimate_ms() and longest_letter_ms() both compute how long a dash takes —
# and the copies have drifted. A dash is DASH_MS (300) + a gap (100) = 400 ms.
#   - estimate_ms(["-"])         should be 300 + 100 + 300(letter gap) = 700
#   - longest_letter_ms(["-"])   should be 300 + 100 = 400
# The drifted copy in longest_letter_ms times the dash as 200, giving 300.
#
# Write an assert that longest_letter_ms(["-"]) == 400. It FAILS until you DRY
# the two functions so the dash duration lives in exactly one place.
#
# Test case category: CONSISTENCY (two functions that must agree on timing)
# ============================================================
def test_dash_timing_is_consistent():
    """The longest single dash letter should be 400 ms, matching estimate_ms."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# STUB 3 — Your turn: demand input validation (pytest.raises)
#
# estimate_ms() trusts its input. Hand it a pattern containing a character that
# isn't real Morse — like the '?' that encode_message() produces for unknown
# characters — and instead of refusing, it returns a confident, wrong number.
#
# After you add a guard clause, estimate_ms(["?"]) should raise ValueError.
# Write that test using:
#       with pytest.raises(ValueError):
#           estimate_ms(["?"])
#
# It FAILS against the starting code (no exception is raised — "DID NOT RAISE")
# and passes once you add validation.
#
# Test case category: EXCEPTION
# ============================================================
def test_estimate_rejects_bad_symbol():
    """A pattern with a non-Morse symbol must raise ValueError."""
    pass   # TODO: replace with a real pytest.raises block


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub. Write the whole thing: function name, docstring, assert(s).
#
# What to test: the INVALID category, end to end. A message containing a
# character that has no Morse code (for example "SOS!") should classify as
# "INVALID", and summarize() of that same message should report "n/a" for the
# time rather than a fake number.
#
# Your test must:
#   1. assert classify_message("SOS!") == "INVALID"
#   2. assert "n/a" in summarize("SOS!")
#
# (Hint: getting summarize to say "n/a" for invalid input is part of your fix —
# the starting summarize() doesn't handle it. This test drives that fix.)
#
# Category: PATH + exception-ish (invalid input handled gracefully).
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE (the capstone bar):
#
#   python -m pytest test_week16.py -v                              -> all PASS
#   python -m pytest test_week16.py --cov=morse_stats --cov-report=term-missing
#                                                                   -> 100%
#   radon cc morse_stats.py -s                            -> every function A/B
#   ruff check morse_stats.py                             -> All checks passed!
#
# Four green lights at once = a module that is correct, fully tested, simple,
# and clean. That is what "done" means for a professional.
# ============================================================
