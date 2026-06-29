# Animate with Costumes — Bringing Sprites to Life

> 📺 ***(Short coming Wed 29 Jul 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Looks (purple)

---

## What This Teaches

A Scratch sprite can have multiple costumes — different images under the same name. Switching between them creates animation.

One sprite. Multiple costumes. One block: `switch costume to [name]`.

---

## The Analogy

A flipbook. Each page is a slightly different drawing. Flick through fast enough and it looks like movement.

In Scratch, each "page" is a costume. The `switch costume to` block turns the page.

---

## How It Works

```
when green flag clicked
forever
  switch costume to [walk1]
  wait (0.1) seconds
  switch costume to [walk2]
  wait (0.1) seconds
end
```

Two costumes, switching every 0.1 seconds. That's a walking animation. Faster switching = smoother motion.

---

## The Score Display Trick

In the Scratch arcade series, costumes do something more clever than animation. The scoreboard sprite has 10 costumes named "0" through "9". The `switch costume to (Score mod 10)` block picks the costume that matches the digit. Costume "7" appears when the score ends in 7.

That's how the retro pixel-font scoreboards work in Pong, Snake, and Frogger — no special font plugin, no extra library.

In Space Invaders, the alien formation toggles between two costumes in unison every step — that's what creates the classic marching-leg animation. One broadcast, 55 clones switching costume at the same moment.

---

## In the Arcade Series

**Appears in:** [Ep 1 — Pong →](../../series/ep-01-pong) · [Ep 2 — Snake →](../../series/ep-02-snake) · [Ep 3 — Frogger →](../../series/ep-03-frogger) · [Ep 4 — Space Invaders →](../../series/ep-04-space-invaders)

*[← if-touching](../if-touching) · [Back to concepts →](../README.md) · Next: [glide-to →](../glide-to)*
