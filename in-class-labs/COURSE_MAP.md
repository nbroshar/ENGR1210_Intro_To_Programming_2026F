# ENGR1210 — 16-Week Course Map
## Morse Code Translator, in three stages

The project runs the whole semester and climbs one ladder: build it in
simulation, prove it in an emulator, then run it on real hardware. The Python
you need is taught just-in-time, one idea per week, against the project.

```
STAGE 1  Weeks 1-9    Build the SIMULATED translator (learn Python + debugging)
STAGE 2  Weeks 10-12  Bring it up in the WOKWI emulator
STAGE 3  Weeks 13-16  Bring it up on REAL HARDWARE   <-- the last month
```

Parallel track (unchanged, you maintain it separately): the **Bug of the
Week** exercises run alongside Weeks 1-8 and mirror each week's Python concept.
Weeks 1-8 of the labs are built to line up with them, so that pairing stays
intact — no changes here.

A "Lab:" line marked **[have]** is a file you already have; **[to build]**
is new content for the hardware/emulator stages (the gaps to fill next).

==============================================================================
## STAGE 1 — The simulated translator (Weeks 1-9)
Everything runs on the PC. The "LED" is a printed line / the stub. This is
where students learn Python and debugging by building something real.

**Week 1 — Variables & Types** (PCC Ch 2)
  Build: timing constants, project metadata.        Lab: week1_lab.py [have]

**Week 2 — Lists** (Ch 3)
  Build: the codebook as parallel lists.            Lab: week2_lab.py [have]

**Week 3 — Loops & Tuples** (Ch 4)
  Build: codebook as tuples; encode with a loop.    Lab: week3_lab.py [have]

**Week 4 — if Statements** (Ch 5)
  Build: classify symbols; robust encode (spaces,
  case, unknowns); transmit decisions.              Lab: week4_lab.py [have]

**Week 5 — Dictionaries** (Ch 6)
  Build: encode map + reverse decode map.           Lab: week5_lab.py [have]

**Week 6 — Input & while Loops** (Ch 7)
  Build: interactive translator; receiver pulse/
  gap classification.                               Lab: week6_lab.py [have]

**Week 7 — Functions: The Great Refactor** (Ch 8)
  Build: wrap inline code into functions, split into
  modules, meet the HAL (hal_stub). Heaviest week.  Lab: week7_lab.py [have]

**Week 8 — Files & Exceptions** (Ch 10)
  Build: save config + session log; try/except;
  wire it together in main().                       Lab: week8_lab.py [have]

**Week 9 — The Protocol (in simulation)** — STAGE 1 CAPSTONE
  Build: the sender/receiver handshake state machine,
  message framing, and a loopback self-test — all on
  the PC stub. The whole translator now works end to
  end in simulation.                                Lab: protocol_lab.py [have]
  Milestone: a complete, tested translator running on the stub.

==============================================================================
## STAGE 2 — The Wokwi emulator (Weeks 10-12)
Same code, swap ONE line (import hal_stub -> import hal_pico), run on a
simulated Raspberry Pi Pico. No physical board required, so everyone can do it.

**Week 10 — Emulator bring-up**
  Build: blink test in Wokwi; swap to hal_pico; run the
  transmitter (main.py) blinking the simulated LED in
  Morse.                          Lab: week-10/ (bring-up Rung 2) [have]
  Milestone: your SOS blinks on the Wokwi Pico.

**Week 11 — Sending from the emulator**
  Build: add a pushbutton in Wokwi; read a GPIO input;
  press to transmit a chosen message; tune the timing
  so the blinks are clearly dot vs dash.            Lab: week11_lab.py [have]

**Week 12 — Receiving in the emulator**
  Build: feed the receiver real (emulated) pulse timings
  and run classify_pulse / classify_gap to decode a blink
  stream back into text; exercise the protocol logic with
  two simulated ready signals.                      Lab: week12_lab.py [have]
  Milestone: encode -> blink -> decode round trip, in the emulator.

==============================================================================
## STAGE 3 — Real hardware (Weeks 13-16)  — the last month
Flash the identical files to a physical Pico. Nothing in the code changes.

**Week 13 — Hardware bring-up**
  Build: install MicroPython; blink test on the real board;
  run the transmitter on the onboard (and an external) LED.
                                   Lab: week-13/ (bring-up Rung 3) [have]
  Milestone: your SOS blinks on a real Pico.

**Week 14 — The receiver on hardware**
  Build: wire a light sensor (phototransistor/LDR) aimed at
  the LED; measure REAL pulse durations; decode live blinks
  back into text.                                   Lab: week14_lab.py [have]
  Milestone: one Pico's blinks, read by a sensor, decode correctly.

**Week 15 — Two-device link (the handshake for real)**
  Build: connect two Picos; the SR/RR ready signals from
  Week 9 become real GPIO wires; send a framed message
  device-to-device with the handshake + ACK/retry.  Lab: week15_tx.py + week15_rx.py + guide [have]
  Milestone: a message travels from one board to another, coordinated.

**Week 16 — Integration, test & demo** — COURSE CAPSTONE
  Build: full end-to-end system; run a test plan; polish;
  present/demo.                                     Lab: week16_capstone.md [have]
  Milestone: a working two-Pico Morse link the team demos.

==============================================================================
## Notes & levers (so you keep control of the calendar)

- Weeks 1-8 are fixed and mirror the Bug-of-the-Week concepts. Don't move them.

- If your real teaching calendar is shorter than 16 weeks (breaks, a midterm,
  exam week), the easiest places to flex are:
    * merge Week 11 + Week 12 into a single "full system in Wokwi" week,
    * or treat Week 16 as the slack/catch-up week.

- The heaviest single week is Week 7 (functions + modules + the HAL all at
  once). If you have a spare week, the cleanest split is:
    Week 7a = write the functions; Week 7b = extract them into modules + HAL.
    (This would push Files to a later week and break the 1-8 debug mirror, so
    only do it if you also shift the Bug-of-the-Week pairing.)

- ALL labs are now built. Stages 1-3 complete: Weeks 1-9 simulated,
  10-12 Wokwi, 13-16 hardware. The MicroPython labs (10-16) are syntax-
  checked and their pure logic is verified, but must be run in Wokwi / on a
  Pico to validate hardware behavior (pins, ADC, light, wiring).

## Folder mapping (zip folder -> week)
  week-01 .. week-08            -> Weeks 1-8   (Python basics, unchanged)
  week-09/                      -> Week 9   (protocol capstone, simulated)
  week-10/                      -> Week 10  (bring-up, Rung 2 = Wokwi)
  week-11/                      -> Week 11  (Wokwi: send on a button)
  week-12/                      -> Week 12  (Wokwi: receive by timing)
  week-13/                      -> Week 13  (bring-up, Rung 3 = real Pico)
  week-14/                      -> Week 14  (hardware: optical receiver)
  week-15/                      -> Week 15  (hardware: two-board link, tx+rx+guide)
  week-16/                      -> Week 16  (capstone: test plan + demo)

  Note: week-10 and week-13 are the SAME bring-up project (blink_test, main.py,
  the guide, the modules). Week 10 runs it in Wokwi (Rung 2); Week 13 runs it
  on a real Pico (Rung 3). Each folder's START_HERE.txt says which rung to do.
  Each week folder is self-contained -- it carries the modules/HAL it needs.
  instructor-answer-key/        -> finished Week 7 modules (answer key)
==============================================================================
