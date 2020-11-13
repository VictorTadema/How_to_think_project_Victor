# Add a method area to the Rectangle class that returns the area of any instance:
# r = Rectangle(Point(0, 0), 10, 5)
# test(r.area() == 50)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        return(self.height * self.width)



