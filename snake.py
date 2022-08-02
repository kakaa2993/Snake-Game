from turtle import Turtle


class Snake:
    """" a class about the snake body and the all movement of the snake"""
    def __init__(self):
        """create a 3 segment in the screen"""
        self.starting_position = [(0, 0), (-20, 0), (-40, 0), ]
        self.segments = []
        for position in self.starting_position:
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
        self.segments[0].forward(20)