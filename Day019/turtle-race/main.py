from turtle import Turtle, Screen
import random

scr = Screen()
scr.setup(width=500, height=400)
user_bet = scr.textinput(title="Make your bet", prompt="Which color turtle will win the race? red,orange,yellow,"
                                                       "green,blue,purple: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for color in colors:
    turtles.append(Turtle(shape="turtle"))
for turtle in turtles:
    turtle.speed(0)
    turtle.penup()
    turtle.color(colors[turtles.index(turtle)])
    turtle.goto(-230, -100 + 50 * turtles.index(turtle))
race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            break
        turtle.forward(random.randint(0, 10))

scr.exitonclick()
