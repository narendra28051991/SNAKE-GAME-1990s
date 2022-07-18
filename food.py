import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.refresh()

    def refresh(self):
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.position()

    def position(self):
        ran_x = random.randint(-270, 270)
        ran_y = random.randint(-270, 270)
        self.goto(ran_x, ran_y)