import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("white")
scr.title("TURTLE CROSSING")
scr.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

scr.listen()
scr.onkeypress(player.move_forward, "Up")

loop_count = 0
game_on = True
while game_on:
    time.sleep(0.1)
    car_manager.advance(scoreboard.level)
    scr.update()
    loop_count += 1
    if loop_count % 6 == 0:
        car_manager.add_car((300, random.randint(-250, 250)))
    if player.ycor() > 300:
        scoreboard.level += 1
        scoreboard.refresh()
        player.goto(player.start)
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_on = False
            scoreboard.game_over()

scr.exitonclick()
