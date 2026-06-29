# I Taught an AI to Farm — Episode 2

> 📺 **[Watch on YouTube →](https://youtu.be/qB2nKoU1dkI)**

**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam) — write real Python to automate a drone and farm the land.

---

## What we built

The Episode 1 cliffhanger resolved: the drone learns where it is. But the real unlock isn't position sensing — it's **operators**. The moment the drone can *compare* two values, the full 3×3 farm snaps into place with grass, bushes and carrots all rotating together.

---

## Concepts covered

### `get_pos_x()` / `get_pos_y()` — the drone finds its place

The drone can now read its own coordinates, so we can make decisions based on *where* it is on the grid.

```python
if get_pos_x() == 2:
    plant(Entities.Carrot)
```

### Comparison operators — `==`, `<`, `>`

The first time the code compares two things. Once a program can evaluate a condition, it can make decisions — this is the shift from automation to logic.

```python
for j in range(get_world_size()):
    if j == 2:
        till()
        plant(Entities.Carrot)
```

### Multi-crop rotation — grass, bushes, carrots together

Each grid position gets a different crop based on coordinates. Three crops, one loop, one drone.

---

## End-state code

> 💻 Code will be added here when the episode is revisited. See the [YouTube video](https://youtu.be/qB2nKoU1dkI) for the full build.

---

← [Back to The Farmer Was Replaced series](../README.md)
