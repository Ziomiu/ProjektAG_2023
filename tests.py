import random
from kd_tree import *
from quadtree import *


def generate_uniform_points(left, right, down, up, n=10 ** 5):
    result = set()
    while len(result) < n:
        result.add((random.randint(left, right), (random.randint(down, up))))
    return list(result)


def run_tests(n, left, right, down, up, region):
    for i in range(1000):
        points = generate_uniform_points(left, right, down, up, n)
        root = KDTree(points)
        result = root.search(region[0], region[1])
        qtree = QuadTree(Rectangle(Point((left, down)), Point((right, up))),
                         points)
        rect = Rectangle(Point(region[0]), Point(region[1]))
        result2 = qtree.find(rect, qtree.node)
        result2 = list(map(Point.get_tuple, result2))
        if set(result) == set(result2):
            print("Test " + str(i) + " zaliczony")
        else:
            print(points)
            print(result)
            print(result2)
            print("Test " + str(i) + " nie zaliczony")
            break
