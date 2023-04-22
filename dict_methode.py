class Classy:
    var = 1

    def __init__(self):
        self.par = "blah"

    def methode(self):
        pass

    def __hidden(self):
        pass

obj = Classy()
print(obj.__dict__)
print(Classy.__dict__)

print(Classy.__name__)
#print(obj.__name__) not working

print(isinstance(obj, Classy))
print(type(obj).__name__)


print(Classy.__module__)
print(obj.__module__)