from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')
CENTER = (0, 0)
UP_THE_WINDOW = (0, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(UP_THE_WINDOW)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(CENTER)
        self.write("GAME OVER.", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
