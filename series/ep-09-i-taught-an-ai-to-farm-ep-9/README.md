# I Taught an AI to Farm — Ep 9: Four Drones, No Signal

> 📺 **[Watch on YouTube →](https://youtu.be/BdORh_gViFk)**

**Series:** I Taught an AI to Farm | **Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)

---

## What We Built

Two drones weren't enough. After unlocking four, the challenge was dividing one field between them — without any shared memory or messaging between drones. The answer: split the field into column lanes based on spawn position, then use *dying* as the communication signal. Each worker runs one pass and returns from its function, which kills the drone. The base sits on `while num_drones() > 1: pass`, waiting to be the last one alive before it does anything that needs isolation.

---

## Concepts Covered

### Lane assignment from spawn position

No arguments, no shared variables — each drone wakes up, reads `get_pos_x()`, and works out which columns it owns from that alone.

```python
LANES = 3
lane = get_world_size() // LANES
if get_pos_x() >= (LANES - 1) * lane:
    lane = get_world_size() - get_pos_x()  # last drone mops up the remainder
```

### Death as a synchronisation gate

Workers run one pass then return — returning kills the drone. The base counts down to 1 before acting.

```python
while num_drones() > 1:
    pass
```

### Jobs that can't be parallelised

The pumpkin merge needs every tile ripe at the same instant, so the honest count can only happen when one drone is alone on the field. The cactus bubble sort has to see the whole grid to swap — splitting it would corrupt the result. Knowing *which* jobs can't split is as important as splitting the ones that can.

---

## End-State Code

Four files from this episode — each a self-contained stage of the drone unlock:

| File | What it does |
|------|-------------|
| [`megafarm2drones.py`](./megafarm2drones.py) | Ep 8 carry-over — two drones (field + sunflower) |
| [`megafarm4dronesmain.py`](./megafarm4dronesmain.py) | Four drones on the main field in lanes |
| [`MegaFarm4DronesPumpkin.py`](./MegaFarm4DronesPumpkin.py) | Four drones on pumpkins with the harvest gate |
| [`megafarms4dronecactus.py`](./megafarms4dronecactus.py) | Four planters + single-drone sort on cactus |

---

[← back to series](../README.md)
