import math


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    # @x.setter
    # def x(self, value):
    #     if not isinstance(value, float) and not isinstance(value, int):
    #         raise ValueError("Value error")
    #     self.__x = value

    @property
    def y(self):
        return self.__y

    # @y.setter
    # def y(self, value):
    #     if not isinstance(value, float) and not isinstance(value, int):
    #         raise ValueError("Value error")
    #     self.__y = value
    #
    def __str__(self):
        return f"({self.x},{self.y})"

    def distance_from_point(self, p):
        return math.hypot(self.x, self.y, p.x, p.y)

    def distance(self, _x, _y):
        return math.hypot(self.x, self.y, _x, _y)


p1 = Point(0, 0)
p2 = Point(1, 1)
print(p1.distance_from_point(p2))
print(p1.distance(1, 1))
