def goodForTree():
	return get_pos_x() % 2 == get_pos_y() % 2


def farm_tile(row):
	if can_harvest():
		harvest()
	if goodForTree():
		change_hat(Hats.Tree_Hat)
		plant(Entities.Tree)
	else:
		if row < 4:
			plant(Entities.Grass)
			change_hat(Hats.Straw_Hat)
		else:
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Carrot)
			change_hat(Hats.Carrot_Hat)
	if get_entity_type() != None and num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
	while get_entity_type() != None and get_water() < 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)


def field_worker():
	# Drone 1: the whole field EXCEPT row y == 0
	while get_pos_y() != 0:
		move(North)
	while True:
		for x in range(get_world_size()):
			for j in range(get_world_size()):
				if j != 0:
					farm_tile(j)
				move(North)
			move(East)


def sunflower_worker():
	# Drone 2: owns row y == 0
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(North)
	while True:
		# 1) plant + water a sunflower on every tile in the row
		for k in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				harvest()
				till()
			if get_entity_type() == None:
				plant(Entities.Sunflower)
				change_hat(Hats.Traffic_Cone)
			while get_water() < 0.75 and num_items(Items.Water) > 0:
				use_item(Items.Water)
			move(East)
		# 2) find the highest petal count in the row
		max_petals = 0
		for k in range(get_world_size()):
			p = measure()
			if p != None and p > max_petals:
				max_petals = p
			move(East)
		# 3) harvest + replant only the fullest sunflower(s)
		for k in range(get_world_size()):
			if measure() == max_petals:
				harvest()
				plant(Entities.Sunflower)
			move(East)


def main():
	if num_drones() < max_drones():
		spawn_drone(sunflower_worker)
	field_worker()


main()
