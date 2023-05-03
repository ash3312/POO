import random
class Vaisseau:
    def __init__(self, nom, modele, longueur, largeur, hauteur, vitesse=0) -> None:
        self.nom = nom
        self.modele = modele
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.integrite = 100
        self.vitesse = vitesse

    def __str__(self) -> str:
        return f"vaisseau ({self.nom}, {self.modele}, {self.longueur}, {self.largeur}, {self.hauteur}, {self.vitesse} : {self.integrite})"
    
    def accelerer(self, vitesse_supplementaire):
        self.vitesse += vitesse_supplementaire

class Chasseur(Vaisseau):
    def __init__(self, nom, modele, longueur, largeur, hauteur, vitesse, furtif=False) -> None:
        super().__init__(nom, modele, longueur, largeur, hauteur, vitesse)
        self.armes = []
        self.furtif = furtif

    def ajouter_arme(self, arme):
        self.armes.append(arme)

    def afficher_armes(self):
        for a in self.armes:
            print(a, "\t")
    
    def activer_furtivite(self):
        self.furtif = True

    def attaquer(self, vaisseau, arme):
        vaisseau.integrite -= arme.power

    def __str__(self) -> str:
        return super().__str__() + f" {self.furtif}"

class Arme:
    def __init__(self, nom, power) -> None:
        self.nom = nom
        self.power = power
    
    def __str__(self) -> str:
        return f"Arme {self.nom}, {self.power}"

class VaisseauDeCombat(Vaisseau):
    def __init__(self, nom, modele, longueur, largeur, hauteur,vitesse, armure) -> None:
        super().__init__(nom, modele, longueur, largeur, hauteur, vitesse)
        self.armure = armure

    def afficher_armure(self):
        return self.armure
    
    def activer_bouclier(self):
        self.armure += 100

    def __str__(self) -> str:
        return super().__str__() + f" {self.armure}"

class FlotteSpatiale:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.vaisseaux= []

    def ajouter_vaisseau(self, vaisseau):
        self.vaisseaux.append(vaisseau)

    def supprimer_vaisseau(self, vaisseau):
        for i in range(len(self.vaisseaux)):
            if self.vaisseaux[i] == vaisseau:
                del self.vaisseaux[i]
                return
            
    def afficher_vaisseaux(self):
        for v in self.vaisseaux:
            print(v, "\t")

    def attaquer_flotte(self, flotte_cible):
        for v in self.vaisseaux:
            idx = random.randint(0,len(flotte_cible.vaisseaux)-1)
            idx_arm = random.randint(0,len(v.armes)-1)
            v.attaquer(flotte_cible.vaisseaux[idx], v.armes[idx_arm])


# v = Vaisseau("Faucon Millenium", "YT-1300", 100, 50, 200, 1050)

# print(v)
# v.accelerer(100)

# print(v)

# ch = Chasseur("X-wing", "khara1", 100,50,200, 1050)

# a1 = Arme("canons laser", 50)
# a2 = Arme("torpilles à proton", 35)

# ch.ajouter_arme(a1)
# ch.ajouter_arme(a2)

# print(ch)
# ch.afficher_armes()

# ch.activer_furtivite()
# print(ch)

# com = VaisseauDeCombat("Destroyer Stellaire", "c1", 200, 500, 100, 1050, 250)

# print(com)

# com.activer_bouclier()
# print(com)
a1 = Arme("canons laser", 50)
a2 = Arme("torpilles à proton", 35)

floote1 = FlotteSpatiale("Flotte1")

ch1_floote1 = Chasseur("X-wing1_f1", "khara1", 100,50,200, 1050)
ch1_floote1.ajouter_arme(a1)
ch1_floote1.ajouter_arme(a2)

ch2_floote1 = Chasseur("X-wing2_f1", "khara1", 100,50,200, 1050)
ch2_floote1.ajouter_arme(a1)
ch2_floote1.ajouter_arme(a2)

floote1.ajouter_vaisseau(ch1_floote1)
floote1.ajouter_vaisseau(ch2_floote1)



floote2 = FlotteSpatiale("Flotte2")

ch1_floote2 = Chasseur("X-wing1_f2", "khara1", 100,50,200, 1050)
ch1_floote2.ajouter_arme(a1)
ch1_floote2.ajouter_arme(a2)

ch2_floote2 = Chasseur("X-wing2_f2", "khara1", 100,50,200, 1050)
ch2_floote2.ajouter_arme(a1)
ch2_floote2.ajouter_arme(a2)

floote2.ajouter_vaisseau(ch1_floote2)
floote2.ajouter_vaisseau(ch2_floote2)


floote1.afficher_vaisseaux()
floote2.afficher_vaisseaux()

print("*" * 20)

floote1.attaquer_flotte(floote2)

floote1.afficher_vaisseaux()
floote2.afficher_vaisseaux()

print("*" * 20)

floote2.attaquer_flotte(floote1)

floote1.afficher_vaisseaux()
floote2.afficher_vaisseaux()