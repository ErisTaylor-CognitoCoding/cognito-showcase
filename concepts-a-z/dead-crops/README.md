# dead-crops — Clear Before Replanting

> 📺 **15 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** `get_growth()`, failure states, clear-then-plant pattern

---

## The Farmer Analogy

Not every crop makes it. A dead plant is still *taking up the tile* — nothing new can grow there until you remove it. Check each tile: if it's dead, pick it up. If the tile's now empty, plant something fresh.

---

## What `get_growth()` Returns

A number representing where the crop is in its lifecycle:
- `0` = dead — worthless, blocking the tile
- `1` = ripe — ready to harvest

```python
if get_entity_type() == Entities.Pumpkin:
    if get_growth() == 0:   # dead
        harvest()           # removes it and clears the tile
```

After `harvest()` on a dead crop, the tile becomes `None` — ready to plant again.

---

## The Full Pattern: Check → Clear → Replant

```python
for x in range(get_world_size()):
    for y in range(get_world_size()):
        entity = get_entity_type()

        # Step 1: if there's a dead pumpkin, clear it
        if entity == Entities.Pumpkin and get_growth() == 0:
            harvest()

        # Step 2: tile is now empty — plant a fresh pumpkin
        if get_entity_type() == None:
            plant(Entities.Pumpkin)

        move(North)
    move(East)
```

Note the two separate `if` checks — the second re-checks `get_entity_type()` because the first `harvest()` may have just cleared the tile.

---

## See It in the Full Episode

[Episode 4](../../series/ep-04-pumpkins) — dead crop clearing is the key to getting ripe pumpkins to cluster and merge.

---

*[← sunflowers](../sunflowers) · [Back to concepts](../README.md) · Next: [trees →](../trees)*
