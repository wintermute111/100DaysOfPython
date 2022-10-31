from turtle import Turtle, Screen
import random


def say_bye(x, y):
    scr.bye()


radius = int(input("Enter a radius integer: "))
rotation_increment = int(input("Enter a rotation increment from 1 to 360: "))

t = Turtle()
scr = Screen()

t.speed(0)
t.width(1)
t.shape("turtle")
scr.colormode(255)
scr.onclick(say_bye)

for angle in range(0,360, rotation_increment):
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.setheading(angle)
    t.circle(radius)

scr.exitonclick()
