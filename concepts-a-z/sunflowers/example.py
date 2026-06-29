# Concept: running maximum with a variable
# The Farmer Was Replaced — Sat Farmer Short (8 Aug 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See in full context: series/ep-05-sunflowers/farm.py

# Only the sunflower with the MOST petals drops a Sun when harvested.
# Walk the whole field. Track the best petal count as you go.
# Update max_petals whenever you find a bigger one.

max_petals = 0   # start at zero — any sunflower will beat this

for x in range(get_world_size()):
    for y in range(get_world_size()):
        if get_entity_type() == Entities.Sunflower:
            if measure() > max_petals:
                max_petals = measure()   # new champion found — remember this count
        move(North)
    move(East)

# After the sweep, max_petals holds the highest petal count in the field.
# Use it in a second pass to harvest only the champion.
