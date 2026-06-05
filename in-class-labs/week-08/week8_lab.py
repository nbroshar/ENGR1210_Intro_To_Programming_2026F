# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 8 Lab: Files and Exceptions
# Chapter 10 — Python Crash Course, 3rd Edition
#
# The project is now real modules. This week you make it remember things
# between runs (files) and survive things going wrong (exceptions), then
# wire the whole pipeline together in one main() function.
#
# USES THE MODULES YOU BUILT:
#   morse_codebook.py, morse_encoder.py, morse_decoder.py, hal_stub.py
#
# DATA FILES (created at runtime by this script):
#   config.json        — saved settings (e.g. dot length, callsign)
#   session_log.json   — a growing list of what you've translated
# =============================================================================

import json
from morse_encoder import encode_message
from morse_decoder import decode_message
import hal_stub as hw

CONFIG_FILE = 'config.json'
LOG_FILE    = 'session_log.json'

DEFAULT_CONFIG = {"dot_ms": 100, "callsign": "STUDENT", "board": "PC"}


# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
# Reading a file can fail two ways: the file isn't there (FileNotFoundError),
# or it's there but corrupt (bad JSON). load_config() handles BOTH and always
# returns a usable config. Study the try / except / else structure.
#
# PORTABILITY NOTE: corrupt JSON raises json.JSONDecodeError on your PC, but
# that name doesn't exist on a MicroPython Pico. JSONDecodeError is a kind of
# ValueError, so catching ValueError works in BOTH places — that's why we
# catch ValueError here.

def load_config():
    """Return the saved config, or sensible defaults if it can't be read."""
    try:
        with open(CONFIG_FILE) as f:
            data = json.load(f)
    except FileNotFoundError:
        print("  No config file yet — using defaults.")
        return dict(DEFAULT_CONFIG)
    except ValueError:                      # corrupt JSON (portable form)
        print("  Config file is corrupt — using defaults.")
        return dict(DEFAULT_CONFIG)
    else:
        return data                          # only runs if no exception


# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. Why return a COPY (dict(DEFAULT_CONFIG)) instead of DEFAULT_CONFIG
#     itself? (Think back to the mutable-default bug in Bug-of-the-Week 7.)
# Q2. What goes in the 'else' block, and how is it different from 'finally'?
# Q3. Why is "use defaults and keep running" usually better here than
#     letting the program crash with a traceback?


# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
# Now WRITE the file instead of reading it. save_config() should write the
# config dict to config.json, and log_session() should append one record to
# session_log.json.

def save_config(config):
    """Write the config dictionary to CONFIG_FILE as JSON."""
    # TODO: open CONFIG_FILE for writing ('w') and json.dump(config, f).
    # Wrap it in try/except OSError so a disk/permission problem prints a
    # message instead of crashing. Print a confirmation on success (else).
    pass    # TODO


def log_session(original, encoded, decoded):
    """Append one translation record to session_log.json."""
    # A log is a LIST of records. We read what's there, add one, write it back.
    record = {"text": original, "morse": " ".join(encoded), "decoded": decoded}

    # TODO Step 1: load the existing log into a list called 'log'.
    #   Reuse the load pattern: try to open LOG_FILE and json.load it;
    #   on FileNotFoundError OR ValueError, start with an empty list  log = []
    log = []    # TODO: replace with the try/except load

    # TODO Step 2: append 'record' to 'log', then write 'log' back to
    #   LOG_FILE with json.dump (wrap the write in try/except OSError).


# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
# main() ties the whole project together: load settings, encode a message,
# transmit it through the HAL, decode it back, and log the session.
# This is the top-level "wiring" — every other file is a module it calls.

def main():
    config = load_config()
    print(f"\n[{config['callsign']}] translator on board: {config['board']}")

    message = "SOS"
    encoded = encode_message(message)
    decoded = decode_message(encoded)

    print(f"  text:    {message}")
    print(f"  morse:   {' '.join(encoded)}")
    print(f"  decoded: {decoded}")

    # Briefly show the HAL transmitting the first letter.
    print("  transmit first letter:")
    for symbol in encoded[0]:
        hw.set_led_timed(True, config['dot_ms'] if symbol == '.' else config['dot_ms'] * 3)
        hw.set_led_timed(False, config['dot_ms'])

    # TODO: call log_session(message, encoded, decoded) so this run is saved.
    #       Then run the program twice and open session_log.json — you should
    #       see TWO records. That is your program "remembering" across runs.


# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
# 1. PORTABILITY: right now file reading/writing uses open() directly. On a
#    Pico you want the SAME calls to work. Add read_file(name) and
#    write_file(name, text) to hal_stub.py, route config/log through the HAL,
#    and note what hal_pico.py would do differently. Why does putting file
#    I/O behind the HAL matter for "one program, two devices"?
#
# 2. Make the corrupt-file case real: hand-edit config.json to invalid JSON,
#    run main(), and confirm it recovers with defaults instead of crashing.
#
# 3. WOKWI / PICO: with the HAL swap (import hal_pico as hw), the same main()
#    blinks a real LED on a simulated Pico at wokwi.com. List which files
#    change for the move to hardware. (Answer: only the import line.)

# TODO: implement a stretch item


# =============================================================================
# DEMO BLOCK — __main__ guard, same pattern as Week 7 and the bug files.
# =============================================================================
if __name__ == "__main__":
    print("=" * 52)
    print("SECTION 1: ANCHOR — load_config()")
    print("=" * 52)
    cfg = load_config()
    print(f"  loaded config: {cfg}")

    print("\n" + "=" * 52)
    print("SECTION 3: EXTENSION — main() pipeline")
    print("=" * 52)
    main()


# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    load_config() returns defaults when no file exists; Q1-Q3
#   [ ] GUIDED:    save_config() writes config.json; log_session() appends
#   [ ] EXTENSION: main() logs each run; two runs => two records in the log
#   [ ] STRETCH:   (optional) file I/O routed through the HAL; corrupt-file
#                  recovery tested; Wokwi/Pico swap identified
#   [ ] I can name the two ways reading a file can fail, and how I caught both
#
# LOOKING AHEAD — Protocol Week (capstone)
#   You can encode, transmit, decode, save, and recover. The last piece is
#   getting TWO devices to agree on WHEN to talk — the Morse Handshake
#   Protocol. That's the capstone.
# =============================================================================
