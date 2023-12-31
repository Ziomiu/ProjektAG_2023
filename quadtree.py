from geometry import *


class QuadNode:
    def __init__(self, rec, type):
        self.rec = rec
        self.points = []
        self.divided = False
        self.right_upper = None
        self.right_lower = None
        self.left_lower = None
        self.left_upper = None
        self.type = type

    def divide(self):
        lowerleft = self.rec.lowerLeft
        upperright = self.rec.upperRight
        half_x = (lowerleft.x + upperright.x) / 2
        half_y = (lowerleft.y + upperright.y) / 2

        lower_left_rect = Rectangle(lowerleft, Point((half_x, half_y)))
        upper_left_rect = Rectangle(Point((lowerleft.x, half_y)), Point((half_x, upperright.y)))
        lower_right_rect = Rectangle(Point((half_x, lowerleft.y)), Point((upperright.x, half_y)))
        upper_right_rect = Rectangle(Point((half_x, half_y)), upperright)

        self.right_upper = QuadNode(upper_right_rect, 0)
        self.right_lower = QuadNode(lower_right_rect, 1)
        self.left_lower = QuadNode(lower_left_rect, 2)
        self.left_upper = QuadNode(upper_left_rect, 3)

    def add(self, point):
        if not self.rec.in_scope(point):
            return False
        self.points.append(point)
        if len(self.points) > 1:
            if not self.divided:
                self.divide()
                self.divided = True
                for el in self.points:
                    if self.right_upper.add(el):
                        continue
                    if self.right_lower.add(el):
                        continue
                    if self.left_lower.add(el):
                        continue
                    if self.left_upper.add(el):
                        continue
            else:
                if self.right_upper.add(point):
                    return True
                if self.right_lower.add(point):
                    return True
                if self.left_lower.add(point):
                    return True
                if self.left_upper.add(point):
                    return True
        return True


class QuadTree:
    def __init__(self, rect, points):
        self.rect = rect
        self.node = QuadNode(rect, -1)
        self.insert_all(points)
        self.result = []

    def insert(self, point):
        self.node.add(point)

    def insert_single(self, point):
        point = Point(point)
        self.insert(point)

    def insert_all(self, points):
        points = list(map(Point, points))
        for point in points:
            self.insert(point)

    def _find(self, rect, node):
        if not rect.intersect(node.rec):
            return []
        if rect.contain(node.rec):
            return node.points
        if node.divided:
            self.result.extend(self._find(rect, node.right_upper))
            self.result.extend(self._find(rect, node.right_lower))
            self.result.extend(self._find(rect, node.left_lower))
            self.result.extend(self._find(rect, node.left_upper))
            if node.type != -1:
                return []
        else:
            if node.type != -1:
                tab = [point for point in node.points if rect.in_scope(point)]
                return tab
        return self.result

    def find(self, rect, node):
        self.result = []
        return self._find(rect, node)
