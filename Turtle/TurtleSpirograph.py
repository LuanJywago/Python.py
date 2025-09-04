import turtle as t
from turtle import Turtle, Screen
import random

yas = Turtle()
yas.shape("turtle")
yas.speed("fastest")
t.colormode(255)

def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return (r, g, b)

yas.speed("fastest")

def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        yas.color(random_color())
        yas.circle(100)
        yas.setheading(yas.heading() + size_of_gap)
        
spirograph(5)

screen = Screen()
screen.exitonclick()
