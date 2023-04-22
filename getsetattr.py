class Classy:
    pass


obj = Classy()

obj.ashraf = "ashraf"

obj.ass = "ass"
obj.i = 5
obj.majdy = "majdy"

def change(o):
    for item in o.__dict__.keys():
        val = getattr(o, item)
        if (isinstance(val, str)):
            if(val.startswith("a")):
                setattr(o, item, val * 2)


print(obj.__dict__)
change(obj)
print(obj.__dict__)
