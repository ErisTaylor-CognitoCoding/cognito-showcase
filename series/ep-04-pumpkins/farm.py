# I Taught an AI to Farm — Episode 4: Pumpkins
# Game: The Farmer Was Replaced (Steam)
# Watch: https://youtu.be/X92lWWj8HbY
#
# Final version from code-pair session.
#
# Concepts:
#   - Corner reset              — always start from (0, 0)
#   - ripe_count variable       — count harvestable tiles in pass 1
#   - Dead_Pumpkin handling     — replant dead tiles immediately
#   - Till before plant         — restore soil if ground type is wrong
#   - Water management          — top up to 0.75 while water items available
#   - Full-field harvest pass   — only triggered when every tile is ripe
#   - Hats                      — Pumpkin_Hat equipped on pumpkin tiles

def pumpkins():
	while get_pos_x() != 0:
		move(East)
	while get_pos_y() != 0:
		move(North)

	ripe_count = 0

	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() == Entities.Pumpkin and can_harvest():
				ripe_count = ripe_count + 1
			if get_entity_type() == Entities.Dead_Pumpkin:
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
