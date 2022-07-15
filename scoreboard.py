from food import Food


class Scoreboard(Food):
    def __init__(self):
        self.point = 0
        super().__init__()

    def score(self):
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(arg=f'Score : {self.point} ', move=False, font=('Arial', 12, 'normal'), align="center", )

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over ! ", move=False, font=('Arial', 12, 'normal'), align="center", )
