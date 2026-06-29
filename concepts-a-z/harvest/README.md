# harvest — Your First Loop

> 📺 **4 Jul 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** `harvest()`, `while True`

---

## The Farmer Analogy

Imagine you're standing in a field. You grab a handful of hay. The grass grows back instantly. You grab another handful.

In code: `harvest()` is the grab. `while True` is "do it forever."

---

## Step 1 — Your very first command

The starting tile already has grass — no planting needed. Just type `harvest`. The drone grabs the hay and the grass grows straight back.

```python
harvest()
```

## Step 2 — After collecting 5 grass, loops unlock

Instead of typing `harvest` over and over, wrap it in `while True`. That runs forever: harvest, regrow, harvest again — non-stop.

```python
while True:
    harvest()
```

One word became an endless farm.

---

## What `while True` Actually Does

A `while` loop keeps running as long as its condition is true. `True` is always true — so it never stops. Everything indented inside runs on repeat until you close the program.

---

## See It in the Full Episode

[Episode 1](../../series/ep-01-first-program) — this is the first thing we built. By the end of that episode, the drone was sweeping a full 1×3 strip.

---

*[← Back to concepts](../README.md) · Next: [if-check →](../if-check)*
