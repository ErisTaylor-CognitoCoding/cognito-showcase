# Episode 6 — Pac-Man

> 📺 *(coming 3 Jul 2026)*

**Series:** Scratch Arcade Series  
**Live Scratch Project:** *(link coming 3 Jul 2026)*

---

## What We Built

Pac-Man — navigate a maze, eat all the dots, dodge (or eat) four ghosts.

This one's the hardest so far. The maze is a grid. Pac-Man moves on that grid — not freely like Donkey Kong, but one tile at a time. The ghosts do too, and they need to decide which direction to go: that's the AI.

Two headline concepts: **grid movement** (snapping to a tile-based layout) and **ghost AI** (simple decision rules that make the ghosts feel like they're hunting you).

---

## Headline Concept: Grid Movement + Ghost AI

### Grid movement — the analogy

Think of a chess board. Pieces don't slide freely — they jump from square to square. Pac-Man works the same way. The maze is a grid of tiles. Every move snaps Pac-Man to the next tile centre. This makes collision detection simple: check the tile ahead before moving, not the pixels.

### Ghost AI — the analogy

A ghost chasing you isn't magic — it's just picking the direction that gets it closest to your current position. At each junction, check all valid directions, calculate which brings it nearer to Pac-Man, go that way. Repeat every few frames. Simple rules, emergent chase.

### Blocks used in this episode

- `go to x: [tile-x] y: [tile-y]` — snap to grid
- `if touching [Wall]` — can't move that way
- Variables `[target-x]` and `[target-y]` — ghost pathfinding target
- `broadcast [scatter]` — switch ghost from chase to scatter mode
- `repeat [4]` — check all four directions
- `if [distance to Pac-Man] < [closest]` — pick best direction

---

## Concepts in this episode

- [variables →](../../concepts-a-z/variables)
- [if-then-else →](../../concepts-a-z/if-then-else)
- [broadcast →](../../concepts-a-z/broadcast)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [if-touching →](../../concepts-a-z/if-touching)
- [costumes →](../../concepts-a-z/costumes)
- [wait →](../../concepts-a-z/wait)

---

*[← Back to episode guide](../README.md) · [Next: Ep 7 — Asteroids →](../ep-07-asteroids)*
