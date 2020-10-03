import turtle


def draw_square(animal, size):
    """
    Make animal draw a square with sides of length size.
    """
    animal.forward(size)
    animal.left(90)
    animal.forward(size)
    animal.left(90)
    animal.forward(size)
    animal.left(90)
    animal.forward(size)
    animal.left(90)


window = turtle.Screen()
window.bgcolor("lightgreen")
bavje = turtle.Turtle()
bavje.color("pink")
bavje.pensize(5)

size = 20
for _ in range(5):
    draw_square(bavje, size)
    size += 20
    bavje.penup()
    bavje.right(90)
    bavje.forward(10)
    bavje.right(90)
    bavje.forward(10)
    bavje.left(180)
    bavje.pendown()

window.mainloop()
