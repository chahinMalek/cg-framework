"""
    Representation of 2D polygon - with helper methods
"""

from typing import List
from line_segment import LineSegment
from triangle import Triangle
from point import Point

class Polygon:

    def __init__(self, points: List[Point]) -> None:
        self.points = points

    def draw(self):
        pass

    def orientation(self) -> int:
        return Triangle(self.points[0], self.points[1], self.points[2]).orientation()

    def is_simple(self) -> bool:
        """

        Returns:

        """
        pass

    def does_contain(self, point: Point) -> bool:
        """

        Args:
            point:

        Returns:

        """
        pass

    def does_intersect(self, line_segment: LineSegment) -> bool:
        """

        Args:
            line_segment:

        Returns:

        """
        pass

    def is_empty(self, points: List[Point]) -> bool:
        """

        Args:
            points:

        Returns:

        """
        pass


    def is_convex(self) -> bool:
        """

        Returns:

        """
        start_triangle_orientation = Triangle(self.points[0], self.points[1], self.points[2]).orientation()
        points_count = len(self.points)
        for i in range(1, points_count):
            first = self.points[i % points_count]
            second = self.points[(i + 1) % points_count]
            third = self.points[(i + 2) % points_count]
            if Triangle(first, second, third).orientation() != start_triangle_orientation:
                return False
        return True

p = Polygon([Point(2, 0), Point(4, 0), Point(6, 2), Point(4, 4), Point(2, 4), Point(0, 2)])
print(p.is_convex())
