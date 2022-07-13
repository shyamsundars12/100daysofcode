import turtle
from turtle import Turtle, Screen
maggie = Turtle()
screen = Screen()


def forward_func():
    maggie.fd(10)


def backward_func():
    maggie.bk(10)


def left_func():
    maggie.left(10)


def right_func():
    maggie.right(10)


def clear_func():
    maggie.clear()
    maggie.penup()
    maggie.home()
    maggie.pendown()


screen.listen()
turtle.onkey(fun=forward_func, key="w")
turtle.onkey(fun=backward_func, key="s")
turtle.onkey(fun=left_func, key="a")
turtle.onkey(fun=right_func, key="d")
turtle.onkey(fun=clear_func, key="c")
screen.exitonclick()
