class Voiture:
    def __init__(self, _couleur, _vitesse, _portes, _marque, _demarree):
        self.couleur = _couleur
        self.vitesse = _vitesse
        self.portes = _portes
        self.marque = _marque
        self.demarree = _demarree

    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, value):
        self.__couleur = value

    @property
    def vitesse(self):
        return self.__vitesse

    @vitesse.setter
    def vitesse(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("wtf")
        self.__vitesse = value

    @property
    def portes(self):
        return self.__portes

    @portes.setter
    def portes(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("wtf")
        self.__portes = value

    @property
    def marque(self):
        return self.__marque

    @marque.setter
    def marque(self, value):
        self.__marque = value

    @property
    def demarree(self):
        return self.__demarree

    @demarree.setter
    def demarree(self, value):
        self.__demarree = value

    def __str__(self):
        # return "self.couleur"+ self.couleur + "self.vitesse"+ str(self.vitesse) + "self.portes"+ str(self.portes) + "self.marque"+ self.marque + "self.demarree"+ str(self.demarree)
        return f"couleur:{self.couleur} vitesse:{self.vitesse} portes:{self.portes} marque:{self.marque} demarree:{self.demarree}"

    def avancer(self):
        if (not self.demarree):
            raise AttributeError("You cannot move the vehicule when it is off")

    def demarrer(self):
        if (not self.demarree):
            self.demarree = True
        else:
            raise AttributeError("the vehicule when it is already on")

    def toggleEngine(self):
        self.demarree = not self.demarree


voiture = Voiture("blue", 240, 4, "BMW", True)
voiture.toggleEngine()
print(voiture)
voiture.toggleEngine()
print(voiture)
