import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("SNAKE!")
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(snake.go_up, "Up")
scr.onkey(snake.go_down, "Down")
scr.onkey(snake.go_left, "Left")
scr.onkey(snake.go_right, "Right")

game_on = True
while game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) <= 17:
        food.refresh()
        scoreboard.score += 1
        scoreboard.refresh()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.game_over()
        snake.reset_snake()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            snake.reset_snake()

scr.exitonclick()
