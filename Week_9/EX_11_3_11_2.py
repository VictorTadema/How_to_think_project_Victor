class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def to_seconds(self):
        """ Return the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def between(self, t1, t2):
        if self.to_seconds() < t1.to_seconds():
            return False
        if self.to_seconds() > t2.to_seconds():
            return False
        if self.to_seconds() == t2.to_seconds():
            return False
        else:
            return True

time1 = MyTime(3, 40, 22)
time2 = MyTime(11, 49, 1)
print(MyTime(8, 22, 6).between(time1, time2))

