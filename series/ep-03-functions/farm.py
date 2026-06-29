# I Taught an AI to Farm — Episode 3: Functions
# Game: The Farmer Was Replaced (Steam)
# Watch: link coming soon (filmed 10 Jun 2026)
#
# End state: copy-pasted mess → one clean function call
#
# Concepts introduced:
#   def              — define a reusable function
#   parameters       — pass size in so the function works at any scale
#   DRY              — Don't Repeat Yourself
#
# The unlock: "I replaced ten lines with one."
#
# Cliffhanger: the function runs the same thing every pass — it has no memory.
# To track what's been planted or grow the farm, we need variables. Next ep.


def harvest_field(size):
    """Walk and harvest the full size×size grid in a snake pattern."""
    for x in range(size):
        for y in range(size):
            if can_harvest():
                harvest()

            # Multi-crop routing (carried forward from Ep 2)
            if get_pos_y() == 0:
                plant(Entities.Bush)
            elif get_pos_y() == 2:
                if get_entity_type() == None:
                    till()
                    plant(Entities.Carrot)

            move(North)
        move(East)


# One line runs the whole farm.
while True:
    harvest_field(get_world_size())
