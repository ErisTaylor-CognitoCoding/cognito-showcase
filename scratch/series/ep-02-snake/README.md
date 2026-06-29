# Episode 2 — Coding Snake

> 📺 **[Watch on YouTube →](https://youtu.be/8qaxgK9FrbM)** · 🎮 **[Open in Scratch →](https://scratch.mit.edu/projects/1328679090)**

**Series:** Scratch Arcade Games
**Headline concept:** Lists — the data structure that IS the snake

---

## What We Built

Snake. The trail, the apple, self-collision, the growing body. Built in Scratch using a list as the core data structure — which it turns out is the whole game.

---

## The Headline Trick — the Snake IS a List

Every time the head moves, it remembers where it just was. It adds that position (x, then y) to the end of a list. The tail removes the oldest position from the front. So the list always contains the exact positions of every body segment.

**When you eat an apple**, you skip the deletion. The list gets one pair longer. The snake gets one segment longer. That's it. That's how Snake works.

The body sprites aren't moving — each frame, a set of clones reads the list and jumps to those positions. The list IS the snake. The clones are just the picture of it.

---

## Other Key Ideas

**Direction blocking** — the classic Snake rule. If you're moving left, pressing right does nothing. You can't reverse straight into yourself. One `if not Direction = 2` check per key handles it.

**Clones** — one Snake Body sprite spawns as many clones as the list needs. Each clone reads one position pair from the list and goes there. The `draw body` broadcast wipes all clones and redraws every frame.

**Grid-snapping** — the apple picks `(pick random -11 to 11) * 20`. The `* 20` locks it to the same 20-pixel grid the snake moves on. Without it, the apple lands between grid squares and the snake can never quite touch it.

**Modulo** — `Score mod 10` gives the ones digit (47 mod 10 = 7). `floor(Score / 10)` gives the tens digit. Same costume trick from Pong for retro pixel numbers.

---

## Coding Concepts in This Episode

- Lists — storing and retrieving position data as pairs
- `add (x position) to [Snake]` + `delete (1) of [Snake]` — the head/tail mechanic
- `create clone of [myself]` — one sprite, many body segments
- Direction variables + opposite-direction blocking
- `pick random ... * 20` — grid-snapping for the apple

---

**Concept deep-dives:** [forever-loop →](../../concepts-a-z/forever-loop) · [variables →](../../concepts-a-z/variables) · [broadcast →](../../concepts-a-z/broadcast)

*[← Ep 1](../ep-01-pong) · [Back to episode guide →](../README.md) · [Next: Ep 3 →](../ep-03-frogger)*
