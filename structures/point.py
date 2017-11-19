"""
    Representation of 2D point
"""

from collections import namedtuple
from tkinter import Canvas
from conf import CENTER

from numpy import inf

# TODO write docs
class Point(namedtuple('Point', ['x', 'y'])):


    def draw(self, canvas: Canvas):
        x = self.x + CENTER
        y = -(self.y - CENTER)
        canvas.create_line(x - 1, y - 1, x + 1, y + 1, width=3, fill="red")

    def euclidean_dist_squared(self, other: 'Point') -> float:
        return (self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y)

    def get_tan(self, other: 'Point') -> tuple:
        """

        Args:
            point:

        Returns:

        """
        distance = self.euclidean_dist_squared(other)

        if self.x == other.x:
            tan = -inf
        else:
            tan = (self.y - other.y) / (self.x - other.x)

        if self.y == other.y:
            distance *= -1

        return tan, distance

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y

    def cmp_by_y_then_x(self, other: 'Point'):
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x

    def slope(self, other: 'Point'):
        return 1.0 * (self.y - other.y) / (self.x - other.x) if self.x != other.x else float('inf')

