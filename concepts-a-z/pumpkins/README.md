# pumpkins — Check Before You Plant

> 📺 **1 Aug 2026** · [Cognito Coding](https://www.youtube.com/@CognitoCoding01)

**Game:** The Farmer Was Replaced  
**Concepts:** `get_entity_type()`, entity checks, conditional planting

---

## The Farmer Analogy

Pumpkins need room. You can't plant one on a tile that already has something on it. A good farmer checks the tile first — if it's empty, plant. If something's already there, leave it.

---

## What `get_entity_type()` Returns

The entity currently on the tile. `None` means the tile is empty.

```python
if get_entity_type() == None:
    plant(Entities.Pumpkin)
```

No wasted seeds. No planting on occupied tiles.

---

## Why Pumpkins Are Different From Grass

Grass self-seeds — it regrows on its own tile with no planting needed. Pumpkins don't. You have to plant them, and they go through states:

- **Growing** — leave it
- **Ripe** — adjacent ripe pumpkins merge into one giant pumpkin, then harvest
- **Dead** — blocking the tile, must be cleared before anything new can grow

Checking before planting is how you avoid dropping seeds on dead or growing tiles.

---

## The Full Pattern

```python
for x in range(get_world_size()):
    for y in range(get_world_size()):
        # Only plant if the tile is completely empty
        if get_entity_type() == None:
            plant(Entities.Pumpkin)
        move(North)
    move(East)
```

---

## See It in the Full Episode

[Episode 4](../../series/ep-04-pumpkins) — the full pumpkin mechanic: clearing dead crops, reading ripe state, harvesting the merge.

---

*[← snake-pattern](../snake-pattern) · [Back to concepts](../README.md) · Next: [sunflowers →](../sunflowers)*
