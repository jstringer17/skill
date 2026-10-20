---
name: launch-subagents
description: Split work into independent pieces, run them as parallel sub-agents, then reconcile the results into one answer. Use when the user says "launch sub-agents", "parallelize this", or asks for search, review across many files, or research that breaks into pieces that don't need each other's output. Not for sequential building, where step 2 needs step 1's answer.
---

# Launch Sub-agents

Run independent work in parallel instead of grinding through it one item at a time, then hand back one reconciled answer.

## Check that the work is actually parallel

Before splitting, confirm each piece can finish without another piece's output. If step 2 needs step 1's answer, do not use sub-agents: they make sequential work slower and worse. Say so and do the work in order instead.

Good fits: searching a codebase from several angles, reviewing many files, researching several separate questions.
Bad fits: building a feature step by step, anything with a shared draft that pieces edit in turn.

## Before launching, tell the user the plan

State, briefly:

1. How many agents you will launch.
2. What each one owns. Every agent owns one independent piece; no two own the same thing.
3. What you will do if two agents come back with contradictory findings.

Then launch them, in one batch, so they run concurrently.

## Brief each agent so it can stand alone

Each agent starts cold. Give it the goal, its exact slice, the paths or sources it should look at, and the shape of the answer you want back (for example: findings with file:line, or "not found" if nothing turns up).

## Reconcile the results yourself

When they finish, combine the results into **one answer, not N reports**.

- Where agents agree, merge and deduplicate.
- Where they contradict each other, **state the conflict before resolving it**: name both claims, check the primary source yourself, and say which one holds and why. Never pick one at random.
- Where an agent came back empty or failed, say so rather than papering over the gap.

## When it goes wrong

| Symptom | Fix |
|---|---|
| Agents contradict each other and one gets picked at random | The reconciliation step was skipped. State the conflict, verify, then resolve. |
| The parallel run was slower than doing it directly | The pieces depended on each other. Do it sequentially next time. |
| Agents duplicated each other's work | The ownership split overlapped. Give each agent a disjoint slice. |
