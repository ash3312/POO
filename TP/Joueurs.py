class Joueur:
    nombre = 0
    def __init__(self, nom, age, score, niveau):
        self.nom = nom
        self.age = age
        self.score = score
        self.niveau = niveau
        Joueur.nombre +=1

    def __str__(self):
        return f"{self.nom} {self.age} {self.niveau} {self.score}"
    
    def augmenter_score(self, point):
        self.score += point

class JoueurExpert(Joueur, object):
    def __init__(self, nom, age, score, niveau, bonus):
        super().__init__(nom, age, score, niveau)
        self.bonus = bonus

    def __str__(self):
        return super().__str__() + f" {self.bonus}"

    def afficher_bonus(self):
        return self.bonus
    
j1 = Joueur("majdy", 40, 0, 1)
print(j1)
print(j1.__dict__)

j2 = JoueurExpert("majdy", 40, 0, 1, 10)
print(j2)
print(j2.__dict__)

print(JoueurExpert.__bases__)

for cls in JoueurExpert.__bases__:
    print(cls.__name__)