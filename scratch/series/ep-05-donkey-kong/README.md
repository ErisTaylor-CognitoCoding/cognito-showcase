# Episode 5 — Donkey Kong

> 📺 **[Watch on YouTube →](https://youtu.be/AdgnAxTkI30)**

**Series:** Scratch Arcade Series  
**Live Scratch Project:** [Open in Scratch →](https://scratch.mit.edu/projects/1335511261/)

---

## What We Built

Donkey Kong — a platformer. Mario runs, jumps, lands, falls off ledges. Barrels roll down the ramps. Reach the top to win.

The game looks complex but it runs on two lines of logic repeated every frame: a `y-velocity` variable that increases downward, and a collision check that stops it when the player hits a platform. That's **gravity** — two variables and a check.

---

## Headline Concept: Gravity

### The analogy

Drop a ball off a table. It doesn't jump to the floor — it accelerates. Slowly at first, then faster. In code, that's a variable that increases every frame until something stops it.

In Scratch: `change [y-velocity] by [-1]` every frame. Then `change y by [y-velocity]`. The player drops faster and faster until they hit a platform. On contact: `set [y-velocity] to [0]`. Gravity off. Standing still.

### How jumping works

Jump = set `y-velocity` to a positive number (say, 10). Gravity drags it back toward zero. The player rises, slows, peaks, falls — all from one variable changing one unit per frame.

### Blocks used in this episode

- `change [y-velocity] by [-1]` — gravity every frame
- `change y by [y-velocity]` — apply velocity
- `if touching [Platform]` — ground check
- `set [y-velocity] to [0]` — land
- `set [y-velocity] to [10]` — jump
- `if touching [Barrel]` — die
- `key [left arrow] pressed` / `key [right arrow] pressed` — movement

---

## Concepts in this episode

- [variables →](../../concepts-a-z/variables)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [if-touching →](../../concepts-a-z/if-touching)
- [arrow-keys →](../../concepts-a-z/arrow-keys)
- [if-then-else →](../../concepts-a-z/if-then-else)
- [costumes →](../../concepts-a-z/costumes)

---

*[← Back to episode guide](../README.md) · [Next: Ep 6 — Pac-Man →](../ep-06-pac-man)*
