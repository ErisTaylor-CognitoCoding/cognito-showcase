# I Taught an AI to Farm — Episode 1: First Program → 1×3 Strip
# Game: The Farmer Was Replaced (Steam)
# Watch: https://youtu.be/maTaBrkHh1o
#
# End state: drone harvests a 1×3 strip of hay on autopilot.
#
# Concepts introduced:
#   harvest()       — grab the current tile
#   while True      — loop forever
#   if can_harvest  — guard before swinging
#   move(North)     — step forward one tile
#
# Cliffhanger: the drone sweeps one row but has no idea where it is on a
# larger grid. Expanding to 3×3 broke — it walked off the edge.
# Next episode: operators + position sensing.

while True:
    if can_harvest():
        harvest()
    move(North)
