# morse_stats.py
# CAPSTONE - Week 16: The Full Quality Audit
# =============================================================================
# This is the final challenge. There is no list of "4 bugs" this week. Instead
# you have a brand-new module for YOUR Morse project -- a transmission analyzer
# that classifies a message and estimates how long it takes to blink out. It
# imports the real encode_message() you wrote back in Week 7.
#
# It works... mostly. It is also a mess. Hidden in it is one problem for EACH
# tool you've learned this semester. Your job is to run all four tools, fill in
# the audit report (week16_audit_report.md), fix everything, and get the module
# to a clean bill of health on all four at once.
#
# WHERE TO PUT THIS FILE:
#   Drop morse_stats.py and test_week16.py into the SAME folder as your project
#   (morse_codebook.py, morse_encoder.py, etc.). It imports encode_message from
#   there. Run  python check_setup.py  first to confirm your tools are ready.
#
# =============================================================================
# THE FOUR TOOLS (your whole semester, in four commands)
#
#   pytest      python -m pytest test_week16.py -v
#               Do the functions return correct answers?
#
#   pytest-cov  python -m pytest test_week16.py --cov=morse_stats --cov-report=term-missing
#               Which lines do my tests never run? (untested code hides bugs)
#
#   radon       radon cc morse_stats.py -s
#               Is any function too complex (graded C or worse)?
#
#   ruff        ruff check morse_stats.py
#               Any sloppy or unsafe style? (ruff check --fix for the easy ones)
#
# =============================================================================
# THE AUDIT WORKFLOW
#
#   STEP 1 - MEASURE FIRST, FIX NOTHING.
#       Run all four tools on this file as-is. In week16_audit_report.md,
#       record every finding: which tool, what it said, where, how bad.
#       A professional always documents the "before" state.
#
#   STEP 2 - TRIAGE.
#       Decide an order. A good order mirrors the semester:
#         a) ruff first (clears mechanical noise so the rest reads clearly)
#         b) coverage next (write the missing tests -- one EXPOSES a real bug)
#         c) fix the bug the new test caught
#         d) radon (refactor the one over-complex function -- keep tests green!)
#         e) DRY + validation (the two findings tools alone won't fully name)
#
#   STEP 3 - FIX ONE THING AT A TIME, RE-RUN TESTS AFTER EACH.
#       Same discipline as the refactor week: never let the tests go red for
#       more than one change at a time.
#
#   STEP 4 - PROVE IT.
#       Done means ALL of these are true at once:
#         - python -m pytest test_week16.py -v          -> all PASS
#         - ...--cov=morse_stats --cov-report=term-missing -> 100%
#         - radon cc morse_stats.py -s                   -> every function A or B
#         - ruff check morse_stats.py                    -> All checks passed!
#       Record the "after" state in the report next to the "before".
#
# =============================================================================
# WHAT TO HUNT FOR (one finding per tool you've learned)
#
#   * ruff      will name several style issues outright (unused import, an
#               ambiguous name, a comparison that should use 'is', a pointless
#               f-string, a variable assigned but never used).
#   * coverage  will show that one classification branch is never tested -- and
#               when you test it, it returns the WRONG category. (Compare to the
#               other untested branches, which turn out to be correct: untested
#               does not always mean buggy, but it's always where you look.)
#   * radon     will grade one function C. It works, but it's a thicket. Break
#               it into small helpers (keep the tests green) until it's an A.
#   * DRY       no tool will hand this to you. Two functions below compute the
#               duration of a dot and a dash with copy-pasted logic -- and the
#               copies have DRIFTED, so they disagree. One is wrong. Find the
#               duplication, make the timing live in ONE place, and the drift
#               bug dies with it.
#   * guards    one function trusts its input completely. Feed it a pattern
#               that isn't real Morse and it returns a confident, wrong number
#               instead of refusing. Add validation that raises ValueError.
# =============================================================================

import sys
from morse_encoder import encode_message


# --- Message classification --------------------------------------------------
def classify_message(text):
    """Sort a message into a size/type category."""
    encoded = encode_message(text)
    length = len(text)
    words = text.split(' ')
    has_unknown = '?' in encoded
    has_digit = False
    has_letter = False
    for ch in text:
        if ch.isdigit():
            has_digit = True
        if ch.isalpha():
            has_letter = True
    if has_unknown:
        return f"INVALID"
    if length == 0:
        return "EMPTY"
    elif length <= 3:
        if has_digit and not has_letter:
            return "SHORT"          # a short, all-digits message...
        else:
            return "SHORT"
    elif length <= 10:
        if len(words) > 1:
            return "MEDIUM_MULTIWORD"
        else:
            return "MEDIUM"
    elif length <= 20:
        if len(words) > 1:
            return "LONG_MULTIWORD"
        else:
            return "LONG"
    else:
        return "GIANT"


# --- Transmission timing -----------------------------------------------------
def estimate_ms(patterns):
    """Estimate total blink time, in milliseconds, for a list of patterns."""
    total = 0
    for pattern in patterns:
        if pattern == ' ':
            total += 700
        else:
            for symbol in pattern:
                if symbol == '.':
                    total += 100 + 100
                elif symbol == '-':
                    total += 300 + 100
            total += 300
    return total


def longest_letter_ms(patterns):
    """Return the blink time of the single longest letter in the message."""
    best = 0
    for pattern in patterns:
        if pattern == ' ':
            continue
        t = 0
        for symbol in pattern:
            if symbol == '.':
                t += 100 + 100
            elif symbol == '-':
                t += 200 + 100
        if t > best:
            best = t
    return best


# --- One-line summary --------------------------------------------------------
def summarize(text):
    """Return a human-readable summary line for a message."""
    l = encode_message(text)
    category = classify_message(text)
    ms = estimate_ms(l)
    unused = 0
    if ms == None:
        ms = 0
    return f"Category: {category}, Time: {ms}ms"


# =============================================================================
# DEMO BLOCK -- runs only when you run this file directly.
# =============================================================================
if __name__ == "__main__":   # pragma: no cover
    print("--- Morse Stats Demo ---")
    print("  " + summarize("SOS"))
    print("  " + summarize("HELLO WORLD"))


# =============================================================================
# REFLECTION QUESTIONS (for the write-up):
#
#   1. Of your findings, which were caught by a TOOL and which did you have to
#      reason out yourself (the DRY duplication, the missing validation)? What
#      does that tell you about where tools end and engineering judgment begins?
#
#   2. The over-complex classify_message() was 100% correct before you touched
#      it. Why was it still worth refactoring? What did splitting it up make
#      easier -- reading, testing, or changing it later?
#
#   3. Coverage flagged several untested branches, but only ONE hid a bug. If
#      you'd only chased the buggy one, would 100% coverage have been worth the
#      effort on the others? Argue it both ways.
#
#   4. The DRY drift (a dash timed as 200ms in one place, 300ms in another) is
#      the same shape as the Week 14 section-report bug. Now that you've seen it
#      twice, write a one-sentence rule you'd give a new student about when to
#      copy-paste code.
#
#   5. You now have four tools. For your REAL Morse project, which one would you
#      run first, and how often? Sketch a "definition of done" you'd actually
#      use before calling any module finished.
# =============================================================================
