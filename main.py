#!/usr/bin/python3
from turtle import Turtle,Screen
import time
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("Black")
starting_position = [(0, 0), (-20, 0), (-40, 0), ]
segments = []
screen.tracer(0)
random_color = ["red","green","blue"]
i = 0
for position in starting_position:
    seg = Turtle(shape="square")
    seg.penup()
    seg.color("white")
    # seg.color(random_color[i])
    # turtle.shapesize(stretch_wid=0.5,stretch_len=.5,outline=0)
    seg.goto(position)
    segments.append(seg)
    i += 1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment_num in range(len(segments) - 1, 0, -1):
        segment_before = segments[segment_num - 1]
        x_position = segment_before.xcor()
        y_position = segment_before.ycor()
        segments[segment_num].goto(x=x_position,y=y_position)
    segments[0].forward(20)



screen.exitonclick()
