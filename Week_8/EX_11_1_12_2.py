# Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point
# about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)

class Point:

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def reflect_x(self):
        var1 = self.x
        var2 = self.y - 2*self.y
        return "({}, {})".format(var1, var2)




