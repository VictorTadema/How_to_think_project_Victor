# Add a method slope_from_origin which returns the slope of the line joining the origin to the point. For
# example,

class Point:
    """"Point class represents and manipulates x, y coordinates."""

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def slope_from_origin(self):
        return self.y/self.x

# when x == 0, the program will give an error as you cannot divide by 0.

print(Point(4, 10).slope_from_origin())