from turtle import Turtle
import random
import math

rand_x = random.randint(10,14)
rand_y = random.randint(10,14)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = rand_x * -1       #random direction and speed
        self.y_move = rand_y * -1
        self.move_speed= 0.1   #slow down   0.5 slower

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_x(self):
        self.y_move *= -1

    def bounce_y(self):
        self.x_move *= -1

    def bounce(self):
        self.x_move *= -1
        self.y_move *= -1

    def restart(self):
        self.home()
        self.x_move *= -1
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed *= 0.8
