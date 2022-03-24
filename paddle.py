from turtle import Turtle


class Paddle(Turtle):

    # Paddle Object Constructor
    def __init__(self, starting_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(starting_pos)

    # Go up
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Go down
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
