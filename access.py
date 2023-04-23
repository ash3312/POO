class Super:
    x = 5
    y = 10

class Sub(Super):
    x = 6


    def getInitial(self):
        return Super.x


s = Sub()
print(s.x)
print(s.y)

print(s.getInitial())
