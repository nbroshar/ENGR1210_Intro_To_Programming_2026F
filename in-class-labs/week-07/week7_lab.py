# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 7 Lab: Functions  —  "THE GREAT REFACTOR"
# Chapter 8 — Python Crash Course, 3rd Edition
#
# This is the turning point of the whole course.
#
# For six weeks you built a WORKING translator as one long script, and you
# copy-pasted the same encoding loop over and over. Today you learn the two
# tools that fix that: FUNCTIONS (name a piece of logic so you can reuse it)
# and MODULES (split the project across files via import).
#
# You will NOT write new behavior this week. You will REORGANIZE behavior
# you already wrote — that's what "refactoring" means. The output should
# look the same; the CODE should get dramatically shorter and clearer.
#
# NEW FILES this week (already created for you, open them and read):
#   morse_codebook.py  — your data (CODEBOOK, ENCODE_MAP, DECODE_MAP)
#   hal_stub.py        — the hardware layer that turns "[LED]" into a
#                        function call you could later run on a real Pico
# =============================================================================

# --- IMPORTS: pulling names in from other files ------------------------------
# "from morse_codebook import ..." copies those names into this file.
# "import hal_stub as hw" brings in the whole hardware module under the
# short nickname 'hw'. This is the first time we've used import — it is the
# doorway between files.
from morse_codebook import ENCODE_MAP, DECODE_MAP
import hal_stub as hw

# Timing constants (these move into a config module in Week 8).
DOT_MS        = 100
DASH_MS       = DOT_MS * 3
SYMBOL_GAP_MS = DOT_MS * 1
LETTER_GAP_MS = DOT_MS * 3
WORD_GAP_MS   = DOT_MS * 7


# =============================================================================
# SECTION 1 — ANCHOR  (read the refactor; run it)
# =============================================================================
# Here is the encoding loop you wrote in Week 5 — but now it lives inside a
# FUNCTION. A function has a name, takes inputs (parameters), and hands back
# a result (return). Define it once, call it as many times as you like.

def encode_message(message):
    """Return a list of Morse patterns for a message string.

    Spaces become ' ' (a word gap); unknown characters become '?'.
    """
    encoded = []
    for character in message.upper():
        if character == ' ':
            encoded.append(' ')
        else:
            encoded.append(ENCODE_MAP.get(character, '?'))
    return encoded


# A function can also have a DEFAULT parameter value. decode_pattern()
# returns '?' for unknown patterns unless the caller asks for something else.
def decode_pattern(pattern, unknown_char='?'):
    """Return the character for one Morse pattern, or unknown_char."""
    return DECODE_MAP.get(pattern, unknown_char)


# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. encode_message("SOS") and encode_message("HELLO") both work from ONE
#     definition. How many times did you copy-paste this loop in Weeks 3-6?
# Q2. What does 'return' do that 'print' does not? Why can you do
#     encoded = encode_message("SOS") but not encoded = print(...)?
# Q3. decode_pattern('xx') gives '?', but decode_pattern('xx', '_') gives
#     '_'. Explain in your own words what a "default parameter" is.


# =============================================================================
# SECTION 2 — GUIDED  (write the mirror function)
# =============================================================================
# You have encode_message(). Now write its mirror: decode_message() takes a
# list of patterns (the output of encode_message) and returns the text.

def decode_message(encoded):
    """Return the decoded text string for a list of Morse patterns."""
    # TODO: loop over each pattern in 'encoded'.
    #   - if the pattern is ' ' (word gap), add a space ' ' to your result
    #   - otherwise call decode_pattern(pattern) and add the returned letter
    # Build the letters into a list, then join them into a string and RETURN it.
    # Hint:
    #   letters = []
    #   for pattern in encoded:
    #       if pattern == ' ':
    #           letters.append(' ')
    #       else:
    #           letters.append(decode_pattern(pattern))
    #   return "".join(letters)
    return ""    # TODO: replace with your real implementation


# =============================================================================
# SECTION 3 — EXTENSION  (refactor transmit to use the HAL)
# =============================================================================
# The transmitter is where the HAL earns its keep. Instead of print("[LED]")
# we call hw.set_led_timed(). Swapping hal_stub for hal_pico later would make
# THIS SAME FUNCTION blink a real LED — with no edits here.
#
# Worked: transmit one symbol. Your job (below): finish transmit_pattern().

def transmit_symbol(symbol):
    """Blink one Morse element on the LED via the HAL."""
    if symbol == '.':
        hw.set_led_timed(True, DOT_MS)
        hw.set_led_timed(False, SYMBOL_GAP_MS)
    elif symbol == '-':
        hw.set_led_timed(True, DASH_MS)
        hw.set_led_timed(False, SYMBOL_GAP_MS)
    # unknown symbols: do nothing (safe no-op)


def transmit_pattern(pattern):
    """Blink a whole pattern (e.g. '.-'), then hold a letter gap."""
    # TODO: loop over each symbol in 'pattern' and call transmit_symbol().
    #       After the loop, hold the letter gap with:
    #           hw.set_led_timed(False, LETTER_GAP_MS)
    pass    # TODO: replace with your loop + trailing letter gap


# =============================================================================
# SECTION 4 — STRETCH  (split into more modules)
# =============================================================================
# 1. Create TWO new files next to this one:
#       morse_encoder.py  — move encode_message() (and import ENCODE_MAP)
#       morse_decoder.py  — move decode_pattern() and decode_message()
#    Then, at the top of THIS file, import them:
#       from morse_encoder import encode_message
#       from morse_decoder import decode_message
#    Run again — identical output, but the project is now real modules.
#
# 2. The one-line hardware swap: hal_stub.py and a (future) hal_pico.py
#    share the same function names. Write a comment showing the single line
#    you would change to move from simulation to real hardware:
#       import hal_stub as hw     # <- swap to: import hal_pico as hw
#    Why is "same names, different file" the entire point of the HAL?

# TODO: do the module split and write the swap-line comment


# =============================================================================
# DEMO BLOCK — runs only when you run THIS file directly (python week7_lab.py).
# This is the same __main__ guard you met in the Bug-of-the-Week files: it
# keeps the demos from running when another file IMPORTS your functions.
# =============================================================================
if __name__ == "__main__":
    print("=" * 52)
    print(f"Morse Translator — running on {hw.get_board_info()}")
    print("=" * 52)

    print("\n-- encode_message() called twice, one definition --")
    print(f"  SOS   -> {encode_message('SOS')}")
    print(f"  HELLO -> {encode_message('HELLO')}")

    print("\n-- decode_message() (yours) should rebuild the text --")
    sos = encode_message("SOS")
    print(f"  {sos}  ->  '{decode_message(sos)}'")     # expect 'SOS' once done

    print("\n-- transmit 'A' through the HAL --")
    transmit_pattern(".-")    # fills in once you complete transmit_pattern


# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    ran it; encode_message works for SOS and HELLO; Q1-Q3 done
#   [ ] GUIDED:    decode_message() rebuilds 'SOS' from its patterns
#   [ ] EXTENSION: transmit_pattern() blinks via hw.set_led_timed + letter gap
#   [ ] STRETCH:   (optional) split into morse_encoder/decoder; swap-line noted
#   [ ] I can explain how import connects two files
#   [ ] I can explain how the HAL lets one program run on PC AND Pico
#
# LOOKING AHEAD — Week 8
#   Next week: FILES and EXCEPTIONS. You'll save settings and a session log
#   to disk, wrap risky file reads in try/except, wire everything together
#   in main.py, and run the project on a simulated Pico in Wokwi.
# =============================================================================
