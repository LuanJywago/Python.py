from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("green")

def square():
    for _ in range(4):
        timmy_turtle.forward(100)
        timmy_turtle.right(90)

def triangle():
    for _ in range(3):
        timmy_turtle.forward(100)
        timmy_turtle.left(120)
        
def door():
    for _ in range(2):
        timmy_turtle.forward(100)
        timmy_turtle.right(90)

    timmy_turtle.forward(40)
    timmy_turtle.right(90)
    timmy_turtle.forward(30)
    timmy_turtle.left(90)
    timmy_turtle.forward(20)
    timmy_turtle.left(90)
    timmy_turtle.forward(30)
    timmy_turtle.right(90)
    timmy_turtle.forward(40)
    timmy_turtle.right(90)
    timmy_turtle.forward(100)
    timmy_turtle.right(90)
    
def house():        
    triangle()
    square()
    door()
    
house()

screen = Screen()
screen.exitonclick()