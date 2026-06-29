# Concept: patience — only harvest when growth is complete
# The Farmer Was Replaced — Sat Farmer Short (29 Aug 2026)
# Channel: https://www.youtube.com/@CognitoCoding01

# Cacti grow slowly. Harvest too early → nothing.
# Check get_growth() == 1 (fully grown) before every cut.
# Unripe cacti are skipped and checked again next pass.
while True:
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            if get_entity_type() == Entities.Cactus:
                if get_growth() == 1:   # fully grown — safe and worthwhile
                    harvest()
                # else: not ready — skip, come back next pass
            move(North)
        move(East)
