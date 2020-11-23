# Overload the necessary operator(s) so that instead of having to write > instead of after

class Nummer:
    def __init__(self, x=0):
        self.x = x

    def __gt__(self, t1):
        return(t1.x > self.x)

print(Nummer(6) > Nummer(8))