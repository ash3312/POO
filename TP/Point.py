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


# p1 = Point(0, 0)
# p2 = Point(1, 1)
# print(p1.distance_from_point(p2))
# print(p1.distance(1, 1))


class Triangle:
    def __init__(self, p1, p2, p3) -> None:
        if not isinstance(p1, Point) or not isinstance(p2, Point) or not isinstance(p2, Point):
            raise TypeError("Should be points")
        self.__points = [p1, p2, p3]

    def perimeter(self):
        somme = 0
        for t in self.__points:
            for tt in self.__points:
              if t != tt:
                somme +=  t.distance_from_point(tt)
        return somme / 2


tr = Triangle(Point(0,0), Point(1,0), Point(0,1))
print(tr.perimeter())