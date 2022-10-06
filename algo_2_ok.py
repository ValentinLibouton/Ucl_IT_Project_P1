def get_direction_on_x(coor_on_x) :
    if coor_on_x > 0 :
        return EAST
    else :
        return WEST

def get_direction_on_y(coor_on_y) :
    if coor_on_y > 0 :
        return SOUTH
    else :
        return NORTH

def may_I_move() :
    return can_move() and not is_in_front_of_enemy()

def dodge() :
    if not is_on_target():#ajout de cette ligne de test
        while not may_I_move():
            turn_left()
        move()

while not is_on_target() :
    coor_on_x = get_target_x() - get_x()
    while coor_on_x != 0 and not is_on_target(): #ajout
        while get_direction() != get_direction_on_x(coor_on_x) :
            turn_left()

        steps = 0
        totalSteps = abs(coor_on_x)

        while may_I_move() and steps < totalSteps :
            move()
            steps = steps + 1
            
    #if steps == totalSteps :
        coor_on_x = get_target_x() - get_x()#ajout
        dodge() #ajout
        
        
    coor_on_y = get_target_y() - get_y()
    while coor_on_y != 0 and not is_on_target():#ajout
        
        while get_direction() != get_direction_on_y(coor_on_y) :
            turn_left()

        steps = 0
        totalSteps = abs(coor_on_y)
        while may_I_move() and steps < totalSteps :
            move()
            steps = steps + 1
        #if steps != totalSteps :
        #    dodge()
    #else :
    #    dodge()
        coor_on_y = get_target_y() - get_y()#ajout
        dodge()#ajout

        
destroy_dark_force()
