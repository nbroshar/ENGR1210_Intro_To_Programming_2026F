# Build-an-AI-Tutor 🤖 — Week 3
## Loops & Tuples
### Your prompting skill this week: **Output structure**

Last week, explicit *rules* kept your tutor honest for a while — then it drifted and
slipped you an answer. This week you tighten the screws by controlling not just *what*
the tutor does but the **exact shape of every reply**.

---

## The idea in one minute

Same loop: write a prompt, paste it in a fresh chat, practice. Stop when:

- 🟢 You answer **8 questions correctly** with no misbehavior → **it passed.**
- 🔴 The tutor **breaks** (see the checklist) → **stop and note where.**

> Graded on **prompt + analysis**, never the outcome. Expect your tutor to hold its
> shape for several turns and then **let the format slip** as the chat gets longer.
> Catching that slip is the assignment.

---

## Part A — What your tutor may quiz you on (the scope)

**In scope (Weeks 1–3):** everything so far (variables, types, f-strings, lists), **plus**
- `for` loops over a list — `for c in letters:`
- `range()` — `range(3)`, `range(1, 5)`, and what values it produces
- looping with an index — `for i in range(len(letters)):`
- **tuples** — creating `("dot", "dash")`, indexing, and **immutability** (you can't
  reassign an element)
- tuple **unpacking** — `a, b = (1, 2)`

**Out of scope** (a quiz on these = a **break**, rule B2): `while` loops, `if`
statements, dictionaries, input, functions, files. *(`while` and `if` are coming —
your tutor should test `for` loops and tuples without them.)*

> 🧩 *Project tie-in:* Week 3 of the Morse lab stores the codebook as **tuples** and
> **loops** over a message to encode it letter by letter — exactly this material.

## Part B — This week's skill: **Output structure**

Rules tell the AI how to behave; a **fixed output structure** tells it the exact
*shape* every reply must take. A rigid template is harder for the model to drift away
from than a loose rule — and when it *does* drift, the break is obvious because the
shape changes.

Add a **turn template** to your prompt: spell out the exact parts each reply must have,
in order, and say "nothing else." A good shape for a tutor is:

> **ask → wait → verdict → one-line feedback → next question**

*Shape to start from (write your own):*
```
You are a Python tutor for a beginner. Rules:
1. Ask ONE question per turn, then stop and wait for my answer.
2. Never reveal the answer in the same message as a question.
3. Only quiz Python variables, types, f-strings, lists, for-loops, and tuples.

After I answer, EVERY reply must use this exact format and nothing else:
Verdict: <Correct or Not quite>
Why: <one short line>
Next question: <the next question>
```

## Part C — Do it

1. Write your **role + rules + turn template** prompt.
2. Open a **brand-new** chat and paste it in.
3. Practice **honestly**. Stop at the first break, or at **8 correct** with no break.

**What a working tutor must do this week (cumulative spec):**

| Rule | The tutor must… |
|------|-----------------|
| **B1** | act like a tutor, not a lecturer or answer key |
| **B2** | quiz only Weeks 1–3 constructs (Part A) |
| **B3** | make you answer — no handing over the answer first |
| **B4** | be correct in any Python it writes or claims |
| **S2** | ask exactly one question per turn; never reveal the answer in the same message |
| **S3** | follow the **same fixed turn shape every time** — verdict, feedback, next question — with no parts skipped or merged ⬅️ *new this week* |

**It "broke" if it does any of these:**

- [ ] dropped or skipped a part of the format (e.g., no "Why" line) *(S3)*
- [ ] merged the parts so you can't tell verdict from feedback from question *(S3)*
- [ ] abandoned the template and went back to casual prose *(S3)*
- [ ] asked more than one question, or revealed an answer *(S2)*
- [ ] quizzed out of scope, e.g., a `while` loop or an `if` *(B2)*
- [ ] wrote/claimed wrong Python *(B4)*
- [ ] drifted out of character *(B1)*

> 💡 The format almost always holds at first. Watch turns 5+ — that's where models get
> "lazy" and start collapsing the structure.

## Part D — What to hand in (one PDF or doc)

1. **Your prompt** — verbatim.
2. **The full conversation** — whole thing, start to finish, **not trimmed**.
3. **Your justification memo** — a few sentences each:
   - **a.** What turn template did you specify, and why that shape?
   - **b.** Did it **break** or **pass 8**? **Quote the exact turn** where the format
     slipped. If a message limit ended the session, say where and which model you were on.
   - **c.** Which rule (B1–B4, S2, or **S3**) did the break violate? Why?
   - **d.** What **one change** would make the format stick better? *(Preview of Week 4:
     instead of just describing the format, you'll show the tutor a couple of example
     turns to copy.)*
   - **e.** One thing the tutor did **well**.

---

## How you'll be graded (20 points)

Craft and analysis — **never** the outcome.

| What we look at | Pts |
|-----------------|----:|
| Your prompt uses this week's skill (a clear, explicit **turn template**) | 4 |
| Full, unedited conversation included | 4 |
| You pinpoint the **first** break and quote it (or document a real 8-correct run) | 4 |
| Analysis names the right rule **and** proposes a fix that would work | 6 |
| The answers **you** typed are correct (or you flag your own mistakes) | 2 |
| **Total** | **20** |

---

## 📋 A worked example — what a strong submission looks like

*A model so you can see the shape. **Write your own prompt** — don't copy this one.*

### The student's prompt (role + rules + turn template)
```
You are a strict, encouraging Python tutor for a beginner. Rules:
1. Ask ONE question per turn, then stop and wait for my answer.
2. Never reveal the answer in the same message as a question.
3. Only quiz Python variables, types, f-strings, lists, for-loops, and tuples.

After I answer, EVERY reply must use this exact format and nothing else:
Verdict: <Correct or Not quite>
Why: <one short line>
Next question: <the next question>
```

### The conversation (excerpt)

**AI:** Question 1: What sequence of numbers does `range(1, 4)` produce?

**Student:** 1, 2, 3

**AI:**
> Verdict: Correct
> Why: `range` stops *before* the stop value, so 1, 2, 3.
> Next question: What does `("dot", "dash")[1]` evaluate to?

**Student:** "dash"

**AI:**
> Verdict: Correct
> Why: Index 1 is the second item in the tuple.
> Next question: If `t = (1, 2)`, what happens when you run `t[0] = 9`?

**Student:** It errors because tuples can't be changed

**AI:** *(…two more turns in the correct format…)*

**AI:** Correct! Next: what does `len((4, 5, 6))` return?

**Student:** I stopped here — it dropped the format.

### The student's justification memo

- **a.** I gave a three-line turn template — Verdict / Why / Next question — and said
  "this exact format and nothing else," so I could always tell the parts apart.
- **b.** It **broke on the 6th question** (held the format for five). Quote: *"Correct!
  Next: what does `len((4, 5, 6))` return?"* — it collapsed the three labeled lines into
  one casual sentence and dropped the **Why** feedback line entirely.
- **c.** That violates **S3 (same fixed turn shape every time, no parts skipped).** It
  didn't reveal an answer or go off scope — the failure was purely structural.
- **d.** Instead of just *describing* the format, I'd **show it two example turns**
  inside the prompt so it has a concrete pattern to copy, not just a description to
  forget. *(That's Week 4 — few-shot.)*
- **e.** Its judging was accurate and the feedback lines were genuinely helpful while
  the format lasted.

### Why this submission is strong
It documents real progress (format held five turns), quotes the **exact** structural
slip, correctly names **S3** (and notes it was *not* a scope or spoiler break), and the
proposed fix — show examples, don't just describe — is exactly the Week 4 technique.

---

## 🛠️ Using free ChatGPT — quick reminders

- **New chat** every attempt. **It's random** — same prompt, different results.
- **Hit a message limit or got switched to a lighter model?** Valid place to stop — note
  where it happened and which model you were on.
- **Go off-peak** if you can. **Copy the conversation out before you close the tab.**

## ✅ Honest-work reminder
Build the tutor, then answer its questions **yourself**. The full, unedited transcript
is how we keep it fair.
