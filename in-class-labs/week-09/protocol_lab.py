# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Protocol Week (Capstone): The Morse Handshake Protocol (MHP)
#
# Everything so far assumed the sender just starts blinking and hopes the
# receiver is watching. Real links don't work that way — both sides must
# AGREE that they're ready before any data moves. That agreement is a
# "handshake," and building one is this capstone.
#
# Two one-bit signals coordinate the link:
#   RR (Receiver Ready) — driven by the receiver: "I'm listening."
#   SR (Sender Ready)   — driven by the sender:   "I'm transmitting."
#
# On real hardware these are two GPIO wires; here we simulate them in
# software so you can watch the state machine work. This capstone uses the
# functions and modules you built in Weeks 7-8.
# =============================================================================

from morse_encoder import encode_message
from morse_decoder import decode_message
import hal_stub as hw

# Prosigns: special Morse "control" patterns that aren't letters.
START = '-.-.-'    # KA — start of message
END   = '.-.-.'    # AR — end of message

# --- Simulated handshake lines (on a Pico these are two GPIO pins) -----------
_RR_READY = False   # receiver ready
_SR_READY = False   # sender ready

def assert_receiver_ready():
    global _RR_READY; _RR_READY = True

def assert_sender_ready():
    global _SR_READY; _SR_READY = True

def reset_lines():
    global _RR_READY, _SR_READY; _RR_READY = False; _SR_READY = False


# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — The Handshake State Machine")
print("=" * 52)

# Given the two ready lines, the link is in exactly one of four states.
# A function reads the lines and reports the state. (if/elif over state.)
def handshake_state():
    """Return the current link state from the two ready signals."""
    if not _RR_READY and not _SR_READY:
        return "IDLE"
    elif _RR_READY and not _SR_READY:
        return "RECEIVER_READY"
    elif _RR_READY and _SR_READY:
        return "LINKED"
    else:
        return "SENDER_WAITING"   # sender ready but receiver isn't (bad)

# Walk the normal startup sequence and print each transition.
reset_lines()
print(f"  Step 1: {handshake_state():<15} both sides booting")
assert_receiver_ready()
print(f"  Step 2: {handshake_state():<15} receiver says 'I'm listening'")
assert_sender_ready()
print(f"  Step 3: {handshake_state():<15} sender joins -> ready to transmit")

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. Why must the RECEIVER assert ready BEFORE the sender starts? What is
#     lost if the sender transmits while the link is still IDLE?
# Q2. "SENDER_WAITING" means the sender is ready but the receiver isn't.
#     Why is that an error state worth naming instead of just transmitting?
# Q3. This is a "state machine": a small set of named states and the rules
#     for moving between them. Where else in the project did you write
#     if/elif logic that was secretly a state machine? (Hint: gaps.)


# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Loopback Test")
print("=" * 52)

# A loopback test sends a message to ourselves: encode it, "transmit" it,
# decode it, and confirm we got the original back — but ONLY once the link
# is LINKED. Complete the function.
def loopback_test(message):
    """Encode->decode 'message' over a LINKED handshake; return True if it
    survived the round trip."""
    reset_lines()
    assert_receiver_ready()
    assert_sender_ready()

    # TODO Step 1: guard on the handshake. If handshake_state() is not
    #   "LINKED", print a refusal and return False.

    # TODO Step 2: encode the message, then decode it back.
    #   encoded = encode_message(message)
    #   decoded = decode_message(encoded)

    # TODO Step 3: compare decoded to message.upper(); print PASS/FAIL and
    #   return whether they matched.
    return False    # TODO: replace with the real result

# (When complete, this should print PASS for "SOS HELP".)
loopback_test("SOS HELP")


# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — Framing a Message")
print("=" * 52)

# Raw patterns have no boundaries — the receiver can't tell where a message
# begins or ends. We FRAME it: a START prosign, the payload, an END prosign,
# plus a checksum (how many letters to expect) so a dropped letter is caught.
#
# Worked: build a frame for "OK".
def frame_message(text):
    """Wrap encoded text with START/END prosigns and a letter count."""
    payload = encode_message(text)
    letter_count = len([p for p in payload if p != ' '])
    return [START] + payload + [END], letter_count

frame, count = frame_message("OK")
print(f"  Framed 'OK': {frame}")
print(f"  Checksum (letters expected): {count}")

# -- YOUR EXTENSION --------------------------------------------------------
# Write receive_frame(frame, expected_count) that:
#   1. confirms frame[0] == START and frame[-1] == END (else report a bad frame)
#   2. decodes the middle (frame[1:-1]) back to text
#   3. checks the decoded letter count matches expected_count
#   4. returns the decoded text if everything checks out, else None
# Test it by framing a word and immediately receiving it back.

# TODO: write and test receive_frame()


# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Acknowledge and Retry")
print("=" * 52)

# Real protocols don't just hope a message arrived — the receiver ACKs it.
#   1. Add an ACK: after receive_frame() succeeds, have the receiver "send"
#      a single prosign back (e.g. 'R' = .-.) meaning "received OK."
#   2. Add a retry: if the checksum fails, the sender re-sends the frame,
#      up to 3 attempts, before giving up. Use a while loop with a counter.
#   3. Two-device version: with the HAL swap (import hal_pico as hw) and a
#      classmate's Pico, the RR/SR lines become real wires. Describe how
#      your software state machine maps onto two physical signals.

# TODO: implement a stretch item


# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    walked IDLE -> RECEIVER_READY -> LINKED; answered Q1-Q3
#   [ ] GUIDED:    loopback_test("SOS HELP") prints PASS
#   [ ] EXTENSION: receive_frame() validates prosigns + checksum
#   [ ] STRETCH:   (optional) ACK and retry logic
#   [ ] I can explain why a handshake must happen BEFORE data moves
#
# YOU BUILT A COMPLETE SYSTEM:
#   data (codebook) -> encode -> transmit (HAL) -> receive -> decode,
#   with saved settings, a session log, error handling, and a real protocol
#   to coordinate two devices. That's a genuine embedded communication stack.
# =============================================================================
