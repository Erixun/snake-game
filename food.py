from random import randint
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.place_randomly()

    def place_randomly(self):
        x, y = randint(-280, 280), randint(-280, 280)
        self.goto(x, y)
    