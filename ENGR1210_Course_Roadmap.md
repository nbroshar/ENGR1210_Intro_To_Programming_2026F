# ENGR 1210 — Course Roadmap

This is the map for ENGR 1210. Three projects run in parallel all term, but they are
really one arc: you **build** a real thing, you **prove** it's good, and you **direct**
an AI to help — without ever being fooled by it.

---

## The Arc — Three Threads, One Engineer

Everything this semester serves one goal: an engineer who can build it, prove it, and
direct the tools, including AI.

| Thread | Verb | What it is |
|---|---|---|
| **Morse Project** | **BUILD** | A real Morse code translator — from a PC simulation to a device that blinks SOS on actual hardware. Every Python idea earns its place here. |
| **Bug of the Week** | **PROVE** | Find bugs, then prevent them. Move from "does it run?" to "is it good?" with a professional's toolkit. |
| **AI Tutor** | **DIRECT** | Learn how AI really works and how to make it do exactly what you want — then verify everything it produces. |

---

## How They Connect — Learn It Once, Use It Three Ways

Every week centers on **one Python idea**. You don't learn it three times — you use it three ways:

- **Build with it** — put the week's concept to work in the Morse translator.
- **Prove it** — find the bugs it introduces, then test so they can't come back.
- **Direct it** — teach an AI the same concept, and learn exactly where it fails.

> **The spine:** *running ≠ working ≠ good — never trust code you haven't verified.*

---

## Two Acts

- **Act I · Foundations (Weeks 1–8).** One Python topic a week. Build it into the Morse
  project, break-and-fix it in Bug of the Week, and direct an AI on it. Three angles on
  the same idea.
- **Act II · Engineering (Weeks 9–16).** The threads converge. Morse moves to real
  hardware. Bug of the Week becomes code-quality engineering — and you turn those same
  tools on the code an AI writes. Finish with two capstones.

---

## The Whole Semester at a Glance

| Thread | Act I · Foundations (Weeks 1–8) | Act II · Engineering (Weeks 9–16) |
|---|---|---|
| **BUILD** · Morse Project | Simulate the Morse translator on a PC. | Wokwi emulator → a real Raspberry Pi Pico. |
| **PROVE** · Bug of the Week | Find bugs: read errors, debug, write tests. | Prevent them: coverage, complexity, lint, audit. |
| **DIRECT** · AI Tutor | Direct an AI tutor through 8 prompting skills. | Use AI to build a program — then audit it. |

**Destination → a Morse device that works, and an AI-built program you can vouch for.**

---

## Week by Week

### Week 1 — Variables & Simple Types · *Act I · Foundations*
- **Build (Morse):** Store text in variables; print the project banner with f-strings.
- **Prove (Bug of the Week):** Read the error: SyntaxError, NameError, TypeError.
- **Direct (AI):** Give an AI a role — and watch it default to giving answers.
- *This week → one idea — variables — built, debugged, and taught to an AI.*

### Week 2 — Lists · *Act I · Foundations*
- **Build (Morse):** Hold the Morse alphabet as lists of dots and dashes.
- **Prove (Bug of the Week):** IndexError, AttributeError — and your first logic bug.
- **Direct (AI):** Add explicit rules so the tutor quizzes instead of tells.
- *This week → lists power the translator, trip the debugger, and rein in the AI.*

### Week 3 — Loops & Tuples · *Act I · Foundations*
- **Build (Morse):** Loop across a message, letter by letter.
- **Prove (Bug of the Week):** Tell a logic error from an outright crash.
- **Direct (AI):** Pin the AI's reply to a fixed output format.
- *This week → repetition is where programs do work — and where bugs hide.*

### Week 4 — if Statements · *Act I · Foundations*
- **Build (Morse):** Branch on dot vs. dash; handle the space between words.
- **Prove (Bug of the Week):** Drive the VS Code debugger; set breakpoints.
- **Direct (AI):** Show the AI examples (few-shot) — and it imitates exactly.
- *This week → decisions add power, and add paths you'll have to test.*

### Week 5 — Dictionaries · *Act I · Foundations*
- **Build (Morse):** The heart of the translator: a letter → code dictionary.
- **Prove (Bug of the Week):** Design test cases: first, middle, last, edge.
- **Direct (AI):** Make the AI track score — and catch it miscounting.
- *This week → the dictionary is the engine; all three threads lean on it.*

### Week 6 — Input & while Loops · *Act I · Foundations*
- **Build (Morse):** Take a live message and translate it on demand.
- **Prove (Bug of the Week):** Hunt infinite loops and boundary cases.
- **Direct (AI):** Pre-load refusals; survive a prompt-injection attack.
- *This week → real input is messy — guard against it everywhere.*

### Week 7 — Functions · *Act I · Foundations*
- **Build (Morse):** Refactor into functions; hide hardware behind a HAL.
- **Prove (Bug of the Week):** Write pytest unit tests.
- **Direct (AI):** Get hints from the AI, not answers.
- *This week → functions are the unit you test, reuse, and reason about.*

### Week 8 — Files & Exceptions · *Act I · Foundations*
- **Build (Morse):** Save and load messages; handle a missing file.
- **Prove (Bug of the Week):** try / except — fail gracefully.
- **Direct (AI):** Make the AI verify its own work.
- *This week → the real world fails; good code expects it.*

### Week 9 — Protocol Capstone · *Act II · Engineering*
- **Build (Morse):** Lock the SOS protocol: timing, spacing, the full message.
- **Prove (Bug of the Week):** Test every branch — think in paths, not lines.
- **Direct (AI):** Capstone — prompt an AI to build a whole program.
- *This week → the simulation is built and proven — now the engineering begins.*

### Week 10 — The Emulator + Coverage · *Act II · Engineering*
- **Build (Morse):** Move to the Wokwi emulator: a virtual Pico and LED.
- **Prove (Bug of the Week):** Measure test coverage with pytest-cov.
- **Direct (AI):** Turn coverage on the AI's code — does every line run?
- *This week → from "it ran for me" to "every line is exercised."*

### Week 11 — Complexity (radon) · *Act II · Engineering*
- **Build (Morse):** Wire up the emulator; structure the firmware.
- **Prove (Bug of the Week):** Measure complexity with radon (A–F).
- **Direct (AI):** Grade the AI's code with radon — running ≠ good.
- *This week → working code can still be a tangled mess.*

### Week 12 — Refactoring · *Act II · Engineering*
- **Build (Morse):** Clean up the emulator code before hardware.
- **Prove (Bug of the Week):** Refactor safely: green tests first, then improve.
- **Direct (AI):** Refactor what the AI generated; keep the tests green.
- *This week → improve the shape without changing the behavior.*

### Week 13 — Readability (ruff) · *Act II · Engineering*
- **Build (Morse):** Flash real hardware: the Raspberry Pi Pico.
- **Prove (Bug of the Week):** Lint with ruff; make it readable.
- **Direct (AI):** Run ruff on AI code; fix the style it skipped.
- *This week → on real hardware, clear code is safe code.*

### Week 14 — DRY (Don't Repeat Yourself) · *Act II · Engineering*
- **Build (Morse):** Drive the physical LED and read the button.
- **Prove (Bug of the Week):** Kill duplication across the codebase.
- **Direct (AI):** Spot the AI's copy-paste; factor it out.
- *This week → duplication is a bug waiting to happen — twice.*

### Week 15 — Validation & Guard Clauses · *Act II · Engineering*
- **Build (Morse):** Handle real-world input from the hardware button.
- **Prove (Bug of the Week):** Validate inputs with guard clauses.
- **Direct (AI):** Harden AI code against the inputs it forgot.
- *This week → hardware meets messy reality; guard every edge.*

### Week 16 — Capstone Audit · *Act II · Engineering*
- **Build (Morse):** Capstone — your Morse device transmits SOS for real.
- **Prove (Bug of the Week):** Full audit: tests, coverage, complexity, lint.
- **Direct (AI):** Capstone — ship an AI-built program you can vouch for.
- *This week → two capstones, one engineer — it works, and it's good.*

---

## The Destination — Two Capstones, One Engineer

By Week 16 the three threads finish as two things you built and one habit you keep.

- **The Device — *it works.*** A Raspberry Pi Pico that transmits Morse for real — built,
  tested, and refactored from week-one variables up.
- **The Program — *it's good.*** An AI-generated program you prompted, then audited with
  the same tools: tests, coverage, radon, ruff.
- **The Habit — *you own it.*** Running ≠ working ≠ good. You never trust code — yours or
  an AI's — until you've proven it.
