from turtle import Turtle, Screen

t = Turtle()
scr = Screen()

t.shape("turtle")

for _ in range(30):
    t.forward(10)
    if t.isdown():
        t.penup()
    else:
        t.pendown()

scr.exitonclick()
