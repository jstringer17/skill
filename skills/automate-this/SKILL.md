---
name: automate-this
description: Plan an automation (a scheduled task, hook, recurring job, or CI workflow) and show the full plan for review before anything is scheduled or set up. Covers what runs, when, exactly which files or services it touches, what happens on failure, and a run log. Use when the user says "automate this", "run this every day", "schedule this", or "set up a job for this".
---

# Automate This

An automation that runs while nobody is watching, with one wrong assumption, is a much bigger problem than a prompt with one wrong assumption. Plan it, show it, and wait.

## Rules

- **Set nothing up until the user has reviewed and approved the plan.** No schedules, hooks, cron entries, workflows, or tokens before approval.
- Prefer automating something that already works by hand. If the task has no reliable, verified manual version yet (ideally a skill that has been run several times), say so and suggest getting that first.

## The plan

Show the user:

1. **What will run**: the exact command, prompt, or skill.
2. **When it will run**: the schedule or trigger, with time zone.
3. **What it touches**: every file, directory, and service it reads, and every one it writes. Be exhaustive.
4. **What happens if a step fails**: does it stop, retry, or alert, and how the user finds out.
5. **Where the log goes**: every run appends to a log (time, what ran, what changed, any errors).

Then ask for approval and stop.

## Scope the first version tight

- Let it **read broadly but write to exactly one place.**
- Have it **show or draft anything it would send or publish** instead of sending it on its own, until it has earned trust.
- **Keep a log of every run.** The first time an automation surprises you, the log is the only way to work out why.

## When it goes wrong

| Symptom | Fix |
|---|---|
| The automation did something unexpected | Its scope was too wide. Narrow it to one destination and rebuild from there. |
| Nobody knows why a run failed | There was no log. Add one before re-enabling. |
| It acted on a wrong assumption | The manual version wasn't reliable yet. Disable it and go back to running it by hand. |
