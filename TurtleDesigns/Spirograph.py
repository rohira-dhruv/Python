import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)
gap_angle = random.choice([5, 10])
no_of_circles = int(360/gap_angle)
orientation = 0
for _ in range(no_of_circles):
    tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.circle(100)
    orientation += gap_angle
    tim.setheading(orientation)

screen = turtle.Screen()
screen.exitonclick()
