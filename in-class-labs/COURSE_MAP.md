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


==============================================================================
## STAGE 1 — The simulated translator (Weeks 1-9)
Everything runs on the PC. The "LED" is a printed line / the stub. This is
where students learn Python and debugging by building something real.

**Week 1 — Variables & Types** 
  Build: timing constants, project metadata.        Lab: week1_lab.py 

**Week 2 — Lists** 
  Build: the codebook as parallel lists.            Lab: week2_lab.py 

**Week 3 — Loops & Tuples** 
  Build: codebook as tuples; encode with a loop.    Lab: week3_lab.py

**Week 4 — if Statements** 
  Build: classify symbols; robust encode (spaces,
  case, unknowns); transmit decisions.              Lab: week4_lab.py 

**Week 5 — Dictionaries** 
  Build: encode map + reverse decode map.           Lab: week5_lab.py 

**Week 6 — Input & while Loops** 
  Build: interactive translator; receiver pulse/
  gap classification.                               Lab: week6_lab.py 

**Week 7 — Functions: The Great Refactor** 
  Build: wrap inline code into functions, split into
  modules, meet the HAL (hal_stub). Heaviest week.  Lab: week7_lab.py 

**Week 8 — Files & Exceptions** 
  Build: save config + session log; try/except;
  wire it together in main().                       Lab: week8_lab.py 

**Week 9 — The Protocol (in simulation)** — STAGE 1 CAPSTONE
  Build: the sender/receiver handshake state machine,
  message framing, and a loopback self-test — all on
  the PC stub. The whole translator now works end to
  end in simulation.                                Lab: protocol_lab.py 
  Milestone: a complete, tested translator running on the stub.

==============================================================================
## STAGE 2 — The Wokwi emulator (Weeks 10-12)
Same code, swap ONE line (import hal_stub -> import hal_pico), run on a
simulated Raspberry Pi Pico. No physical board required, so everyone can do it.

**Week 10 — Emulator bring-up**
  Build: blink test in Wokwi; swap to hal_pico; run the
  transmitter (main.py) blinking the simulated LED in
  Morse.                          Lab: week-10/ (bring-up Rung 2) 
  Milestone: your SOS blinks on the Wokwi Pico.

**Week 11 — Sending from the emulator**
  Build: add a pushbutton in Wokwi; read a GPIO input;
  press to transmit a chosen message; tune the timing
  so the blinks are clearly dot vs dash.            Lab: week11_lab.py 

**Week 12 — Receiving in the emulator**
  Build: feed the receiver real (emulated) pulse timings
  and run classify_pulse / classify_gap to decode a blink
  stream back into text; exercise the protocol logic with
  two simulated ready signals.                      Lab: week12_lab.py 
  Milestone: encode -> blink -> decode round trip, in the emulator.

==============================================================================
## STAGE 3 — Real hardware (Weeks 13-16)  — the last month
Flash the identical files to a physical Pico. Nothing in the code changes.

**Week 13 — Hardware bring-up**
  Build: install MicroPython; blink test on the real board;
  run the transmitter on the onboard (and an external) LED.
                                   Lab: week-13/ (bring-up Rung 3) 
  Milestone: your SOS blinks on a real Pico.

**Week 14 — The receiver on hardware**
  Build: wire a light sensor (phototransistor/LDR) aimed at
  the LED; measure REAL pulse durations; decode live blinks
  back into text.                                   Lab: week14_lab.py 
  Milestone: one Pico's blinks, read by a sensor, decode correctly.

**Week 15 — Two-device link (the handshake for real)**
  Build: connect two Picos; the SR/RR ready signals from
  Week 9 become real GPIO wires; send a framed message
  device-to-device with the handshake + ACK/retry.  Lab: week15_tx.py + week15_rx.py + guide 
  Milestone: a message travels from one board to another, coordinated.

**Week 16 — Integration, test & demo** — COURSE CAPSTONE
  Build: full end-to-end system; run a test plan; polish;
  present/demo.                                     Lab: week16_capstone.md 
  Milestone: a working two-Pico Morse link the team demos.

==============================================================================
## Notes & levers

- Weeks 1-8 are fixed and mirror the Bug-of-the-Week concepts. Don't move them.

- If need labs to be shorter than 16 weeks (breaks, a midterm,
  exam week), the easiest places to flex are:
    * merge Week 11 + Week 12 into a single "full system in Wokwi" week,
    * or treat Week 16 as the slack/catch-up week.

- The heaviest single week is Week 7 (functions + modules + the HAL all at
  once). 


## Folder mapping (by week)
  week-01 .. week-08            -> Weeks 1-8   (Python basics)
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
  on a real Pico (Rung 3). 
==============================================================================
