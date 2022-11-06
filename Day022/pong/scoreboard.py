from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 230)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}", align=ALIGNMENT, font=FONT)
