from geometry import *
from visualizer.main import Visualizer


class QuadNodeVis:
    def __init__(self, rec, type):
        self.rec = rec
        self.points = []
        self.divided = False
        self.right_upper = None
        self.right_lower = None
        self.left_lower = None
        self.left_upper = None
        self.type = type

    def divide(self, vis, lines):
        lowerleft = self.rec.lowerLeft
        upperright = self.rec.upperRight
        half_x = (lowerleft.x + upperright.x) / 2
        half_y = (lowerleft.y + upperright.y) / 2
        lines.append(((lowerleft.x, half_y), (upperright.x, half_y)))
        lines.append(((half_x, lowerleft.y), (half_x, upperright.y)))
        vis.add_line_segment(((lowerleft.x, half_y), (upperright.x, half_y)))
        vis.add_line_segment(((half_x, lowerleft.y), (half_x, upperright.y)))

        lower_left_rect = Rectangle(lowerleft, Point((half_x, half_y)))
        upper_left_rect = Rectangle(Point((lowerleft.x, half_y)), Point((half_x, upperright.y)))
        lower_right_rect = Rectangle(Point((half_x, lowerleft.y)), Point((upperright.x, half_y)))
        upper_right_rect = Rectangle(Point((half_x, half_y)), upperright)

        self.right_upper = QuadNodeVis(upper_right_rect, 0)
        self.right_lower = QuadNodeVis(lower_right_rect, 1)
        self.left_lower = QuadNodeVis(lower_left_rect, 2)
        self.left_upper = QuadNodeVis(upper_left_rect, 3)

    def add(self, point, vis, lines):
        vis.add_point(point.get_tuple(), color="yellow")
        if not self.rec.in_rect(point):
            pol = vis.add_polygon(((self.rec.upperRight.x, self.rec.upperRight.y),
                                   (self.rec.upperRight.x, self.rec.lowerLeft.y),
                                   (self.rec.lowerLeft.x, self.rec.lowerLeft.y),
                                   (self.rec.lowerLeft.x, self.rec.upperRight.y)), alpha=0.3, color="red")
            vis.remove_figure(pol)
            return False
        pol = vis.add_polygon(((self.rec.upperRight.x, self.rec.upperRight.y),
                               (self.rec.upperRight.x, self.rec.lowerLeft.y),
                               (self.rec.lowerLeft.x, self.rec.lowerLeft.y),
                               (self.rec.lowerLeft.x, self.rec.upperRight.y)), alpha=0.3, color="green")
        vis.remove_figure(pol)
        self.points.append(point)
        if len(self.points) > 1:
            if not self.divided:
                pol = vis.add_polygon(((self.rec.upperRight.x, self.rec.upperRight.y),
                                       (self.rec.upperRight.x, self.rec.lowerLeft.y),
                                       (self.rec.lowerLeft.x, self.rec.lowerLeft.y),
                                       (self.rec.lowerLeft.x, self.rec.upperRight.y)), alpha=0.3, color="yellow")
                vis.remove_figure(pol)
                self.divide(vis, lines)
                self.divided = True
                vis.add_point(point.get_tuple(), color="blue")
                for el in self.points:
                    if self.right_upper.add(el, vis, lines):
                        continue
                    if self.right_lower.add(el, vis, lines):
                        continue
                    if self.left_lower.add(el, vis, lines):
                        continue
                    if self.left_upper.add(el, vis, lines):
                        continue
            else:
                if self.right_upper.add(point, vis, lines):
                    vis.add_point(point.get_tuple(), color="green")
                    return True
                if self.right_lower.add(point, vis, lines):
                    vis.add_point(point.get_tuple(), color="green")
                    return True
                if self.left_lower.add(point, vis, lines):
                    vis.add_point(point.get_tuple(), color="green")
                    return True
                if self.left_upper.add(point, vis, lines):
                    vis.add_point(point.get_tuple(), color="green")
                    return True
        vis.add_point(point.get_tuple(), color="green")
        return True


class QuadTreeVis:
    def __init__(self, rect, points, visbuild, visfind):
        self.rect = rect
        self.node = QuadNodeVis(rect, -1)
        self.visbuild = visbuild
        self.visfind = visfind
        lines = []
        self.insert_all(points, lines)
        self.result = []
        self.visfind.add_point(points)
        self.visfind.add_line_segment(lines)

    def insert(self, point, lines):
        self.node.add(point, self.visbuild, lines)

    def insert_all(self, points, lines):
        points = list(map(Point, points))
        for point in points:
            self.insert(point, lines)

    def _find(self, rect, node):
        if node.type == -1:
            self.visfind.add_line_segment(
                ((rect.upperRight.x, rect.upperRight.y), (rect.upperRight.x, rect.lowerLeft.y)), color="black")
            self.visfind.add_line_segment(((rect.upperRight.x, rect.lowerLeft.y), (rect.lowerLeft.x, rect.lowerLeft.y)),
                                          color="black")
            self.visfind.add_line_segment(((rect.lowerLeft.x, rect.lowerLeft.y), (rect.lowerLeft.x, rect.upperRight.y)),
                                          color="black")
            self.visfind.add_line_segment(
                ((rect.lowerLeft.x, rect.upperRight.y), (rect.upperRight.x, rect.upperRight.y)), color="black")
            self.result = []
        else:
            pol = self.visfind.add_polygon(((node.rec.upperRight.x, node.rec.upperRight.y),
                                            (node.rec.upperRight.x, node.rec.lowerLeft.y),
                                            (node.rec.lowerLeft.x, node.rec.lowerLeft.y),
                                            (node.rec.lowerLeft.x, node.rec.upperRight.y)), alpha=0.3, color="yellow")
            self.visfind.remove_figure(pol)
        if not rect.intersect(node.rec):
            pol = self.visfind.add_polygon(((node.rec.upperRight.x, node.rec.upperRight.y),
                                            (node.rec.upperRight.x, node.rec.lowerLeft.y),
                                            (node.rec.lowerLeft.x, node.rec.lowerLeft.y),
                                            (node.rec.lowerLeft.x, node.rec.upperRight.y)), alpha=0.3, color="red")
            self.visfind.remove_figure(pol)
            return []
        if rect.contain(node.rec):
            pol = self.visfind.add_polygon(((node.rec.upperRight.x, node.rec.upperRight.y),
                                            (node.rec.upperRight.x, node.rec.lowerLeft.y),
                                            (node.rec.lowerLeft.x, node.rec.lowerLeft.y),
                                            (node.rec.lowerLeft.x, node.rec.upperRight.y)), alpha=0.3, color="green")
            for el in node.points:
                self.visfind.add_point(el.get_tuple(), color="green")
            self.visfind.remove_figure(pol)
            return node.points
        if node.divided:
            pol = self.visfind.add_polygon(((node.rec.upperRight.x, node.rec.upperRight.y),
                                                (node.rec.upperRight.x, node.rec.lowerLeft.y),
                                                (node.rec.lowerLeft.x, node.rec.lowerLeft.y),
                                                (node.rec.lowerLeft.x, node.rec.upperRight.y)), alpha=0.3,
                                               color="orange")
            self.visfind.remove_figure(pol)
            self.result.extend(self._find(rect, node.right_upper))
            self.result.extend(self._find(rect, node.right_lower))
            self.result.extend(self._find(rect, node.left_lower))
            self.result.extend(self._find(rect, node.left_upper))
            if node.type != -1:
                return []
        else:
            if node.type != -1:
                pol = self.visfind.add_polygon(((node.rec.upperRight.x, node.rec.upperRight.y),
                                                (node.rec.upperRight.x, node.rec.lowerLeft.y),
                                                (node.rec.lowerLeft.x, node.rec.lowerLeft.y),
                                                (node.rec.lowerLeft.x, node.rec.upperRight.y)), alpha=0.3,
                                               color="orange")
                tab = [point for point in node.points if rect.in_rect(point)]
                for el in tab:
                    self.visfind.add_point(el.get_tuple(), color="green")
                self.visfind.remove_figure(pol)
                return tab
        return self.result

    def find(self, rect):
        self.result = []
        return self._find(rect, self.node)
