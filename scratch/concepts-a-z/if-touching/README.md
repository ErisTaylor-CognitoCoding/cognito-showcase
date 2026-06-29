# if-touching — Collision Detection

> 📺 **22 Jul 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 22 Jul 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

Before you grab something, you check: is my hand close enough to reach it? Collision detection is that check, done 30 times per second by the game.

In Scratch: `if touching [SpriteName]` — true if the sprites overlap, false if they don't.

---

## What it does

Scratch compares the pixel boundaries of two sprites every time the block runs. If any pixel from sprite A overlaps any pixel from sprite B, `touching` returns true.

It's the building block of every game interaction:
- Ball touching paddle → bounce
- Player touching enemy → lose a life
- Bullet touching enemy → destroy enemy
- Player touching coin → score point

Without it, sprites pass through each other and nothing happens.

---

## Two flavours

`if touching [SpriteName]` — checks against another named sprite.

`if touching [edge]` — checks if the sprite has hit the screen boundary. Used constantly: the ball hits the edge in Pong, the frog hits the top in Frogger, the alien formation hits the side in Space Invaders.

---

## Where it appears in the series

- [Pong →](../../series/ep-01-pong) — ball vs paddle, ball vs edge
- [Snake →](../../series/ep-02-snake) — head vs food, head vs body
- [Frogger →](../../series/ep-03-frogger) — frog vs cars, frog vs logs
- [Space Invaders →](../../series/ep-04-space-invaders) — bullet vs alien, alien vs edge
- [Donkey Kong →](../../series/ep-05-donkey-kong) — Mario vs platform, Mario vs barrel

---

*[← Back to concepts](../README.md) · Next: [costumes →](../costumes)*
