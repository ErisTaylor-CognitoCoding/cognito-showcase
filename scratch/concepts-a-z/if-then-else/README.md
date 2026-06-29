# If-Then-Else — Two Paths, One Decision

> 📺 ***(Short coming Wed 9 Sep 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Control (orange)

---

## What This Block Does

`if-then-else` checks a condition. If it's true, run the top set of blocks. If it's false, run the bottom set.

`if-then` handles "do this if true." `if-then-else` handles "do this if true, *or do that if false*." Two paths, one condition, always one taken.

---

## The Analogy

A fork in the road. You arrive at the junction: left goes to the café, right goes home. Is the café open? If yes, go left. If no, go right. You always take exactly one path.

---

## How It Works

```
if <(Score mod 10) = 0> then
  switch costume to (10)
else
  switch costume to (Score mod 10)
end
```

This is the costume-zero workaround from the arcade series. Scratch's costume picker is zero-indexed differently from costume names — when the digit is 0, you need the else branch to handle it explicitly.

---

## The AI Paddle in Pong

```
if <(y position) < (y position of Ball)> then
  change y by (4)
else
  change y by (-4)
end
```

Two behaviours. One check. If the ball is above, move up. If it's below, move down. That's the entire AI. One `if-then-else` block, four lines, unbeatable at speed 10.

---

## In the Arcade Series

**Appears in:** [Ep 1 — Pong →](../../series/ep-01-pong) (AI paddle + score display) · [Ep 2 — Snake →](../../series/ep-02-snake) (direction blocking + score display) · all episodes

*[← repeat](../repeat) · [Back to concepts →](../README.md) · Next: [wait →](../wait)*
