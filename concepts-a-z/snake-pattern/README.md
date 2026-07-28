# Snake Pattern — The Farmer Was Replaced

**Series:** Tue Farmer Short  
**Concept:** Nested loops used to sweep a field in a snake/column-by-column pattern

## What This Is

A nested loop that walks every tile in a grid field — column by column — harvesting, planting, and moving on without manual steering.

The outer loop steps East (one column at a time). The inner loop walks North through that column tile by tile. When a harvestable tile is found, it harvests, plants a bush, and pops the purple hat on.

## The Code

```python
while True:
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
                plant(Entities.Bush)
                change_hat(Hats.Purple_Hat)
        move(North)
    move(East)
```

## Why Nested Loops

A single loop walks one column. Nest a loop inside a loop and you walk the whole field. One small block covers all of it — no manual steering needed.

## Stack

- Language: Python (The Farmer Was Replaced API)
- Game: [The Farmer Was Replaced](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) on Steam

## Maintainer

Cognito Coding — [cognitocoding.com](https://cognitocoding.com)
