# Snake Pattern Field Sweep — The Farmer Was Replaced
# Nested loops: outer loop steps East (column), inner loop walks North (row)
# Every tile in the field gets visited without manual steering

while True:
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if can_harvest():
                harvest()
                plant(Entities.Bush)
                change_hat(Hats.Purple_Hat)
        move(North)
    move(East)
