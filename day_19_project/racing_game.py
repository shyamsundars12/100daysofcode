import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
race_is_continue = False
user_choice = screen.textinput(title="make a choice", prompt="enter the choice of the turtle! Enter the colour of your "
                                                             "choice?")
turtle_color = ["red", "blue", "green", "yellow", "purple", "black"]
turtle_directions = [-80, -50, -10, 20, 50, 80]
screen.setup(width=500, height=400)
six_turtle = []
for index in range(0, 6):
    maggie = Turtle(shape="turtle")
    maggie.color(turtle_color[index])
    maggie.penup()
    maggie.goto(x=-230, y=turtle_directions[index])
    six_turtle.append(maggie)

if user_choice:
    race_is_continue = True

while race_is_continue:
    for turtle in six_turtle:
        if turtle.xcor() > 230:
            win_color = turtle.pencolor()
            race_is_continue = False
            if user_choice == win_color:
                print(f"you have won the race. the winner is {win_color}")
            else:
                print(f"you have lost the race. the winner is {win_color}")
        random_move = random.randint(0, 10)
        turtle.forward(random_move)






screen.exitonclick()

