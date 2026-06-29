# Concept: if statement / conditional guard
# The Farmer Was Replaced — Sat Farmer Short (11 Jul 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See in full context: series/ep-01-first-program/farm.py

# Before: harvest without checking — breaks with faster speeds
while True:
    harvest()

# After: add can_harvest() as a guard before every swing.
# The drone only harvests when the tile is actually ready.
# Skips the swing if the crop isn't ready yet — no wasted moves.
while True:
    if can_harvest():
        harvest()
