import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turtle.speed("fastest")
turtle.width(4)
directions = [0, 90, 180, 270]

for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
