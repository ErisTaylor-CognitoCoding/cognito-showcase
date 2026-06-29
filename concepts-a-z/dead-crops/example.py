# Concept: handling failure states — clear dead crops, replant on empty tiles
# The Farmer Was Replaced — Sat Farmer Short (15 Aug 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See in full context: series/ep-04-pumpkins/farm.py

# Dead crops block the tile. Clear them before replanting.
# Pattern: dead? → remove. Empty? → plant fresh.
# Two separate if checks — the second re-checks after the first may have cleared the tile.
for x in range(get_world_size()):
    for y in range(get_world_size()):
        entity = get_entity_type()

        # Step 1: clear dead pumpkins — they're blocking the tile
        if entity == Entities.Pumpkin and get_growth() == 0:
            harvest()   # removes the dead crop, tile becomes None

        # Step 2: tile is now clear — plant a fresh pumpkin
        if get_entity_type() == None:
            plant(Entities.Pumpkin)

        move(North)
    move(East)
