import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

game_on = True

# Setup window
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Classic Pong")
window.tracer(0)

# Create paddle object
paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))

# Create ball object
ball = Ball()

# Create scoreboard object
scoreboard = ScoreBoard()

# Movement control listeners
window.listen()
window.onkey(key="w", fun=paddle1.up)
window.onkey(key="s", fun=paddle1.down)
window.onkey(key="Up", fun=paddle2.up)
window.onkey(key="Down", fun=paddle2.down)

while game_on:
    window.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detect collisions with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collisions with
    if ball.distance(paddle1) < 50 and ball.xcor() < -320 or ball.distance(paddle2) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collisions if ball goes out of boundaries for right side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increment_l_score()

    # Detect collisions if ball goes out of boundaries for left side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increment_r_score()

window.exitonclick()
