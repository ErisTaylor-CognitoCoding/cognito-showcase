while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
				change_hat(Hats.Straw_Hat)
				while get_water() < 0.75:
					use_item(Items.Water)
				if get_pos_y() == 0:
					if get_ground_type() != Grounds.Soil:
						till()
					change_hat(Hats.Carrot_Hat)
					plant(Entities.Carrot)
				else:
					plant(Entities.Bush)
				change_hat(Hats.Purple_Hat)
		move(North)
	move(East)
