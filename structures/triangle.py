"""
    Representation of 2D triangle - with helper methods
"""

from typing import List
from structures.point import Point
from util import sign
from math import fabs


class Triangle:

    def __init__(self, first: Point, second: Point, third: Point) -> None:
        self.first = first
        self.second = second
        self.third = third

    def draw(self) -> None:
        pass

    def __eq__(self, other: 'Triangle') -> bool:
        """
        Determines if two triangles (self, other) are the same.
        Args:
            other: Other triangle object
        Returns:
            True if triangles are the same, False otherwise
        """
        return self.first == other.first and self.second == other.second and self.third == other.third

    def determinant(self) -> float:
        """
        Calculates the determinant of a triangle (cross product of 2 vector sides)
        Returns:
            Determinant of the triangle (self)
        """
        return (self.second.x - self.first.x) * (self.third.y - self.second.y) - \
               (self.third.x - self.second.x) * (self.second.y - self.first.y)

    def orientation(self) -> int:
        """
        Determines orientation of a triangle (self)
        Returns:
            -1 for CW, 1 for CCW and 0 for collinear
        """
        return sign(self.determinant())

    def area(self):
        """
        Calculates area of a triangle (self)
        Returns:
            Area of the triangle (self)
        """
        return fabs(self.determinant())/2.0

    def does_contain(self, point: Point) -> bool:
        """
        Determines if point is inside the triangle (self)
        Args:
            point: Point object to be tested
        Returns:
            True if point is inside the triangle (self), False otherwise
        """
        t1_area = Triangle(point, self.first, self.second).area()
        t2_area = Triangle(point, self.second, self.third).area()
        t3_area = Triangle(point, self.first, self.third).area()
        return t1_area + t2_area + t3_area == self.area()

    def is_empty(self, points: List[Point]) -> bool:
        """
        For a given list of points, checks if any of them are in triangle (self)
        Args:
            points: List of point objects to be tested
        Returns:
            True if none of the points are inside the triangle, False otherwise
        """
        for point in points:
            if self.does_contain(point):
                return False
        return True

    def __str__(self):
        return "Triangle: " + str(self.first) + ", " + str(self.second) + ", " + str(self.third)
