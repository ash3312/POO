class Chateau:
    nombre_chateaux = 0

    def __init__(self, nom, proprietaire, annee_construction, nombre_pieces):
        self.nom = nom
        self.proprietaire = proprietaire
        self.annee_construction = annee_construction
        self.nombre_pieces = nombre_pieces
        Chateau.nombre_chateaux += 1

    def ajouter_pieces(self, no):
        self.nombre_pieces += no

    def info(self):
        return f"{self.nom} {self.proprietaire} {self.annee_construction} {self.nombre_pieces}  {Chateau.nombre_chateaux}"


c1 = Chateau("palace", "me", 2010, 4)
c2 = Chateau("palace 1", "you", 1900, 2)

print(c1.info())
print(c2.info())

c1.ajouter_pieces(2)
print(c1.info())
