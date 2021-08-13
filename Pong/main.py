import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("PONG")
screen.tracer(0)

scoreboard = Scoreboard()
l_paddle = Paddle((-450, 0))
r_paddle = Paddle((450, 0))
ball = Ball()


screen.listen()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce()

    # detect collision with paddle
    if abs(ball.xcor()) >= 435 and (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50):
        ball.hit()

    if ball.xcor() > 500:
        ball.reset_position()
        scoreboard.increase_score(1)

    if ball.xcor() < -500:
        ball.reset_position()
        scoreboard.increase_score(2)

    if scoreboard.score_player2 >= 10 or scoreboard.score_player1 >= 10:
        game_is_on = False

screen.exitonclick()
