class Serpent:
    def __init__(self, _longueur, _couleur, _vitesse, _venimeux):
        self.longueur = _longueur
        self.couleur = _couleur
        self.vitesse = _vitesse
        self.venimeux = _venimeux

    @property
    def longueur(self):
        self.khara = 'True'
        return self.__longueur

    @longueur.setter
    def longueur(self, value):
        # if type(value) != int and type(value) != float:
        #     raise TypeError("error type of value")
        # self.__longueur = value
        if type(value) == int or type(value) == float:
            self.__longueur = value
        else:
            raise TypeError("error type of value")

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
        # if type(value) != int and type(value) != float:
        #     raise TypeError("error type of value")
        # self.__longueur = value
        if type(value) == int or type(value) == float:
            self.__vitesse = value
        else:
            raise TypeError("error type of value")

    @property
    def venimeux(self):
        return self.__venimeux

    @venimeux.setter
    def venimeux(self, value):
        self.__venimeux = value

    def afficherInfo(self):
        print("longueur:", self.__longueur, "couleur:", self.__couleur, "vitesse:", self.__vitesse, "venimeux:",
              self.__venimeux)

    def seDeplacer(self):
        print("running")

    def manger(self):
        print("eating")


ser = Serpent(5, 2, 2, 5) # compiled
#ser = Serpent("5", 2, 2, 5) # incompiled
ser.afficherInfo()
ser.seDeplacer()
ser.manger()
ser.longueur = 51.5
print(ser._Serpent__longueur)
