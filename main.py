from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Brick
from ball import Ball
from scoreboard import Scoreboard
import time


colors = ['yellow', 'blue', 'orange', 'red', 'violet', 'green']
all_bricks = []

scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=750)
screen.title("Breakout")
screen.tracer(0)
paddle = Paddle(0)
ball = Ball()
game_on = True

def create():
    for row in range(6):
        for n in range(8):
            brick = Brick(-350+n*100, 150+row*30)
            brick.color(colors[row])
            all_bricks.append(brick)


create()
while game_on:
    time.sleep(ball.move_speed)  # slow down   0.5 slower
    screen.update()
    ball.move()
    screen.listen()
    screen.onkey(paddle.r, "Right")
    screen.onkeypress(paddle.r, "Right")
    screen.onkey(paddle.l, "Left")
    screen.onkeypress(paddle.l, "Left")
    if ball.ycor() > 300: #collision with top
        ball.bounce_x()
    if ball.xcor() > 430 or ball.xcor() < -430: #collision with sides
        ball.bounce_y()
    if ball.ycor() < -280:  #game over
        game_on = False
        go_on = screen.textinput(title="GAME OVER", prompt="Do you want to conitnue? y/n")  #pop-up
        if go_on == "y" or go_on == "Y":
            game_on = True
            ball.restart()
            create()
            scoreboard.reset()
        else:
            screen.bye()        #exit game

    for brick in all_bricks:        #destroy brick
        if ball.distance(brick) <40:
            ball.bounce_y()
            brick.hideturtle()
            scoreboard.new_score()
            if scoreboard.score % 6 == 0:
                ball.increase_speed()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                ball.bounce_y()
            else:
                ball.bounce_x()
                ball.bounce_y()
            all_bricks.remove(brick)
    if ball.distance(paddle) <100 and ball.ycor() < -270:
        ball.bounce_x()

    if not all_bricks:
        game_on = False
        scoreboard.won()

screen.exitonclick()
