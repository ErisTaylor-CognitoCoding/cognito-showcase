# broadcast — Sprites Talking to Each Other

> 📺 **19 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 19 Aug 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

A stadium announcer. One person at a microphone says "goal!" and 50,000 people in the crowd all react — cheering, jumping, checking the scoreboard. The announcer didn't tell each one what to do individually. They broadcast a message. Everyone who heard it reacted in their own way.

In Scratch: one sprite broadcasts a message. Every sprite with a matching `when I receive` block reacts immediately.

---

## What it does

`broadcast [message]` sends a signal to every sprite in the project. Any sprite with `when I receive [message]` runs that script when the signal arrives.

This lets sprites coordinate without directly controlling each other. The game controller sprite broadcasts `game over`. Every enemy, every counter, every animation stops and runs its own `when I receive [game over]` behaviour.

---

## Why this matters

In Space Invaders, when the alien formation reaches the screen edge, one clone detects the edge and broadcasts `[change direction]`. Every other clone — all 55 of them — receives that broadcast and reverses direction simultaneously. One message, 55 reactions. Without broadcast, this would be impossible to coordinate.

---

## Where it appears in the series

- [Space Invaders →](../../series/ep-04-space-invaders) — formation direction change, alien destroyed
- [Pac-Man →](../../series/ep-06-pac-man) — ghost mode switch (chase / scatter / frightened)
- [Tetris →](../../series/ep-08-tetris) — line clear signal triggers score and animation

---

*[← Back to concepts](../README.md) · Next: [random-numbers →](../random-numbers)*
