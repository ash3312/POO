import random
import time

class Bear:
    def __str__(self) -> str:
        return "Bear"

class Fish:
    def __str__(self) -> str:
        return "Fish"

def choose():
    r = random.randint(0,2)
    match r:
        case 0:
            return Bear()
        case 1:
            return Fish()
        case 2:
            return None

animals = [ choose() for _ in range(10) ]

adj = [ None for _ in range(10) ]

def show_list(l, name):
    text = ""
    for a in l:
        text += a.__str__() + " "
    print(name + ": "+ text)
    

while True:
    show_list(animals, "animals")
    show_list(adj, "adj")
    print("*" * 20)
    if (None not in animals and None not in adj):
        break

    if all(x is None for x in animals ):
        break
    
    time.sleep(0.01)
    r1 = random.randint(0,10-1)
    print("r1", r1)
    animal = animals[r1]
    # block None type to move
    if animal is None:
        continue

    r2 = random.randint(0,10-1)
    print("r2", r2)
    if adj[r2] is None :
        adj[r2] = animal
        animals[r1] = None
    elif isinstance(adj[r2], type(animal)):
        for i in range(len(animals)):
            if animals[i] is None:
                animals[i] = type(animal)()
                break