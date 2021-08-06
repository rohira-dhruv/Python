from turtle import *
my_turtle = Turtle()


def body(color):
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.lt(90)
    my_turtle.circle(60, 180)
    my_turtle.fd(150)
    my_turtle.circle(20, 180)
    my_turtle.fd(40)
    my_turtle.rt(90)
    my_turtle.fd(40)
    my_turtle.rt(90)
    my_turtle.fd(40)
    my_turtle.circle(20, 180)
    my_turtle.fd(150)
    my_turtle.end_fill()


def backpack(color):
    my_turtle.fillcolor(color)
    my_turtle.penup()
    my_turtle.goto(-120, 0)
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.left(90)
    my_turtle.fd(30)
    my_turtle.left(90)
    my_turtle.fd(120)
    my_turtle.left(90)
    my_turtle.fd(30)
    my_turtle.end_fill()


def eyes():
    my_turtle.penup()
    my_turtle.goto(-10, 0)
    my_turtle.pendown()
    my_turtle.fillcolor("white")
    my_turtle.begin_fill()
    my_turtle.fd(10)
    my_turtle.circle(-25, 180)
    my_turtle.fd(50)
    my_turtle.circle(-25, 180)
    my_turtle.fd(40)
    my_turtle.end_fill()


my_turtle.pensize(10)
my_turtle.hideturtle()
# colour = input("What color do you want for the image? ")
my_screen = Screen()
colour = my_screen.textinput("Color", "What color do you want for the image? ")
body(colour)
backpack(colour)
eyes()
my_screen.exitonclick()
