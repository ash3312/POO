import random
import time

def generate_ip():
    return str.join("." , [str(random.randint(0,255)) for _ in range(4)])


traduction = {"Hello" : "salut", "name" : "nom", "good morning" : "bonjour" }


class Client:
    def __init__(self) -> None:
        self.ip = generate_ip()
        self.msgs = []

    def send(self, other):
        keys = list(traduction.keys())
        idx = random.randint(0, len(keys)-1)
        msg = keys[idx]
        other.msgs.append(msg)
        print(self.ip, "send:" , msg)

    def receive(self):
        msg = traduction.get(self.msgs[-1])
       
        print(self.ip, "receive:", msg)


client1 = Client()
client2 = Client()


while True:
    client1.send(client2)
    client2.receive()
    time.sleep(5)