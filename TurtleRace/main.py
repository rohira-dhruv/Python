import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(height=400, width=500)
screen.delay(0)


def finish_line():
    tim = Turtle()
    tim.speed(0)
    tim.hideturtle()
    tim.penup()
    tim.goto(200, 185)
    tim.pd()
    for i in range(1, 39):
        if i % 2 != 0:
            tim.fillcolor("black")
        else:
            tim.fillcolor("white")
        for __ in range(4):
            tim.begin_fill()
            for _ in range(4):
                tim.fd(10)
                tim.lt(90)
            tim.fd(10)
            tim.end_fill()
            if tim.fillcolor() == "white":
                tim.fillcolor("black")
            else:
                tim.fillcolor("white")
        tim.pu()
        tim.goto(200, 185 - 10*i)
        tim.pd()
    tim.penup()
    tim.home()
    tim.pd()


user_bet = screen.textinput(title="Make a bet", prompt="Which color turtle do you think will win? ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_start = -100
finish_line()
screen.delay(5)
for colour in colours:
    new_turtle = Turtle("turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    turtles.append(new_turtle)
    new_turtle.goto(-220, y_start)
    y_start += 40

if user_bet:
    is_race_on = True
else:
    is_race_on = False

while is_race_on:

    for race_turtle in turtles:
        if race_turtle.xcor() > 230:
            is_race_on = False
            winner_color = race_turtle.pencolor()
            if user_bet.lower() == winner_color:
                print(f"You've Won! The {winner_color} turtle is the winner.")
            else:
                print(f"You've Lost! The {winner_color} turtle is the winner.")
        race_turtle.forward(random.randint(0, 10))

screen.bye()
