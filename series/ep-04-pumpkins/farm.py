# I Taught an AI to Farm — Episode 4: Pumpkins
# Game: The Farmer Was Replaced (Steam)
# Watch: https://youtu.be/X92lWWj8HbY
#
# End state: drone reads each pumpkin tile, clears dead ones, harvests ripe merges
#
# Concepts introduced:
#   variables        — drone remembers values between passes
#   if / elif        — branch on what's actually on the tile
#   get_entity_type()— what crop is here? (None = empty)
#   get_growth()     — lifecycle state: 0 = dead, 1 = ripe (for pumpkins)
#
# Pumpkin mechanic:
#   - Adjacent ripe pumpkins merge into one giant pumpkin (then harvest for max yield)
#   - Dead pumpkins block the tile — must be cleared before ripes can cluster
#
# Cliffhanger: layout is random — ripe pumpkins keep landing next to dead ones,
# so half the merges fail. Next ep: sunflowers + the layout fix.

while True:
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            entity = get_entity_type()

            if entity == Entities.Pumpkin:
                growth = get_growth()
                if growth == 1:      # ripe — harvest the merge
                    harvest()
                elif growth == 0:    # dead — clear the tile so ripes can cluster
                    harvest()

            # Tile is now empty — plant a fresh pumpkin
            if get_entity_type() == None:
                plant(Entities.Pumpkin)

            move(North)
        move(East)
