# `pumpkins-need-space` in 60 seconds

> 📺 **[Watch on YouTube →](https://youtube.com/shorts/jJSJQHcTkJ8?feature=share)**

---

Pumpkins aren't carrots. A carrot is one tile — a pumpkin wants to merge with the ones next to it. But they only merge when the **whole field is ripe at the same time**. Harvest one early and you break the merge.

The code loops over the full grid on every pass, counting ripe pumpkins and patching dead ones as it goes. The harvest only fires when `ripe_count` equals the total number of tiles — every square ripe at once. Then one clean pass clears the lot and the giant merged pumpkin appears.

```python
if ripe_count == get_world_size() * get_world_size():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
            plant(Entities.Pumpkin)
            move(North)
        move(East)
```

See [`pumpkin.py`](./pumpkin.py) for the full working script.

---

*[← back to concepts](../README.md)*
