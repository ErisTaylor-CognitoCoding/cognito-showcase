# I Taught an AI to Farm — Ep 7: Fertiliser + Maze Unlock

> 📺 **[Watch on YouTube →](https://youtu.be/fI1fF9-VIo8)**

**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)  
**Series:** [← Back to episode guide](../README.md)

---

## What we built

The drone farm goes from passive (growing on a timer) to active (growing on demand). We add `use_item(Items.Fertilizer)` to cut every crop's grow time, scale the grid to 16×16 without changing a single loop, and pick up 21,000 Weird Substance in the process — which unlocks Mazes. Ends on a cliffhanger: the Maze is open but the drone has no idea how to navigate it.

---

## Concepts covered

### `use_item(Items.Fertilizer)` — grow crops instantly

Calling `use_item` with an item type consumes one unit from the drone's inventory and applies its effect immediately. Fertilizer knocks two seconds off a crop's grow timer. Across a 16×16 farm, those two-second gains compound fast.

```python
if get_entity_type() != None and num_items(Items.Fertilizer) > 0:
    use_item(Items.Fertilizer)
```

**Order matters:** fertilise *before* watering. `use_item(Items.Fertilizer)` resets the tile's water to zero as a side effect — water poured before fertilising is silently wasted.

---

### `get_world_size()` — never hardcode the grid

Every loop in this codebase reads the grid size from the game at runtime. When the farm expanded from 12×12 to 16×16, the same code ran untouched:

```python
for i in range(get_world_size()):
    for j in range(get_world_size()):
        # covers every tile, any grid size
```

A **magic number** (`for i in range(16)`) would break in nine places at once. `get_world_size()` breaks in zero.

---

### Python indentation — grammar, not decoration

Python uses indentation to define which code belongs to which block. When `use_item(Items.Fertilizer)` landed at the wrong indent level after pasting, Python raised an `IndentationError` — not because the logic was wrong, but because the line was sitting outside the `if` it was supposed to belong to. Four tabs in, level with `if can_harvest()`, and it's fixed.

Don't mix tabs and spaces. On screen they look identical. To Python they are completely different characters — it will refuse to run.

---

### Debugging by watching, not guessing

When the farm went quiet mid-run it looked broken. It wasn't — the drone had run out of water and was waiting to replenish. The lesson: before optimising any loop, find out what it's *actually* waiting on. Nine times out of ten it's not the code.

---

## End-state code

See [`main.py`](./main.py) — the exact file running at the end of this episode.

Key additions vs Ep 6:
- `use_item(Items.Fertilizer)` inside the main planting loop, *before* the water block
- `sunflowers()` helper extracted and called at the top of `main()` to sweep the sunflower row separately
- All loops read `get_world_size()` — no hardcoded grid dimensions anywhere

---

## What's next

The Maze is unlocked. The drone can't navigate it yet. That's Ep 8.

[Episode 8 →](../ep-08-i-taught-an-ai-to-farm-ep-8)

---

*[← Back to series](../README.md) · [Cognito Coding YouTube](https://www.youtube.com/@CognitoCoding01)*
