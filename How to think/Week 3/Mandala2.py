import turtle
window = turtle.Screen()
gert = turtle.Turtle()
gert.shape("turtle")
gert.speed(50)
gert.penup()
gert.right(90)
gert.forward(75)
gert.pendown()

colors = ['yellow', 'orange', 'red', 'blue', 'green']

for element in range(45):
    gert.color(colors[element % 5])
    gert.left(30)
    gert.forward(100)
    gert.left(260)
    gert.forward(100)

jan = turtle.Turtle()
jan.shape("turtle")
jan.speed(50)
jan.penup()
jan.right(105)
jan.forward(105)
jan.pendown()

colors1 = ['yellow', 'orange', 'red', 'blue', 'green']

for element in range(60):
    jan.color(colors1[element % 5])
    jan.left(30)
    jan.forward(70)
    jan.left(260)
    jan.forward(70)





window.exitonclick()