# Concept: while True loop
# The Farmer Was Replaced — Sat Farmer Short (4 Jul 2026)
# Channel: https://www.youtube.com/@CognitoCoding01
# See in full context: series/ep-01-first-program/farm.py

# Step 1: Your very first command.
# The starting tile already has grass — no planting needed.
harvest()

# Step 2: After collecting 5 grass, loops unlock.
# Wrap harvest() in while True and it runs forever:
#   harvest → regrow → harvest → regrow → non-stop.
while True:
    harvest()
