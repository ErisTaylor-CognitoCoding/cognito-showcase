# Forever Loop — Runs Until You Stop It

> 📺 ***(Short coming Wed 15 Jul 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Control (orange)

---

## What This Block Does

The `forever` block runs everything stacked inside it over and over, for as long as the program is running. It never stops by itself.

This is the engine of every game. Pong's ball moves because it's inside a forever loop. Snake's head checks for input inside a forever loop. Space Invaders' formation steps inside a forever loop. Without `forever`, your game would run once and freeze.

---

## The Analogy

A hamster wheel. The hamster runs and runs. The wheel never stops on its own — you have to take the hamster out.

In code: the hamster is your game logic. The wheel is the forever loop. Every frame, it runs again.

---

## How It Works

```
when green flag clicked
forever
  move (10) steps
  if <on edge?> then
    bounce
  end
end
```

Without the `forever`, the sprite moves 10 steps once and stops. With it, the sprite moves 10 steps every frame, bouncing off edges forever.

---

## Stopping It

`stop [this script]` breaks out of a forever loop. Use it when a game-over condition is met — stop the ball, stop the enemies, end the game. In Snake, `Game Running = 0` gates the forever loop so all movement pauses on death without needing to stop the script.

---

## In the Arcade Series

`forever` is in every game. It is the game loop.

**Appears in:** [Ep 1 — Pong →](../../series/ep-01-pong) · [Ep 2 — Snake →](../../series/ep-02-snake) · all episodes

*[← arrow-keys](../arrow-keys) · [Back to concepts →](../README.md) · Next: [if-touching →](../if-touching)*
