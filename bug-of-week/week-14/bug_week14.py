# bug_week14.py
# QUALITY CHECK OF THE WEEK - Week 14: Don't Repeat Yourself (DRY)
#
# A NOTE ON THIS WEEK'S FORMAT:
# This week the quality smell and a real BUG are the same thing.
# The three functions below are near-identical copies of each
# other. Someone updated the passing rule in two of them and
# forgot the third. That forgotten copy now gives wrong answers —
# and it's the duplication that caused it. You will fix the bug
# by removing the duplication, not by patching the one copy.
#
# ============================================================
# THE PRINCIPLE: DON'T REPEAT YOURSELF (DRY)
#
# DRY says: every piece of knowledge should live in exactly ONE
# place in your code. If the rule "passing is 60 or above" is
# written three times, then it can be CHANGED in one place and
# forgotten in the other two. The copies drift apart, and the
# forgotten one quietly produces wrong results.
#
# Copy-paste is the enemy here. The moment you copy a block of
# code and tweak it, you've created two things that must be kept
# in sync forever by hand — and humans are bad at that.
#
# THE FIX: pull the repeated logic into ONE function and call it
# from every place that needs it. Then there is only one copy of
# the knowledge, and drift becomes impossible by construction.
#
# TWO THINGS TO KEEP IN MIND (so you don't over-apply DRY):
#
#   THE RULE OF THREE: one copy is fine. Two can be fine. When
#   you reach for a THIRD copy, that's the signal to extract a
#   function. (We are well past that here.)
#
#   DRY IS ABOUT KNOWLEDGE, NOT TEXT: two blocks that merely LOOK
#   alike but mean different things ("passing >= 60" vs. "adult
#   age >= 60") should NOT be merged just because they resemble
#   each other. They will evolve differently. The test is not
#   "do these lines look the same?" but "do they say the same
#   THING?"
#
# ============================================================
# DON'T TAKE THE SHORTCUT
#
# You will be tempted to fix this week's bug by changing one
# character in report_evening (the > back to >=). DO NOT.
#
# That patches one symptom and leaves the disease: three copies
# that can drift again next time someone edits them. Fix the
# ROOT CAUSE — make the passing rule exist in exactly one place —
# and this bug, plus every future drift bug like it, becomes
# impossible. That is the difference between treating a bug and
# preventing a whole category of bugs.
# ============================================================
#
# ============================================================
# YOUR WORKFLOW THIS WEEK:
#
#   STEP 1: Run the tests. Most pass. One fails — the evening
#           boundary test. That failure is the drift bug.
#   STEP 2: Read all three functions side by side. They are the
#           SAME logic three times. Spot the one that drifted.
#   STEP 3: Write ONE new helper that holds the logic a single
#           time, for example:
#               def _section_report(name, scores):
#                   ...the shared logic, with >= 60 ...
#   STEP 4: Rewrite the three functions so each one is a single
#           line that calls your helper with its own name:
#               def report_morning(scores):
#                   return _section_report("Morning", scores)
#   STEP 5: Run the tests. All green now — including the evening
#           boundary, which is fixed automatically because there
#           is only one definition of "passing" left.
#
# (Optional: run  radon cc bug_week14.py -s  before and after.
#  Notice the per-function complexity barely changes — the cost
#  of duplication was never complexity. It was having THREE
#  places to keep in sync.)
# ============================================================


# --- Section reports. Three copies of the same logic. ---
# Read them top to bottom. Two are identical; one has drifted.

def report_morning(scores):
    """Summarize the morning section's scores."""
    average = sum(scores) / len(scores)
    passed = 0
    for s in scores:
        if s >= 60:
            passed += 1
    return f"Morning: avg {average}, {passed}/{len(scores)} passed"


def report_afternoon(scores):
    """Summarize the afternoon section's scores."""
    average = sum(scores) / len(scores)
    passed = 0
    for s in scores:
        if s >= 60:
            passed += 1
    return f"Afternoon: avg {average}, {passed}/{len(scores)} passed"


def report_evening(scores):
    """Summarize the evening section's scores."""
    average = sum(scores) / len(scores)
    passed = 0
    for s in scores:
        if s > 60:          # DRIFT: every other copy uses >= 60.
            passed += 1     # A student who scored exactly 60 is
                            # silently dropped from this section only.
    return f"Evening: avg {average}, {passed}/{len(scores)} passed"


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# Watch the evening count: the same scores that pass in the
# morning section come up short in the evening section.
# ============================================================
if __name__ == "__main__":   # pragma: no cover
    print("--- Section Reports ---")
    print("  " + report_morning([60, 75, 40]))
    print("  " + report_afternoon([60, 75, 40]))
    print("  " + report_evening([60, 75, 40]))   # 60 wrongly excluded here


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. The drift bug only existed because the logic was copied.
#      Explain how DRYing the code didn't just FIX the bug but
#      made that whole TYPE of bug impossible. Why is "preventing
#      a category of bugs" more valuable than "fixing one bug"?
#
#   2. After your refactor, the three report_ functions are each
#      one line that differs only by a section name. Is that
#      still "repetition"? Is it the dangerous kind? When is a
#      little repetition acceptable, and how does the Rule of
#      Three help you decide?
#
#   3. Imagine the passing threshold changes from 60 to 65 next
#      semester. Describe exactly what you'd have to do in the
#      ORIGINAL (three-copy) version versus your DRY version.
#      Which one would you trust a tired person to get right at
#      11pm?
#
#   4. "DRY is about knowledge, not text." Give an example of two
#      code blocks that look identical but should NOT be merged
#      because they actually represent different rules. What
#      would go wrong later if you merged them anyway?
# ============================================================
