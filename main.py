from turtle import Screen

from ball import Ball
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
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ((ball.distance(paddle_p1) < 50 and ball.xcor() > 320) or (
            ball.distance(paddle_p2) < 50 and ball.xcor() < -330)):
        ball.bounce_x()


screen.exitonclick()
