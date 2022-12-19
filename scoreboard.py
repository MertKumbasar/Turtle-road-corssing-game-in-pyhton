from turtle import Turtle
Font = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"level: {self.level}", align="left", font=Font)

    def update_board(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=Font)

    def increase_score(self):

        self.level += 1
