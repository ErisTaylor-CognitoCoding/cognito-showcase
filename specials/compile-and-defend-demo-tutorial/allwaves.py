#wave 1 
for e in me.enemies_in_range:
    me.shoot(e)


#wave 2
if len(me.enemies_in_range) > 0:
    target = me.enemies_in_range[0]
    me.shoot(target)


#wave 3
if len(me.enemies_in_range) > 0:
    target = me.enemies_in_range[0]
    for e in me.enemies_in_range:
        if e.distance_to_exit < target.distance_to_exit:
            target = e
    me.shoot(target)

#wave 4
target = 0
found = False

for e in me.enemies_in_range:
    if e.is_flying == me.is_tesla:
        if found == False:
            target = e
            found = True
        elif e.distance_to_exit < target.distance_to_exit:
            target = e

if found == True:
    me.shoot(target)

#wave 5
target = 0
found = False

for e in me.enemies_in_range:
    if e.is_armored == me.is_sniper:
        if found == False:
            target = e
            found = True
        elif e.distance_to_exit < target.distance_to_exit:
            target = e

if found == True:
    me.shoot(target)

#wave 6
if len(me.enemies_in_range) > 0:
    target = me.enemies_in_range[0]
    for e in me.enemies_in_range:
        if e.distance_to_exit < target.distance_to_exit:
            target = e
    me.shoot(target)

#wave 7
target = 0

for e in me.enemies_in_range:
    if e.is_flying == False or me.can_hit_air == True:
        if target == 0:
            target = e
        elif e.is_flying != target.is_flying:
            if e.is_flying == True:
                target = e
        elif e.is_armored != target.is_armored:
            if e.is_armored == True:
                target = e
        elif e.distance_to_exit < target.distance_to_exit:
            target = e

if target != 0:
    me.shoot(target)
