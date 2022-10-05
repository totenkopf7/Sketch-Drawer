from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()


