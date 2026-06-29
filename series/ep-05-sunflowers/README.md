# Episode 5 — Sunflowers (Running Maximum)

> 📺 **Video link coming** *(published 24 Jun 2026)*

**Series:** I Taught an AI to Farm  
**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)

---

## What We Built

Tightened the pumpkin code from EP4, then unlocked sunflowers on a big **12×12** grid. The catch: only the sunflower with the **most petals** drops a Sun when harvested. Cut the wrong one and it's wasted.

The solution: sweep the entire grid tracking a `max_petals` variable. Update it whenever you find a bigger one. At the end, sweep again and harvest only the champion.

---

## Coding Concepts Covered

### `measure()` — reading a numeric property
Returns a number you can compare. For sunflowers: the petal count. More petals = more valuable.

### The running-max pattern
Classic technique. Start with zero, compare everything you see, update when you find something bigger.

```python
max_petals = 0
# for every sunflower on the grid:
if measure() > max_petals:
    max_petals = measure()   # new champion — remember this count
```

By the end of the sweep, `max_petals` holds the highest petal count in the field.

### Double sweep
1. **First sweep** — find the maximum petal count across the whole 12×12.
2. **Second sweep** — walk the grid again, harvest only the tile where `measure() == max_petals`.

---

## Cliffhanger

We tracked the best *petal count* — but never *where* the champion was. After sweep one, the drone had to re-walk the entire 12×12 to find it. One variable holds one value.

Next episode: **lists** — so the drone can remember both the petal count *and* the position together.

---

## End-State Code

See [`farm.py`](./farm.py)

---

**Concept deep-dive:** [sunflowers →](../../concepts-a-z/sunflowers)

*[← Ep 4](../ep-04-pumpkins) · [Back to guide](../README.md)*
