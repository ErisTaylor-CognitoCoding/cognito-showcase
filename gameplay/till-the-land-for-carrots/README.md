# Till the Land for Carrots

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/87-V31wpaZc?feature=share)**

> 🎮 Played in [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) — available on Steam

---

Row zero is carrots, and carrots are fussy — they only go in tilled soil. Every other row is bush, worked twice a lap for the wood and the hay that pay for those carrots. One extra check in the loop is what makes the whole field work.

---

## What the code does

The drone sweeps a column at a time, then steps east. On every ripe tile it harvests, tops the water up to 75% with a `while` loop, then checks which row it's on.

Row zero gets carrots — but only after a ground check. Carrots only plant on tilled soil, so the code reads `get_ground_type()` before calling `till()`. Two unlocks required before this line will run: **Senses** (for `get_ground_type`) and **Operators** (for `!=`).

Every other row gets bush. Each pass yields two hay; one hay buys one carrot seed. Know your exchange rate before you code — if the bush rows don't fund the carrot row, the loop starves.

---

## Concepts in this Short

| Concept | What it does |
|---------|-------------|
| `get_pos_y() == 0` | Returns the drone's Y position — row zero is the carrot row, everything else is bush |
| `get_ground_type() != Grounds.Soil` | Read the tile before acting — the `!=` operator needs the Operators unlock |
| `till()` | Prepares the ground; carrots won't plant without it |
| Nested `for` loops | Sweep the whole 2D field — outer loop steps east, inner loop moves north |
| `while get_water() < 0.75` | Top the water up before planting — runs until the tile hits 75% |

---

## Code

Full code: [`carrots.py`](carrots.py)

```python
while True:
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
                change_hat(Hats.Straw_Hat)
                while get_water() < 0.75:
                    use_item(Items.Water)
                if get_pos_y() == 0:
                    if get_ground_type() != Grounds.Soil:
                        till()
                    change_hat(Hats.Carrot_Hat)
                    plant(Entities.Carrot)
                else:
                    plant(Entities.Bush)
                change_hat(Hats.Purple_Hat)
        move(North)
    move(East)
```

---

*[← Back to gameplay](../README.md)*
