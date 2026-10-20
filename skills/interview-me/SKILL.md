---
name: interview-me
description: Interview the user one question at a time before starting a task, until the job is clear enough to hand to a stranger. Asks about what they actually want, unmentioned edge cases, and what "done" looks like, then summarises and flags anything vague. Use when the user says "interview me", "ask me questions first", or when a request is underspecified and building the wrong thing would be expensive.
---

# Interview Me

Understand the job before building it.

## Rules

- **Ask exactly one question per message, then wait for the answer.** Never batch questions. If you ask ten at once, the user answers three. This is not optional.
- **Only ask what you don't already know** from what the user has said or what you can find in the code or files yourself. Never ask the user to repeat themselves.
- Keep each question short and concrete. Where it helps, offer two or three likely answers to pick from.

## What to ask about

Work through these, in roughly this order, skipping anything already answered:

1. **What they actually want**, not just what they said. The goal behind the request.
2. **Who or what it's for**, and the context it will be used in.
3. **Edge cases they haven't mentioned**: empty input, failure, scale, the unusual user.
4. **Constraints**: what must not change, tools or styles to match, deadlines.
5. **What "done" looks like**: how they will judge the result.

## When to stop

Stop when you could hand this to someone who has never spoken to the user and they would build the right thing.

Then write a summary:

- **What I learned**: the job, in a few bullets.
- **Still vague**: anything the user answered loosely or that you are assuming. Flag each one explicitly.

Ask whether to proceed.

## When it goes wrong

| Symptom | Fix |
|---|---|
| Several questions landed in one message | Go back to one per message. |
| The questions are generic | Drop anything you could infer. Ask only about real gaps in this specific task. |
| The interview never ends | Stop at "a stranger could build it", not at "nothing left to ask". |
