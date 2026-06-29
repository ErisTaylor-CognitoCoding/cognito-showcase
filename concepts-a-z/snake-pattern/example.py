# Concept: nested for loops — cover every tile of the grid
# The Farmer Was Replaced — Sat Farmer Short (25 Jul 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See in full context: series/ep-02-operators/farm.py

# Outer loop: one step per column (move East after each full column)
# Inner loop: one step per row within that column (move North across each tile)
# Together: every tile in the grid visited exactly once.
for x in range(get_world_size()):
    for y in range(get_world_size()):
        if can_harvest():
            harvest()
        move(North)
    move(East)
