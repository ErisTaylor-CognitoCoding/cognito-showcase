def opposite(d):
	if d == North:
		return South
	if d == South:
		return North
	if d == East:
		return West
	return East

def cell():
	return get_pos_x() * get_world_size() + get_pos_y()

def explore(came_from, seen):
	if get_entity_type() == Entities.Treasure:
		return True
	seen.append(cell())
	for d in [North, East, South, West]:
		if d != came_from:
			if move(d):
				if cell() not in seen:
					if explore(opposite(d), seen):
						return True
				move(opposite(d))
	return False

def mazes():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	while True:
		if explore(None,[]):
			use_item(Items.Weird_Substance, substance)
			change_hat(Hats.Straw_Hat)
mazes()
