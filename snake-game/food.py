from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()  # inherited
        self.shape("turtle")
        self.penup()
        # stretch size along length and width
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)    #default size is 20 x 20 pixels
        self.color("tomato", "#419f6a")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-290, 290)    # should not in the edge of the screen
        random_y = random.randint(-290, 290)    # We don't want it appear on the cornor
        self.goto(random_x, random_y)
