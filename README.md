
<a href="http://aiforui.dev/">
<img width="360" height="202" alt="opengraph-image 2" src="https://github.com/user-attachments/assets/84fca9a6-0b2b-4927-8f48-f3ce194a5c47" />
</a>

# Skills For Designers and Engineers

[![skills.sh](https://skills.sh/b/emilkowalski/skills)](https://skills.sh/emilkowalski/skills)

For designers and engineers to help them build better user interfaces.

Knowing whether you made a right choice when it comes to animations, or design in general, is hard. These skills aim to help you get to those right decisions faster.

They are based on my years of experience working at companies like Vercel and Linear.

All the skills here are a side-effect of domain-expertise. AI doesn’t replace such expertise, it amplifies what you can get out of it and makes you way better relative to others.

So learn to code, design, or develop expertise in any other field. It’s extremely valuable.

You can stay up to date with my skills here:

[Sign Up To The Newsletter](https://aiforui.dev/skills)

## Install

```bash
npx skills@latest add emilkowalski/skills
```

## Why use it?

Agents don’t have great taste

I have seen plenty of times that agents don’t pick the right ingredients for an animation. An `ease-in` easing for an enter animation when it’s supposed to be `ease-out` ([here’s why](https://emilkowal.ski/ui/7-practical-animation-tips#4.-choose-the-right-easing)). Or they choose a solid border instead of a semi-transparent shadow for your UIs.

All these small things compound and make your interface either amazing, or just... not that great.

As explained in [Agents with Taste](https://emilkowal.ski/ui/agents-with-taste), these skills list all the little mistakes agents can potentially make and explain how to fix them.

This is your shortcut to great interfaces. A shortcut to stand out in a sea of slop.

## Reference

- **[emil-design-eng](./skills/emil-design-eng/SKILL.md)** — The main skill that consists of mostly animation, but also some design advice.
- **[animate](./skills/animate/SKILL.md)** — Builds an animation from scratch while choosing the correct curve, duration, properties, and so on.
- **[animate-expo](./skills/animate-expo/SKILL.md)** — The same bar, for React Native and Expo: gestures, sheets, haptics, screen transitions, and keeping motion off the JS thread.
- **[review-animations](./skills/review-animations/SKILL.md)** — Review your animations in a strict way, based on my rules.
- **[improve-animations](./skills/improve-animations/SKILL.md)** — Audit all the animations in your codebase and get prioritized, self-contained plans that any agent can execute.
- **[find-animation-opportunities](./skills/find-animation-opportunities/SKILL.md)** — Search your UI for places that would genuinely benefit from motion, while also telling you what not to animate.
- **[animation-performance](./skills/animation-performance/SKILL.md)** — Fix animations that drop frames. It includes lots of subtle issues that most agents miss.
- **[animation-vocabulary](./skills/animation-vocabulary/SKILL.md)** — Get better animations from an AI by telling it exactly what you want by using the right words.
- **[apple-design](./skills/apple-design/SKILL.md)** — Apple’s principles for interface design and fluid motion, distilled from their WWDC design talks and translated for the web.
- **[write-swift](./skills/write-swift/SKILL.md)** — Write modern Swift. Includes: value types, Swift 6 concurrency, generics, performance, and Swift Testing.
- **[pick-ui-library](./skills/pick-ui-library/SKILL.md)** — Have your agent pick the right library for the task based on libraries I use and trust, instead of letting AI hand-roll a toast component or install an abandoned package.
- **[prototype](./skills/prototype/SKILL.md)** — Build multiple different versions of a UI piece you describe and go through them using a switcher.
- **[mobile-native](./skills/mobile-native/SKILL.md)** — Make your web app feel native on a phone: sticky hover states, tap highlight flashes, the 100vh bug, inputs that zoom the page, laggy taps, safe areas, and the rest of the small fixes that separate a website from an app.
- **[break-ui](./skills/break-ui/SKILL.md)** — Try to break the UI you built with worst-case data: long names, unusual emails, one-letter names, huge counts, empty lists, long labels.
- **[ask-sonner](./skills/ask-sonner/SKILL.md)** — Your guide to working with [Sonner](https://sonner.emilkowal.ski), my toast library. Contains setup, styling, recipes, and fixes for the most common issues.

## Workflow skills

Six prompts that change how Claude works on a task. On a real task, use them in this order: **interview-me**, then **implementation-spec**, then **verify-before-build**, then **build-skill**. Bring in **launch-subagents** for research during the first two steps. Save **automate-this** for after a skill has run enough times that you trust it.

- **[interview-me](./skills/interview-me/SKILL.md)** — Asks one question at a time until the job is clear enough to hand to a stranger.
- **[implementation-spec](./skills/implementation-spec/SKILL.md)** — Writes the plan first: files, order, risks, what's out of scope, and the three calls you'll most likely disagree with. No code until you say go.
- **[verify-before-build](./skills/verify-before-build/SKILL.md)** — Picks how to prove the change works before building it, then reports in a fixed VERIFIED / NOT VERIFIED block.
- **[build-skill](./skills/build-skill/SKILL.md)** — Turns what the conversation worked out into a reusable skill written as instructions.
- **[launch-subagents](./skills/launch-subagents/SKILL.md)** — Splits independent work across parallel sub-agents and reconciles them into one answer.
- **[automate-this](./skills/automate-this/SKILL.md)** — Plans an automation (what runs, when, what it touches, how it fails, where it logs) and waits for your review before setting anything up.
