---
name: verify-before-build
description: Decide how to prove a change works before building it, name what that check won't catch, then run it after building and report in a fixed VERIFIED / NOT VERIFIED format. Use when the user says "verify before you build", "prove it works", "how will you test this", or for any change where "it should work" isn't good enough.
---

# Verify Before You Build

Make "done" mean something by choosing the proof up front and reporting it honestly.

## Before building

Tell the user how you will prove this works. Pick the **strongest option you actually have**, in roughly this order of strength:

1. A test you write and run.
2. A command whose output the user can read.
3. Real data you process end to end.
4. A second pass reading your own diff against the requirement (weakest; use only when nothing runnable exists).

Then say **what that check would NOT catch**.

"I reviewed the code" is not a verifier. If something runnable exists, run it.

## After building

Run the check. Report in exactly this shape:

```
VERIFIED: [what you ran, what it returned]
NOT VERIFIED: [what you couldn't check and why]
```

The format is mandatory. Without a required shape, "it should work" slides in. NOT VERIFIED forces honesty: if everything is verified, write `NOT VERIFIED: nothing`, and only when that is true.

If the check fails, say so with the output, fix it, and run it again. Do not report success on a failing check.

## Making it permanent

To apply this to every task in a project, add this rule to the project's `CLAUDE.md`:

```markdown
## Verification
Before building, state how you'll prove the change works (a test you run, a command's output, real data, or as a last resort a diff re-read) and what that check won't catch. After building, run it and report:
VERIFIED: [what you ran, what it returned]
NOT VERIFIED: [what you couldn't check and why]
```

## When it goes wrong

| Symptom | Fix |
|---|---|
| The verifier is "I reviewed the code" | Reject it. Find something to run. |
| NOT VERIFIED is missing or says "nothing" by reflex | List the real gaps: other platforms, untested inputs, things only production shows. |
| The check passed but proved nothing | The check didn't exercise the change. Make it fail on the old code first. |
