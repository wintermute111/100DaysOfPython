import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.penup()
        self.hideturtle()
        for _ in range(10):
            self.add_car((random.randint(0, 300), random.randint(-250, 250)))

    def advance(self, level):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)

    def add_car(self, location):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(location)
        self.cars.append(new_car)
