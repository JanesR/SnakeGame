from turtle import Turtle
import random
MIN_X = -280
MAX_X = 280
MIN_Y = -280
MAX_Y = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("turtle")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.penup()
        self.refresh()

    def refresh(self):
        position_x = random.randint(MIN_X, MAX_X)
        position_y = random.randint(MIN_Y, MAX_Y)
        self.goto(position_x, position_y)