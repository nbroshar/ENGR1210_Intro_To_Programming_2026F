# bug_week4.py
# BUG OF THE WEEK - Week 4: if Statements
# 
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Two bugs (1 & 2) you can find with the STANDARD debugging process.
# Two bugs (3 & 4) are LOGIC ERRORS that are much easier to find
# using the VS Code Python Debugger. Instructions for each are below.
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#
#   STEP 1: Run the program — read the error type and line number.
#   STEP 2: Go to that line, fix ONE bug, save, and run again.
#   STEP 3: Repeat until no crashes.
#   STEP 4: CHECK YOUR OUTPUT — a program that runs is not
#           necessarily a program that works.
#
# ============================================================
# HOW TO USE THE VS CODE DEBUGGER (new this week):
#
#   SET A BREAKPOINT:
#     Click in the gray margin to the LEFT of a line number.
#     A red dot appears — that is your breakpoint.
#     Python will PAUSE execution at that line before running it.
#
#   START THE DEBUGGER:
#     Press F5  (or Run menu → Start Debugging)
#     Choose "Python File" if prompted.
#
#   DEBUGGER TOOLBAR (appears at top of screen):
#     ▶  Continue (F5)     — run until the next breakpoint
#     ⤵  Step Over (F10)   — run the current line and pause on the next
#     ⤵  Step Into (F11)   — step inside a function call
#     ⏹  Stop (Shift+F5)   — quit the debugger
#
#   VARIABLES PANEL (left side, while paused):
#     Shows the current value of every variable in scope.
#     Watch it change as you Step Over each line.
#     This is how you catch logic errors — you can SEE the
#     variable values instead of guessing.
#
#   WHEN TO USE THE DEBUGGER vs. PRINT STATEMENTS:
#     print() is fast for checking one value.
#     The debugger is better when you need to watch MULTIPLE
#     variables change together across several lines of code.
# ============================================================


# ============================================================
# BUG 1 — Find with: standard run (SyntaxError / crash)
#
# HINT: Read about comparison operators carefully.
#       The assignment operator = and the comparison operator ==
#       are NOT the same thing.
#       Which one belongs inside an if condition?
# ============================================================
print("--- Grade Checker ---")
grade = 91

if grade = 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B.")
else:
    print("Keep working at it.")


# ============================================================
# BUG 2 — Find with: standard run + check output (logic error)
#
# HINT: Read about checking whether a value is NOT in a list.
#       The goal: print a warning ONLY if "admin" is NOT in the
#       user list. Does the operator below do what we intend?
# ============================================================
print("\n--- User Check ---")
approved_users = ["admin", "natalie", "carlos", "priya"]
current_user = "guest"

if current_user in approved_users:
    print(f"WARNING: '{current_user}' is not an approved user!")
else:
    print(f"Welcome, {current_user}!")


# ============================================================
# BUG 3 — Find with: VS Code Debugger  ← NEW THIS WEEK
#
# This is a LOGIC ERROR. The program runs and prints something,
# but the output is wrong for certain inputs. Running it won't
# show an error — you must WATCH the variables to catch it.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on the line: if age < 2:
#   2. Press F5 to start the debugger.
#   3. In the Variables panel, confirm: what is the value of age?
#   4. Press F10 (Step Over) one line at a time.
#   5. Watch which branch of the if-elif-else gets entered.
#      Does it match the correct stage of life for that age?
#   6. Keep stepping — does the printed message match age = 15?
#
# HINT: Read the if-elif-else chain carefully (p. 83-85).
#       There are three conditions. Is the boundary for "teenager"
#       correct? A 15-year-old should print "teenager."
#       What does it print instead, and why?
# ============================================================
print("\n--- Stage of Life ---")
age = 15

if age < 2:
    print("Stage: infant")
elif age < 13:
    print("Stage: child")
elif age < 13:           # <-- set your breakpoint here, then Step Over
    print("Stage: teenager")
else:
    print("Stage: adult")


# ============================================================
# BUG 4 — Find with: VS Code Debugger  ← NEW THIS WEEK
#
# Another logic error. The program runs silently — it prints
# nothing at all for some inputs. You need the debugger to
# understand WHY certain conditions are never reached.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on the line: requested_topping = "mushrooms"
#   2. Press F5 to start the debugger.
#   3. In the Variables panel, watch: available_toppings, requested_topping
#   4. Step Over each line of the if-elif chain.
#   5. Which branch runs? Which ones are skipped?
#   6. Look carefully at HOW each topping is stored in the list
#      vs. HOW the requested topping is written.
#      What is different about the capitalization?
#
# HINT: Read about string comparisons and case sensitivity.
#       Python comparisons are case-sensitive: "Mushrooms" != "mushrooms"
#       What STRING method could make both sides match? 
# ============================================================
print("\n--- Pizza Topping Checker ---")
available_toppings = ["Pepperoni", "Mushrooms", "Green Peppers", "Olives"]
requested_topping = "mushrooms"    # <-- set your breakpoint here

if requested_topping == available_toppings[0]:
    print("Adding pepperoni.")
elif requested_topping == available_toppings[1]:
    print("Adding mushrooms.")
elif requested_topping == available_toppings[2]:
    print("Adding green peppers.")
elif requested_topping == available_toppings[3]:
    print("Adding olives.")
else:
    print(f"Sorry, we don't have {requested_topping}.")


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. Bug 1: What is the difference between = and == in Python?
#      Give an example of when you would use each one.
#
#   2. Bug 2: What is the difference between 'in' and 'not in'?
#      Write a one-line example of each from your own life
#      (e.g., checking whether a song is in a playlist).
#
#   3. Bug 3: Could you have found this bug WITHOUT the debugger?
#      How? Would it have been faster or slower than using the
#      debugger? What would you have had to change to catch it
#      with print() statements alone?
#
#   4. Bug 4: The fix for Bug 4 requires calling a string METHOD
#      on each comparison. Which method fixes the case mismatch?
#      Should you fix the list, the request, or both — and why
#      does that decision matter in a real program?
# ============================================================