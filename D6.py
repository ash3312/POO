from random import randint

class D6:
    def __init__(self):
        self.lancer()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
       self.__value = v

    def lancer(self):
        self.__value = randint(1, 6)


des = [D6() for _ in range(6)]
count = 0
while True:
    somme = 0
    for d in des:
        d.lancer()
        somme += d.value
    print(somme)
    count += 1
    if somme >= 36:
        print(count)
        break
