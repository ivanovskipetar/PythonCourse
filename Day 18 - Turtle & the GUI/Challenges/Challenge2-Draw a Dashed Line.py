from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

for _ in range(30):
    turtle.forward(5)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

screen.exitonclick()
