from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE_OF_TURTLE = "square"
COLOR_OF_TURTLE = "white"


class Snake:

    def __init__(self):
        self.segments = []
        self.__create_snake()
        self.head = self.segments[0]

    def __create_snake(self):
        """Creates 3 starting square segments which
        represent the snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Creating a new segment (Turtle object) and appending it to the segments list."""
        new_segment = Turtle(SHAPE_OF_TURTLE)
        new_segment.color(COLOR_OF_TURTLE)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.__create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Extending the snake for one segment."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake segments forward by 20 paces.
        The last one moves to the position of the segment
        which is in front of him and so on until it comes
        to the head.Then the head is moved forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Takes the first segment(head) and changes it's direction to north."""
        heading = self.head.heading()
        self.head.setheading(UP) if heading != DOWN else None

    def down(self):
        """Takes the first segment(head) and changes it's direction to south."""
        heading = self.head.heading()
        self.head.setheading(DOWN) if heading != UP else None

    def left(self):
        """Takes the first segment(head) and changes it's direction to west."""
        heading = self.head.heading()
        self.head.setheading(LEFT) if heading != RIGHT else None

    def right(self):
        """Takes the first segment(head) and changes it's direction to east"""
        heading = self.head.heading()
        self.head.setheading(RIGHT) if heading != LEFT else None
