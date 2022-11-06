from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor("black")
scr.title("PONG")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(r_paddle.go_up, "Up")
scr.onkey(r_paddle.go_down, "Down")
scr.onkey(l_paddle.go_up, "w")
scr.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    scr.update()
    ball.move()
    # Detect collision with wall top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # Detect r_paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.refresh()
    # Detect l_paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.refresh()

scr.exitonclick()
