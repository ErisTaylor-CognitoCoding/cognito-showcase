# Concept: arithmetic — converting harvest count into gold
# The Farmer Was Replaced — Sat Farmer Short (5 Sep 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See what comes next: concepts-a-z/upgrade/example.py

# After harvest, calculate how much gold your hay is worth.
# num_items() returns the current inventory count for an item type.

hay = num_items(Items.Hay)   # how many hay bales in the drone's inventory?
gold_per_hay = 10            # market rate: 10 gold per bale

gold_earned = hay * gold_per_hay   # total gold if you trade all hay now
