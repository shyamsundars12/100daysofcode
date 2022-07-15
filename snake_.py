from turtle import Turtle
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_snake_squares = []
        self.create_snake()
        self.head = self.all_snake_squares[0]

    def create_snake(self):
        for place in SNAKE_POSITIONS:
            self.snake_segment(place)

    def snake_segment(self, place):
        maggie = Turtle(shape="square")
        maggie.color("white")
        maggie.penup()
        maggie.goto(place)
        self.all_snake_squares.append(maggie)

    def extend(self):
        self.snake_segment(self.all_snake_squares[-1].position())

    def snake_move(self):
        for index in range(len(self.all_snake_squares) - 1, 0, -1):
            new_x = self.all_snake_squares[index - 1].xcor()
            new_y = self.all_snake_squares[index - 1].ycor()
            self.all_snake_squares[index].goto(new_x, new_y)
        self.head.fd(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
