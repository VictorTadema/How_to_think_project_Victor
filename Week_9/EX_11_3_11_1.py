# Write a Boolean function between that takes two MyTime objects, t1 and t2, as arguments, and returns
# True if the invoking object falls between the two times

class Nummer:


    def __init__(self, x=0):
        self.x = x

    def between(self, t1, t2):
        if self.x < t1.x:
            return False
        if self.x > t2.x:
            return False
        if self.x == t2.x:
            return False
        else:
            return True

print(Nummer(8).between((Nummer(2)), (Nummer(8))))
#yeah