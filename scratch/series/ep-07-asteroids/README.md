# Episode 7 — Asteroids

> 📺 *(coming 10 Jul 2026)*

**Series:** Scratch Arcade Series  
**Live Scratch Project:** *(link coming 10 Jul 2026)*

---

## What We Built

Asteroids — rotate your ship, thrust forward, shoot the rocks. Big rocks split into two medium rocks. Medium rocks split into two small rocks. Small rocks disappear.

The key difference from everything before: the ship doesn't move on a grid. It moves in any direction depending on which way it's pointing. That's **vector movement** — velocity with a direction baked in.

---

## Headline Concept: Vector Movement + Rotation

### The analogy

Imagine throwing a ball. The direction you're facing when you throw determines where it goes. In Asteroids, the ship's heading (stored as a rotation variable) sets the direction of thrust. Press forward and you accelerate along whatever angle you're currently pointing.

### How the physics works

Two velocity variables: `vx` and `vy`. When you thrust, add a small amount in the current direction to both. `vx` controls left-right drift; `vy` controls up-down drift. The ship keeps drifting after you release thrust — there's no friction in space.

Rotation just changes the ship's direction variable. Thrust uses that direction to update `vx` and `vy`.

### The splitting rocks

Each rock is a clone. When a bullet hits a large rock, delete that clone and create two medium ones at the same position, each with a different velocity. Medium rocks split into small. Small delete. The whole asteroid field manages itself.

### Blocks used in this episode

- `turn [N] degrees` — rotate the ship
- `change [vx] by [sin of direction]` — thrust x component
- `change [vy] by [cos of direction]` — thrust y component
- `change x by [vx]` + `change y by [vy]` — apply velocity
- `create clone of [myself]` — split rocks
- `if touching [Bullet]` — rock hit check
- `set size to [N]%` — small, medium, large rock sizes

---

## Concepts in this episode

- [variables →](../../concepts-a-z/variables)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [if-touching →](../../concepts-a-z/if-touching)
- [if-then-else →](../../concepts-a-z/if-then-else)
- [arrow-keys →](../../concepts-a-z/arrow-keys)

---

*[← Back to episode guide](../README.md) · [Next: Ep 8 — Tetris →](../ep-08-tetris)*
