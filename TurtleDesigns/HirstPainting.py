# The colorgram package was used to extract a palette of colors from an image.
# import colorgram
# colors = colorgram.extract("hirst.jpg", 30)
# color_list = []
# for _ in colors:
#     color_list.append((_.rgb.r, _.rgb.g, _.rgb.b))
# print(color_list)

import random
import turtle
from turtle import Turtle, Screen

colors = [(26, 108, 164), (193, 38, 81), (237, 161, 50),
          (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
          (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
          (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221),
          (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]
tim = Turtle()
turtle.colormode(255)


def print_row(size):
    for _ in range(size):
        tim.fillcolor(random.choice(colors))
        print_spot()
        tim.pu()
        tim.fd(70)
        tim.pd()


def print_spot():

    tim.begin_fill()
    tim.rt(90)
    tim.circle(10)
    tim.lt(90)
    tim.end_fill()


tim.speed(0)
y_cord = -300
for _ in range(10):
    tim.pu()
    tim.goto(-300, y_cord)
    tim.pd()
    print_row(10)
    y_cord += 70
tim.hideturtle()
screen = Screen()
screen.screensize(500, 500)
screen.exitonclick()
