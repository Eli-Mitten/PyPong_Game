from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pl1_score = 0
        self.pl2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.pl1_score, align="center", font=("Arial", 70, "normal"))
        self.goto(100, 200)
        self.write(self.pl2_score, align="center", font=("Arial", 70, "normal"))

    def pl1_point(self):
        self.pl1_score += 1
        self.update_scoreboard()

    def pl2_point(self):
        self.pl2_score += 1
        self.update_scoreboard()

