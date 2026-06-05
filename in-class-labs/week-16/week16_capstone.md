# Week 16 — Capstone: Integration, Test & Demo

You've built every piece: a codebook, an encoder and decoder, a transmitter, a
light receiver, and a wired handshake. This week you put them together, prove
they work with a real test plan, and demo a message crossing from one Pico to
another.

## 1. The whole system, in one sentence
Type a message on the sender -> it's encoded -> blinked on an LED -> read by a
light sensor on the other board -> decoded back to text, with the two boards
agreeing over wires on when to talk.

## 2. Integrate
- Sender = `week15_tx.py` as `main.py` on board A (+ `morse_codebook.py`,
  `morse_encoder.py`, `hal_pico.py`).
- Receiver = `week15_rx.py` as `main.py` on board B (+ `morse_codebook.py`,
  `morse_decoder.py`).
- Wire and calibrate per `week15_link_guide.md`.
- Optional polish: let the sender pick the message from a button (Week 11) or
  from `input()` over the USB serial REPL.

## 3. Test plan — run these and record PASS/FAIL

| # | Test | Input | Expected result |
|---|------|-------|-----------------|
| 1 | Happy path | send "SOS" | receiver prints "SOS" |
| 2 | Two words | send "SOS HELP" | receiver prints "SOS HELP" (one space) |
| 3 | Every letter | send "THE QUICK BROWN FOX" | decoded text matches |
| 4 | Repeat | send the same message 5x | all 5 arrive correctly |
| 5 | Handshake gate | start sender BEFORE pressing RX ready | sender waits; nothing sends until RX is ready |
| 6 | ACK / flow | send back-to-back | sender waits for RR to cycle between frames |
| 7 | Light blocked | cover the sensor mid-message | receiver reports a frame error, not garbage; recovers on the next frame |
| 8 | Ground pulled | remove the shared GND wire | link fails (document it — this is WHY GND matters) |
| 9 | Timing edge | speed the sender up until it breaks | find the fastest reliable DOT_MS; note the limit |

Keep a simple log: test #, what you sent, what arrived, pass/fail, notes.
Test 7 and 8 are the important ones — a system that fails *safely* and *visibly*
is better than one that silently lies.

## 4. No second board? Single-board loopback fallback
You can test the full pipeline on ONE Pico by pointing its own LED at its own
sensor and tying RR to SR through a wire (or asserting both in code). Same
`transmit_frame` -> light -> `receive_frame`, decoded on the same board. Good
for debugging before you pair up.

## 5. Demo checklist (what "done" looks like)
- [ ] Grounds tied; handshake verified with the lights off (ANCHOR step).
- [ ] Sensor calibrated; threshold written down.
- [ ] "SOS" sends and decodes correctly, board to board.
- [ ] A multi-word message round-trips.
- [ ] Blocking the light produces a clean frame error, then recovers.
- [ ] You can explain: where data is wireless, where control is wired, and the
      ONE line that changed between PC, Wokwi, and hardware.

## 6. Acceptance criteria (suggested grading)
- Encodes/decodes correctly in software (Stages 1) .......... carried from earlier
- Runs in Wokwi with the LED blinking Morse (Stage 2) ....... pass/fail
- Receiver decodes real light on hardware (Week 14) ......... pass/fail
- Two boards exchange a framed message with the handshake ... pass/fail
- Handles a blocked-light error without crashing ........... pass/fail
- Team can explain the HAL and the data/control split ...... oral

## 7. Where this goes next (optional extensions)
- Add a checksum (send the letter count as a digit before END) and have the
  receiver verify it.
- Bidirectional: give each board both an LED and a sensor for two-way chat.
- Variable speed: negotiate DOT_MS during the handshake.
