# `tfwr-running-max` — Sunflowers and the max-petal check

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/96X7_4E_yv0?feature=share)**

---

Twelve sunflowers in a row and only one of them's worth harvesting: the one with the most petals. The drone can't see the whole row at once — so it has to remember. One variable does the entire job.

## The pattern — running max

```python
best = 0

for i in range(get_world_size()):
    petals = measure()
    if petals > best:
        best = petals
```

One variable called `best`. Starts at zero. Every tile, compare the petal count. If it's bigger, `best` gets updated. End of row — `best` holds the highest petal count on the farm. No list. No sort. No second pass.

## What's happening

- Set `best = 0` before the loop — needs a starting baseline to compare against from tile one.
- `measure()` returns the petal count for the current tile.
- One `if`: is this tile better than the current best? Update. If not, keep flying.
- After the loop, `best` is the answer.

This is the **running max** pattern. Same shape works for high scores, longest words, closest targets — anything where you only need to keep the winner, not the whole list.

*Part of the **The Farmer Was Replaced** gameplay short series.*  
*[← back to gameplay](../README.md)*
