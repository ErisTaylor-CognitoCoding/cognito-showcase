# Episode 2 — Snake

> 📺 **[Watch on YouTube →](https://youtu.be/8qaxgK9FrbM)**

**Series:** Scratch Arcade Series  
**Live Scratch Project:** [Open in Scratch →](https://scratch.mit.edu/projects/1328679090)

---

## What We Built

Snake — eat the food, grow longer, don't hit the wall or yourself.

The game looks simple. The implementation is not. Because the snake body isn't a shape — it's a **list**. Every segment remembers where the head was a few steps ago. Grow the snake? Add to the list. Die? Clear it.

Once you see that the snake body IS a list, the whole game clicks into place.

---

## Headline Concept: Lists

### The analogy

Think of a conga line at a party. The lead dancer moves. Everyone else follows, each one stepping into the spot the person ahead just left. The snake body is exactly that — a chain of positions following the head.

In Scratch, we store those positions as two lists: `body-x` and `body-y`. Each frame, add the head's position to the front, delete the last entry. The snake moves without anything actually moving — only the list changes.

### How eating works

When the head touches the food, skip the delete step. The list gets one entry longer. The snake grows — without touching a single sprite position.

### Blocks used in this episode

- `add [value] to [list]` — insert at the back
- `insert [value] at [1] of [list]` — insert at the front
- `delete [last] of [list]` — remove the tail
- `item [n] of [list]` — read a position
- `length of [list]` — how long is the snake?
- `if touching [Food]` — eat check

---

## Concepts in this episode

- [variables →](../../concepts-a-z/variables)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [if-touching →](../../concepts-a-z/if-touching)
- [random-numbers →](../../concepts-a-z/random-numbers)

---

*[← Back to episode guide](../README.md) · [Next: Ep 3 — Frogger →](../ep-03-frogger)*
