# random-numbers — Controlled Unpredictability

> 📺 **26 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 26 Aug 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

A dice roll. You don't know what number you'll get, but you know it'll be between 1 and 6. That's the deal with randomness in games — bounded chaos. Unpredictable enough to feel alive, constrained enough to stay playable.

---

## What it does

`pick random [N] to [M]` returns a whole number anywhere in that range, with equal probability. Use it for positions, speeds, directions, spawning — anywhere a fixed value would make the game predictable and boring.

---

## Where games use it

**Food spawn in Snake:** The food appears at a random grid position every time it's eaten. Without random, the food always appears in the same spot — trivial to predict after one run.

**Enemy fire timing in Space Invaders:** Aliens fire at random intervals from random columns. `wait [pick random 30 to 120] frames` between shots. Keeps you guessing.

**Asteroid directions:** Split rocks shoot off in random directions. Without randomness, each game plays out identically.

**Car stagger in Frogger:** Cars in the same lane appear at slightly different intervals so they don't clump up immediately.

---

## Where it appears in the series

- [Snake →](../../series/ep-02-snake) — food spawn position
- [Frogger →](../../series/ep-03-frogger) — initial car positions, clone stagger timing
- [Space Invaders →](../../series/ep-04-space-invaders) — alien fire timing and column selection

---

*[← Back to concepts](../README.md) · Next: [repeat →](../repeat)*
