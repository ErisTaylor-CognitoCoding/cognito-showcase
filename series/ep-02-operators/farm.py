# I Taught an AI to Farm — Episode 2: Operators → Full 3×3
# Game: The Farmer Was Replaced (Steam)
# Watch: https://youtu.be/qB2nKoU1dkI
#
# End state: full 3×3 farm running three crops in rotation
#   Row 0: bushes (wood)
#   Row 1: hay (grass, self-seeds)
#   Row 2: carrots (tilled soil)
#
# Concepts introduced:
#   get_pos_x() / get_pos_y()   — drone knows where it is on the grid
#   == / < / >                  — comparison operators: the decision-making unlock
#   till()                      — prepare soil before planting carrots
#   plant(Entities.X)           — drop a seed on the current tile

while True:
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            if can_harvest():
                harvest()

            if get_pos_y() == 0:
                plant(Entities.Bush)
            elif get_pos_y() == 2:
                if get_entity_type() == None:
                    till()
                    plant(Entities.Carrot)

            move(North)
        move(East)
