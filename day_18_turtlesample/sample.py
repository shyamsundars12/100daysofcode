import turtle
from turtle import Turtle, Screen
import random
maggie = Turtle()
screen = Screen()
turtle.colormode(255)

def move_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(size):
    for _ in range(int(360/ size)):
        maggie.speed(0)
        maggie.circle(100)
        maggie.color(move_color())
        now_pos = maggie.heading()
        maggie.setheading(now_pos+size)
spirograph(9)





screen.exitonclick()


