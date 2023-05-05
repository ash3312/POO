class Flower:
    def __init__(self, nom, petals, price) -> None:
        self.nom = nom
        self.petals = petals 
        self.price = price

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def petals(self):
        return self.__petals

    @petals.setter
    def petals(self, value):
        if isinstance(value, int):
            self.__petals = value
        else:
            raise ValueError("should be int")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, float):
            self.__price = value
        else:
            raise ValueError("should be float")
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.nom} {self.petals} {self.price}"
    
f1 = Flower("jouri", 1000, 12.5)
print(f1)