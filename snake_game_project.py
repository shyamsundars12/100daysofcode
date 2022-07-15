from turtle import Screen
from snake_ import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
screen.title("Branded Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_continue = True
while game_continue:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food) < 15:
        food.refresh()
        if food.refresh():
            score.clear()
            score.point += 1
            snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_continue = False
        score.game_over()
        for segment in snake.all_snake_squares[1:]:
            if snake.head.distance(segment) < 10:
                game_continue = False
                score.game_over()
            snake.snake_move()
    score.score()
     


screen.exitonclick()
