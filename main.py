#!/usr/bin/python3
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("Black")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # Detect the collision with the food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect the collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # Detect if there is a collision between the segments
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
