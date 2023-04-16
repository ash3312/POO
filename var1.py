class Var:
    __a = 1

    def __init__(self):
        self.__b = 5
        Var.__a += 1

print(Var.__dict__)

var = Var()
var1 = Var()
var.__c = 6

print(var.__dict__)
print(Var.__dict__)