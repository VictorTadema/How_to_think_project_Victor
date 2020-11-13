
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

r = Rectangle((0, 0), 10, 5)
print((r.perimeter() == 30))