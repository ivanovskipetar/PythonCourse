from turtle import Turtle
import random

FOOD_SHAPE = "circle"
FOOD_COLOR = "blue"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Get a new random position of the food(turtle object)."""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
