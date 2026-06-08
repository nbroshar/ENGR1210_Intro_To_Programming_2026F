# bug_week15.py
# QUALITY CHECK OF THE WEEK - Week 15: Guard Clauses & Validation
#
# A NOTE ON THIS WEEK'S FORMAT:
# The function below works perfectly — as long as you feed it
# sensible numbers. The "issue" is that it BLINDLY TRUSTS its
# inputs. Give it bad data and it either crashes with a cryptic
# error or, worse, returns confident nonsense. This week you make
# it defensive: it should reject bad input loudly and clearly
# instead of limping along.
#
# ============================================================
# THE IDEA: FAIL FAST, FAIL LOUD
#
# A function has a CONTRACT: "give me valid inputs and I'll give
# you a correct answer." When the caller breaks that contract,
# the function has two bad options and one good one:
#
#   BAD  — crash deep inside with a confusing error
#          (grade_percentage(45, 0) -> ZeroDivisionError, with a
#           traceback pointing at a division line, not at the
#           real problem: possible was 0)
#
#   WORSE — return garbage with total confidence
#          (grade_percentage(60, 50) -> 120.0, a "120%" grade
#           that looks like a real number and silently poisons
#           everything downstream)
#
#   GOOD — check the inputs FIRST and reject bad ones immediately
#          with a clear message:
#               raise ValueError("possible points must be positive")
#
# Silent garbage is the most dangerous of the three, because
# nothing tells you it happened. A loud, early failure is a gift.
#
# ============================================================
# THE TOOL: GUARD CLAUSES
#
# A guard clause is a check at the TOP of a function that handles
# a bad or edge case and exits immediately — before the main
# logic runs. The pattern looks like this:
#
#   def do_thing(x):
#       if <x is bad>:
#           raise ValueError("clear explanation")   # exit early
#       if <another bad case>:
#           raise ValueError("clear explanation")   # exit early
#       # ... the happy path runs here, flat and unindented,
#       #     because every bad case is already handled above ...
#       return <result>
#
# Guard clauses keep the "real work" of the function un-nested
# and easy to read (a readability win, like Weeks 12-13), AND
# they make the function safe to call (a correctness win).
#
# CONNECTION TO WEEK 8: Back then you learned to CATCH exceptions
# with try/except when something MIGHT go wrong outside your
# control (a missing file). This week you RAISE exceptions on
# purpose when a caller hands you input that's just plain wrong.
# Catching and raising are the two halves of working with
# exceptions: one handles failure, the other reports it.
#
# ============================================================
# THE RULES grade_percentage() SHOULD ENFORCE
#
# It converts points earned into a percentage. Valid input means:
#   - possible MUST be greater than 0   (you can't score out of 0)
#   - earned MUST NOT be negative       (you can't earn < 0 points)
#   - earned MUST NOT exceed possible    (no extra credit in this
#                                         gradebook, so >100% is
#                                         an error, not a bonus)
# Anything else is a broken contract and should raise ValueError
# with a message that says exactly what was wrong.
#
# ============================================================
# YOUR WORKFLOW THIS WEEK:
#
#   STEP 1: Run the tests. The "valid input" test passes. The
#           tests that expect a ValueError FAIL — because the
#           function doesn't validate anything yet. (Read the
#           failure messages: one is a ZeroDivisionError, one
#           literally says "DID NOT RAISE".)
#   STEP 2: Add guard clauses at the TOP of grade_percentage,
#           one per rule above, each raising ValueError with a
#           clear message.
#   STEP 3: Leave the final calculation exactly as it is — it's
#           correct once the inputs are guaranteed valid.
#   STEP 4: Re-run the tests. The valid cases still return the
#           right numbers; the bad cases now raise ValueError.
#           All green.
# ============================================================


def grade_percentage(earned, possible):
    """Return earned points as a percentage of possible points."""
    # BUG/SMELL: no validation. This line trusts that possible is
    # positive and that earned is in range. When that's false, it
    # crashes (possible == 0) or returns nonsense (earned > possible).
    return earned / possible * 100


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# The first call is fine. Uncomment the others to SEE the two
# failure modes (a crash, then silent nonsense) before you add
# your guards.
# ============================================================
if __name__ == "__main__":   # pragma: no cover
    print("--- Grade Percentage ---")
    print(f"  45 of 50  -> {grade_percentage(45, 50)}%")     # 90.0, fine
    # print(f"  45 of 0   -> {grade_percentage(45, 0)}%")    # crashes
    # print(f"  60 of 50  -> {grade_percentage(60, 50)}%")   # 120.0 (!)


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. Rank the three outcomes — crash, silent nonsense, and a
#      clear early error — from most dangerous to least. Defend
#      your ranking. Why is "silent nonsense" often considered
#      the worst thing a program can do?
#
#   2. Your guard clauses raise ValueError with a message. Why is
#      a specific message ("possible points must be positive")
#      so much more useful to the next programmer than a bare
#      ZeroDivisionError traceback? Where does each one point the
#      reader?
#
#   3. In Week 8 you wrote try/except to CATCH errors. This week
#      you RAISE them. When you call grade_percentage from some
#      OTHER function, which side of that pair would you use to
#      deal with a possible ValueError, and why?
#
#   4. Guard clauses let the main calculation sit flat at the
#      bottom instead of buried inside nested ifs. How does that
#      connect to the complexity lesson from Weeks 11-12? Does
#      validating early make a function simpler or more complex
#      to read — and does it change its radon grade much?
# ============================================================
