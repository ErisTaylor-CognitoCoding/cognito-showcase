LANES = 3   # tender drones; the base drone holds the harvest gate


def tend_tile():
	# your existing per-tile logic, lifted out verbatim
	if get_entity_type() == Entities.Dead_Pumpkin:
		harvest()
		plant(Entities.Pumpkin)
		change_hat(Hats.Pumpkin_Hat)
	if get_ground_type() != Grounds.Soil:
		harvest()
		till()
		plant(Entities.Pumpkin)
		change_hat(Hats.Pumpkin_Hat)
	if get_entity_type() != None:
		while get_water() < 0.75 and num_items(Items.Water) > 0:
			use_item(Items.Water)


def pumpkin_tender():
	# Owns a block of columns, starting from wherever it was spawned.
	lane = get_world_size() // LANES
	if get_pos_x() >= (LANES - 1) * lane:
		lane = get_world_size() - get_pos_x()   # last lane mops up the remainder
	while get_pos_y() != 0:
		move(North)
	# ONE pass, then return - returning kills the drone and frees the slot
	for c in range(lane):
		for j in range(get_world_size()):
			tend_tile()
			move(North)
		move(East)


def pumpkins():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(North)

	lane = get_world_size() // LANES

	while True:
		# 1) send the tenders out, one per lane
		for k in range(LANES):
			spawn_drone(pumpkin_tender)
			if k < LANES - 1:
				for c in range(lane):
					move(East)
		# wrap the rest of the way East, back to x = 0
		for c in range(get_world_size() - (LANES - 1) * lane):
			move(East)

		# 2) wait until we are the only drone left alive
		while num_drones() > 1:
			pass

		# 3) alone now, so nothing can change under us - honest scan
		all_ripe = True
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if not can_harvest():
					all_ripe = False
				move(North)
			move(East)

		# 4) whole field ripe at the same instant - take the lot
		if all_ripe:
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					harvest()
					plant(Entities.Pumpkin)
					change_hat(Hats.Pumpkin_Hat)
					move(North)
				move(East)


pumpkins()
