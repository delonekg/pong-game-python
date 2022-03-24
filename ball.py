from turtle import Turtle


class Ball(Turtle):

    # Ball Object Constructor
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Move the ball to the top right
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    # Bounce the ball according to it's x coordinate
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Bounce the ball according to it's y coordinate
    def bounce_y(self):
        self.y_move *= -1

    # Reset ball's position
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
