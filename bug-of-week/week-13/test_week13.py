# test_week13.py
# UNIT TESTS — Week 13: Style Cleanup (Behavior Preservation)
#
# HOW TO RUN:
#   python -m pytest test_week13.py -v
#
# Run these BEFORE you start cleaning up, and again after EVERY
# change (including after 'ruff check --fix'). Cleaning up style
# must never change what the function returns. If a test goes
# red, your "cleanup" actually altered behavior — undo it.
#
# Both files must be in the SAME FOLDER.
#
# RUNNING TEST CASE CATEGORIES:
#   first | middle | last | missing | edge | boundary | empty
#   | stateful | exception | PATH (one test per branch)
# ============================================================

import pytest
from bug_week13 import summarize


# ============================================================
# WORKED TESTS — fully written. Study them, then keep them green.
# ============================================================

def test_mixed_class():
    """A normal mix of passing and failing scores."""
    # MIDDLE / typical case. Two of three pass (90 and 70).
    assert summarize([90, 50, 70]) == "Average: 70.0, Passed: 2/3"

def test_everyone_passes_flag():
    """When all scores pass, the 'perfect class' flag appears."""
    # PATH: the everyone_passed branch.
    assert summarize([88, 92]) == "Average: 90.0, Passed: 2/2 (perfect class!)"


# ============================================================
# STUB 1 — Your turn: the EMPTY list case
#
# summarize([]) should return exactly "No scores recorded."
# (Note: after you fix the F541 finding, the function returns a
# plain string instead of an f-string — but the TEXT must be
# identical, so this test should pass before AND after cleanup.)
#
# Write the assert.
#
# Test case category: EMPTY
# ============================================================
def test_empty_list():
    """An empty score list returns the 'no scores' message."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub. Write the whole thing: function name,
# docstring, and assert.
#
# What to test: the BOUNDARY score of exactly 60. A score of 60
# counts as passing (the rule is "60 or above"). Give summarize
# a list where the only passing score is exactly 60 — for
# example [60, 30] — and assert the result reports 1 passed.
#
# Work out the expected string by hand first:
#   average of [60, 30] = 45.0, passed = 1 of 2.
#   So the expected return is "Average: 45.0, Passed: 1/2".
#
# This guards the magic-number line (score >= 60) so that if
# anyone later "cleans up" 60 into the wrong value, you catch it.
#
# Category: BOUNDARY.
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
#   1. python -m pytest test_week13.py -v   -> all PASS
#   2. ruff check bug_week13.py             -> "All checks passed!"
#
# Both at once = same behavior, clean style. Then do STEP 6 in
# bug_week13.py (the named constant) — a human improvement no
# tool demanded.
# ============================================================
