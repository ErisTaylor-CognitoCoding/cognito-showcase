# Variables — Keeping Score

> 📺 ***(Short coming Wed 12 Aug 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Variables (orange)

---

## What a Variable Does

A variable is a named box that holds a number (or text). You can put a value in, read it out, or change it.

```
set [Score] to (0)
change [Score] by (1)
```

`Score` starts at 0. Every time you eat an apple, hit an alien, or land on a lily pad, you add 1. Scratch remembers that number across the whole game.

---

## The Analogy

A whiteboard with a label. The label doesn't change — "Score" is always "Score". But the number written on it gets erased and rewritten every time you score. That's a variable.

---

## For All Sprites vs This Sprite Only

When you create a variable in Scratch, it asks: **For all sprites** or **For this sprite only**.

- **For all sprites** — every sprite can read and change it. Use this for shared game state: `Score`, `Lives`, `Game Running`, `Formation DX`.
- **This sprite only** — only this sprite can see it. Use this for clone-local state: a clone's health, its direction, its dive phase.

Getting this wrong is the most common Scratch variable bug. A clone variable set to "for all sprites" gets overwritten by every other clone simultaneously — chaos.

---

## In the Arcade Series

Variables run every game:
- `Score` and `Lives` — Pong, Snake, Frogger, all of them
- `Y Velocity` — Donkey Kong's gravity engine (change it by -0.6 each frame)
- `Formation DX` — Space Invaders' direction (shared across all 55 alien clones)
- `Direction` — Snake's movement direction (1=right, 2=left, 3=up, 4=down)
- `Game Running` — the on/off flag that gates all game logic

Every mechanic in every game is built on at least one variable.

**Appears in:** [Ep 1 — Pong →](../../series/ep-01-pong) · [Ep 2 — Snake →](../../series/ep-02-snake) · all episodes

*[← glide-to](../glide-to) · [Back to concepts →](../README.md) · Next: [broadcast →](../broadcast)*
