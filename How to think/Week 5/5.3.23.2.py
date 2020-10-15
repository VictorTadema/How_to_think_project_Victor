import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")

screen = turtle.Screen()

tess.forward(50)



screen.exitonclick()

# putting tess forward by 50 results exactly in the same as doing it for alex. Both turtles are thus aliased