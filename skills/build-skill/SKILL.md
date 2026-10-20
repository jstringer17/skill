---
name: build-skill
description: Turn what was just worked out in the current conversation into a reusable skill (a SKILL.md) so it never has to be explained again, including when it should fire, the exact steps, the prompts that worked, the mistakes hit and their fixes, and what to do when it goes wrong. Use when the user says "based on this conversation, build me a skill", "turn this into a skill", or "save this workflow".
---

# Build a Skill From This Conversation

Capture what this conversation worked out so the next time is free.

## Timing

This works best the **second** time a problem is solved, not the first. The first time, nobody yet knows which parts mattered. If this is clearly a first attempt, say so and ask whether to proceed anyway.

## What goes in

Read back through the conversation and extract:

1. **When it should fire**: the requests and situations that should trigger it. This becomes the frontmatter `description`, which is what decides whether the skill loads, so make it specific and include the phrases a user would actually say.
2. **The exact steps, in order.**
3. **The prompts and commands that actually worked**, verbatim.
4. **The mistakes we hit and how we fixed them.**
5. **What to do when it goes wrong.**

Leave out anything that was a dead end and taught nothing.

## How to write it

- **Write instructions to a future agent, in the imperative.** "Run X. Check Y." Not a description of what we did ("we tried X, then Y").
- Write for someone who has the user's context but not their memory: no references to "earlier" or "what we discussed".
- **Keep it under 300 lines.** Move long reference material into a sibling file and link it.
- Use this layout:

```markdown
---
name: <kebab-case-name>
description: <what it does>. Use when <triggers>.
---

# <Title>

<one line on the goal>

## Steps
## What worked
## When it goes wrong
```

Save it as `skills/<name>/SKILL.md` in the current skills repo, or `.claude/skills/<name>/SKILL.md` in the current project if there is no skills repo. Ask if unsure.

## When it goes wrong

| Symptom | Fix |
|---|---|
| The skill reads like a summary | Rewrite every sentence as an instruction in the imperative. |
| It never triggers | The description is too vague. Add the concrete phrases and situations. |
| It's 600 lines | Cut dead ends and move reference tables into a separate file. |
