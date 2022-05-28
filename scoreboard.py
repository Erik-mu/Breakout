from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 330)
        self.write(f" Score: {self.score}", align="center", font= ("Courier", 20, "normal"))
    def new_score(self):        #increase score
        self.clear()
        self.score +=1
        self.write(f" Score: {self.score}", align="center", font= ("Courier", 20, "normal"))
    def reset(self):
        self.clear()
        self.score = 0
        self.write(f" Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def won(self):
        self.goto(0, 0)
        self.write("YOU HAVE WON!!!", align="center", font= ("Courier", 24, "bold"))
