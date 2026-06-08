# Build-an-AI-Tutor 🤖 — Week 4
## if Statements
### Your prompting skill this week: **Few-shot examples**

Last week you *described* an exact turn format — and the tutor still drifted out of it
after a few turns. This week you stop describing and start **showing**: you give the
tutor worked examples to copy.

---

## The idea in one minute

Same loop: write a prompt, paste it in a fresh chat, practice. Stop when:

- 🟢 You answer **8 questions correctly** with no misbehavior → **it passed.**
- 🔴 The tutor **breaks** (see the checklist) → **stop and note where.**

> Graded on **prompt + analysis**, never the outcome. This week your format should
> finally stick — so watch a different failure: whether the tutor actually **judges
> your answers correctly**, or just keeps saying "Correct."

---

## Part A — What your tutor may quiz you on (the scope)

**In scope (Weeks 1–4):** everything so far (variables, types, f-strings, lists,
for-loops, tuples), **plus**
- `if` / `elif` / `else`
- comparison operators — `==`, `!=`, `<`, `>`, `<=`, `>=`
- boolean logic — `and`, `or`, `not`
- membership — `"a" in mylist`, `"x" not in mylist`
- an `if` *inside* a `for` loop (both are in scope now)

**Out of scope** (a quiz on these = a **break**, rule B2): `while` loops, dictionaries,
input, functions, files.

> 🧩 *Project tie-in:* Week 4 of the Morse lab uses `if`/`elif` to **classify a symbol**
> (dot vs. dash vs. space) and decide what to transmit — exactly this material.

## Part B — This week's skill: **Few-shot examples**

"Zero-shot" prompting = you *tell* the AI what to do. **Few-shot** = you *show* it, with
one or more worked examples of the behavior you want. Models imitate examples far more
reliably than they follow descriptions — which is why few-shot fixes the format drift
from Week 3.

But there's a catch you'll discover this week: **the tutor imitates exactly what your
examples demonstrate.** If every example shows a *correct* answer being praised, the
tutor learns to praise *everything*. Good few-shot examples have to cover the cases you
care about — including a **wrong** answer and a **partially-right** one.

Add a few **example turns** to your prompt. Show the exact format *and* show the tutor
judging different kinds of answers.

*Shape to start from (write your own — and decide which cases to demonstrate):*
```
You are a strict, encouraging Python tutor for a beginner.
Rules:
1. Ask ONE question per turn, then wait for my answer.
2. Never reveal the answer in the same message as a question.
3. Only quiz variables, types, f-strings, lists, for-loops, tuples, and if-statements.

After I answer, reply in EXACTLY this format:
Verdict: <Correct / Partly / Not quite>
Why: <one short line>
Next question: <the next question>

Examples of how to respond:
---
Me: 3
You:
Verdict: Correct
Why: range(1,4) is 1,2,3 — three numbers.
Next question: What does `5 > 3` evaluate to?
---
(add more examples — including a WRONG answer marked "Not quite" — yourself)
```

## Part C — Do it

1. Write your **prompt with example turns** (few-shot).
2. Open a **brand-new** chat and paste it in.
3. Practice **honestly** — and consider deliberately giving one slightly-wrong or vague
   answer to test whether the tutor catches it. Stop at the first break, or at **8
   correct** with no break.

**What a working tutor must do this week (cumulative spec):**

| Rule | The tutor must… |
|------|-----------------|
| **B1** | act like a tutor, not a lecturer or answer key |
| **B2** | quiz only Weeks 1–4 constructs (Part A) |
| **B3** | make you answer — no handing over the answer first |
| **B4** | be correct in any Python it writes or claims |
| **S2** | one question per turn; never reveal the answer in the same message |
| **S3** | follow the same fixed turn shape every time |
| **S4** | **judge answers correctly** — catch wrong answers, don't accept vague/hand-wavy ones, and handle partially-correct answers fairly ⬅️ *new this week* |

**It "broke" if it does any of these:**

- [ ] marked a wrong answer "Correct" *(S4)*
- [ ] accepted a vague or hand-wavy answer as fully correct *(S4)*
- [ ] marked a correct answer "wrong" *(S4)*
- [ ] mishandled a partially-correct answer (all-or-nothing when it shouldn't be) *(S4)*
- [ ] broke the format, asked two questions, or revealed an answer *(S3 / S2)*
- [ ] quizzed out of scope, e.g., a `while` loop *(B2)*
- [ ] wrote/claimed wrong Python *(B4)*

> 💡 The easiest way to find this week's break is to **answer one question imperfectly
> on purpose** and see whether the tutor calls it.

## Part D — What to hand in (one PDF or doc)

1. **Your prompt** — verbatim (including your example turns).
2. **The full conversation** — whole thing, start to finish, **not trimmed**.
3. **Your justification memo** — a few sentences each:
   - **a.** What example turns did you include, and which cases did they cover?
   - **b.** Did it **break** or **pass 8**? **Quote the exact turn** where it broke. If a
     message limit ended the session, say where and which model you were on.
   - **c.** Which rule (B1–B4, S2, S3, or **S4**) did the break violate? Why?
   - **d.** What **one change** would prevent it? *(Hint: which kind of example were you
     missing?)*
   - **e.** One thing the tutor did **well**.

---

## How you'll be graded (20 points)

Craft and analysis — **never** the outcome.

| What we look at | Pts |
|-----------------|----:|
| Your prompt uses this week's skill (real **example turns**) | 4 |
| Full, unedited conversation included | 4 |
| You pinpoint the **first** break and quote it (or document a real 8-correct run) | 4 |
| Analysis names the right rule **and** proposes a fix that would work | 6 |
| The answers **you** typed are correct (or you flag your own mistakes) | 2 |
| **Total** | **20** |

---

## 📋 A worked example — what a strong submission looks like

*A model so you can see the shape. **Write your own prompt** — don't copy this one.*

### The student's prompt (few-shot — but only "Correct" examples)
```
You are a strict, encouraging Python tutor for a beginner.
Rules:
1. Ask ONE question per turn, then wait.
2. Never reveal the answer in the same message as a question.
3. Only quiz variables, types, f-strings, lists, for-loops, tuples, and if-statements.

After I answer, reply in EXACTLY this format:
Verdict: <Correct or Not quite>
Why: <one short line>
Next question: <the next question>

Examples:
---
Me: 3
You:
Verdict: Correct
Why: range(1,4) is 1,2,3 — three numbers.
Next question: What does ("dot","dash")[0] return?
---
Me: "dot"
You:
Verdict: Correct
Why: Index 0 is the first item.
Next question: What does `5 > 3` evaluate to?
---
```

### The conversation (excerpt)

**AI:** What does `5 > 3` evaluate to?
**Student:** True
**AI:**
> Verdict: Correct
> Why: 5 is greater than 3, so the comparison is True.
> Next question: Is `"a" in ["a", "b", "c"]` True or False?

**Student:** True
**AI:** *(…two more clean, correctly-formatted turns…)*

**AI:**
> Next question: When does the `else` block run in an `if/else`?

**Student:** when the if is done

**AI:**
> Verdict: Correct
> Why: Right — the else comes after the if.
> Next question: What does `not (3 > 5)` evaluate to?

**Student:** I stopped here — "when the if is done" is wrong, and it said Correct.

### The student's justification memo

- **a.** I gave two example turns showing the exact format. Both examples showed a
  *correct* answer being marked "Correct."
- **b.** The **format held perfectly** the entire time — last week's drift is gone. But
  it **broke on judging at Q5.** I answered *"when the if is done"* for when `else` runs,
  which is wrong (it runs when the `if` condition is **False**), and it replied
  *"Verdict: Correct."*
- **c.** That violates **S4 (judge answers correctly).** I think the cause is my
  few-shot: every example I gave showed a *correct* answer being praised, so the tutor
  learned to praise and move on — it never saw what "Not quite" should look like.
- **d.** Add example turns that show a **wrong** answer getting "Not quite" with a
  correction, and a **partial** answer handled strictly. Few-shot examples have to cover
  the cases you care about, not just the happy path. *(Also: it never told me my running
  score — I had to count myself. That's next week's job.)*
- **e.** The format was rock-solid on every single turn — the examples fixed last week's
  drift completely.

### Why this submission is strong
It proves few-shot solved the Week 3 format problem, isolates the **judging** break and
quotes it, correctly names **S4**, and — crucially — diagnoses *why* (examples only
covered the happy path). The fix is the real few-shot lesson, and the score-tracking
aside teases Week 5.

---

## 🛠️ Using free ChatGPT — quick reminders

- **New chat** every attempt. **It's random** — same prompt, different results.
- **Hit a message limit or got switched to a lighter model?** Valid place to stop — note
  where it happened and which model you were on.
- **Go off-peak** if you can. **Copy the conversation out before you close the tab.**

## ✅ Honest-work reminder
Build the tutor, then answer its questions **yourself** (a deliberately-imperfect answer
to *test* the tutor is fair game — just say so in your memo). The full, unedited
transcript is how we keep it fair.
