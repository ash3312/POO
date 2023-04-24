class Robot:
    nombre = 0

    def __init__(self, nom, battery) -> None:
        self.nom = nom
        self.battery = battery
        self.nombre +=1

    @property
    def battery(self):
        return self.__battery
    
    @battery.setter
    def battery(self, value):
        if not isinstance(value, int) or value > 100 or value < 0 :
            raise ValueError("value error")
        else:
            self.__battery = value 


    
    def se_deplacer(self, direction):
        if self.battery > 0:
            return self.nom + " va " + direction
    
    def se_recharger(self):
        if self.battery + 10 > 100 :
            raise ValueError("value error")
        return self.battery + 10


class Drone(Robot):
    def __init__(self, nom, battery, range, hasCamera) -> None:
        super().__init__(nom, battery)
        self.range= range
        self.hasCamera = hasCamera

    def se_deplacer(self, direction):
        return self.nom + " va " + direction
    
    def vol_stationnaire(self, alt):
        return alt

class RobotDanseur(Robot):
    def __init__(self, nom, battery, niveau, partenaire = None) -> None:
        super().__init__(nom, battery)
        self.niveau= niveau
        self.__partenaire = partenaire
        self.dances = []
        if partenaire is not None:
            if partenaire.partenaire is not None:
                partenaire.partenaire.partenaire = None
            partenaire.partenaire = self

        
    @property
    def partenaire(self):
        return self.__partenaire
    
    @partenaire.setter
    def partenaire(self, value):
        self.__partenaire = value 

    def add_dance(self, dance):
        self.dances.append(dance)

    def se_deplacer(self, direction):
        return self.nom + " va " + direction
    
    def dancer(self):
        if self.partenaire is None:
            print( self.nom + " Im alone")
            return
        for d1 in self.dances:
            if d1 in self.partenaire.dances:
                print( self.nom +" dances " + d1 + " with " +  self.partenaire.nom )
                break

d1 = RobotDanseur("d1", 20, 1)
d1.add_dance("salsa")
d1.add_dance("dabka")

d2 = RobotDanseur("d2", 20, 1, d1)
d2.add_dance("dabka")
# d2.dancer()
# d1.dancer()

d3 = RobotDanseur("d3", 20, 1, d1)
d3.add_dance("dabka")

d1.dancer()
d2.dancer()
d3.dancer()