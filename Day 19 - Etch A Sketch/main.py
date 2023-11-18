import turtle as t

tom = t.Turtle()
scr = t.Screen()


def move_forward():
    tom.forward(20)


def move_backward():
    tom.backward(20)


def turn_left():
    tom.setheading(tom.heading() + 10)


def turn_right():
    tom.setheading(tom.heading() - 10)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


scr.listen()
scr.onkey(move_forward, "w")
scr.onkey(move_backward, "s")
scr.onkey(turn_left, "a")
scr.onkey(turn_right, "d")
scr.onkey(clear, "c")
scr.exitonclick()
