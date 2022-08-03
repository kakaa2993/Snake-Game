from turtle import Turtle
FONT = ("Courier", 20, 'normal')
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.scoreboard()
        self.speed("fastest")

    def scoreboard(self):
        self.goto(x=0, y=260)
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align= ALIGN, font= FONT)
        self.color('chartreuse')

    def game_over(self):
        self.color("red")
        self.goto(x=0, y=0)
        self.write(arg="Game Over", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.scoreboard()
