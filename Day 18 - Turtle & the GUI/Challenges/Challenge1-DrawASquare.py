from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen.exitonclick()
