# Till the Land for Carrots

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/87-V31wpaZc?feature=share)**

**Game:** The Farmer Was Replaced (Steam)

---

Row zero is carrots, and carrots are fussy — they only go in tilled soil. Every other row is bush, worked twice a lap for the wood and the hay that pay for those carrots. One extra check in the loop is what makes the whole field work.

---

## What the code does

The drone sweeps a column at a time, then east. For every ripe tile it:
1. Harvests
2. Waters up to 75% with a `while` loop
3. Checks `get_pos_y()` — row zero gets carrots, every other row gets bush

On row zero, before planting, it reads `get_ground_type()`. If the ground isn't tilled soil, it calls `till()` first — carrots won't plant on anything else. That single line needs two unlocks before it runs: **Senses** (for `get_ground_type`) and **Operators** (for `!=`).

The bush rows fund the carrot row. Each pass: harvest the bush for wood → harvest the hay that grows back → replant the bush. Two hay per pass, one hay buys one carrot seed.

---

## Concepts covered

| Concept | What it does |
|---------|-------------|
| Nested `for` loops | Sweeps every tile: inner loop moves North, outer loop steps East |
| `while` loop | Waters each tile until `get_water() >= 0.75` |
| `get_pos_y()` | Returns the drone's Y position — splits row zero from the rest |
| `get_ground_type()` | Reads the tile's ground type before deciding to till |
| `till()` | Converts ground to farmable soil — required before planting carrots |
| `plant(Entities.Carrot)` | Plants a carrot — only works on tilled soil |
| `plant(Entities.Bush)` | Plants a bush — the economy crop that funds the carrot row |

---

## End-state code

See [`carrots.py`](carrots.py) — the full script from the episode.

---

*[← back to gameplay](../README.md)*
