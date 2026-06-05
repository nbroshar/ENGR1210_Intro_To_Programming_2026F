# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 11 Lab (STAGE 2 — Wokwi): Sending on a Button Press
#
# In Wokwi, THIS FILE is your main.py (Wokwi auto-runs main.py).
# Goal: press a button -> the Pico blinks a message in Morse on its LED.
# New skill: reading a digital INPUT pin. Everything else is code you already
# wrote and refactored into modules.
#
# WIRING (build it in Wokwi with the "+" parts menu, then wire it):
#   - Raspberry Pi Pico (onboard LED is the transmitter — no LED wiring needed)
#   - 1x Pushbutton: connect one leg to GP14, and the diagonally-opposite leg
#     to a GND pin on the Pico.
#   We use the Pico's INTERNAL pull-up resistor, so an UNpressed button reads 1
#   and a PRESSED button reads 0 (it connects the pin to GND).
#   (A starter diagram11.json is included, but confirm the button wiring in
#    Wokwi's editor — drag the button and check the two legs.)
# =============================================================================

import hal_pico as hw                       # the LED, behind the HAL
from morse_encoder import encode_message    # your Week 5/7 module
from machine import Pin
import utime

# Timing (same constants all the way from Week 1)
DOT_MS        = 100
DASH_MS       = DOT_MS * 3
SYMBOL_GAP_MS = DOT_MS * 1
LETTER_GAP_MS = DOT_MS * 3
WORD_GAP_MS   = DOT_MS * 7

# The button. PULL_UP means: not pressed -> reads 1, pressed -> reads 0.
button = Pin(14, Pin.IN, Pin.PULL_UP)


# --- given: the transmitter you built (uses the HAL, so it blinks the LED) ---
def transmit_pattern(pattern):
    for symbol in pattern:
        if symbol == '.':
            hw.set_led_timed(True, DOT_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)
        elif symbol == '-':
            hw.set_led_timed(True, DASH_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)
    hw.set_led_timed(False, LETTER_GAP_MS)

def transmit_message(text):
    print("  transmitting:", text)
    for item in encode_message(text):
        if item == ' ':
            hw.set_led_timed(False, WORD_GAP_MS)
        else:
            transmit_pattern(item)


# =============================================================================
# SECTION 1 — ANCHOR: detect a button press
#
# A button "press" is the moment the pin goes from 1 (up) to 0 (down). We watch
# for that change instead of just reading the level, so one press = one event.
# Run this, click the button in Wokwi, and watch the console.
# =============================================================================
def wait_for_press():
    """Block until the button is pressed (a 1 -> 0 transition), then return."""
    while button.value() == 1:      # wait while NOT pressed
        utime.sleep_ms(5)
    # button is now down
    utime.sleep_ms(20)              # tiny debounce
    while button.value() == 0:      # wait until released
        utime.sleep_ms(5)


# =============================================================================
# SECTION 2 — GUIDED: transmit a message when the button is pressed
#
# In the main loop below, call wait_for_press(), and when it returns, transmit
# a message. Fill in the TODO.
# =============================================================================

# =============================================================================
# SECTION 3 — EXTENSION: cycle through several messages
#   Make a list of messages, e.g. ["SOS", "HI", "OK"]. Each press sends the
#   NEXT one in the list (wrap back to the start after the last). Print which
#   message you're sending. (Hint: keep an index variable; use % len(messages).)
# =============================================================================

# =============================================================================
# SECTION 4 — STRETCH: a "panic" double-press
#   If two presses happen within 500 ms, send "SOS" no matter what. Otherwise
#   send the normal cycled message. (Hint: time the gap with utime.ticks_ms()
#   and utime.ticks_diff().)
# =============================================================================


print("Board:", hw.get_board_info())
print("Press the button to transmit.")

messages = ["SOS", "HI", "OK"]    # for the EXTENSION
index = 0

while True:
    wait_for_press()
    # TODO (GUIDED): transmit a message here. Start with:
    #     transmit_message("SOS")
    # Then for the EXTENSION, send messages[index] and advance index.
    pass
