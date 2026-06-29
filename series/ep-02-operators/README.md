# Episode 2 — Operators → Full 3×3

> 📺 **[Watch on YouTube →](https://youtu.be/qB2nKoU1dkI)**

**Series:** I Taught an AI to Farm  
**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)

---

## What We Built

Cracked the EP1 cliffhanger. The drone navigates a full 3×3 farm — grass, bushes, and carrots all running together in one pass. The unlock wasn't a new function. It was **operators**. The first time the drone could *compare* two things.

---

## Coding Concepts Covered

### `get_pos_x()` and `get_pos_y()`
Position sensing. The drone finally knows where it is on the grid. `get_pos_x()` returns the current column, `get_pos_y()` the current row.

### Comparison operators: `==`, `<`, `>`
The unlock. Instead of just doing things, the drone can now *decide* based on where it is.

```python
if get_pos_y() == 2:
    till()
    plant(Entities.Carrot)
```

### `till()`
Prepares tilled soil for planting carrots. Grass grows on untilled soil; carrots need tilled soil first.

### Three crops in rotation
- Row 0 → bushes (for wood)
- Row 1 → hay (grass, self-seeds)
- Row 2 → carrots (need tilling first)

One nested loop covers all three.

---

## End-State Code

See [`farm.py`](./farm.py)

---

**Concept deep-dives:** [grass-strip →](../../concepts-a-z/grass-strip) · [snake-pattern →](../../concepts-a-z/snake-pattern)

*[← Ep 1](../ep-01-first-program) · [Back to guide](../README.md) · [Next: Ep 3 →](../ep-03-functions)*
