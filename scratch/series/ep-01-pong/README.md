# Episode 1 — Pong

> 📺 **[Watch on YouTube →](https://youtu.be/95Ty51EgzHw?si=81bWZf24PAPJ0VeC)**

**Series:** Scratch Arcade Series  
**Live Scratch Project:** *(not yet linked — check the video description)*

---

## What We Built

Pong — the original arcade game. Two paddles, one ball, zero margin for error.

The ball bounces around the screen. Each paddle deflects it back. Miss it and your opponent scores. First to 11 wins.

Episode 1 is built around one trick that underpins every game ever made: **collision detection** — checking whether two things are touching, and reacting when they are. Pong's AI turns out to be a single line of code.

---

## Block Coding Concepts Covered

### Collision detection — the headline trick
Every frame, the ball asks: "Am I touching the paddle right now?" If yes — bounce.

`if touching [Paddle]` → `point in direction (pick random -45 to -135)` → `move 15 steps`

The `move 15 steps` after the bounce clears the ball from the paddle — without it, the ball gets stuck inside and fires the bounce over and over.

### Angles and direction
`point in direction (pick random 30 to 150)` on serve — always heading sideways, never straight up or down.

### Simple AI — one line of code

```
if y position < y position of Ball → change y by 4
if y position > y position of Ball → change y by -4
```

Speed 4 vs player speed 7 — that gap is the difficulty dial. Set both to the same speed and the AI is unbeatable.

### Broadcasting — how sprites talk
`broadcast GAME OVER` fires from the Ball script when someone hits 11. The Game Over sprite listens and shows itself. Sprites never talk directly — they broadcast and let others react.

### Costume trick — fake pixel font
`switch costume to (Player Score)` — the variable's value picks which costume to display. Each costume is a pixel-art number. Retro scoreboards without needing custom fonts.

---

## Concepts in This Episode

Expanded in the Wednesday Shorts:

- [if-touching →](../../concepts-a-z/if-touching)
- [arrow-keys →](../../concepts-a-z/arrow-keys)
- [forever-loop →](../../concepts-a-z/forever-loop)
- [variables →](../../concepts-a-z/variables)

---

*[← Back to episode guide](../README.md) · [Next: Ep 2 — Snake →](../ep-02-snake)*
