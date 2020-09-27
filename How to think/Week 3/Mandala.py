import turtle
window = turtle.Screen()
gert = turtle.Turtle()
gert.shape("turtle")
gert.speed(50)
gert.penup()
gert.right(90)
gert.forward(75)
gert.pendown()

for _ in range(50):
    gert.left(30)
    gert.forward(50)
    gert.left(260)
    gert.forward(50)

jan = turtle.Turtle()
jan.shape("turtle")
jan.speed(50)
jan.penup()
jan.left(100)
jan.forward(75)
jan.pendown()
for _ in range(60):
    jan.left(30)
    jan.forward(50)
    jan.left(260)
    jan.forward(50)

harm = turtle.Turtle()
harm.shape("turtle")
harm.speed(50)
harm.penup()
harm.forward(95)
harm.pendown()
for _ in range(60):
    harm.left(30)
    harm.forward(50)
    harm.left(260)
    harm.forward(50)

henk = turtle.Turtle()
henk.shape("turtle")
henk.speed(50)
henk.penup()
henk.left(10)
henk.forward(300)
henk.pendown()
for _ in range(60):
    henk.left(230)
    henk.forward(50)
    henk.left(260)
    henk.forward(50)


window.exitonclick()