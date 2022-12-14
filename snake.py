import turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0), ]
MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """" a class about the snake body and the all movement of the snake"""
    def __init__(self):
        """create a 3 segment in the screen"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        seg = turtle.Turtle(shape="square")
        seg.penup()
        seg.color("white")
        seg.goto(position)
        self.segments.append(seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(-1000,-1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(position=self.segments[-1].position())

    def move(self):
        """ moving the Snake forward """
        for segment_num in range(len(self.segments) - 1, 0, -1):
            segment_before = self.segments[segment_num - 1]
            x_position = segment_before.xcor()
            y_position = segment_before.ycor()
            self.segments[segment_num].goto(x=x_position, y=y_position)
        self.head.forward(MOVEMENT_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)