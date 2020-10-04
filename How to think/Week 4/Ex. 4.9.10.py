# Extend your program above. Draw five stars, but between each, pick up the pen,
# move forward by 350 units, turn right by 144, put the pen down, and draw the next star.

import turtle

def draw_five_stars(animal, length):
    for _ in range(6):
        animal.right(144)
        animal.forward(length)
    animal.right(180)
    animal.penup()
    animal.forward(350)
    animal.pendown()
    animal.right(36)
    for _ in range(6):
        animal.right(144)
        animal.forward(length)
    animal.right(180)
    animal.penup()
    animal.forward(350)
    animal.pendown()
    animal.right(36)
    for _ in range(6):
        animal.right(144)
        animal.forward(length)
    animal.right(180)
    animal.penup()
    animal.forward(350)
    animal.pendown()
    animal.right(36)
    for _ in range(6):
        animal.right(144)
        animal.forward(length)
    animal.right(180)
    animal.penup()
    animal.forward(350)
    animal.pendown()
    animal.right(36)




window = turtle.Screen()
window.bgcolor("lightgreen")
bavje = turtle.Turtle()
draw_five_stars(bavje, 100)

window.mainloop()