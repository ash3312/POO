class Super1:
    x = 1


class Super2:
    x = 2


class Sub(Super1, Super2):
    pass


sub = Sub()
print(sub.x)
