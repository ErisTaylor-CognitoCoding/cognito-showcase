def goodForTree():
	return get_pos_x() % 2 == get_pos_y() % 2


def main():
	first = True
	while True:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest() and j != 0:
					harvest()
				if j == 0:
					if get_ground_type() != Grounds.Soil:
						till()
					if get_entity_type() == None:
						plant(Entities.Sunflower)
						change_hat(Hats.Traffic_Cone)
				else:
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

			# back at y==0 on column i — but only once the field's fully planted
			if not first:
				best = 0
				for k in range(get_world_size()):
					p = measure()
					if p != None and p > best:
						best = p
					move(East)
				done = False
				for k in range(get_world_size()):
					if not done and can_harvest() and measure() == best:
						harvest()
						plant(Entities.Sunflower)
						done = True
					move(East)
