from turtle import Turtle
MOVE_DISTANCE = 20


class Ball(Turtle):

    def __init__(self):
        """creates a ball in the center of the screen"""
        super().__init__(shape="circle")
        self.color("white")
        self.setheading(45)
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.move_speed /= 1.15

    def reset_position(self):
        self.home()
        self.hit()
        self.move_speed = 0.1
