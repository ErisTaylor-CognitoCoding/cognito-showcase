# grass-strip — Farm a Full Row

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/TGDX4BRNBDw)**

**Game:** The Farmer Was Replaced  
**Concepts:** `for` loop, `range()`, `move(North)`

---

## The Farmer Analogy

Walking a row of crops from one end to the other — harvesting each patch, stepping forward, harvesting again. When you reach the end, you stop.

`for i in range(get_world_size())` is the walk. `move(North)` is each step.

---

## What `for` Does

A counted loop. Unlike `while True` (which runs forever), `for` runs a fixed number of times and stops automatically.

```python
for i in range(get_world_size()):
    if can_harvest():
        harvest()
    move(North)
```

`get_world_size()` returns however wide the farm is — so this always covers exactly one full row, at any grid size.

---

## Why This Beats `while True` for Row Navigation

`while True` never knows when it's done. A `for` loop stops automatically after `get_world_size()` steps — the drone reaches the end of the row and *knows it*. Essential once you need to know when a pass is finished before moving to the next column.

---

## The Difference

| | runs | stops |
|---|---|---|
| `while True` | forever | only if you break out |
| `for i in range(n)` | exactly `n` times | automatically |

---

## See It in the Full Episode

[Episode 2](../../series/ep-02-operators) — we chain two `for` loops together to cover the full 3×3 grid.

---

*[← if-check](../if-check) · [Back to concepts](../README.md) · Next: [snake-pattern →](../snake-pattern)*
