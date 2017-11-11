"""
    Representation od 2D oriented line segment - with helper methods
"""

from triangle import Triangle
from point import Point


class LineSegment:
    def __init__(self, first: Point, second: Point):
        self.first = first
        self.second = second

    def draw(self):
        pass

    def __eq__(self, other: 'LineSegment'):
        """
            Determines if self is same as other.
        Args:
            other: Another lineSegment object

        Returns:
            bool: True if line segments are the same, False otherwise
        """
        return self.first == other.first and self.second == other.second

    def contains_point(self, point: Point) -> bool:
        """
            Determines if point "lies" in self
        Args:
            point: Point object

        Returns:
            bool: True if point is part of self LineSegment, False otherwise
        """
        return Triangle(self.first, self.second, point).orientation() == 0

    def does_intersect(self, other: 'LineSegment') -> bool:
        """
        Determines if self intersects with other.
        Args:
            other: Another LineSegment object

        Returns:
            bool: True if two segments instersect or match. False otherwise
        """
        if self == other:
            return True

        if self.contains_point(other.first) or self.contains_point(other.second):
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
