def goodForTree():
    return get_pos_x() % 2 == get_pos_y() % 2


def main():
    sunflowers()
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if j != 0:
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

        # Back at j==0 — scan the whole row, harvest only the biggest, then move on
        max_petals = 0
        for k in range(get_world_size()):
            p = measure()
            if p != None and p > max_petals:
                max_petals = p
            move(East)
        for k in range(get_world_size()):
            if can_harvest() and measure() == max_petals:
                harvest()
                plant(Entities.Sunflower)
            move(East)

        move(East)


def sunflowers():
    while get_pos_x() != 0:
        move(East)
    for i in range(get_world_size()):
        if get_ground_type() != Grounds.Soil:
            till()
        if get_entity_type() == None:
            plant(Entities.Sunflower)
            change_hat(Hats.Traffic_Cone)
        while get_entity_type() != None and get_water() < 0.75 and num_items(Items.Water) > 0:
            use_item(Items.Water)
        move(East)
