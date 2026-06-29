# Episode 1 — Coding Pong

> 📺 ***(YouTube link coming)*** · 🎮 ***(Scratch project link coming)***

**Series:** Scratch Arcade Games
**Headline concept:** Collision detection — the trick behind every game ever made

---

## What We Built

Pong from scratch in Scratch. Two paddles, one ball, a scoreboard, and a simple AI opponent — all in one episode. Pong is the right starting point because it contains almost every mechanic in every other game: collision, direction, score, win condition.

---

## How the Game Works

**The ball** moves in a direction every frame. When it hits a wall, Scratch bounces it automatically. When it hits a paddle, the game redirects it at a random angle — so rallies stay unpredictable.

**Collision detection** is the headline trick. Every loop, the ball checks: *"am I touching the paddle?"* If yes, bounce. That one check is how Pong works. It's how every game works.

**The "stuck inside the paddle" bug** — and how to fix it. When the ball bounces, move it 15 steps immediately to get it *out* of the paddle. Without that, the bounce fires over and over on the same frame and the ball gets stuck. This is the most common Pong bug, and the fix teaches you something true about every collision system.

**The AI opponent** is one line of code. If the AI paddle's y is below the ball's y, move up. If it's above, move down. Speed 4 vs the player's 7 — that's the difficulty dial. Crank it to 10 and it's unbeatable.

**Variables** track the score for both players. First to 11 wins.

**Broadcasting** — when someone hits 11, the ball broadcasts `GAME OVER`. The Game Over sprite is listening and appears.

**The costume scoreboard trick** — the score picks a costume by number. Costume named "7" appears when the score is 7. That gives you retro pixel-font numbers for free.

---

## Coding Concepts in This Episode

- `if <touching [Paddle]?>` — collision detection
- `point in direction (pick random 30 to 150)` — random serve angle
- `point in direction (pick random -45 to -135)` — random bounce angle
- `move (15) steps` after bounce — getting out of the paddle
- `if y position < y position of Ball` — the one-line AI
- `broadcast [GAME OVER]` — sprites communicating
- `switch costume to (Score)` — the costume font trick

---

**Concept deep-dives:** [if-touching →](../../concepts-a-z/if-touching) · [variables →](../../concepts-a-z/variables) · [broadcast →](../../concepts-a-z/broadcast)

*[Back to episode guide →](../README.md) · [Next: Ep 2 →](../ep-02-snake)*
