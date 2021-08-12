from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 26, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER.", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
