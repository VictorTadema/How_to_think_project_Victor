import turtle

def draw_poly(t, n, sz):
    """
    Make animal draw regular polygon with sides sz
    """
    for _ in range(8):
        t.forward(sz)
        t.left(360/n)


window = turtle.Screen()
window.bgcolor("lightgreen")
bavje = turtle.Turtle()
bavje.color("pink")
bavje.pensize(5)
draw_poly(bavje, 8, 50)

window.mainloop()