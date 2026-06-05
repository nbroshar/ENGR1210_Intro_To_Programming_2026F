# =============================================================================
# ENGR1210 — Week 15 (STAGE 3): Two-Board Link — SENDER
# This is the TX board's main.py.
#
# TWO CHANNELS:
#   DATA      goes WIRELESS — this board's LED -> the other board's light sensor.
#   HANDSHAKE goes by WIRE   — two GPIO lines coordinate WHEN to talk:
#       RR (Receiver Ready): driven by the RX board, READ by us.
#       SR (Sender Ready):   driven by US, read by the RX board.
#
# WIRING BETWEEN THE TWO PICOS (see week15_link_guide.md for the full picture):
#   TX GP16 (SR out)  ->  RX GP16 (SR in)
#   RX GP17 (RR out)  ->  TX GP17 (RR in)
#   TX GND            <-> RX GND        <-- REQUIRED: shared ground, or the
#                                            logic levels are meaningless.
#   TX LED  ---- aimed at ---->  RX light sensor   (the wireless data channel)
# =============================================================================

import hal_pico as hw
from morse_encoder import encode_message
from machine import Pin
import utime

DOT_MS        = 100
DASH_MS       = DOT_MS * 3
SYMBOL_GAP_MS = DOT_MS * 1
LETTER_GAP_MS = DOT_MS * 3
WORD_GAP_MS   = DOT_MS * 7

START = '-.-.-'      # KA: start-of-frame prosign
END   = '.-.-.'      # AR: end-of-frame prosign

sr = Pin(16, Pin.OUT)                      # SR: WE drive this ("I'm sending")
rr = Pin(17, Pin.IN, Pin.PULL_DOWN)        # RR: we READ this (receiver ready)
# PULL_DOWN: if the wire is loose, RR reads 0 (not ready) -- safe default.


def transmit_pattern(pattern):
    for symbol in pattern:
        if symbol == '.':
            hw.set_led_timed(True, DOT_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)
        elif symbol == '-':
            hw.set_led_timed(True, DASH_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)
    hw.set_led_timed(False, LETTER_GAP_MS)

def transmit_frame(text):
    """Blink START, the message, then END, so the receiver knows the bounds."""
    transmit_pattern(START)
    for item in encode_message(text):
        if item == ' ':
            hw.set_led_timed(False, WORD_GAP_MS)
        else:
            transmit_pattern(item)
    transmit_pattern(END)


# =============================================================================
# BRING IT UP IN STAGES (do these in order):
#
# ANCHOR — handshake wires only (no light yet). Replace the transmit call in
#   the loop with a single blink, e.g. hw.set_led_timed(True, 300);
#   hw.set_led_timed(False, 300). Confirm: this board only blinks AFTER the RX
#   board asserts RR. That proves the wires + shared GND work.
#
# GUIDED — real transmission. Use transmit_frame(message) as written below.
#
# EXTENSION — wait for an ACK. After sending, the RX board drops RR while it
#   processes, then raises it again. Wait for that low->high before the next
#   send (see the TODO).
#
# STRETCH — retry: if RR doesn't come back high within ~3 s, re-send the frame
#   (up to 3 attempts), then report a failure.
# =============================================================================

print("TX board:", hw.get_board_info())
sr.value(0)
message = "SOS HELP"

while True:
    print("Waiting for receiver ready (RR high)...")
    while rr.value() == 0:
        utime.sleep_ms(10)

    sr.value(1)                 # tell the receiver: I'm about to send
    utime.sleep_ms(300)         # give the receiver a moment to start listening
    print("Transmitting:", message)
    transmit_frame(message)     # GUIDED
    sr.value(0)                 # done sending

    # TODO (EXTENSION): wait for the receiver's ACK before sending again:
    #   while rr.value() == 1: utime.sleep_ms(5)   # RR dropped = "got it / busy"
    #   while rr.value() == 0: utime.sleep_ms(5)   # RR back up = "ready again"
    utime.sleep_ms(2500)
