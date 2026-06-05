# bug_week2.py
# BUG OF THE WEEK - Week 2: Introducing Lists
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Follow the SAME structured debugging process from Week 1.
#
# ============================================================
# HOW TO DEBUG IN A STRUCTURED WAY (review from Week 1):
#
#   STEP 1: Run the program and READ the error message carefully.
#           - What LINE number does it point to?
#           - What TYPE of error is it? (IndexError, TypeError,
#             AttributeError, SyntaxError...)
#
#   STEP 2: Go to that line and look for the problem.
#           - Fix ONE bug at a time — don't change anything else!
#
#   STEP 3: Fix that ONE bug, then SAVE and RUN again.
#
#   STEP 4: Repeat Steps 1-3 until the program runs cleanly.
#
#   NEW THIS WEEK: You may also see an IndexError or AttributeError.
#           - IndexError  → you asked for a position that doesn't exist
#           - AttributeError → you called a method that doesn't belong
#                              to that data type
# ============================================================

# --- OUR LIST OF COURSES ---
# This line is correct — no bug here.
courses = ["Python", "circuits", "technical writing", "calculus"]

# ============================================================
# BUG 1
# BUG HINT: Lists are zero-indexed.
#           What is the index of the FIRST item in a list?
#           Count the items — is index 4 valid for this list?
# ============================================================
print("First course: " + courses[4])

# ============================================================
# BUG 2
# BUG HINT: Read about modifying list elements.
#           You want to replace "circuits" with "electronics".
#           The correct syntax is: list_name[index] = "new value"
#           What is wrong with the syntax on this line?
# ============================================================
courses(1) = "electronics"

# ============================================================
# BUG 3
# BUG HINT: Read about list methods.
#           .append() adds ONE item to the END of a list.
#           What data type does .append() expect as its argument?
#           Check what is being passed in on this line.
# ============================================================
courses.append(["philosophy", "statistics"])

# ============================================================
# BUG 4
# BUG HINT: Read about permanently sorting a list.
#           .sort() sorts the list — but does it take an argument
#           to sort in reverse order, or is there a separate method?
# ============================================================
courses.sort(reverse_order=True)
print(courses)

# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#   1. What is the difference between an IndexError and an
#      AttributeError? Which one is harder to spot and why?
#   2. Bug 3 won't cause an error crash — it causes a LOGIC error.
#      What is the difference between a runtime error and a logic error?
#      How do you find a logic error if Python doesn't tell you about it?
#   3. What does zero-indexing mean, and why do you think Python
#      (and most languages) start counting at 0 instead of 1?
# ============================================================