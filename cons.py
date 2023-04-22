class One:
    __par = 5
    def __init__(self):
        print("OK")
    def __met (self):
        print("met")

one = One()

one.__init__()

one._One__met()
# one._One__init__() not working

print(one._One__par)