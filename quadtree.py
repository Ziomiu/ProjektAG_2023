from geometry import *


# Klasa odpowiada za wezel drzewa
class Node:
    #Konstruktro przyjumje boki obszaru, rodzica, oraz numer poddrzewa (root bedzie miec -1)
    def __init__(self, max_y, min_x, miny, max_x, par=None, typ=-1):
        self.parent = par
        self.max_y = max_y
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = miny
        self.half_x = (self.max_x + self.min_x) / 2
        self.half_y = (self.max_y + self.min_y) / 2
        self.children = [None for _ in range(4)]
        self.point = None
        self.type = typ
        self.childrencount = 0

    # Dodawanie poddrzewa
    def add_child(self, num, other):
        self.children[num] = other
        self.childrencount += 1

    # Znajdywanie poddrzewa
    def get_child(self, num):
        return self.children[num]
