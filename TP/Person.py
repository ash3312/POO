class Person:
    type = "human"
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


p1 = Person("ashraf", "daood")
print(p1.__dict__)
print(Person.__dict__)