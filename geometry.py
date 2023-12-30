import numpy as np


class Point:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    # Funkcja zwracajaca punkt jako krotke
    def get_tuple(self):
        return tuple((self.x, self.y))

    # Funkcja zwracajaca punkt lanuch znakow
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def x(self):
        return self.x

    def y(self):
        return self.y


class Rectangle:
    # Konstruktor klasy przyjmuje punkty
    def __init__(self, lowerLeft, upperRight, ):
        self.upperRight = upperRight
        self.lowerLeft = lowerLeft

    # Funkcja zwracajaca lancuch znakow
    def __str__(self):
        return str(self.lowerLeft) + ', ' + str(self.upperRight);

    # Funkcja zwracajaca obszar jako wierzcholki
    def get_tuple(self):
        return (self.lowerLeft, self.upperRight)

    # Funkcja sprawdzajaca czy punkt nalezy do prostokata
    def in_scope(self, point):
        return self.lowerLeft.x <= point.x <= self.upperRight.x and self.lowerLeft.y <= point.y <= self.upperRight.y

    # Funkcja sprawdzajaca, czy inny prostokat zawiera sie w danym
    def contain(self, other):
        return (self.lowerLeft.x <= other.lowerLeft.x
                and self.upperRight.x >= other.upperRight.x
                and self.lowerLeft.y <= other.lowerLeft.y
                and self.upperRight.y >= other.upperRight.y)

    # Funkcja sprawdzajaca czy dwa prostokaty maja przeciecie
    def intersect(self, other):
        if self.lowerLeft.x > other.upperRight.x or other.lowerLeft.y > self.upperRight.y:
            return False

        if self.lowerLeft.y > other.upperRight.y or other.lowerLeft.y > self.upperRight.y:
            return False

        else:
            return True

    # Funkcja wczytująca nowe dane
    def load(self, lowerleft, upperright):
        self.upperRight = upperright
        self.lowerLeft = lowerleft
