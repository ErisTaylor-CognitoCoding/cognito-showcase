# Episode 1 — Pong

> 📺 *(video coming soon)*

**Series:** Scratch Arcade Series  
**Live Scratch Project:** *(link coming)*

---

## What We Built

Pong — the original arcade game. Two paddles, one ball, zero margin for error.

The ball bounces around the screen. Each paddle deflects it back. Miss it and your opponent scores. First to a target wins.

Pong is the perfect starting point because it has exactly one trick that underpins every game ever made: **collision detection** — checking whether two things are touching, and reacting when they are.

---

## Headline Concept: Collision Detection

### The analogy

Imagine reaching out to shake someone's hand. Before you grab, you check: are they close enough? Collision detection is that check, done 30 times a second by the game engine.

In Scratch, the block is `if touching [Paddle]`. Every frame, the ball asks: "Am I touching the paddle right now?" If yes — bounce. If no — keep going.

### Why it matters

Without collision detection there is no game. The ball passes through the paddle, the bullet ignores the enemy, the player falls through the floor. Every interaction in every game is a collision check.

### Blocks used in this episode

- `if touching [Paddle1]` — ball checks left paddle
- `if touching [Paddle2]` — ball checks right paddle
- `if on edge, bounce` — built-in wall reflection
- `set rotation style [left-right]` — keeps the paddle upright
- `key [up arrow] pressed` / `key [w] pressed` — two-player input

---

## Concepts in this episode

These building blocks appear in the Wednesday Shorts:

- [if-touching →](../../concepts-a-z/if-touching)
- [arrow-keys →](../../concepts-a-z/arrow-keys)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [variables →](../../concepts-a-z/variables)

---

*[← Back to episode guide](../README.md) · [Next: Ep 2 — Snake →](../ep-02-snake)*
