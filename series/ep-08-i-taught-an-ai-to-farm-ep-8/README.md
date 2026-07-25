# I Taught an AI to Farm — Ep 8: Solving a Maze

> 📺 **[Watch on YouTube →](https://youtu.be/mT0pmo3Obfo)**

**Series:** [The Farmer Was Replaced](../README.md) — Wed Farmer  
**Game:** [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) (Steam)

---

## What We Built

A hedge maze grows from a single bush — pour Weird Substance on it and the whole plot explodes into corridors. Somewhere inside is the treasure. We built a depth-first search (DFS) solver that flies the drone through the maze, backs out of dead ends, and tries the next corridor until it finds the gold. That worked perfectly on a fresh maze. Then we tried reusing the maze by pouring substance on the treasure to respawn it instead of harvesting — but that removes walls randomly, creating loops. The solver got stuck circling and never came back. The fix was two lines of Python: a visited list. Tree becomes graph, solver carries on indefinitely.

---

## Concepts Covered

### `opposite()` — reverse direction helper

```python
def opposite(d):
    if d == North:
        return South
    if d == South:
        return North
    if d == East:
        return West
    return East
```

When the drone hits a dead end it needs to fly back the way it came. `opposite()` hands back the reverse of any direction — four lines, always accurate.

### `cell()` — encode a 2D position as one number

```python
def cell():
    return get_pos_x() * get_world_size() + get_pos_y()
```

Every grid square gets a unique number: `x × world_size + y`. It turns a 2D grid into something you can store in a flat list and check against instantly — the same trick NES Tetris used in 1989.

### `explore()` — depth-first search (DFS) with recursion

```python
def explore(came_from, seen):
    if get_entity_type() == Entities.Treasure:
        return True
    seen.append(cell())
    for d in [North, East, South, West]:
        if d != came_from:
            if move(d):
                if cell() not in seen:
                    if explore(opposite(d), seen):
                        return True
                move(opposite(d))
    return False
```

A function that calls itself — that's **recursion**. The drone flies as far down one corridor as it can, asking the same question at each new square. Hit a dead end → return `False` → caller tries the next direction. The `came_from` guard stops it immediately doubling back. The `seen` list is the fix: if a square is already in `seen`, skip it — the drone never circles.

### The visited list — the bug and the fix

Without `seen`, the solver hangs on any loop. The drone writes its trail but never reads it back — keeping a diary and never opening it. Adding `if cell() not in seen:` before every forward move is the whole fix. The bug wasn't in the DFS logic; it was in a broken assumption: the docs said mazes have no loops. Reusing the maze by respawning the treasure removes walls, creates loops, and silently invalidates that contract.

### Respawning treasure — farming the maze indefinitely

```python
def mazes():
    plant(Entities.Bush)
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)
    while True:
        if explore(None, []):
            use_item(Items.Weird_Substance, substance)
            change_hat(Hats.Straw_Hat)
mazes()
```

Pour the same amount of Weird Substance on the found treasure to collect the gold and spawn a new treasure in the same maze — no regrow needed. The drone loops indefinitely, hat tip on every score.

---

## End-State Code

Full solution in [`farmer.py`](./farmer.py) — `opposite()`, `cell()`, the full `explore()` DFS with visited list, and the outer `mazes()` loop.

---

*[← back to series](../README.md) · [Next: Ep 9 →](../ep-09-i-taught-an-ai-to-farm-ep-9)*
