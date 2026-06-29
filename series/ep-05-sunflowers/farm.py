# I Taught an AI to Farm — Episode 5: Sunflowers
# Game: The Farmer Was Replaced (Steam)
# Watch: link coming soon (published 24 Jun 2026)
#
# End state: drone finds and harvests ONLY the sunflower with the most petals
#
# Concepts introduced:
#   measure()        — returns a number (petal count) you can compare
#   running max      — track the best value as you sweep the grid
#   max_petals       — variable that holds the current champion petal count
#   double sweep     — pass 1 to find the max, pass 2 to harvest the champion
#
# Sunflower mechanic:
#   Only the sunflower with the MOST petals on the grid drops a Sun when harvested.
#   Harvest any other and you wasted the cut.
#
# Cliffhanger: we tracked the best PETAL COUNT but not WHERE the champion was,
# so the drone re-walks the whole 12×12 to find it.
# Next episode: lists — remember both the value AND the position.

# --- Pass 1: find the maximum petal count across the 12×12 grid ---
max_petals = 0

for x in range(get_world_size()):
    for y in range(get_world_size()):
        if get_entity_type() == Entities.Sunflower:
            petals = measure()
            if petals > max_petals:
                max_petals = petals      # new champion — update the best
        move(North)
    move(East)

# --- Pass 2: harvest only the champion ---
for x in range(get_world_size()):
    for y in range(get_world_size()):
        if get_entity_type() == Entities.Sunflower:
            if measure() == max_petals:
                harvest()                # this is the one — collect the Sun
        move(North)
    move(East)
