def cactus():
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() == None:
                plant(Entities.Cactus)
                change_hat(Hats.Brown_Hat)
            while get_entity_type() != None and get_water() < 0.75 and num_items(Items.Water) > 0:
                use_item(Items.Water)
            move(North)
        move(East)

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
