# Episode 1 — First Program → 1×3 Strip

> 📺 **[Watch on YouTube →](https://youtu.be/maTaBrkHh1o)**

**Series:** I Taught an AI to Farm  
**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)

---

## What We Built

Zero → working farm in one episode. Started with a blank drone on a single tile of grass, ended with a 1×3 strip harvesting on autopilot. Then hit the first real problem: the drone can sweep one row but has no idea how to navigate a full grid.

---

## Coding Concepts Covered

### `harvest()`
The first command. Grabs whatever is ready on the current tile. Grass regrows automatically — no replanting needed.

### `while True:`
An infinite loop. Everything inside runs forever. One call to `harvest()` becomes an endless farm.

```python
while True:
    harvest()
```

### `if can_harvest():`
A guard condition. Before swinging, check whether the tile is actually ready. On grass it nearly always passes — but adding the check now means your code won't break when you add crops that take time to grow.

```python
while True:
    if can_harvest():
        harvest()
```

### `move(North)`
Moves the drone one tile in a direction. Paired with a loop, it walks a full row.

---

## Cliffhanger

The drone swept a 1×3 strip fine. But expanding to a full 3×3 broke — it walked off the grid because it had no idea where it was. Episode 2 solves it: **operators**, and the drone learns to compare.

---

## End-State Code

See [`farm.py`](./farm.py)

---

**Concept deep-dives:** [harvest →](../../concepts-a-z/harvest) · [if-check →](../../concepts-a-z/if-check)

*[← Back to episode guide](../README.md) · [Next: Ep 2 →](../ep-02-operators)*
