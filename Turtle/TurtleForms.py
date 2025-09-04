import turtle as t

yas = t.Turtle()
yas.shape("turtle")
yas.color("green")
yas.speed("fastest")

number_of_sides = int(input("Enter the number of sides for the polygon: "))

def draw_polygon(sides):
    angle = 360 / sides
    for _ in range(sides):
        yas.forward(50)
        yas.right(angle)
        
draw_polygon(number_of_sides)

screen = t.Screen()
screen.exitonclick()