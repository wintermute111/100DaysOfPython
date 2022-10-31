from turtle import Turtle, Screen
import random
import colorgram


def say_bye(x, y):
    scr.bye()


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    if color.rgb.r < 220 and color.rgb.g < 220 and color.rgb.b < 220:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

radius = int(input("Enter a dot radius integer: "))
spacing = int(input("Enter the space between dots integer: "))
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

t = Turtle()
scr = Screen()

t.speed(0)
t.shape("turtle")
scr.colormode(255)
scr.onclick(say_bye)
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(250)
t.setheading(0)

for row in range(rows):
    for column in range(columns):
        t.dot(radius, random.choice(rgb_colors))
        t.forward(spacing)
    t.setheading(180)
    t.forward(columns * spacing)
    t.setheading(90)
    t.forward(spacing)
    t.setheading(0)

scr.exitonclick()
