from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=640, height=480)

is_game_on = False

user_input = screen.textinput(title="Enter your bet", prompt="Which turtle will win the race?")
colors = ["green", "yellow", "blue", "red", "orange", "pink"]
turtles = []
y = -100

if user_input:
    is_game_on = True

for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-300, y=y)
    turtles.append(new_turtle)
    y += 30

while is_game_on:

    for turtle in turtles:
        if turtle.xcor() > 300:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0,10))

screen.exitonclick()
