import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
size = 20
for _ in range(30):
tess.stamp()
size = size + 3
tess.forward(size)
tess.right(24)

window.mainloop()