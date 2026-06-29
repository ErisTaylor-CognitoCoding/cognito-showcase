# Wait Blocks — Pacing

> 📺 ***(Short coming Wed 16 Sep 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Control (orange)

---

## What This Block Does

`wait (1) seconds` pauses the script for that many seconds before running the next block.

Without waits, loops run at Scratch's maximum frame rate. Sometimes that's right — the Pong ball should move every frame. Sometimes you need a controlled pause: the snake needs 0.1 seconds between steps, the turtle needs 3 seconds underwater, the Space Invaders formation needs a beat between moves.

---

## The Analogy

A traffic light. Green for 30 seconds — wait — amber for 3 seconds — wait — red for 30 seconds. Each phase runs for a fixed duration before the next begins. `wait` is the pause between phases.

---

## The Snake Difficulty Dial

```
# Slower snake (easier):
wait (0.2) seconds

# Default:
wait (0.1) seconds

# Faster snake (harder):
wait (0.05) seconds
```

In Snake, the `wait` inside the forever loop controls how fast the snake moves. Change one number to change the difficulty. That's a difficulty dial — one block, one value, the whole feel of the game shifts.

---

## Dynamic Waits — Space Invaders Tempo

`wait` can take a variable instead of a fixed number:

```
wait (Formation Step) seconds
```

In Space Invaders, `Formation Step` gets smaller as aliens are destroyed (`Formation Step = Initial Step × Aliens Left / 55`). The wait shrinks. The pace accelerates. One variable feeding one `wait` block — that's the entire Space Invaders tempo mechanic.

---

## In the Arcade Series

**Appears in:** [Ep 2 — Snake →](../../series/ep-02-snake) (difficulty dial) · [Ep 3 — Frogger →](../../series/ep-03-frogger) (hop cooldown) · [Ep 4 — Space Invaders →](../../series/ep-04-space-invaders) (formation step interval)

*[← if-then-else](../if-then-else) · [Back to concepts →](../README.md)*
