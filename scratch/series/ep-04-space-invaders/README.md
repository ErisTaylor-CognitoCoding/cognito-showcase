# Episode 4 — Space Invaders

> 📺 **[Watch on YouTube →](https://youtu.be/mVugtGz6oL0)**

**Series:** Scratch Arcade Series  
**Live Scratch Project:** [Open in Scratch →](https://scratch.mit.edu/projects/1331615967/)

---

## What We Built

Space Invaders — 55 aliens in a formation, marching back and forth, slowly descending. You shoot up. They shoot back.

We didn't draw 55 sprites. We drew one, and cloned it 54 times. That's the key insight of this episode: **cloning** — one sprite, multiplied.

---

## Headline Concept: Cloning

### The analogy

Think of a photocopier. You put one sheet in, press the button, get 54 identical copies out. Each copy can then be positioned differently — different row, different column — but they all started from the same original.

In Scratch, `create clone of [myself]` does exactly that. One alien sprite, looped 55 times in a nested repeat, fills the entire formation. Each clone gets its own position from variables set just before creation.

### How the formation moves

All clones share a single broadcast signal. When the formation reaches the edge, the original sends `[change direction]`. Every clone receives it and reverses. The formation moves as one block without any clone needing to know about the others.

### Blocks used in this episode

- `create clone of [myself]` — multiply sprites
- `when I start as a clone` — each clone runs this independently
- `delete this clone` — remove when shot
- `broadcast [message]` — formation-wide signal
- `when I receive [message]` — each clone reacts
- `repeat [N]` — nested loops for rows and columns

---

## Concepts in this episode

- [broadcast →](../../concepts-a-z/broadcast)
- [repeat →](../../concepts-a-z/repeat)
- [variables →](../../concepts-a-z/variables)
- [if-touching →](../../concepts-a-z/if-touching)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [random-numbers →](../../concepts-a-z/random-numbers)

---

*[← Back to episode guide](../README.md) · [Next: Ep 5 — Donkey Kong →](../ep-05-donkey-kong)*
