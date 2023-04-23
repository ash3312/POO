# x = 5
# y = 5
#
# print(id(x))
# print(id(y))
# print(x == y)
# print(x is y)



# x = "txt"
# y = "txt"
#
#
# print(x == y)
# print(x is y)
#
# y = y +' '
# print(x == y)
# print(x is y)

l1 = list("1")
l2 = list("1")
print(id(l1))
print(id(l2))
print(l1 is l2)


class V:
    pass

v1= V()
v2= V()

print(v1 is v2)