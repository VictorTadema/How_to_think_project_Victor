# Rewrite the distance function from the chapter titled Fruitful functions so that it takes two Points as
# parameters instead of four numbers.

class Point:
    """"Point class represents and manipulates x, y coordinates."""

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def distance_from_origin(self):
        distance = (self.x * self.x + self.y * self.y) ** .5
        return distance