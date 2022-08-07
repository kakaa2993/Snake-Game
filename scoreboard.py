from turtle import Turtle
FONT = ("Courier", 20, 'normal')
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.speed("fastest")

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align= ALIGN, font= FONT)
        self.color('chartreuse')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0



    # def game_over(self):
    #     self.color("red")
    #     self.goto(x=0, y=0)
    #     self.write(arg="Game Over", move=False, align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
