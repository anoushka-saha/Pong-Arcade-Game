#Anoushka Saha
#Day 22 Project
#Pong Arcade Game
#May 25th, 2024

from turtle import Turtle, Screen

#Screen setup
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

#Paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid = 5, stretch_len = 1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
    y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), y)

def go_down():
    y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()