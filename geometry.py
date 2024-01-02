class Point:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def get_tuple(self):
        return tuple((self.x, self.y))

    def x(self):
        return self.x

    def y(self):
        return self.y


class Rectangle:
    def __init__(self, lowerLeft, upperRight):
        self.upperRight = upperRight
        self.lowerLeft = lowerLeft

    def get_tuple(self):
        return (self.lowerLeft, self.upperRight)

    def in_rect(self, point):
        return self.lowerLeft.x <= point.x <= self.upperRight.x and self.lowerLeft.y <= point.y <= self.upperRight.y

    def contain(self, other):
        return (self.lowerLeft.x <= other.lowerLeft.x
                and self.upperRight.x >= other.upperRight.x
                and self.lowerLeft.y <= other.lowerLeft.y
                and self.upperRight.y >= other.upperRight.y)

    def intersect(self, other):
        if self.lowerLeft.x > other.upperRight.x or other.lowerLeft.x > self.upperRight.x:
            return False

        if self.lowerLeft.y > other.upperRight.y or other.lowerLeft.y > self.upperRight.y:
            return False

        else:
            return True
