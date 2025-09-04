import turtle as t
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("fastest")

screen = Screen()

def move_forward():
    tim.forward(10)
    
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_backward():
    tim.backward(10)
    
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def stop_drawing():
    tim.penup()
    
def start_drawing():
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="x", fun=stop_drawing)
screen.onkey(key="space", fun=start_drawing)
screen.exitonclick()