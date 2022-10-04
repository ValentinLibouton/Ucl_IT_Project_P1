while get_x() != get_target_x() or get_y() != get_target_y():
    while not (can_move() or is_in_front_of_enemy()) and not is_on_target():
        turn_left()
        if can_move():
            move()
            turn_right()

    if not is_on_target():
        move()

    objective = get_direction()
    if get_x() < get_target_x():
        objective = EAST
    else:
        objective = WEST
    if get_y() < get_target_y():
        objective = SOUTH
    else:
        objective = NORTH

    while get_direction() != objective:
        turn_left()
destroy_dark_force()
