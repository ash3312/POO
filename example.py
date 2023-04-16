class Example:
    a = 1

    def __init__(self):
        self.b = 2
        #self.__b = 11

ex = Example()
#ex1 = Example()

print(hasattr(ex, 'a'))
print(hasattr(ex, 'b'))
print(hasattr(Example, 'a'))
print(hasattr(Example, 'b'))
# ex.khara = 5
# ex.__khara = 5
print(ex.__dict__)
# print(ex1.__dict__)
print(Example.__dict__)