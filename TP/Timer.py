from time import sleep
class Timer:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        if value < 0 or value > 24:
            raise ValueError('Hour value is incorrect')
        self.__h = value

    @property
    def m(self):
        return self.__m

    @m.setter
    def m(self, value):
        if value < 0 or value > 60:
            raise ValueError('Minute value is incorrect')
        self.__m = value

    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, value):
        if value < 0 or value > 60:
            raise ValueError('Second value is incorrect')
        self.__s = value

    def next_sec(self):
        self.s += 1
        if self.s == 60:
            self.m += 1
            self.s = 0
        if self.m == 60:
            self.h += 1
            self.m = 0
        if self.h == 24:
            self.h = 0
            self.m = 0
            self.s = 0
    def prev_sec(self):
        self.s -=1

    def info(self):
        return f"{add_zeros(self.h)}:{add_zeros(self.m)}:{add_zeros(self.s)}"

def add_zeros(v):
   return '0' + str(v) if v < 10 else v

t = Timer()
print(t.info())
for i in range(1000):
    sleep(1)
    t.next_sec()
    print(t.info())


