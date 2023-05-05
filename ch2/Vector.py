class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        if isinstance(d, int):
            self._coords = [0] * d

        else:
            try:
                iter(d)
            except TypeError as te:
                raise ValueError("either int or a iterable")

        """Create a d-dimensional vector of zeros or based on the iterable."""

        try:  # check if d_or_iter is an integer
            d = int(d)
            self._coords = [0] * d
        except TypeError:  # d_or_iter is not an integer, assume it's an iterable
            self._coords = [float(x) for x in d]

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector.”"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on len method
            raise ValueError(" dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self, other):
        """Return sub of two vectors."""
        if len(self) != len(other):  # relies on len method
            raise ValueError(" dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __mul__(self, other):
        # """Return mul of no vector times."""
        # result = Vector(len(self))
        # for j in range(len(self)):
        #     result[j] = self[j] * no
        # return result
        """Return sub of two vectors."""
        if len(self) != len(other):  # relies on len method
            raise ValueError(" dimensions must agree")
        dot = 0
        for j in range(len(self)):
            dot += self[j] * other[j]
        return dot
    

    def __rmul__(self, no):
        return self.__mul__(no)
    
    def __neg__(self):
        """Return neg of vector."""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = - self[j]
        return result
    
    def __str__ (self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>' # adapt list representation


v1 = Vector(2)
#v1.__setitem__(0,5)
v1[0] =5
#v1.__setitem__(1,6)
v1[1] =6

v2 = Vector(2)
#v2.__setitem__(0,4)
v2[0] =4
#v2.__setitem__(1,10)
v2[1] =10

v3 = v1 + v2
print(v3)

# v4 = v3 *3
# print(v4)

# v5 = 3*  v3
# print(v5)

print(v1 * v2)


viter = Vector([5,3,5])
print(viter + viter)