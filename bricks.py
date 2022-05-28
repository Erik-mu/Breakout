from turtle import Turtle

class Brick(Turtle):
    def __init__(self, x,y):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=1)    #80*20px
        self.goto(x, y)
