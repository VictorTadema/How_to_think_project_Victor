import turtle

def draw_poly(t, n, sz):
    """
    Make animal draw regular polygon with sides sz
    """
    for _ in range(8):
        t.forward(sz)
        t.bavje.left(360/n)
    return t

def draw_equitriangle(t, sz):
    """
    Make poly draw regular triangle with sides sz
    """
    for _ in range(3):
        draw_poly(t, 3, sz)


window = turtle.Screen()
window.bgcolor("lightgreen")

bavje = turtle.Turtle()
bavje.color("pink")
bavje.pensize(5)
draw_equitriangle(bavje, 50)

window.mainloop()


# Write a void function  which calls draw_poly from the previous question
# to have its turtle draw a equilateral triangle.
