# Concept: reading entity state before planting
# The Farmer Was Replaced — Sat Farmer Short (1 Aug 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See in full context: series/ep-04-pumpkins/farm.py

# Pumpkins need space — only plant on empty tiles.
# get_entity_type() returns what's on the current tile.
# None means the tile is empty and ready for a new seed.
for x in range(get_world_size()):
    for y in range(get_world_size()):
        if get_entity_type() == None:
            plant(Entities.Pumpkin)
        move(North)
    move(East)
