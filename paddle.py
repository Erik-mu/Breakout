from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_len=10, stretch_wid=1)    #200*20px
        self.goto(position, -280)
        self.color("white")

    def r(self):
        new_x = self.xcor() + 50
        self.goto(new_x, self.ycor())

    def l(self):
        new_x = self.xcor() - 50
        self.goto(new_x, self.ycor())
