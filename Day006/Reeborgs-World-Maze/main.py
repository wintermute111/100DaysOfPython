def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()

turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif not wall_on_right():
        turn_right()
        move()
    else:
        turn_left()
