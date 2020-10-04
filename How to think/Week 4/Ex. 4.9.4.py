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
bavje.color("blue")
bavje.pensize(2)

for _ in range(10):
    draw_square(bavje, 100)
    bavje.forward(50)
    bavje.left(90)
    bavje.forward(50)
    bavje.right(18)
    bavje.forward(50)

window.mainloop()
