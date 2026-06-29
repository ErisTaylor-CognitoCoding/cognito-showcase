# Episode 3 — Frogger

> 📺 **[Watch on YouTube →](https://youtu.be/gfHLoLGMHIg)**

**Series:** Scratch Arcade Series  
**Live Scratch Project:** [Open in Scratch →](https://scratch.mit.edu/projects/1331052891/)

---

## What We Built

Frogger — dodge the traffic, cross the road, don't get flattened.

Five lanes, five different speeds. Logs on the river, cars on the road. Time your jumps right and you reach the other side. Time them wrong and you respawn at the bottom.

The game teaches the thing that makes real-time games feel alive: **timing**. Not game clock timing — the balance between hazard speed, player reaction time, and the wait blocks that pace everything.

---

## Headline Concept: Timing

### The analogy

Think of a crossing guard. Cars can only go during the green light. Pedestrians cross during the red. The guard sets the timing — and if the timing is wrong, things collide.

In Frogger, each lane of traffic has a different pace. Slow everything down and the game's too easy. Speed it all up and it's unplayable. Timing is the design.

### How the hazards work

Each lane uses `glide N secs to x: [far edge] y: [lane-y]` in a forever loop. Changing `N` changes the speed. Cloning that sprite multiplies hazards per lane without extra scripts.

### Blocks used in this episode

- `glide [N] secs to x: [value] y: [value]` — smooth movement across the lane
- `forever` — keeps hazards looping
- `create clone of [myself]` — multiple cars per lane
- `if touching [Frog]` — collision with player
- `wait [N] secs` — stagger when clones appear
- `go to x: [start] y: [lane]` — reset position

---

## Concepts in this episode

- [glide-to →](../../concepts-a-z/glide-to)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [if-touching →](../../concepts-a-z/if-touching)
- [wait →](../../concepts-a-z/wait)
- [random-numbers →](../../concepts-a-z/random-numbers)

---

*[← Back to episode guide](../README.md) · [Next: Ep 4 — Space Invaders →](../ep-04-space-invaders)*
