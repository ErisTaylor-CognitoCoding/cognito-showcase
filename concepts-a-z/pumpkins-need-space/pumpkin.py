def pumpkins():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(North)

	while True:
		ripe_count = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_entity_type() == Entities.Pumpkin and can_harvest():
					ripe_count = ripe_count + 1
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
				move(North)
			move(East)

		if ripe_count == get_world_size() * get_world_size():
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if can_harvest():
						harvest()
					plant(Entities.Pumpkin)
					move(North)
				move(East)
			return


pumpkins()
