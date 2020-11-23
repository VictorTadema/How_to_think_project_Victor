# Rewrite increment as a method that uses our “Aha” insight.

class MyTime:

    def __init__(self, hours=0, minutes=0, seconds=0):
        totalsecs = hours * 3600 + minutes * 60 + seconds
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        if self.hours < 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            
    def __str__(self):
        return "({} hours, {} minutes, and {} seconds)".format(self.hours, self.minutes, self.seconds)

    def to_seconds(self):
        """ Return the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def increment(self, seconds):
        secs = self.to_seconds() + seconds
        return MyTime(0, 0, secs)


time1 = MyTime(4, 20, 49)
print(time1)
print(time1.increment(-8000000))