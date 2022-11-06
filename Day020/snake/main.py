# Day 20 Snake Game (will continue on Day 21)
from turtle import Screen
from snake import Snake
import time

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("SNAKE!")
scr.tracer(0)

snake = Snake()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_on = True
while game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

scr.exitonclick()
