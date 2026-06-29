# Episode 3 — Coding Frogger

> 📺 **[Watch on YouTube →](https://youtu.be/gfHLoLGMHIg)** · 🎮 **[Open in Scratch →](https://scratch.mit.edu/projects/1331052891/)**

**Series:** Scratch Arcade Games
**Headline concept:** Timing — two hazard types at different speeds, so the player has to wait for gaps

---

## What We Built

Frogger — five lanes of road traffic, a river section with logs and diving turtles, three lives, and a home row of lily pads to fill. The classic 1981 arcade game, rebuilt in Scratch.

---

## The Headline Trick — Timing

Pong had one speed. Snake had one speed. Frogger has five road lanes each moving at a *different* speed. Two lanes at different speeds is genuinely harder than one fast lane — the gaps don't line up, you can't memorise the pattern, you have to watch and wait.

Two hazard types make it richer:
- **Road** — if you touch a car, you die. Don't touch the cars.
- **River** — if you're in the river *without* standing on a log or turtle, you drown. The water is the hazard, not the thing moving on it.

The player has to switch mental model mid-game. That's what makes Frogger feel deep.

---

## Other Key Ideas

**Ride the log** — one line of code. While the frog is touching a log clone, change the frog's x by the same amount the log moved. No parenting, no physics — just "copy the log's x change." Visually identical to riding.

**Wrapping clones** — three cars per road lane. When a clone exits the right edge, it teleports to the left edge. Endless traffic from three sprites.

**Lives and the death animation** — a `Lives` variable displayed as small frog icons in the corner. On death: show splat costume for 0.4 seconds, subtract a life, reset to start.

**Diving turtles** — each turtle group clone runs its own dive cycle: visible → tipping → underwater → surfacing. If you're standing on a turtle when it goes underwater, you drown. The randomised dive offset per clone means you can never memorise the safe turtle — the pattern shifts every run.

---

## Coding Concepts in This Episode

- Multiple clones with independent speeds and directions
- `if <touching [Log]?>` — detecting what the frog is standing on
- `change x by (Log Speed)` — the riding trick
- `Lives` variable + death/respawn sequence
- Clone-local variables — each turtle group runs its own state machine

---

**Concept deep-dives:** [if-touching →](../../concepts-a-z/if-touching) · [random-numbers →](../../concepts-a-z/random-numbers) · [wait →](../../concepts-a-z/wait)

*[← Ep 2](../ep-02-snake) · [Back to episode guide →](../README.md) · [Next: Ep 4 →](../ep-04-space-invaders)*
