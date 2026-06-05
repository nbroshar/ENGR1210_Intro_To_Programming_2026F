# bug_week1.py
# BUG OF THE WEEK - Week 1: Variables & Simple Data Types
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Follow the structured debugging steps below to find and fix them all.
#
# ============================================================
# HOW TO DEBUG IN A STRUCTURED WAY:
#
#   STEP 1: Run the program and READ the error message carefully.
#           - What LINE number does it point to?
#           - What TYPE of error is it? (SyntaxError, NameError, TypeError...)
#
#   STEP 2: Go to that line and look for the problem.
#           - Don't fix anything else yet — fix ONE bug at a time.
#
#   STEP 3: Fix that ONE bug, then SAVE and RUN again.
#
#   STEP 4: Repeat Steps 1-3 until the program runs cleanly.
#
#   NOTE: Python stops at the FIRST error it finds.
#         There may be more bugs hiding behind it!
# ============================================================

# --- YOUR VARIABLES --- 
# BUG HINT: Read variable naming rules in your textbook.
#           Can a variable name contain a space?
First Name = "jordan"

# BUG HINT: Look very carefully at the quote marks on this line.
#           Does the string open and close with the same type of quote?
last_name = 'Smith"

# This line is correct — no bug here.
age = "28"

# --- YOUR PRINT STATEMENTS ---
# BUG HINT: Python is case-sensitive
#           Are all variable names spelled EXACTLY the same as when you defined them?
print("Name: " + first_name.title() + " " + Last_name.title())

# BUG HINT: Look at the data type of 'age' on line 30.
#           Can you concatenate a string and an integer directly?
print("Age: " + age + 1)

# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#   1. How many times did you have to run the program to fix all 4 bugs?
#   2. Which error message was the most helpful? Which was confusing?
#   3. What is the difference between a SyntaxError, a NameError, and a TypeError?
# ============================================================