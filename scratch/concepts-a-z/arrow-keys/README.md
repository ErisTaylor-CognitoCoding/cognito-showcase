# Arrow Keys + Move 10 Steps — Basic Player Control

> 📺 ***(Short coming Wed 8 Jul 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Events + Motion

---

## What This Teaches

How to make a sprite respond to the player.

Two blocks working together:
- `if <key [right arrow] pressed?>` — checks whether a key is held down this frame
- `move (10) steps` — moves the sprite 10 pixels in whichever direction it's facing

Stack them inside a `forever` loop and your sprite responds instantly, every frame.

---

## The Analogy

Arrow keys are the bridge between the player and the game. Without them, the game plays itself. With them, the player is in control.

---

## How It Works

```
when green flag clicked
forever
  if <key [right arrow] pressed?> then
    point in direction (90)
    move (10) steps
  end
  if <key [left arrow] pressed?> then
    point in direction (-90)
    move (10) steps
  end
end
```

`point in direction` sets the facing direction first. Then `move 10 steps` moves in that direction. The `forever` loop runs this check every frame — held keys feel smooth and responsive.

---

## The 10 Steps Number

10 is a starting point. Bigger = faster. Smaller = slower. In Pong, the player paddle moves at 7 (and the AI at 4). In Donkey Kong, Mario moves at 4. These numbers are your difficulty dial — tune them by feel.

---

## In the Arcade Series

**Appears in:** [Ep 1 — Pong →](../../series/ep-01-pong) · [Ep 5 — Donkey Kong →](../../series/ep-05-donkey-kong)

*[← green-flag](../green-flag) · [Back to concepts →](../README.md) · Next: [forever-loop →](../forever-loop)*
