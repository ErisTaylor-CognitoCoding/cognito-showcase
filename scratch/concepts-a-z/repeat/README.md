# Repeat N Times — A Counted Loop

> 📺 ***(Short coming Wed 2 Sep 2026)*** · 🎮 ***(Scratch project coming soon)***

**Series:** Wednesday Scratch Shorts — [Cognito Coding](https://www.youtube.com/@CognitoCoding01)
**Block category:** Control (orange)

---

## What This Block Does

`repeat (10)` runs everything inside it exactly 10 times, then stops.

Different from `forever`: `forever` never stops. `repeat` stops after the exact count you give it.

---

## The Analogy

Press-ups. "Do 10 press-ups" — you do 10, then stop. You don't keep going until someone tells you to stop. You do the count.

`forever` is "keep running until I say stop." `repeat` is "do this exact number of times."

---

## How It Works

```
repeat (10)
  move (10) steps
  wait (0.1) seconds
end
```

The sprite moves 10 steps, 10 times, with a pause between each. Total movement: 100 steps. Then it stops.

---

## Building the Space Invaders Formation

`repeat` is how 55 alien clones get spawned in Space Invaders. Two nested repeat loops — one for rows (5), one for columns (11) — create a clone for each grid cell:

```
repeat (5)       [rows]
  repeat (11)    [columns]
    create clone of [myself]
  end
end
```

55 clones. Two blocks. One grid pattern.

**Snake** uses `repeat` in the body-drawing step — it repeats half the length of the Snake list, one iteration per position pair.

---

## In the Arcade Series

**Appears in:** [Ep 2 — Snake →](../../series/ep-02-snake) · [Ep 4 — Space Invaders →](../../series/ep-04-space-invaders)

*[← random-numbers](../random-numbers) · [Back to concepts →](../README.md) · Next: [if-then-else →](../if-then-else)*
