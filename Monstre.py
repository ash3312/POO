class Monstre:
    def __init__(self, _race, _type, _nom, _age, _dangereux=False):
        self.race = _race
        self.type = _type
        self.nom = _nom
        self.age = _age
        self.dangereux = _dangereux

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value):
        self.__race = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def age(self):
        self.khara = 'True'
        return self.__age

    @age.setter
    def age(self, value):
        # if type(value) != int and type(value) != float:
        #     raise TypeError("error type of value")
        # self.__age = value
        if type(value) == int:
            self.__age = value
        else:
            raise TypeError("error type of value")

    @property
    def dangereux(self):
        return self.__dangereux

    @dangereux.setter
    def dangereux(self, value):
        self.__dangereux = value

    def __str__(self):
        return f"race:{self.race} nom:{self.nom} age:{self.age} type:{self.type} dangereux:{self.dangereux}"

    def vieillir(self):
        self.age += 1
        self.devenirDangereux()

    def devenirDangereux(self):
        if self.age >= 10:
            self.dangereux = True

mon = Monstre("Dragon", "Humanoïdes", "KAKA", 9, False)
print(mon)
mon.vieillir()

print(mon)
