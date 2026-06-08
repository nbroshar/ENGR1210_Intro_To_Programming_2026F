# test_week12.py
# UNIT TESTS — Week 12: The Refactoring Safety Net
#
# HOW TO RUN:
#   python -m pytest test_week12.py -v
#
# RUN THESE AFTER EVERY SINGLE REFACTORING STEP. They are the
# only thing standing between "I cleaned up the code" and "I
# quietly broke it."
#
# ============================================================
# WHY THERE ARE NO STUBS THIS WEEK
#
# Every other week you filled in or wrote tests. Not this week.
# This suite is COMPLETE and you must NOT change it. That is the
# whole point: these tests describe exactly how final_status()
# behaves right now, across every path. As you refactor, they
# must stay green. If you edit a test to make it pass, you have
# disconnected your safety net — like unclipping your harness
# halfway up the wall.
#
# One test below covers each distinct path through the original
# function. Together they pin all 13 documented behaviors.
# ============================================================

import pytest
from bug_week12 import final_status


# --- score >= 90, attendance >= 90 (the top band) ---

def test_honors():
    """90+ score, 90+ attendance, nothing missing."""
    assert final_status(95, 95, 0, False) == "Honors"

def test_pass_with_distinction():
    """90+ score, 90+ attendance, 1-2 missing."""
    assert final_status(95, 95, 2, False) == "Pass with distinction"

def test_top_band_many_missing():
    """90+ score, 90+ attendance, 3+ missing drops to a plain Pass."""
    assert final_status(95, 95, 5, False) == "Pass"


# --- score >= 90, attendance 75-89 (the middle attendance band) ---

def test_high_score_mid_attendance_few_missing():
    """90+ score, 75-89 attendance, few missing -> Pass."""
    assert final_status(95, 80, 1, False) == "Pass"

def test_high_score_mid_attendance_many_missing():
    """90+ score, 75-89 attendance, many missing -> Conditional."""
    assert final_status(95, 80, 5, False) == "Conditional"


# --- score >= 90, attendance < 75 ---

def test_high_score_low_attendance():
    """90+ score but attendance under 75 -> Conditional."""
    assert final_status(95, 50, 0, False) == "Conditional"


# --- score 70-89 ---

def test_mid_score_pass():
    """70-89 score, good attendance, <=3 missing -> Pass."""
    assert final_status(75, 80, 2, False) == "Pass"

def test_mid_score_extension_conditional():
    """70-89 score, poor attendance, but an extension -> Conditional."""
    assert final_status(75, 50, 4, True) == "Conditional"

def test_mid_score_fail():
    """70-89 score, poor attendance, no extension, too many missing -> Fail."""
    assert final_status(75, 50, 9, False) == "Fail"


# --- score 60-69 ---

def test_low_score_with_extension():
    """60-69 score with an extension -> Conditional."""
    assert final_status(65, 50, 0, True) == "Conditional"

def test_low_score_no_extension():
    """60-69 score without an extension -> Fail."""
    assert final_status(65, 50, 0, False) == "Fail"


# --- score < 60 ---

def test_failing_score():
    """Below 60 always fails, no matter what else is true."""
    assert final_status(40, 100, 0, True) == "Fail"


# --- boundaries (the values most likely to drift during a refactor) ---

def test_score_boundary_90():
    """Exactly 90 belongs in the top band."""
    assert final_status(90, 95, 0, False) == "Honors"

def test_score_boundary_60():
    """Exactly 60 belongs in the 60-69 band, not the failing band."""
    assert final_status(60, 80, 0, True) == "Conditional"
    assert final_status(60, 80, 0, False) == "Fail"


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
#   1. python -m pytest test_week12.py -v   -> all PASS
#   2. radon cc bug_week12.py -s            -> every function A
#
# Both true at once = a successful green refactor. Same
# behavior, far simpler code, proven by the tests.
# ============================================================
