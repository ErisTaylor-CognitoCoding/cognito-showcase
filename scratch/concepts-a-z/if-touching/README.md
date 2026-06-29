# If Touching — Collision Detection

> 📺 ***(Short coming Wed 22 Jul 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Sensing (cyan)

---

## What This Block Does

`if <touching [Sprite]?>` checks whether two sprites are overlapping. If they are, the blocks inside the `if` run.

This is the trick behind every game ever made. Pong checks if the ball is touching the paddle. Snake checks if the head is touching the body. Frogger checks if the frog is touching a car. Space Invaders checks if a bullet is touching an alien. Same block, every time.

---

## The Analogy

A touch sensor on a lift door. If something is in the way, the door doesn't close. If the sensor is clear, carry on.

---

## How It Works

```
forever
  if <touching [Paddle]?> then
    point in direction (pick random -45 to -135)
    move (15) steps
  end
end
```

Every frame, the ball checks if it's touching the paddle. If yes: bounce to a random angle, then move 15 steps to get *out* of the paddle. That last part matters — without it, the ball gets stuck inside the paddle and bounces over and over on the same frame.

---

## One Block, Many Consequences

In Frogger, the same `if touching` check means three different things:
- Touch a car → die
- Touch a log → ride it
- Touch nothing in the river → drown

The block is identical. The consequence changes based on where the frog is (which zone, which row). That's how a simple block creates a complex game.

---

## In the Arcade Series

**Appears in:** [Ep 1 — Pong →](../../series/ep-01-pong) · [Ep 2 — Snake →](../../series/ep-02-snake) · [Ep 3 — Frogger →](../../series/ep-03-frogger) · all episodes

*[← forever-loop](../forever-loop) · [Back to concepts →](../README.md) · Next: [costumes →](../costumes)*
