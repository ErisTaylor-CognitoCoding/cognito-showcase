# Concept: if/elif — handle multiple resource types in one pass
# The Farmer Was Replaced — Sat Farmer Short (22 Aug 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See in full context: series/ep-02-operators/farm.py

# A mixed field: trees drop Wood, bushes drop Fruit.
# Same harvest() call works on both — branch on what entity is on the tile.
# One loop, one pass, both crop types handled correctly.
for x in range(get_world_size()):
    for y in range(get_world_size()):
        entity = get_entity_type()

        if entity == Entities.Tree:
            if can_harvest():
                harvest()   # gets Wood

        elif entity == Entities.Bush:
            if can_harvest():
                harvest()   # gets Fruit

        move(North)
    move(East)
