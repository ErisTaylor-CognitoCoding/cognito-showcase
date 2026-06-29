# Episode 4 — Pumpkins (Variables + Tile State)

> 📺 **[Watch on YouTube →](https://youtu.be/X92lWWj8HbY)**

**Series:** I Taught an AI to Farm  
**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)

---

## What We Built

Resolved EP3's cliffhanger — the drone can now *remember* things between passes using variables. Then unlocked pumpkins: a crop with three states — growing, ripe, and dead. The code reads each tile, branches on what's there, and handles each state differently.

**The big mechanic:** adjacent ripe pumpkins merge into one giant pumpkin. Clear the dead ones so ripe pumpkins can cluster — then harvest the giant.

---

## Coding Concepts Covered

### Variables — the drone finally remembers
Store a value and use it across the run. Unlike functions (which reset after each call), a variable keeps its value.

```python
# Start with a baseline, update as you go
found_ripe = 0
```

### `if / elif / else` — branching on tile state
Read what's on the tile with `get_entity_type()` and `get_growth()`, then do the right thing for each case.

```python
entity = get_entity_type()
if entity == Entities.Pumpkin:
    growth = get_growth()
    if growth == 1:      # ripe — harvest the merge
        harvest()
    elif growth == 0:    # dead — clear the tile
        harvest()
```

### Reading tile state
- `get_entity_type()` — what crop is on this tile? (`None` = empty)
- `get_growth()` — how far through its lifecycle? `0` = dead, `1` = ripe (for pumpkins)

---

## Cliffhanger

The pumpkin layout is random — ripe pumpkins keep landing next to dead ones, so half the merges fail. Next episode: sunflowers and a trick that fixes the layout for both.

---

## End-State Code

See [`farm.py`](./farm.py)

---

**Concept deep-dives:** [pumpkins →](../../concepts-a-z/pumpkins) · [dead-crops →](../../concepts-a-z/dead-crops)

*[← Ep 3](../ep-03-functions) · [Back to guide](../README.md) · [Next: Ep 5 →](../ep-05-sunflowers)*
