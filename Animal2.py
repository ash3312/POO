class Animal2:
    def __init__(self):
        self.__age = 0
        print("animal created")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

animal = Animal2()
print(animal.age)
animal.age = 10
print(animal.age)
