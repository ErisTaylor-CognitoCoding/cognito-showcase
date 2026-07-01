# Episode 6 — Cactus

**Series:** I Taught an AI to Farm  
**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)  
**Watch:** [Watch on YouTube →](https://youtu.be/iuiQK3me25M)

---

## What This Episode Covers

Episode 6 fixes a power farm that was leaking energy, banks the surplus, and unlocks cactus — which turns out to be a sorting puzzle in disguise.

### Concepts

| Concept | What it teaches |
|---------|----------------|
| `measure()` | Read the size of a cactus (or its neighbour by direction) |
| `swap()` | Trade the cactus under the drone with an adjacent one |
| `num_items()` | Check your inventory mid-loop to make decisions |
| Bubble sort | Compare neighbours, swap if out of order, repeat until no swaps needed |
| Boundary guard | Check `get_pos_x/y()` before swapping to avoid going off-grid |
| Orchestration | One controller calling multiple specialised crop functions |

### How the controller works

```
Always → main()              (grass, trees, carrots + sunflowers every loop)
If Power > 5000 → pumpkins() (top up the power buffer)
If Cactus < 1000 → cactus()  (sort and harvest the cactus field)
```

Each crop lives in its own module. The controller decides **when** to run each one.

### The key insight — cactus is a sorting problem

Harvest one fully-grown cactus while all its neighbours are in sorted order and it spreads across the whole patch in one explosion. The payout is the count harvested, **squared**. So the goal isn't "harvest cactus" — it's "sort the field first, then harvest one."

Sort rule: smallest bottom-left, largest top-right. Every neighbour to the north and east must be the same size or larger; south and west the same size or smaller. One out-of-place cactus breaks the chain.

---

## Files

| File | What it is |
|------|-----------| 
| `cactus.py` | The cactus routine — plant, water, bubble sort, harvest |
| `farmer.py` | Same routine as saved in the game's code editor |
| `controller.py` | The main orchestration loop — calls all crop modules |

---

## Previous Episodes

← [Episode 5 — Sunflowers](../ep-05-sunflowers) · [Episode 7 →](../ep-07-i-taught-an-ai-to-farm-ep-7) · [All Episodes](../README.md)
