# Write a Boolean function between that takes two MyTime objects, t1 and t2, as arguments, and returns
# True if the invoking object falls between the two times
from Week_8.EX_11_1_12_1 import Point

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def perimeter(self):
        return(self.height * 2 + self.width * 2)

r = Rectangle(Point(0, 0), 10, 5)
print(r.perimeter() == 30)