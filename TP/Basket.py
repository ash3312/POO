class Joueur:

    def __init__(self, nom, age, taille, poste) -> None:
        self.nom = nom
        self.age = age
        self.taille = taille
        self.poste = poste

    def __str__(self) -> str:
        return f"{self.nom}: {self.age} {self.taille} {self.poste}"
    
class VoleyPlayer(Joueur):
    def __init__(self, nom, age, taille, poste, sex) -> None:
        super().__init__(nom, age, taille, poste)
        self.sex = sex

class Equipe:
    def __init__(self, nom, joueurs=None) -> None:
        self.nom = nom
        if joueurs is None:
            self.joueurs = []
        else:
            self.joueurs = joueurs

    def add_joueur(self, joueur):
        if isinstance(joueur ,Joueur):
            if joueur not in self.joueurs:
                self.joueurs.append(joueur)
        return self

    def remove_joueur(self, joueur):
       if isinstance(joueur ,Joueur):
            for i in range(len(self.joueurs)) :
                if joueur == self.joueurs[i]:
                    del self.joueurs[i]
                    return self

    def moyenne_age(self):
        sum = 0
        for joueur in self.joueurs:
            sum += joueur.age
        return sum / len(self.joueurs)

    def joueur_plus_grand(self):
        max = self.joueurs[0]
        for joueur in self.joueurs:
            if joueur.taille > max.taille:
                max = joueur
        return max
    
    def joueur_plus_petit(self):
        min = self.joueurs[0]
        for joueur in self.joueurs:
            if joueur.taille < min.taille:
                min = joueur
        return min

    def joueur_au_poste(self, poste):
        for joueur in self.joueurs:
            if joueur.poste == poste:
                return joueur
        return None
    
j1 = Joueur("a", 20, 150, "a1")
j2 = Joueur("b", 25, 160, "b1")
j3 = Joueur("c", 30, 180, "c1")

e = Equipe("shit", [j1])

e.add_joueur(j2).add_joueur(j3)

for j in e.joueurs:
    print(j)
print("*" *10)
print(e.moyenne_age())
print(e.joueur_plus_grand())
print(e.joueur_plus_petit())
print(e.joueur_au_poste("c1"))

print("*" *10)

e.remove_joueur(j3).remove_joueur(j2)

for j in e.joueurs:
    print(j)

print("*" *10)
e2 = Equipe("Salamieh")
ibrahim = VoleyPlayer("hendawi", 30, 180, "attackeur", "t")
ali = VoleyPlayer("hamwai", 28, 150, "passeur", "t")

e2.add_joueur(ibrahim).add_joueur(ali)

for j in e2.joueurs:
    print(j)

print("*" *10)
print(e2.moyenne_age())
print(e2.joueur_plus_grand())
print(e2.joueur_plus_petit())
print(e2.joueur_au_poste("passeur"))