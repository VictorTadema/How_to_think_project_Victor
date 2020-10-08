# Write a void function to draw a star, where the length of each side is 100 units.
# (Hint: You should turn the turtle by 144 degrees at each point.)

import turtle

def draw_star(animal, length):
    for _ in range(5):
        animal.right(144)
        animal.forward(length)

window = turtle.Screen()
bavje = turtle.Turtle()
draw_star(bavje, 200)

window.mainloop()

