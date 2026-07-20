def sunflowers():

    while get_pos_x() != 0:
        move(East)
    while get_pos_y() != 0:
        move(North)

    # Pass 1 - prep plant water and scan
    max_petals = 0

    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_entity_type() == Entities.Sunflower and can_harvest():
                change_hat(Hats.Traffic_Cone)
            if get_ground_type() != Grounds.Soil:
                harvest()
                till()
                plant(Entities.Sunflower)
                change_hat(Hats.Traffic_Cone)
            if get_entity_type() == None:
                plant(Entities.Sunflower)
            if get_entity_type() != None:
                while get_water() < 0.75 and num_items(Items.Water) > 0:
                    use_item(Items.Water)
            p = measure()
            if p != None and p > max_petals:
                max_petals = p
            move(North)
        move(East)

    # Pass 2 - harvest the most petals and replant
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if measure() == max_petals:
                harvest()
            plant(Entities.Sunflower)
            move(North)
        move(East)
