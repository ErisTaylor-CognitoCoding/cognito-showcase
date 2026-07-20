def goodForTree():
	return get_pos_x() % 2 == get_pos_y() % 2


def main():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
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
