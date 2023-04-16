class Animal1:
    def __init__(self):
        self.__age = 0
        print("animal created")
    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

animal = Animal1()
print(animal.get_age())
animal.set_age(10)
print(animal.get_age())
