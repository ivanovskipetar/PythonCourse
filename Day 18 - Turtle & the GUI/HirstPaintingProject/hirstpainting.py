import colorgram
import random
import turtle as t

t.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188),
              (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15),
              (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206),
              (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212),
              (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

turtle = t.Turtle()
screen = t.Screen()
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

for count in range(1, 101):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen.exitonclick()
