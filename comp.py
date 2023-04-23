class Voiture:

    def __init__(self, obj):
        obj.do()


class Ext:
    def __init__(self, msg):
        self.msg = msg

    def do(self):
        print(self.msg)


ext = Ext("ext1")
car = Voiture(ext)

car1 = Voiture(Ext("ext2"))
