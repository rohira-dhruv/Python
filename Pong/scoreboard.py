from turtle import Turtle
FONT = ("Courier", 40, "bold")
ALIGNMENT = "center"
MAX_HEIGHT = 300


class Scoreboard(Turtle):

    def __init__(self):
        """Creates the screen setup"""
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.score_player1 = 0
        self.score_player2 = 0
        self.draw_mid_line()
        self.update_scoreboard()

    def draw_mid_line(self):
        """Draws the halfway line in the center of the screen"""
        self.setheading(270)
        self.goto(x=0, y=MAX_HEIGHT)
        while self.ycor() >= -MAX_HEIGHT:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.clear()
        self.draw_mid_line()
        self.goto(x=-100, y=MAX_HEIGHT - 70)
        self.write(arg=f"{self.score_player1}", align=ALIGNMENT, font=FONT)
        self.goto(x=100, y=MAX_HEIGHT - 70)
        self.write(arg=f"{self.score_player2}", align=ALIGNMENT, font=FONT)

    def increase_score(self, player_num):
        """Increases the score of the player whose number is given as argument"""
        if player_num == 1:
            self.score_player1 += 1
        else:
            self.score_player2 += 1
        self.update_scoreboard()

    def game_over(self):
        pass
