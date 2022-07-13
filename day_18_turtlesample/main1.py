import turtle as t
import random
maggie = t.Turtle()
screen = t.Screen()
t.colormode(255)
maggie.pensize(15)
maggie.speed(0)


def move_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
for _ in range(200):
    maggie.color(move_color())
    maggie.forward(30)
    maggie.setheading(random.choice(directions))

screen.exitonclick()
