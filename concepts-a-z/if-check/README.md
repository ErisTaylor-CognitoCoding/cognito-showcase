# if-check — Only Act When Ready

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/-wpMsjlb5yE)**

**Game:** The Farmer Was Replaced  
**Concepts:** `if can_harvest()`, conditional guards

---

## The Farmer Analogy

A farmer doesn't swing the scythe at every patch — they check first. Is there anything to harvest? If yes, harvest. If not, wait.

The drone does the same: `if can_harvest()` is the check before the swing.

---

## Before and After

**Before** — harvests without checking (breaks once you unlock speed upgrades):
```python
while True:
    harvest()
```

**After** — guard before every swing:
```python
while True:
    if can_harvest():
        harvest()
```

---

## Why This Matters

Speed upgrades make the drone fast enough to arrive at a tile *before* the crop is ready. Without the check, the drone wastes a harvest swing on an empty tile.

With the check: the drone arrives, checks, waits if needed — no broken runs, no missed crops.

On grass it nearly always passes straight through. But building the habit now means your code survives every crop that comes after.

---

## What `if` Does

A conditional. Python evaluates the expression after `if`. If it's `True`, the indented block runs. If it's `False`, the block is skipped.

`can_harvest()` is a built-in game function that returns `True` when the current tile is ready to harvest.

---

## See It in the Full Episode

[Episode 1](../../series/ep-01-first-program) — we add this guard early on and carry it through every episode after.

---

*[← harvest](../harvest) · [Back to concepts](../README.md) · Next: [grass-strip →](../grass-strip)*
