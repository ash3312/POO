class Snake:
    pass


class Python(Snake):
    pass

class Python1():
    pass


class Python2(Python, Python1):
    pass


print(Python.__name__, 'is a', Snake.__name__)
print(Python.__bases__[0].__name__, 'can be', Python.__name__)
print(Python.__bases__[0].__bases__[0].__name__)
print(Python2.__bases__[1].__name__)
