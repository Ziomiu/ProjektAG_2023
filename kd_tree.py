import numpy as np
import matplotlib.pyplot as plt
from visualizer.main import Visualizer


class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None
        self.upper_right = None
        self.lower_left = None


def partition(arr, left, right, k, idx):
    pi = arr[right][idx]
    i = left - 1

    for j in range(left, right):
        if arr[j][idx] < pi:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_select(arr, left, right, k, idx):
    if left <= right:
        pivot_index = partition(arr, left, right, k, idx)
        if pivot_index == k:
            return
        if pivot_index > k:
            quick_select(arr, left, pivot_index - 1, k, idx)
        else:
            quick_select(arr, pivot_index + 1, right, k, idx)


def find_max(points):
    x = max(points, key=lambda x: x[0])
    y = max(points, key=lambda x: x[1])
    return x[0], y[1]


def find_min(points):
    x = min(points, key=lambda x: x[0])
    y = min(points, key=lambda x: x[1])
    return x[0], y[1]


class KDTree:
    def __init__(self, points, vis=None):
        self.root = self.build(points, 0)
        self.vis = vis
        self.root.upper_right = find_max(points)
        self.root.lower_left = find_min(points)
        self.region(self.root, 0)
        self.result = []
        self.points = points

    def build(self, points, depth):
        n = len(points)
        if n < 1:
            return None
        if n == 1:
            return Node(points[0])

        idx = depth % 2
        mid = n // 2
        quick_select(points, 0, n - 1, mid, idx)
        root = Node(points[mid])
        root.left = self.build(points[:mid], depth + 1)
        root.right = self.build(points[mid + 1:], depth + 1)
        return root

    def region(self, root, depth):
        if root.right is None and root.left is None:
            root.lower_left = None
            root.upper_right = None
            return

        if self.vis is not None:
            if depth % 2 == 0:
                self.vis.add_line_segment(((root.point[0], root.lower_left[1]), (root.point[0], root.upper_right[1])))
                self.vis.show()
            else:
                self.vis.add_line_segment(((root.lower_left[0], root.point[1]), (root.upper_right[0], root.point[1])))
                self.vis.show()

        if root.right is not None:
            if depth % 2 == 0:  # oś x
                root.right.lower_left = (root.point[0], root.lower_left[1])
            else:  # oś y
                root.right.lower_left = (root.lower_left[0], root.point[1])

            root.right.upper_right = root.upper_right
            self.region(root.right, depth + 1)

        if root.left is not None:
            if depth % 2 == 0:
                root.left.upper_right = (root.point[0], root.upper_right[1])
            else:
                root.left.upper_right = (root.upper_right[0], root.point[1])

            root.left.lower_left = root.lower_left
            self.region(root.left, depth + 1)

    def report_subtree(self, root):
        self.result.append(root.point)
        if self.vis is not None:
            self.vis.add_point([root.point])
            self.vis.show()

        if root.left:
            self.report_subtree(root.left)

        if root.right:
            self.report_subtree(root.right)

    def search(self, lower_left, upper_right):
        self.result = []
        if self.vis is not None:
            self.vis.add_polygon(
                (lower_left, (upper_right[0], lower_left[1]), upper_right, (lower_left[0], upper_right[1])))
            self.vis.add_point(self.points, color='green')
            self.vis.show()

        def search_kd_tree(root, ll, ur):
            if root is None:
                return

            if point_inside(root.point, ll, ur):
                self.result.append(root.point)
                if self.vis is not None:
                    self.vis.add_point([root.point], color='red')
                    self.vis.show()

            if root.left is not None:
                if region_inside(root.lower_left, root.upper_right, ll, ur):
                    self.report_subtree(root.left)
                elif region_intersects(root.lower_left, root.upper_right, ll, ur):
                    search_kd_tree(root.left, ll, ur)

            if root.right is not None:
                if region_inside(root.lower_left, root.upper_right, ll, ur):
                    self.report_subtree(root.right)
                elif region_intersects(root.lower_left, root.upper_right, ll, ur):
                    search_kd_tree(root.right, ll, ur)

        search_kd_tree(self.root, lower_left, upper_right)
        return self.result


def point_inside(point, ll, ur):
    return ll[0] <= point[0] <= ur[0] and ll[1] <= point[1] <= ur[1]


def region_inside(region_ll, region_ur, ll, ur):
    return point_inside(region_ll, ll, ur) and point_inside(region_ur, ll, ur)


def region_intersects(region_ll, region_ur, ll, ur):
    return (
            point_inside(region_ll, ll, ur)
            or point_inside(region_ur, ll, ur)
            or point_inside(ll, region_ll, region_ur)
            or point_inside(ur, region_ll, region_ur)
            or point_inside((region_ll[0], region_ur[1]), ll, ur)
            or point_inside((ll[0], ur[1]), region_ll, region_ur)
    )
