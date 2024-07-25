from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PyPong Game")
screen.tracer(0)

paddle_p1 = Paddle(1)
paddle_p2 = Paddle(2)
ball = Ball()

screen.listen()
screen.onkeypress(paddle_p1.move_up, "Up")
screen.onkeypress(paddle_p1.move_down, "Down")
screen.onkeypress(paddle_p2.move_up, "w")
screen.onkeypress(paddle_p2.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)

screen.exitonclick()
