from datetime import datetime


class Humain:
    def __init__(self, _nom, _prenom, _annee, _enfants=None):
        self.nom = _nom
        self.prenom = _prenom
        self.annee = _annee
        if (_enfants == None):
            self.enfants = []
        else:
            self.enfants = _enfants

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, value):
        if type(value) == int:
            self.__annee = value
        else:
            raise TypeError("error type of value")

    @property
    def enfants(self):
        return self.__enfants

    @enfants.setter
    def enfants(self, value):
        if type(value) == list:
            self.__enfants = value
        else:
            raise TypeError("error type of value")

    def calculerAge(self):
        return int(datetime.now().strftime("%Y")) - self.annee

    def addEnfant(self, enfant):
        self.enfants.append(enfant)

    def sePresenter(self):
        return f"{self.nom} {self.prenom}, {self.annee} , {len(self.enfants)} enfants"

    def __str__(self):
        enfantCaption = "enfants" if len(self.enfants) > 0 else ""
        return f"{self.nom} {self.prenom}, {self.annee} , {len(self.enfants)} {enfantCaption} {[en.sePresenter() for en in self.enfants]}"


humain = Humain("daood", "majdy", 1983)
print(humain.sePresenter())
enfant1 = Humain("daood", "ayhamj", 2050)
enfant2 = Humain("daood", "ashrafj", 2051)
humain.addEnfant(enfant1)
humain.addEnfant(enfant2)

print(humain.calculerAge())

print(humain)

for enf in humain.enfants:
    print(enf.sePresenter())
