import turtle

import colorgram
from turtle import Turtle, Screen
import random
turtle.colormode(255)
# colors = colorgram.extract('image.jpg', 6)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     cc = (r, g, b)
#     color_list.append(cc)


# print(color_list)
color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171)]
maggie = Turtle()
screen = Screen()
maggie.speed("fastest")
maggie.penup()
maggie.ht()
maggie.setheading(225)
maggie.fd(300)
maggie.setheading(0)
count_ra = 100
for count in range(1, count_ra+1):
    maggie.dot(20, random.choice(color_list))
    maggie.fd(50)
    if count == 10 or count == 20 or count == 30 or count ==40 or count ==50 or count ==60 or count ==70 or count ==80\
            or count==90 or count ==100:
        maggie.setheading(90)
        maggie.fd(50)
        maggie.setheading(180)
        maggie.fd(500)
        maggie.setheading(0)












screen.exitonclick()