
from turtle import Turtle
# Define constant
STARTING_POSITION = [(0,0), (-20, 0), (-40,0)]  # different x-coordinates
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []  # movable action
        self.create_snake()
        self.head = self.segments[0]


    # Create a 3 segments snake using the starting position
    def create_snake(self):
        for i in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()     # Avoid drawing line
            new_segment.goto(i)
            self.segments.append(new_segment)

    def move(self):
        # move in reverse order, where seg_num -1 is the 2nd to last segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[seg_num - 1].xcor()
            newY = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

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

