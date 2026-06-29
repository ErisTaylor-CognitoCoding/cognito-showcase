# Concept: conditional buying — check balance before spending, break when done
# The Farmer Was Replaced — Sat Farmer Short (12 Sep 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See what comes next: concepts-a-z/full-farm/example.py

# Goal: farm until you can afford the speed upgrade, then buy it and stop.
# Pattern: keep doing something → check threshold → act and break when reached.

UPGRADE_COST = 100

while True:
    if can_harvest():
        harvest()   # keep farming

    if num_items(Items.Hay) >= UPGRADE_COST:
        use_item(Items.Hay, UPGRADE_COST)   # spend the hay
        break                               # upgrade purchased — exit the loop
