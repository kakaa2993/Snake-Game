#!/usr/bin/python3
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("Black")
starting_position = [(0, 0), (-20, 0), (-40, 0), ]
for position in starting_position:
    turtle = Turtle(shape="square")
    turtle.color("White")
    # turtle.shapesize(stretch_wid=0.5,stretch_len=.5,outline=0)
    turtle.goto(position)


screen.exitonclick()
