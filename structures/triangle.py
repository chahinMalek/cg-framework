"""
    Representation of 2D triangle - with helper methods
"""

from typing import List
from point import Point
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

        Args:
            other:

        Returns:

        """
        return self.first == other.first and self.second == other.second and self.third == other.third

    def determinant(self) -> float:
        """

        Returns:

        """
        return (self.second.x - self.first.x) * (self.third.y - self.second.y) - \
               (self.third.x - self.second.x) * (self.second.y - self.first.y)

    def orientation(self) -> int:
        """

        Returns:

        """
        return sign(self.determinant())

    def area(self):
        """

        Returns:

        """
        return fabs(self.determinant())/2.0

    def does_contain(self, point: Point) -> bool:
        """

        Args:
            point:

        Returns:

        """
        t1_area = Triangle(point, self.first, self.second).area()
        t2_area = Triangle(point, self.second, self.third).area()
        t3_area = Triangle(point, self.first, self.third).area()
        return t1_area + t2_area + t3_area == self.area()

    def is_empty(self, points: List[Point]) -> bool:
        """

        Args:
            points:

        Returns:

        """
        for point in points:
            if self.does_contain(point):
                return False
        return True


