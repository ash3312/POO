import datetime

class Personnage:
    def __init__(self, nom, puissance, pointDeVie) -> None:
        self.nom = nom
        self.puissance = puissance 
        self.pointDeVie= pointDeVie

    def attacker(self, enemmi):
        enemmi.perdrePointDeVie(self.puissance)

    def perdrePointDeVie(self, pointAPerdre):
        self.pointDeVie -= pointAPerdre
        if self.pointDeVie < 0:
            self.pointDeVie = 0

    def est_ko(self):
        return self.pointDeVie == 0
    
    def __str__(self) -> str:
        return f"{self.nom} {self.__class__.__name__}: {self.pointDeVie}"
    

class SuperHeros(Personnage):
    def __init__(self, nom, puissance, pointDeVie, secretNom, etat) -> None:
        super().__init__(nom, puissance, pointDeVie)
        self.secretNom = secretNom
        self.etat = etat
        self.puissanceForte = self.puissance + 10
        self.puissanceNormal = self.puissance

    def __eq__(self,  other) -> bool:
        return self.nom == other.nom
    
    def attacker(self, enemmi):
        if self not in enemmi.heros:
            enemmi.heros.append(self)
        enemmi.perdrePointDeVie(self.puissance * 2)

    def superPowerActive(self):
        self.superPowerfuture = datetime.datetime.now() + datetime.timedelta(seconds=10)

    def utiliser_pouvoir_special(self):
        if datetime.datetime.now() <= self.superPowerfuture:
            self.puissance = self.puissanceForte
        else:
            self.puissance  = self.puissanceNormal


class SuperVilain(Personnage):
    def __init__(self, nom, puissance, pointDeVie, code, but) -> None:
        super().__init__(nom, puissance, pointDeVie)
        self.code = code 
        self.but = but
        self.heros = []


# superHero = SuperHeros("khara",50,100,"kharakbir",True)
#print(superHero.puissance)

# superHero.superPowerActive()

# while True:
#     superHero.utiliser_pouvoir_special()
#     print(superHero.puissance)
#     if superHero.puissance == 50:
#         break

superHero = SuperHeros("khara",50,1000,"kharakbir",True)
print(superHero)
vilain = SuperVilain("vilain",50,1000, "123", "killing")
print(vilain)

superHero.attacker(vilain)
print(superHero)
print(vilain)

superHero.superPowerActive()
superHero.utiliser_pouvoir_special()
superHero.attacker(vilain)
print(superHero)
print(vilain)

print(vilain.heros)