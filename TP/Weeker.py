class WeekValueError(Exception):
    pass

class Weeker:
    week_days = ("lun", "mar", "mer", "jeu", "ven", "sam", "dim")

    def __init__(self, d):
        self.d = d

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value):
        if value not in Weeker.week_days:
            raise WeekValueError("value error")
        self.__d = value

    def __str__(self):
        return f"{self.d}"

    def add_days(self, n):
        idx = (Weeker.week_days.index(self.d) + n) % 7
        self.d = Weeker.week_days[idx]
    def sub_days(self, n):
        idx = (Weeker.week_days.index(self.d) - n) % 7
        self.d = Weeker.week_days[idx]

w = Weeker("lun")

print(w)
w.add_days(1)
print(w)

w.add_days(6)
print(w)

w.sub_days(1)
print(w)

t = Weeker("Mon")
