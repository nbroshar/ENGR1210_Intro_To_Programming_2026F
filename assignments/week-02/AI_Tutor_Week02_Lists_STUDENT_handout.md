# Build-an-AI-Tutor 🤖 — Week 2
## Lists
### Your prompting skill this week: **Explicit rules & constraints**

Last week you used a bare *role* and watched the tutor hand you the answers almost
instantly. This week you fix that — by giving the AI **rules**, not just a job title.

---

## The idea in one minute

Same loop as Week 1: write a prompt, paste it into a fresh chat, practice. Stop when:

- 🟢 You answer **8 questions correctly** with no misbehavior → **it passed.**
- 🔴 The tutor **breaks** (see the checklist) → **stop and note where.**

> Still graded on your **prompt + analysis**, never on the outcome. This week your
> tutor should survive **noticeably longer** than last week's — and when it breaks,
> it'll break in a subtler way. That contrast *is* the lesson.

---

## Part A — What your tutor may quiz you on (the scope)

**In scope (Weeks 1–2):** everything from Week 1, **plus**
- Creating a list — `letters = ["a", "b", "c"]`
- Indexing (zero-based) — `letters[0]`, `letters[2]`
- Negative indexing — `letters[-1]`
- Replacing an item — `letters[1] = "z"`
- List methods — `.append()`, `.insert()`, `.remove()`
- Length — `len(letters)`
- Simple slicing — `letters[0:2]`

**Out of scope** (a quiz on these = a **break**, rule B2): loops/`for`, `if`,
dictionaries, input, functions, files. *(Loops are next week — your tutor should test
lists without asking you to loop over them.)*

> 🧩 *Project tie-in:* Week 2 of the Morse lab stores the codebook as **parallel
> lists** — one list of letters, one list of Morse codes — and looks up a code by
> index. Great source material for practice questions.

## Part B — This week's skill: **Explicit rules & constraints**

A role says *who* the AI is. **Rules** say *how* it must behave. Modern chatbots default
to "be maximally helpful," which is why a role alone spills the answers. You override
that with a short, numbered list of **explicit constraints**.

Build your prompt as **a role + a numbered rule list**. Aim to cover at least:
- ask **one** question at a time, then **stop and wait** for the student's answer
- **never** include the answer in the same message as the question
- only quiz Weeks 1–2 topics
- after the student answers, say clearly whether it was **right or wrong**

*Shape to start from (write your own, and add more rules if you like):*
```
You are a Python tutor for a beginner. Follow these rules exactly:
1. Ask me ONE question at a time, then stop and wait for my answer.
2. Never show the answer in the same message as the question.
3. Only ask about Python variables, types, f-strings, and lists.
4. After I answer, tell me if I'm right or wrong before the next question.
```

## Part C — Do it

1. Write your **role + rules** prompt.
2. Open a **brand-new** chat and paste it in.
3. Practice **honestly**. Stop at the first break, or at **8 correct** with no break.

**What a working tutor must do this week (the spec — now cumulative):**

| Rule | The tutor must… |
|------|-----------------|
| **B1** | act like a tutor, not a lecturer or answer key |
| **B2** | quiz only Weeks 1–2 constructs (Part A) |
| **B3** | make you answer — no handing over the answer first |
| **B4** | be correct in any Python it writes or claims |
| **S2** | ask **exactly one** question per turn, and **never reveal the answer in the same message** ⬅️ *new this week* |

**It "broke" if it does any of these:**

- [ ] asked more than one question in a turn *(S2)*
- [ ] put the answer in the same message as the question — even as a "hint" *(S2)*
- [ ] gave the answer before you attempted it *(B3)*
- [ ] lectured instead of quizzing *(B1)*
- [ ] quizzed something out of scope *(B2)*
- [ ] wrote/claimed wrong Python *(B4)*
- [ ] drifted out of character *(B1)*

> 💡 Watch the **later** turns. A rule list often holds for the first few questions,
> then the model starts to slip as the conversation gets longer. That slip is your break.

## Part D — What to hand in (one PDF or doc)

1. **Your prompt** — verbatim.
2. **The full conversation** — whole thing, start to finish, **not trimmed**.
3. **Your justification memo** — a few sentences each:
   - **a.** What rules did you give, and why those?
   - **b.** Did it **break** or **pass 8**? **Quote the exact turn** where it broke.
     If it survived longer than your Week 1 tutor, say so — that's progress worth noting.
   - **c.** Which rule (B1–B4 or **S2**) did the break violate? Why?
   - **d.** What **one change** would prevent it? *(Preview of Week 3: a fixed turn
     structure the model can't drift away from.)*
   - **e.** One thing the tutor did **well**.

---

## How you'll be graded (20 points)

Craft and analysis — **never** the outcome.

| What we look at | Pts |
|-----------------|----:|
| Your prompt uses this week's skill (clear, explicit **rules**) | 4 |
| Full, unedited conversation included | 4 |
| You pinpoint the **first** break and quote it (or document a real 8-correct run) | 4 |
| Analysis names the right rule **and** proposes a fix that would work | 6 |
| The answers **you** typed are correct (or you flag your own mistakes) | 2 |
| **Total** | **20** |

---

## 📋 A worked example — what a strong submission looks like

*A model so you can see the shape. **Write your own prompt** — don't copy this one.*

### The student's prompt (role + rules)
```
You are a strict but encouraging Python tutor for a beginner. Follow these rules:
1. Ask exactly ONE question, then stop and wait for my answer.
2. Never include the answer or a hint that gives it away in the same message.
3. Only quiz me on Python variables, data types, f-strings, and lists.
4. After each answer, tell me "Correct" or "Not quite" and then ask the next question.
```

### The conversation (excerpt)

**AI:** What does `colors[0]` return if `colors = ["red", "green", "blue"]`?

**Student:** "red"

**AI:** Correct. What is the value of `len(colors)` for that same list?

**Student:** 3

**AI:** Correct. How would you change the second item to `"yellow"`?

**Student:** colors[1] = "yellow"

**AI:** Correct. *(…two more clean turns…)*

**AI:** Nice work! Next one: which list method adds an item to the **end** of a list —
for example, `colors.____("purple")`? *(It's `append`, by the way — that's the one
that tacks an item onto the end.)*

**Student:** I stopped here — it slipped the answer into the question.

### The student's justification memo

- **a.** I gave four rules: one question at a time, no answer in the same message,
  scope limited to Weeks 1–2, and a clear right/wrong before each next question.
- **b.** It **broke on the 6th question** — much better than my Week 1 tutor, which
  broke on turn 1. Quote: *"which list method adds an item to the end… (It's `append`,
  by the way…)"* — it gave the answer away inside the question.
- **c.** That violates **S2 (never reveal the answer in the same message).** The rules
  held for five questions, then the model drifted back to being "helpful."
- **d.** I'd stop relying on a flat rule and give it a **fixed turn structure** it has
  to repeat every time — e.g., always `QUESTION:` on one line, then wait; never anything
  else. A rigid format is harder to drift away from than a rule. *(That's Week 3.)*
- **e.** Its judging was accurate and its tone stayed encouraging the whole way.

### Why this submission is strong
It shows real progress over Week 1 (broke on Q6, not Q1), quotes the **exact** slip,
names the right rule (**S2**), and the proposed fix correctly diagnoses *why* a flat
rule list decays — setting up the Week 3 structure lesson.

---

## 🛠️ Using free ChatGPT — quick reminders

- **New chat** every attempt. **It's random** — same prompt, different results.
- **Hit a message limit or got switched to a lighter model?** That's a valid place to
  stop — note where it happened and which model you were on.
- **Go off-peak** if you can. **Copy the conversation out before you close the tab.**

## ✅ Honest-work reminder
Build the tutor, then answer its questions **yourself**. The full, unedited transcript
is how we keep it fair.
