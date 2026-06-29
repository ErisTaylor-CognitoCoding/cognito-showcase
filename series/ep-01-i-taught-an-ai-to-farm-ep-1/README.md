# I Taught an AI to Farm — Episode 1

> 📺 **[Watch on YouTube →](https://youtu.be/maTaBrkHh1o)**

**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam) — write real Python to automate a drone and farm the land.

---

## What we built

Welcome to the series. Starting from a blank script and a single patch of grass, we go from writing our very first `harvest()` call all the way to a running 3×3 farm — grass, bushes and hay all going at once. Along the way we hit our first real problem: the drone can sweep one row, but it has no idea where it is on the grid. That cliffhanger sets up Episode 2.

---

## Concepts covered

### `while True` — the forever loop

The drone keeps farming until we tell it to stop. Without this, it runs once and quits.

```python
while True:
    harvest()
    move(North)
```

### `if can_harvest()` — only act when ready

Crops take time to grow. This check stops the drone wasting a move on an empty tile.

```python
while True:
    if can_harvest():
        harvest()
    move(North)
```

### Expanding the grid — `move(North)` + row logic

Moving north after each harvest steps the drone through a column. Combining directions lets us sweep a strip.

```python
for i in range(get_world_size()):
    harvest()
    move(North)
move(East)
```

---

## End-state code

> 💻 Code will be added here when the episode is revisited. See the [YouTube video](https://youtu.be/maTaBrkHh1o) for the full build.

---

← [Back to The Farmer Was Replaced series](../README.md)
