from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PyPong Game")
screen.tracer(0)

paddle_pl2 = Paddle(1)
paddle_pl1 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_pl2.move_up, "Up")
screen.onkeypress(paddle_pl2.move_down, "Down")
screen.onkeypress(paddle_pl1.move_up, "w")
screen.onkeypress(paddle_pl1.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ((ball.distance(paddle_pl2) < 55 and ball.xcor() > 320) or (
            ball.distance(paddle_pl1) < 55 and ball.xcor() < -330)):
        ball.bounce_x()

    if ball.xcor() >= 400:
        ball.restart_position()
        scoreboard.pl1_point()

    if ball.xcor() <= -400:
        ball.restart_position()
        scoreboard.pl2_point()


screen.exitonclick()
