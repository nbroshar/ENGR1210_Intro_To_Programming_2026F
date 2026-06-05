# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 12 Lab (STAGE 2 — Wokwi): Receiving by Timing a Signal
#
# In Wokwi, THIS FILE is your main.py.
# Goal: tap out Morse on a button and watch the Pico DECODE it back to text.
# This is the whole receiver pipeline:
#       time a pulse  ->  classify (dot/dash/gap)  ->  build a letter  ->  decode
#
# Why a button? In Stage 2 the button stands in for "light on / light off."
# In Week 14 you replace the button with a real light sensor — and this exact
# timing+classify+decode logic stays the same. (That's the point of building
# the logic now, where it's easy to test.)
#
# HOW TO "SEND" A LETTER BY HAND:
#   short tap  = dot       long press = dash
#   tap quickly within a letter; pause ~1/3 second between letters.
#   Example: S = three short taps, then pause.   O = three long presses.
#
# WIRING: a Pushbutton, one leg to GP14, opposite leg to GND (internal pull-up).
# =============================================================================

from morse_decoder import decode_pattern    # your Week 5/7 module
from machine import Pin
import utime

DOT_MS = 100        # base unit (same as the transmitter)
# Gap thresholds (multiples of DOT_MS), matching the receiver design from Week 6:
SYMBOL_GAP_MAX = DOT_MS * 2     # gaps shorter than this stay within a letter
LETTER_GAP_MAX = DOT_MS * 5     # shorter than this = letter gap; longer = word gap

button = Pin(14, Pin.IN, Pin.PULL_UP)   # pressed -> reads 0


def classify_pulse(duration_ms):
    """A HIGH (pressed) duration -> 'dot' or 'dash'. Boundary = 2 dot units."""
    if duration_ms < DOT_MS * 2:
        return 'dot'
    else:
        return 'dash'

def classify_gap(duration_ms):
    """A LOW (released) duration -> which kind of gap."""
    if duration_ms < SYMBOL_GAP_MAX:
        return 'symbol_gap'      # still inside one letter
    elif duration_ms < LETTER_GAP_MAX:
        return 'letter_gap'      # end of a letter
    else:
        return 'word_gap'        # end of a word


# =============================================================================
# SECTION 1 — ANCHOR: measure ONE press and classify it
#
# utime.ticks_ms() is a clock in milliseconds. ticks_diff(end, start) gives the
# elapsed time safely. We time how long the button is held, then classify it.
# Run this and tap/hold the button — short taps print 'dot', long ones 'dash'.
# =============================================================================
def time_one_press():
    """Wait for a press, time how long it's held, return the duration in ms."""
    while button.value() == 1:          # wait for the press (1 -> 0)
        utime.sleep_ms(2)
    start = utime.ticks_ms()
    while button.value() == 0:          # wait for the release (0 -> 1)
        utime.sleep_ms(2)
    return utime.ticks_diff(utime.ticks_ms(), start)


# =============================================================================
# SECTION 2 — GUIDED: assemble dots/dashes into a letter, then decode it
#
# The plan:
#   - Keep a string 'pattern' that you add '.' or '-' to as taps come in.
#   - After each release, watch the GAP. If the gap grows past a letter gap
#     with no new press, the letter is finished: decode 'pattern' and reset it.
#
# Use this helper, then fill the TODO loop below it.
# =============================================================================
def gap_until_next_press(timeout_ms):
    """After a release, measure the idle gap. Return the gap length in ms once
    the button is pressed again, OR timeout_ms if no press arrives in time."""
    start = utime.ticks_ms()
    while button.value() == 1:
        if utime.ticks_diff(utime.ticks_ms(), start) >= timeout_ms:
            return timeout_ms            # timed out -> the gap is "long"
        utime.sleep_ms(2)
    return utime.ticks_diff(utime.ticks_ms(), start)

# TODO (GUIDED): complete the receive loop.
#   pattern = ""
#   while True:
#       press_ms = time_one_press()
#       symbol = classify_pulse(press_ms)        # 'dot' or 'dash'
#       pattern += '.' if symbol == 'dot' else '-'
#       gap_ms = gap_until_next_press(LETTER_GAP_MAX)   # wait out the gap
#       kind = classify_gap(gap_ms)
#       if kind != 'symbol_gap':                 # letter (or word) finished
#           letter = decode_pattern(pattern)     # your module does the lookup
#           print("letter:", letter)
#           pattern = ""                         # start the next letter


# =============================================================================
# SECTION 3 — EXTENSION: build up the whole message
#   Instead of printing each letter, append it to a 'message' string. On a
#   word_gap, append a space. Print the running message so you can watch it
#   grow as you tap. (Hint: track the gap 'kind' you already computed.)
# =============================================================================

# =============================================================================
# SECTION 4 — STRETCH: tune and show your work
#   1. Print each press as "120ms -> dash" so you can SEE your timing and adjust
#      how fast you tap.
#   2. The boundaries assume DOT_MS = 100. If your taps are slower, raise
#      DOT_MS. What happens to dot/dash classification if you tap too evenly?
# =============================================================================


print("Tap Morse on the button. Short = dot, long = dash. Pause between letters.")

# Start with the ANCHOR so you can feel the timing, then switch to your
# GUIDED loop above.
while True:
    duration = time_one_press()
    print(duration, "ms ->", classify_pulse(duration))
