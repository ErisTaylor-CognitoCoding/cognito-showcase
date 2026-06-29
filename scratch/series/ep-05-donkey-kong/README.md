# Episode 5 — Coding Donkey Kong

> 📺 **[Watch on YouTube →](https://youtu.be/AdgnAxTkI30)** · 🎮 **[Open in Scratch →](https://scratch.mit.edu/projects/1335511261/)**

**Series:** Scratch Arcade Games
**Headline concept:** Gravity — two lines of code that run every platformer ever made

---

## What We Built

Donkey Kong — four slanted girders, broken ladders, rolling barrels that drop down ladders at random, an oil drum that spawns fireballs, and a hammer power-up. Mario at the bottom, Pauline at the top.

---

## The Headline Trick — Gravity is Two Lines

```
change [Y Velocity] by (-0.6)
change y by (Y Velocity)
```

That's it. Every tick, the velocity gets a little more negative (gravity pulling down), and Mario moves by whatever velocity currently is. So he accelerates as he falls — just like real falling.

**Jumping is one push.** Set `Y Velocity` to a positive number (e.g. 12) and let gravity do the rest. The velocity goes: 12, 11.4, 10.8... 0... -0.6... -1.2 — he slows, stops at the top of the arc, falls back down. That parabola comes free from the maths. No animation, no keyframes needed.

Every barrel, every fireball in the game runs these same two lines.

---

## Slanted Girders as Maths

The girders aren't pictures — they're lines. Each one is: `surface height = A + (B × x)`. Walk right and your floor rises or falls because the formula says so.

Landing check: "Am I near that line AND not moving upward? If yes — snap my y to the surface height plus a foot offset."

The foot offset matters. Mario's y is his centre point. Without the offset, the girder cuts through his belly and his feet float. One number to tune per sprite.

---

## Other Key Ideas

**Position-based ladders** — instead of "touching colour", each ladder is checked by x and y range. Is Mario between this ladder's left/right x and between its top and bottom y? If yes, he can climb. No colour-matching, no mid-air climbing.

**The chaos rule** — every barrel has a 1-in-8 chance to drop *down* a ladder instead of rolling past. One `pick random 1 to 8` check. That's what makes the level feel alive — you can't memorise a safe route.

**The hammer** — pick it up and you smash barrels for 5 seconds. But you can't jump or climb while holding it. Pure risk vs reward. One variable, one timer.

---

## Coding Concepts in This Episode

- `change [Y Velocity] by (-0.6)` + `change y by (Y Velocity)` — gravity engine
- Setting velocity positive to jump — the arc comes from the maths
- Surface height formula for sloped girders — `A + (B × x position)`
- Position-based collision for ladders (no colour sensing)
- `pick random 1 to 8 = 1` — the chaos rule for barrels

---

**Concept deep-dives:** [forever-loop →](../../concepts-a-z/forever-loop) · [variables →](../../concepts-a-z/variables) · [random-numbers →](../../concepts-a-z/random-numbers)

*[← Ep 4](../ep-04-space-invaders) · [Back to episode guide →](../README.md) · [Next: Ep 6 →](../ep-06-pac-man)*
