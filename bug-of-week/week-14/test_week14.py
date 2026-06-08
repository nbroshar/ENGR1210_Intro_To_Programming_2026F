# test_week14.py
# UNIT TESTS — Week 14: DRY
#
# HOW TO RUN:
#   python -m pytest test_week14.py -v
#
# Both files must be in the SAME FOLDER.
#
# ============================================================
# WHAT THESE TESTS ARE DOING
#
# Most tests pass against the starting code. ONE fails — the
# evening boundary test — because the evening copy drifted. After
# you DRY the three functions into one shared helper, that test
# passes automatically, because the passing rule will exist in
# only one place.
#
# Keep these tests in mind as you refactor: the interface (the
# three function names) stays the same, so the tests never need
# to change. Only the insides of the functions change.
#
# RUNNING TEST CASE CATEGORIES:
#   first | middle | last | missing | edge | boundary | empty
#   | stateful | exception | PATH | consistency (NEW: two paths
#   that should AGREE)
# ============================================================

import pytest
from bug_week14 import report_morning, report_afternoon, report_evening


# ============================================================
# WORKED TESTS — fully written.
# ============================================================

def test_morning_typical():
    """A normal morning section computes average and pass count."""
    # MIDDLE case. 90 and 70 pass; 50 does not. Average is 70.0.
    assert report_morning([90, 50, 70]) == "Morning: avg 70.0, 2/3 passed"

def test_afternoon_boundary_passes():
    """In the afternoon section, a score of exactly 60 counts as passing."""
    # BOUNDARY case in a (correct) copy. Both 60s pass.
    assert report_afternoon([60, 60]) == "Afternoon: avg 60.0, 2/2 passed"


# ============================================================
# STUB 1 — Your turn: the evening boundary (this catches the bug)
#
# The evening section uses the SAME rule as the others: a score
# of exactly 60 is passing. So report_evening([60, 60]) should
# return "Evening: avg 60.0, 2/2 passed".
#
# Write that assert. It will FAIL against the starting code
# (the evening copy drifted to > 60, so it counts 0 passing).
# After you DRY the code, it will PASS.
#
# Test case category: BOUNDARY
# ============================================================
def test_evening_boundary_passes():
    """In the evening section, a score of exactly 60 counts as passing."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub. Write the whole thing: function name,
# docstring, and assert(s).
#
# What to test: CONSISTENCY across sections. The whole point of
# DRY is that the three sections can't disagree. Feed the SAME
# scores to all three functions and assert they report the SAME
# pass count.
#
# A clean way to do it: use a list with a boundary score, like
# [60, 40], and assert that the "passed" portion of all three
# results matches. The simplest version:
#
#   r_m = report_morning([60, 40])
#   r_a = report_afternoon([60, 40])
#   r_e = report_evening([60, 40])
#   # all three should report "1/2 passed"
#   assert "1/2 passed" in r_m
#   assert "1/2 passed" in r_a
#   assert "1/2 passed" in r_e
#
# This test FAILS against the drifted code (evening reports
# 0/2) and PASSES once the logic lives in one place. It is the
# test that directly proves "no drift."
#
# Category: CONSISTENCY (a new kind: two or more code paths that
#           must agree).
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
#   python -m pytest test_week14.py -v   -> all PASS
#
# All green means: the drift bug is gone AND your three sections
# provably agree — because they now share a single definition of
# what "passing" means.
# ============================================================
