from turtle import Turtle, Screen
from random import randint

t = Turtle()
scr = Screen()

t.speed(0)
t.shape("turtle")
num_sides = int(input("Number of sides? "))
length = int(input("Length of sides? "))
scr.colormode(255)
t.penup()
t.left(90)
t.forward(500)
t.right(90)
t.pendown()

for sides in range(3, num_sides + 1):
    angle = 360 / sides
    t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for side in range(sides):
        t.forward(length)
        t.right(angle)

scr.exitonclick()
