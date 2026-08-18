# `till-the-land-for-carrots` — Till First, Then Plant

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/87-V31wpaZc?feature=share)**

---

Row zero is carrots, and carrots are fussy — they only go in tilled soil. Every other row is bush, worked twice a lap for the wood and the hay that pay for those carrots. One extra check in the loop is what makes the whole field work.

## The code

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

Full file: [`carrots.py`](carrots.py)

## What's happening

- The drone sweeps a column at a time, then steps east.
- Every ripe tile: harvest, then water up to 75% (a `while` loop).
- Row zero (`get_pos_y() == 0`) is split off for carrots — check the ground, `till()` if it isn't soil, then plant.
- Every other row: harvest bush for wood, replant bush. The hay that grows in between funds the carrot seeds.
- One carrot costs one hay. Each pass brings two — one back in the ground, one to the store.

*Part of the **The Farmer Was Replaced** gameplay short series.*  
*[← back to gameplay](../README.md)*
