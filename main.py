import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from turtle import Turtle
from scoreboard import Scoreboard
positions = [(300, -250), (300, -200), (300, -150), (300, -100), (300, -50), (300, 0), (300, 50), (300, 100), (300, 150), (300, 200), (300, 250)]


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")

# setting lines
line = Turtle()
line.width(2)
for pos in positions:
    line.penup()
    line.goto(pos)
    line.pendown()
    line.backward(600)
# setting lines

game_is_on = True
while game_is_on:
    scoreboard.update_board()
    time.sleep(0.01)
    screen.update()
    cars.generate_car()
    cars.move_cars()
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False

    if turtle.ycor() > 280:
        scoreboard.increase_score()
        turtle.goto(0, -280)


screen.exitonclick()
