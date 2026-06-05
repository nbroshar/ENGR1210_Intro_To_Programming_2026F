# =============================================================================
# ENGR1210 — Week 15 (STAGE 3): Two-Board Link — RECEIVER
# This is the RX board's main.py.
#
# It drives RR ("I'm ready"), waits for the sender to raise SR, then reads the
# light pulses, rebuilds letters, and validates the frame by its START/END
# prosigns. The decode pipeline is the same one from Weeks 12 and 14.
#
# WIRING (mirror of the sender; full picture in week15_link_guide.md):
#   RX GP16 (SR in)   <-  TX GP16 (SR out)
#   RX GP17 (RR out)  ->  TX GP17 (RR in)
#   RX GND <-> TX GND                          <-- REQUIRED shared ground.
#   RX light sensor   <- aimed at -  TX LED    (wireless data channel)
#   Sensor divider into GP26 (ADC0), as in Week 14.
# =============================================================================

from morse_decoder import decode_pattern
from machine import ADC, Pin
import utime

DOT_MS = 100
SYMBOL_GAP_MAX = DOT_MS * 2
LETTER_GAP_MAX = DOT_MS * 5

START = '-.-.-'
END   = '.-.-.'

rr = Pin(17, Pin.OUT)                      # RR: WE drive this ("ready")
sr = Pin(16, Pin.IN, Pin.PULL_DOWN)        # SR: we READ this (sender sending)
sensor = ADC(Pin(26))
LIGHT_THRESHOLD = 30000                    # calibrate as in Week 14

def is_lit():
    return sensor.read_u16() > LIGHT_THRESHOLD

def classify_pulse(ms):
    return 'dot' if ms < DOT_MS * 2 else 'dash'

def classify_gap(ms):
    if ms < SYMBOL_GAP_MAX:
        return 'symbol_gap'
    elif ms < LETTER_GAP_MAX:
        return 'letter_gap'
    else:
        return 'word_gap'

def time_one_pulse():
    while not is_lit():
        utime.sleep_ms(2)
    start = utime.ticks_ms()
    while is_lit():
        utime.sleep_ms(2)
    return utime.ticks_diff(utime.ticks_ms(), start)

def gap_until_next_pulse(timeout_ms):
    start = utime.ticks_ms()
    while not is_lit():
        if utime.ticks_diff(utime.ticks_ms(), start) >= timeout_ms:
            return timeout_ms
        utime.sleep_ms(2)
    return utime.ticks_diff(utime.ticks_ms(), start)


def receive_frame():
    """Read light until the END prosign. Return the decoded text, or None if a
    valid frame (START ... END) was never seen."""
    started = False
    message = ""
    pattern = ""
    while True:
        pulse_ms = time_one_pulse()
        pattern += '.' if classify_pulse(pulse_ms) == 'dot' else '-'
        kind = classify_gap(gap_until_next_pulse(LETTER_GAP_MAX))
        if kind != 'symbol_gap':                 # a letter just finished
            if pattern == START:
                started = True                   # frame begins
            elif pattern == END:
                return message if started else None   # frame ends
            elif started:
                message += decode_pattern(pattern)
                if kind == 'word_gap':
                    message += ' '
            pattern = ""


# =============================================================================
# BRING IT UP IN STAGES (match the sender's stages):
#
# ANCHOR — handshake only. Set rr.value(1), then loop printing sr.value().
#   Confirm the sender only acts after you assert RR, and that you see SR go
#   high when it sends. That proves the two wires + shared GND.
#
# GUIDED — real reception. Use receive_frame() as in the loop below; print it.
#
# EXTENSION — ACK back to the sender: after a good frame, drop RR (busy), print
#   the message, then raise RR again (ready for the next). The sender waits for
#   that low->high (its EXTENSION step).
#
# STRETCH — reject bad frames: receive_frame returns None if it never saw a
#   START; print a "frame error" instead of garbage, and keep listening.
# =============================================================================

print("RX board ready. Asserting RR, waiting for sender...")
rr.value(1)                                  # I'm ready to receive

while True:
    while sr.value() == 0:                   # wait for the sender to start
        utime.sleep_ms(10)

    print("SR high -> receiving...")
    msg = receive_frame()                    # GUIDED

    rr.value(0)                              # ACK / busy while we handle it
    if msg is None:
        print("frame error (no valid START/END)")
    else:
        print("received:", repr(msg))
    utime.sleep_ms(500)
    rr.value(1)                              # ready for the next frame
