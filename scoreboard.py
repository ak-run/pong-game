from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 45, "normal")
SCREEN_TOP = (0, 270)
SCREEN_CENTRE = (0, 0)
COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor(COLOR)
        self.hideturtle()
        self.penup()
        self.goto(SCREEN_TOP)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

