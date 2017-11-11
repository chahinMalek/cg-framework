"""
    Representation of 2D point
"""

from collections import namedtuple


class Point(namedtuple('Point', ['x', 'y'])):

    def draw(self):
        pass

    def euclidean_dist_squared(self, other: 'Point') -> float:
        return (self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y)

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y
