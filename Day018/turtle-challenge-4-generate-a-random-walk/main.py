from turtle import Turtle, Screen
import random


def say_bye(x, y):
    scr.bye()


angle_type = input("Angles right or random? ")

t = Turtle()
scr = Screen()

t.speed(0)
t.width(5)
t.shape("turtle")
scr.colormode(255)
scr.onclick(say_bye)

while True:
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if angle_type == "right":
        angle = random.choice([0, 90, 180, 270])
    else:
        angle = random.randint(0, 359)

    t.setheading(angle)
    t.forward(25)
