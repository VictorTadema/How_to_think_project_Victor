class Point:
    """"Point class represents and manipulates x, y coordinates."""

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def get_line_to(self, target):
        a = (target.y - self.y) / (target.y - self.x)
        b = self.y - self.x * a
        return "({}, {})".format(a, b)

# from Week_8.EX_11_1_12_4 import Point

# point_p = Point()
# target = Point()
# point_p.x = 8
# point_p.y = 6
# target.x = 6
# target.y = 10


print("The points are", Point(4, 11).get_line_to(Point(6, 15)))