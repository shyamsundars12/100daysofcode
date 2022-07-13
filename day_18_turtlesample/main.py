from turtle import Turtle, Screen
import random
maggie = Turtle()
screen = Screen()
maggie.shape("turtle")

colour = [ "black", "blue", "green", "yellow", "red", "orange", "pink", "violet"]
def move_turtle(position):
    angles = (360 / position)
    for _ in range(position):
        maggie.forward(100)
        maggie.right(angles)


for fat in range(3, 11):
    maggie.color(random.choice(colour))
    maggie.speed(1)
    move_turtle(fat)


screen.exitonclick()