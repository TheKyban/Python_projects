import time
from turtle import Turtle, Screen, onclick
from Paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard

window = Screen()
window.tracer(0)
window.bgcolor("black")
window.setup(800,600)


Paddle_L = Paddle((-380,0))
Paddle_R = Paddle((380,0))

Score = ScoreBoard()

ball = Ball()

window.listen()

window.onkey(Paddle_L.go_up,"w")
window.onkey(Paddle_L.go_down,"s")

window.onkey(Paddle_R.go_up,"Up")
window.onkey(Paddle_R.go_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    window.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    if ball.distance(Paddle_R) < 50 and ball.xcor() > 350:
        ball.bounce_x()
        Score.increase_right_score()
    if ball.distance(Paddle_L) < 50 and ball.xcor() < 350:
        ball.bounce_x()
        Score.increase_left_score()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()
window.exitonclick()
