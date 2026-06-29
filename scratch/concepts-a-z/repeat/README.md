# repeat — Do Something Exactly N Times

> 📺 **2 Sep 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)  
> Short: *(link coming 2 Sep 2026)*

**Scratch project:** *(link coming)*

---

## The Analogy

A stamper. You press it once, you get one print. You press it ten times, you get ten prints. Same action, counted. When you hit ten, you stop — unlike `forever`, which never stops.

`repeat [10]` does the blocks inside exactly 10 times, then moves on.

---

## What it does

A counted loop. Unlike `forever` (which runs endlessly), `repeat` runs a fixed number of times and stops. Everything after the `repeat` block runs once it's done.

This is Scratch's equivalent of Python's `for i in range(N)`.

---

## Where games use it

**Building the alien formation in Space Invaders:**

Nest two `repeat` blocks — one for rows, one for columns:

```
repeat [5]       ← 5 rows
  repeat [11]    ← 11 columns per row
    create clone of myself
```

That's 55 aliens from 8 blocks. Without nested `repeat`, you'd need 55 separate `create clone` blocks.

**Scanning a row in Tetris:**

```
repeat [10]      ← check each of 10 columns
  if item [n] of [board] = 0
    set [row-full] to false
```

**Stamping the snake body:**

```
repeat [length of [body-x]]
  go to x: [item [n] of [body-x]] y: [item [n] of [body-y]]
  stamp
```

---

## Where it appears in the series

- [Space Invaders →](../../series/ep-04-space-invaders) — building the 11×5 alien formation
- [Tetris →](../../series/ep-08-tetris) — scanning rows for line clears

---

*[← Back to concepts](../README.md) · Next: [if-then-else →](../if-then-else)*
