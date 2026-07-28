LANES = 3 # field drones (the fourth does the sunflowers)

def goodForTree():
	return get_pos_x() % 2 == get_pos_y() % 2


def farm_tile(row):
	if can_harvest():
		harvest()
	if goodForTree():
		change_hat(Hats.Tree_Hat)
		plant(Entities.Tree)
	else:
		if row < 11:
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
	# Drones Own a block of columns excluding row 1, starting where they spawn_drone
	lane = get_world_size() // LANES
	if get_pos_x() >= (LANES - 1) * lane:
		lane = get_world_size() - get_pos_x() # Last lane mops up remainder
	while get_pos_y() != 0:
		move(North)
	while True:
		for c in range(lane):
			for j in range(get_world_size()):
				if j != 0:
					farm_tile(j)
				move(North)
			move(East)
		# wrap the long way round back to the start
		for c in range(get_world_size() - lane):
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
	lane = get_world_size() // LANES
	spawn_drone(sunflower_worker) #drone 2
	spawn_drone(field_worker) #drone 3
	for c in range(lane):
		move(East)
	spawn_drone(field_worker) #drone 4
	for c in range(lane):
		move(East)
	field_worker() #drone 1

main()
