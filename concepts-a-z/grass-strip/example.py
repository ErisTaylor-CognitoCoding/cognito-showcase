# Concept: for loop — walk and harvest a full row
# The Farmer Was Replaced — Sat Farmer Short (18 Jul 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See in full context: series/ep-02-operators/farm.py

# Walk the drone along a full row, harvesting each tile.
# range(get_world_size()) = exactly as many steps as the farm is wide.
# The loop stops automatically when the row is done.
for i in range(get_world_size()):
    if can_harvest():
        harvest()
    move(North)
