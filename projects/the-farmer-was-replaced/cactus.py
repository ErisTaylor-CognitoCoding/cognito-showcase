def reverse(dir):
    if dir == East: return West
    if dir == West: return East
    if dir == North: return South
    if dir == South: return North


def back():
    while get_pos_x() != 0 or get_pos_y() != 0:
        if get_pos_x() > 0:
            move(West)
        if get_pos_y() > 0:
            move(South)


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


def sort_cactus():
    size = get_world_size()
    dir = East
    sorted = False
    vsorted = False
    while not sorted or not vsorted:
        sorted = True
        vsorted = True
        for i in range(size):
            for j in range(size):
                current = measure()
                neighbor = measure(dir)
                down = measure(South)
                up = measure(North)
                if get_pos_x() != size - 1 and dir == East and neighbor != None and current > neighbor:
                    swap(East)
                    sorted = False
                if get_pos_x() != 0 and dir == West and neighbor != None and current < neighbor:
                    swap(West)
                    sorted = False
                if get_pos_y() != 0 and down != None and current < down:
                    swap(South)
                    vsorted = False
                if get_pos_y() != size - 1 and up != None and current > up:
                    swap(North)
                    vsorted = False
                if j != size - 1:
                    move(dir)
            if i != size - 1:
                move(North)
            dir = reverse(dir)


cactus()
sort_cactus()
back()
harvest()
