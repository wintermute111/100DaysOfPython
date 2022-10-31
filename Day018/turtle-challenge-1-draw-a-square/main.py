from turtle import Turtle, Screen

t = Turtle()
scr = Screen()

t.shape("turtle")
# sides = int(input("How many sides? "))
# length = int(input("Length of sides? "))
# angle = 360 / sides

for _ in range(4):
    t.forward(100)
    t.right(90)

scr.exitonclick()
