# snake-pattern — Cover Every Tile

> 📺 **25 Jul 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** nested `for` loops, grid navigation

---

## The Farmer Analogy

A field isn't a line — it's a grid. To cover every patch without doubling back, you walk one row from left to right, step sideways to the next row, then walk that one. Then the next. That's the snake pattern.

---

## What Nested Loops Do

A loop inside a loop. The **inner loop** covers one full column (`move(North)` across each tile). The **outer loop** steps to the next column after each one is done (`move(East)`).

```python
for x in range(get_world_size()):   # outer: columns
    for y in range(get_world_size()):   # inner: rows within each column
        if can_harvest():
            harvest()
        move(North)
    move(East)   # done with this column — step to the next
```

Every tile visited. No wasted moves. No missed crops.

---

## How to Read It

```
Column 0: move North x3, harvest each tile → move East
Column 1: move North x3, harvest each tile → move East
Column 2: move North x3, harvest each tile → done
```

For a 3×3 grid: 9 tiles covered in 9 steps.

---

## Why the Inner Loop Runs First

Python executes the inner loop completely for each single step of the outer loop. Think of it as: "for every column (outer), cover all rows in that column (inner)."

---

## See It in the Full Episode

[Episode 2](../../series/ep-02-operators) — this is the core navigation pattern we use from here on. Every episode after this builds on it.

---

*[← grass-strip](../grass-strip) · [Back to concepts](../README.md) · Next: [pumpkins →](../pumpkins)*
