# I Taught an AI to Farm — Episode 6: Cactus
# Game: The Farmer Was Replaced (Steam)
# Watch: link coming soon
#
# End state: a multi-crop controller that manages grass/trees/carrots,
# pumpkins for power, and cactus farming in one loop.
#
# Concepts introduced:
#   num_items()       — check your inventory count mid-loop
#   conditional swap  — switch which crop runs based on what you need
#   orchestration     — one controller calling multiple specialised functions
#
# How it works:
#   1. Always run main() — harvests grass, trees, carrots
#   2. If Power > 5000, switch to pumpkins (Power crop) until buffer refills
#   3. If Cactus stock < 1000, run the cactus routine to top it up
#
# Each crop lives in its own module — this controller just decides WHEN to run each.

from Reset import reset
from Main import main
from pumpkins import pumpkins
from Cactus import cactus


def controller():
    while True:
        reset()
        main()
        if num_items(Items.Power) > 5000:
            reset()
            pumpkins()
        if num_items(Items.Cactus) < 1000:
            reset()
            cactus()


controller()
