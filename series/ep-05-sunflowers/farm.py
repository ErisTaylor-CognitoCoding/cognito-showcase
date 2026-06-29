# I Taught an AI to Farm — Episode 5: Sunflowers
# Game: The Farmer Was Replaced (Steam)
#
# Mid-point snapshot: sunflowers() integrated into main loop.
# The drone now handles sunflowers on row 0, then runs the
# standard tree / grass / carrot logic across the rest of the grid.
#
# Concepts in play:
#   sunflowers()     — dedicated function called first, resets x to 0
#   measure()        — returns petal count for comparison
#   running max      — max_petals tracks the best petal count
#   double sweep     — pass 1: prep + scan; pass 2: harvest champion + replant
#   goodForTree()    — helper using modulo to checker-board trees
#   change_hat()     — visual feedback per crop type
#   get_ground_type() / till() — soil prep before planting carrots


def goodForTree():
	return get_pos_x() % 2 == get_pos_y() % 2


def main():
	sunflowers()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if j != 0:
				if can_harvest():
					harvest()
				if goodForTree():
					change_hat(Hats.Tree_Hat)
					plant(Entities.Tree)
				else:
					if j < 4:
						plant(Entities.Grass)
						change_hat(Hats.Straw_Hat)
					else:
						if get_ground_type() != Grounds.Soil:
							till()
						plant(Entities.Carrot)
						change_hat(Hats.Carrot_Hat)
				while get_entity_type() != None and get_water() < 0.75 and num_items(Items.Water) > 0:
					use_item(Items.Water)
			move(North)
		move(East)


def sunflowers():
	while get_pos_x() != 0:
		move(East)

	# Pass 1 - prep, plant, water and scan for max petals
	max_petals = 0

	for i in range(get_world_size()):
		if get_entity_type() == Entities.Sunflower and can_harvest():
			change_hat(Hats.Traffic_Cone)
		if get_ground_type() != Grounds.Soil:
			harvest()
			till()
			plant(Entities.Sunflower)
			change_hat(Hats.Traffic_Cone)
		if get_entity_type() == None:
			plant(Entities.Sunflower)
		if get_entity_type() != None:
			while get_water() < 0.75 and num_items(Items.Water) > 0:
				use_item(Items.Water)
		p = measure()
		if p != None and p > max_petals:
			max_petals = p
		move(East)

	# Pass 2 - harvest the champion and replant
	for i in range(get_world_size()):
		if measure() == max_petals:
			harvest()
		plant(Entities.Sunflower)
		move(East)
