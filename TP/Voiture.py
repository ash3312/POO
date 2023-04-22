class Voiture:
    nombre_de_voitures = dict()
    couleurs_disponibles = ("blue", "red")

    def __init__(self, marque, modele, annee, couleur, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.kilometrage = kilometrage
        Voiture.nombre_de_voitures[marque] = Voiture.nombre_de_voitures.get(marque, 0) + 1

    def changer_colour(self, new_colour):
        if new_colour in Voiture.couleurs_disponibles:
            self.couleur = new_colour
        else:
            raise ValueError("the color is not available")

    def info(self):
        return f"{self.marque} {self.modele} {self.annee} {self.couleur} {self.kilometrage} {Voiture.nombre_de_voitures}"

car1 = Voiture("BMW", "c6", 1990, "red", 10000)
print(car1.info())
car2 = Voiture("Mercides", "bense base", 2000, "blue", 20000)
car3 = Voiture("Mercides", "bense base", 2000, "blue", 20000)
print(car2.info())
#car2.changer_colour("green")

print(car1.__dict__)

