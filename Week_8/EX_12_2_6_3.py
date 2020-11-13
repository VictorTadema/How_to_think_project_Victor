# Write a flip method in the Rectangle class that swaps the width and the height of any rectangle instance


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def flip(self):
        (self.width, self.height) = (self.height, self.width)

r = Rectangle((100, 50), 10, 5)
print(r.width == 10 and r.height == 5)

r.flip()
print(r.width == 5 and r.height == 10)