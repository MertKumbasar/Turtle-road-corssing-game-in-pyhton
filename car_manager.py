
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
RANDOM_LOC_FOR_CARS = [4.5, 3.5, 2.5, 1.5, 0.5, -0.5, -1.5, -2.5, -3.5, -4.5]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.pre_y = 0
        self.cur_y = 1
        self.pre_y2 = 2
        self.pre_y3 = 3

    def generate_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.penup()
            self.pre_y3 = self.pre_y2
            self.pre_y2 = self.pre_y
            self.pre_y = self.cur_y
            self.cur_y = random.choice(RANDOM_LOC_FOR_CARS) * 50
            while self.pre_y == self.cur_y or self.pre_y2 == self.cur_y or self.cur_y == self.pre_y3:
                self.cur_y = random.choice(RANDOM_LOC_FOR_CARS) * 50
            car.goto(300, self.cur_y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
            #if statment to delete cars from list when they are no longer in the screen
            if car.xcor() < -330:
                self.all_cars.remove(car)
