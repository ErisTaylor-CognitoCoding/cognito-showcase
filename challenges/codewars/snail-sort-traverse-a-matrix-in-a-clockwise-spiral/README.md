# Snail Sort — Traverse a Matrix in a Clockwise Spiral

**Source:** [Codewars — 4 kyu](https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1)
**Category:** Algorithmic
**Difficulty:** Intermediate
**Estimated time:** 1–2 hr

> Nothing makes you think about arrays spatially like a clockwise spiral — and the moment the pattern clicks the solution almost writes itself. Classic "aha" kata.

## The challenge

Given an n×n 2D array, return all elements arranged from outermost to centre, travelling clockwise — like a snail's shell. The kata is [4 kyu on Codewars](https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1) with 85,000+ completions: well-trodden enough to have great discussion, but tricky enough to make you think spatially. The solution fits in under 20 lines once the pattern clicks.

## Approach

The elegant trick: **peel + rotate**.

After collecting the top row (going right), rotate the remaining matrix 90° counter-clockwise. Now what was the right column is the new top row. Collect it. Rotate again. Repeat until empty.

```
[[1, 2, 3],     → peel [1,2,3]  → rotate CCW →  [[6, 9],
 [4, 5, 6],                                        [5, 8],
 [7, 8, 9]]                                        [4, 7]]

→ peel [6,9]    → rotate CCW →  [[8, 7],
                                  [5, 4]]

→ peel [8,7]    → rotate CCW →  [[4],
                                  [5]]

→ peel [4]      → rotate CCW →  [[5]]

→ peel [5]      → done

Result: [1, 2, 3, 6, 9, 8, 7, 4, 5]  ✓
```

The rotation step is `list(zip(*matrix))[::-1]`: `zip(*matrix)` transposes, `[::-1]` reverses row order — together that's a 90° CCW rotation in one expression.

## Solution

```python
def snail(snail_map):
    result = []
    while snail_map:
        # Peel the top row (left → right)
        result += list(snail_map.pop(0))
        # Rotate remaining 90° counter-clockwise so right column → new top row
        if snail_map and snail_map[0]:
            snail_map = [list(row) for row in zip(*snail_map)][::-1]
    return result
```

Full solution with tests: [`solution.py`](./solution.py)

## Concepts used

- **2D array traversal** — moving through a grid using indices to control direction rather than relying on nested loops alone
- **Clockwise spiral** — tracking direction changes (right → down → left → up) to peel one complete ring off the matrix per cycle
- **Layer-by-layer reduction** — each pass strips the outermost ring and works inward until the array is empty
- **zip + slice rotation** — `list(zip(*m))[::-1]` is the Python idiom for a 90° CCW matrix rotation
- **Edge-case handling** — correctly terminating when the matrix is empty (`[]`) or the final ring is a single element

[← back to challenges index](../../README.md)
