import random
from kd_tree import *
from quadtree_with_vis import *
from quadtree import *
import time


def test_uniform_points(n):
    points = set()
    while len(points) < n:
        points.add((np.random.uniform(0, 100), (np.random.uniform(0, 100))))
    region = ((0, 0), (50, 50))
    points = list(points)
    kd_build_start = time.time()
    root = KDTree(points)
    kd_build_end = time.time()
    kd_find_start = time.time()
    result = root.search(region[0], region[1])
    kd_find_end = time.time()
    qd_build_start = time.time()
    qtree = QuadTree(Rectangle(Point((0, 0)), Point((100, 100))),
                     points)
    qd_build_end = time.time()
    rect = Rectangle(Point(region[0]), Point(region[1]))
    qd_find_start = time.time()
    result2 = qtree.find(rect)
    qd_find_end = time.time()
    result2 = list(map(Point.get_tuple, result2))
    if set(result) == set(result2):
        print("Test uniform zaliczony")
        print("Czas budowy kdtree: " + str(round(kd_build_end - kd_build_start, 5)) + " s")
        print("Czas budowy quadtree: " + str(round(qd_build_end - qd_build_start, 5)) + " s")
        print("Czas znalezienia punktów w kdtree: " + str(round(kd_find_end - kd_find_start, 5)) + " s")
        print("Czas znalezienia punktów w quadtree:  " + str(round(qd_find_end - qd_find_start, 5)) + " s")
        print("-----------------------------------------------")
    else:
        print("Test uniform nie zaliczony")
        print("Czas budowy kdtree: " + str(round(kd_build_end - kd_build_start, 2)))
        print("Czas budowy quadtree: " + str(round(qd_build_end - qd_build_start, 2)))
        print("Czas znalezienia punktów w kdtree: " + str(round(kd_find_end - kd_find_start, 2)))
        print("Czas znalezienia punktów w quadtree:  " + str(round(qd_find_end - qd_find_start, 2)))


def test_rectangle_points(n):
    points = []
    for i in range(n // 4):
        point = (np.random.uniform(0, 100), 0)
        points.append(point)
    for i in range(n // 4):
        point = (0, np.random.uniform(0, 100))
        points.append(point)
    for i in range(n // 4):
        point = (100, np.random.uniform(0, 100))
        points.append(point)
    for i in range(n // 4 + n % 4):
        point = (np.random.uniform(0, 100), 100)
        points.append(point)
    region = ((0, 0), (100, 100))
    kd_build_start = time.time()
    root = KDTree(points)
    kd_build_end = time.time()
    kd_find_start = time.time()
    result = root.search(region[0], region[1])
    kd_find_end = time.time()
    qd_build_start = time.time()
    qtree = QuadTree(Rectangle(Point((0, 0)), Point((100, 100))),
                     points)
    qd_build_end = time.time()
    rect = Rectangle(Point(region[0]), Point(region[1]))
    qd_find_start = time.time()
    result2 = qtree.find(rect)
    qd_find_end = time.time()
    result2 = list(map(Point.get_tuple, result2))
    if set(result) == set(result2):
        print("Test rectangle zaliczony")
        print("Czas budowy kdtree: " + str(round(kd_build_end - kd_build_start, 5)) + " s")
        print("Czas budowy quadtree: " + str(round(qd_build_end - qd_build_start, 5)) + " s")
        print("Czas znalezienia punktów w kdtree: " + str(round(kd_find_end - kd_find_start, 5)) + " s")
        print("Czas znalezienia punktów w quadtree:  " + str(round(qd_find_end - qd_find_start, 5)) + " s")
        print("-----------------------------------------------")
    else:
        print("Test rectangle nie zaliczony")
        print("Czas budowy kdtree: " + str(round(kd_build_end - kd_build_start, 2)))
        print("Czas budowy quadtree: " + str(round(qd_build_end - qd_build_start, 2)))
        print("Czas znalezienia punktów w kdtree: " + str(round(kd_find_end - kd_find_start, 2)))
        print("Czas znalezienia punktów w quadtree:  " + str(round(qd_find_end - qd_find_start, 2)))


def test_lines_points(n):
    points = []
    for i in range(n // 4):
        point = (20, np.random.uniform(0, 100))
        points.append(point)
    for i in range(n // 4):
        point = (40, np.random.uniform(0, 100))
        points.append(point)
    for i in range(n // 4):
        point = (60, np.random.uniform(0, 100))
        points.append(point)
    for i in range(n // 4 + n % 4):
        point = (80, np.random.uniform(0, 100))
        points.append(point)
    region = ((25, 25), (75, 75))
    kd_build_start = time.time()
    root = KDTree(points)
    kd_build_end = time.time()
    kd_find_start = time.time()
    result = root.search(region[0], region[1])
    kd_find_end = time.time()
    qd_build_start = time.time()
    qtree = QuadTree(Rectangle(Point((0, 0)), Point((100, 100))),
                     points)
    qd_build_end = time.time()
    rect = Rectangle(Point(region[0]), Point(region[1]))
    qd_find_start = time.time()
    result2 = qtree.find(rect)
    qd_find_end = time.time()
    result2 = list(map(Point.get_tuple, result2))
    if set(result) == set(result2):
        print("Test lines zaliczony")
        print("Czas budowy kdtree: " + str(round(kd_build_end - kd_build_start, 5)) + " s")
        print("Czas budowy quadtree: " + str(round(qd_build_end - qd_build_start, 5)) + " s")
        print("Czas znalezienia punktów w kdtree: " + str(round(kd_find_end - kd_find_start, 5)) + " s")
        print("Czas znalezienia punktów w quadtree:  " + str(round(qd_find_end - qd_find_start, 5)) + " s")
        print("-----------------------------------------------")
    else:
        print("Test lines nie zaliczony")
        print("Czas budowy kdtree: " + str(round(kd_build_end - kd_build_start, 2)))
        print("Czas budowy quadtree: " + str(round(qd_build_end - qd_build_start, 2)))
        print("Czas znalezienia punktów w kdtree: " + str(round(kd_find_end - kd_find_start, 2)))
        print("Czas znalezienia punktów w quadtree:  " + str(round(qd_find_end - qd_find_start, 2)))


def test_groups_points(n):
    points = []
    for i in range(n // 4):
        point = (np.random.uniform(0, 20), np.random.uniform(0, 25))
        points.append(point)
    for i in range(n // 4):
        point = (np.random.uniform(40, 60), np.random.uniform(50, 75))
        points.append(point)
    for i in range(n // 4):
        point = (np.random.uniform(0, 20), np.random.uniform(50, 75))
        points.append(point)
    for i in range(n // 4 + n % 4):
        point = (np.random.uniform(60, 80), np.random.uniform(25, 50))
        points.append(point)
    region = ((25, 25), (75, 75))
    kd_build_start = time.time()
    root = KDTree(points)
    kd_build_end = time.time()
    kd_find_start = time.time()
    result = root.search(region[0], region[1])
    kd_find_end = time.time()
    qd_build_start = time.time()
    qtree = QuadTree(Rectangle(Point((0, 0)), Point((100, 100))),
                     points)
    qd_build_end = time.time()
    rect = Rectangle(Point(region[0]), Point(region[1]))
    qd_find_start = time.time()
    result2 = qtree.find(rect)
    qd_find_end = time.time()
    result2 = list(map(Point.get_tuple, result2))
    if set(result) == set(result2):
        print("Test groups zaliczony")
        print("Czas budowy kdtree: " + str(round(kd_build_end - kd_build_start, 5)) + " s")
        print("Czas budowy quadtree: " + str(round(qd_build_end - qd_build_start, 5)) + " s")
        print("Czas znalezienia punktów w kdtree: " + str(round(kd_find_end - kd_find_start, 5)) + " s")
        print("Czas znalezienia punktów w quadtree:  " + str(round(qd_find_end - qd_find_start, 5)) + " s")
        print("-----------------------------------------------")
    else:
        print("Test groups nie zaliczony")
        print("Czas budowy kdtree: " + str(round(kd_build_end - kd_build_start, 2)))
        print("Czas budowy quadtree: " + str(round(qd_build_end - qd_build_start, 2)))
        print("Czas znalezienia punktów w kdtree: " + str(round(kd_find_end - kd_find_start, 2)))
        print("Czas znalezienia punktów w quadtree:  " + str(round(qd_find_end - qd_find_start, 2)))


def run_tests(n):
    test_uniform_points(n)
    test_rectangle_points(n)
    test_groups_points(n)
    test_lines_points(n)
