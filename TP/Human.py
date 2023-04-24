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


class Moldus(Humain):
    def __init__(self, _nom, _prenom, _annee, travail, niveau_magie, _enfants=None):
        super().__init__(_nom, _prenom, _annee, _enfants)
        self.travail = travail
        self.niveau_magie = niveau_magie

    def sePresenter(self):
        return super().sePresenter() + f" {self.travail} {self.niveau_magie}"

    def decouvrir_magie(self):
        return self.niveau_magie
    
class Sorciers(Humain):
    maisons = ("Gryffondor", "Poufsouffle", "Serdaigle", "Serpentard")
    def __init__(self, _nom, _prenom, _annee, baguette, maison, _enfants=None):
        super().__init__(_nom, _prenom, _annee, _enfants)
        self.baguette = baguette
        self.sortileges = []
        self.maison = maison

    def sePresenter(self):
        return super().sePresenter() + f" {self.baguette} {self.sortileges} {Sorciers.maisons[self.maison]}"

    def lancerSort(self, nom):
        if nom in self.sortileges: 
            return f" le sort {nom} a été créé"
        else:
            return "Error no sort"
        
    def apprendre(self, nom):
        self.sortileges.append(nom)
    
# m1 = Moldus("majdy", "m", 2010, "it", 0, [Humain("ashraf", "ash", 1993)])

# print(m1)

s1 = Sorciers("daood","majdy", 1983, "b1", 0)

print(s1.sePresenter())
print(s1.lancerSort("abra"))

s1.apprendre("abra")
print(s1.lancerSort("abra"))
print(s1.sePresenter())