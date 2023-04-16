class Animal:
    def __init__(self):
        self.__age = 0
        print("animal created")
    def growUp(self):
        self.__age +=1

animal = Animal()
animal.growUp()
print(animal._Animal__age)
