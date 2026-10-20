---
name: implementation-spec
description: Write an implementation spec before touching any code, covering what will be built, which files change, the order, the risks at each step, what is explicitly out of scope, and the three decisions the user is most likely to disagree with. Then wait for the user's go. Use when the user says "write me an implementation spec", "spec this out", "plan before you build", or before any change large enough that a wrong assumption would cost real time.
---

# Implementation Spec

Write the plan first so bad calls get caught in minutes instead of forty minutes into the build.

## Rules

- **Do not write or edit code until the user says go.** Reading code to inform the spec is fine; changing it is not.
- Name concrete file paths and function names. If you can't name the files, you haven't thought about it yet: go read the code until you can.

## The spec

Write these sections, in this order:

1. **What I'm building.** One short paragraph on the outcome, in the user's terms.
2. **Files.** Every file you will create or change, by path, with one line on what changes in each.
3. **Order.** The steps in the order you will do them. Each step should leave the project in a working state where possible.
4. **What could go wrong.** For each step, the specific way it could fail and how you'd notice.
5. **Not doing.** What you are explicitly leaving out, so scope can't creep silently.
6. **Decisions you'll likely disagree with.** The three choices in this plan the user is most likely to push back on, and why you made each one. This is the most important section: it surfaces the assumption that would otherwise show up forty minutes in. Pick real judgment calls, not filler.

End by asking for the go-ahead, and stop.

## When it goes wrong

| Symptom | Fix |
|---|---|
| The spec is vague | Replace every general statement with a file path and a function name. |
| The "disagree" section is padding ("I chose clean code") | Pick decisions where a reasonable person would choose differently: a library, a data shape, a boundary, a tradeoff. |
| Code got written before approval | Stop, revert the unapproved change, and present the spec. |
