# Extend your program above. Draw five stars, but between each, pick up the pen,
# move forward by 350 units, turn right by 144, put the pen down, and draw the next star.

import turtle

def draw_star(animal, length):
    for _ in range(5):
        animal.right(144)
        animal.forward(length)

window = turtle.Screen()
bavje = turtle.Turtle()

for _ in range(5):
    draw_star(bavje, 100)
    bavje.penup()
    bavje.forward(300)
    bavje.left(144)
    bavje.pendown()

window.mainloop()