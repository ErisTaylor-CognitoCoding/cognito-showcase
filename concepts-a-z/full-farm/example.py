# Concept: combining everything into one automated farm
# The Farmer Was Replaced — Sat Farmer Short (19 Sep 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# Full context: series/ — episodes 1 through 5

# Fully automated farm: sunflowers, pumpkins, hay, carrots — all in one run.
# Every concept from the I Taught an AI to Farm series, running together.

max_petals = 0

while True:
    # --- Pass 1: scan the whole grid for the champion sunflower ---
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            if get_entity_type() == Entities.Sunflower:
                if measure() > max_petals:
                    max_petals = measure()   # running max — new champion found
            move(North)
        move(East)

    # --- Pass 2: act on every tile ---
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            entity = get_entity_type()

            if entity == Entities.Sunflower:
                if measure() == max_petals:
                    harvest()        # champion — collect the Sun
                    max_petals = 0   # reset for next cycle

            elif entity == Entities.Pumpkin:
                growth = get_growth()
                if growth == 0:      # dead — clear the tile
                    harvest()
                elif growth == 1:    # ripe — harvest the merge
                    harvest()

            elif can_harvest():
                harvest()            # hay, carrots, everything else

            move(North)
        move(East)
