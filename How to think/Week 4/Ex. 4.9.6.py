import turtle

def draw_poly(animal, sides, size):
    for _ in range(sides):
        animal.forward(size)
        animal.left(360/sides)


def draw_equitriangle(animal, size):
    draw_poly(animal, 5, size)


screen = turtle.Screen()
poly = turtle.Turtle()

draw_equitriangle(poly, 50)

screen.exitonclick()


# Write a void function  which calls draw_poly from the previous question
# to have its turtle draw a equilateral triangle.
