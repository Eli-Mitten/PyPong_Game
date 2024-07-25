from turtle import Turtle

STARTING_POSITION_P1 = (350, 0)
STARTING_POSITION_P2 = (-360, 0)
MOVE_DISTANCE = 20
SCREEN_HEIGHT = 600

class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        if player == 1:
            self.goto(STARTING_POSITION_P1)
        else:
            self.goto(STARTING_POSITION_P2)


    def move_up(self):
        if self.ycor() + MOVE_DISTANCE <= (SCREEN_HEIGHT / 2 - 25):
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() - MOVE_DISTANCE >= -(SCREEN_HEIGHT / 2 - 50):
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
