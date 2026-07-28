PLANT_LANES = 4   # nothing to gate while planting, so the base takes a lane too


def my_lane(lanes):
	lane = get_world_size() // lanes
	if get_pos_x() >= (lanes - 1) * lane:
		lane = get_world_size() - get_pos_x()   # last lane mops up the remainder
	return lane


def plant_tile():
	# your existing per-tile logic, lifted out verbatim
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() == None:
		plant(Entities.Cactus)
		change_hat(Hats.Brown_Hat)
	while get_entity_type() != None and get_water() < 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)


def cactus_planter():
	# Owns a block of columns, starting from wherever it was spawned.
	lane = my_lane(PLANT_LANES)
	while get_pos_y() != 0:
		move(North)
	# ONE pass, then return - returning kills the drone and frees the slot
	for c in range(lane):
		for j in range(get_world_size()):
			plant_tile()
			move(North)
		move(East)


def cactus():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(North)

	lane = get_world_size() // PLANT_LANES

	# 1) plant the field in lanes
	for k in range(PLANT_LANES - 1):
		spawn_drone(cactus_planter)
		for c in range(lane):
			move(East)
	cactus_planter()            # base works the last lane itself

	# 2) wait until we are the only drone left alive
	while num_drones() > 1:
		pass

	# 3) alone now - the sort is one drone's job forever
	keep_sorting = True
	while keep_sorting:
		keep_sorting = False
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_pos_y() < get_world_size() - 1 and measure() > measure(North):
					swap(North)
					keep_sorting = True
				if get_pos_x() < get_world_size() - 1 and measure() > measure(East):
					swap(East)
					keep_sorting = True
				move(North)
			move(East)

	harvest()


cactus()
