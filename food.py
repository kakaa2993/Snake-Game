from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275,275)
        random_y = random.randint(-275,275)
        self.goto(x=random_x, y=random_y)