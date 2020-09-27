import turtle
window = turtle.Screen()
gert = turtle.Turtle()
gert.shape("turtle")


for _ in range(20):
    gert.forward(100)
    gert.left(45)


for _ in range(5):
    gert.forward(100)
    gert.left(120)

window.exitonclick()