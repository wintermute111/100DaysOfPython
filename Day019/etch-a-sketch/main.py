from turtle import Turtle, Screen

t = Turtle()
scr = Screen()
scr.setup(width=500, height=400)

def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_right():
    t.right(10)


def turn_left():
    t.left(10)


def clear_screen():
    # scr.resetscreen() resets all turtles if there are multiple,
    # the below 4 lines will only reset the specified turtle
    t.clear()
    t.penup()
    t.home()
    t.pendown()


t.speed(0)
scr.listen()
scr.onkey(key="Up", fun=move_forwards)
scr.onkey(key="Down", fun=move_backwards)
scr.onkey(key="Left", fun=turn_left)
scr.onkey(key="Right", fun=turn_right)
scr.onkey(key="c", fun=clear_screen)
scr.exitonclick()
