from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0), ]
MOVEMENT_DISTANCE = 20


class Snake:
    """" a class about the snake body and the all movement of the snake"""
    def __init__(self):
        """create a 3 segment in the screen"""
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            seg = Turtle(shape="square")
            seg.penup()
            seg.color("white")
            seg.goto(position)
            self.segments.append(seg)

    def move(self):
        """ moving the Snake forward """
        for segment_num in range(len(self.segments) - 1, 0, -1):
            segment_before = self.segments[segment_num - 1]
            x_position = segment_before.xcor()
            y_position = segment_before.ycor()
            self.segments[segment_num].goto(x=x_position, y=y_position)
        self.segments[0].forward(MOVEMENT_DISTANCE)