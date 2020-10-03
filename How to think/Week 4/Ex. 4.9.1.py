import turtle


def draw_square(animal, size):
    """
    Make animal draw a square with sides of length size.
    """
    for _ in range(5):
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.forward(size)
        animal.left(90)
        animal.penup()
        animal.forward(50)
        animal.pendown()



window = turtle.Screen()
window.bgcolor("lightgreen")
bavje = turtle.Turtle()
bavje.color("pink")
bavje.pensize(5)
draw_square(bavje, 20)

window.mainloop()
