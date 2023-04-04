from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 8


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car = random.randint(0, 6)
        random_y = random.randint(-250, 250)
        x = 300
        random_car = random.randint(1, 6)
        if random_car == 6:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.goto(x, random_y)
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.car_list.append(car)

    def car_move(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

