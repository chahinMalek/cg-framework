"""
    Representation od 2D oriented line segment - with helper methods
"""

from structures.triangle import Triangle
from structures.point import Point
from conf import CENTER


class LineSegment:
    def __init__(self, first: Point, second: Point):
        self.first = first
        self.second = second

    def draw(self, canvas):
        first_x = self.first.x + CENTER
        first_y = -(self.first.y - CENTER)
        second_x = self.second.x + CENTER
        second_y = -(self.second.y - CENTER)

        canvas.create_line(first_x, first_y, second_x, second_y, width=1, fill="blue")

    def __eq__(self, other: 'LineSegment'):
        """
        Determines if two line segments (self and other) are the same
        Args:
            other: Another LineSegment object
        Returns:
            bool: True if line segments are the same, False otherwise
        """
        return self.first == other.first and self.second == other.second

    def does_contain(self, point: Point) -> bool:
        """
        Determines if point "lies" in line segment (self)
        Args:
            point: Point object
        Returns:
            bool: True if point is part of self LineSegment, False otherwise
        """
        return Triangle(self.first, self.second, point).orientation() == 0

    def does_intersect(self, other: 'LineSegment') -> bool:
        """
        Determines if two line segments (self and other) intersect
        Args:
            other: Another LineSegment object
        Returns:
            bool: True if two segments intersect or match. False otherwise
        """
        if self == other:
            return True

        if self.does_contain(other.first) or self.does_contain(other.second):
            return True

        orientation_1 = Triangle(self.first, self.second, other.first).orientation()
        orientation_2 = Triangle(self.first, self.second, other.second).orientation()
        if orientation_1 == orientation_2:
            return False

        orientation_3 = Triangle(other.first, other.second, self.first).orientation()
        orientation_4 = Triangle(other.first, other.second, self.second).orientation()
        if orientation_3 == orientation_4:
            return False

        return True

    def __str__(self):
        return "Line segment: " + str(self.first) + ", " + str(self.second)