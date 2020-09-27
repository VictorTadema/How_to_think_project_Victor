import turtle
window = turtle.Screen()
gert = turtle.Turtle()
gert.shape("turtle")
gert.speed(10)

for degree in [160, -43, 270, -97, -43, 200, -940, 17,-86]:
    gert.forward(100)
    gert.left(degree)

#Question 17:
sjaak = turtle.Turtle()
sjaak.shape("turtle")
sjaak.color("yellow")
sjaak.speed(2)
sjaak.left(231)
sjaak.forward(100)

#so gert has moved overall a distance of 100 with a direction of 231 towards the left

#Question 18: 360 / 18 = 20


window.exitonclick()