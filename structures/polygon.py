"""
    Representation of 2D polygon - with helper methods
"""

from typing import List

from numpy import inf
import operator
from structures.line_segment import LineSegment
from structures.triangle import Triangle
from structures.point import Point


class Polygon:

    def __init__(self, points: List[Point]) -> None:
        self.points = points

    def draw(self, canvas):
        first = self.points[0]

        for i in range(0, len(self.points) - 1):
            LineSegment(self.points[i], self.points[i + 1]).draw(canvas)

        LineSegment(self.points[-1], first).draw(canvas)

    def orientation(self) -> int:
        return Triangle(self.points[0], self.points[1], self.points[2]).orientation()

    def number_of_intersections(self, line_segment: LineSegment) -> int:
        """

        Args:
            line_segment:

        Returns:

        """
        intersections_counter = 0
        points_count = len(self.points)

        for i in range(0, points_count-1):

            first = self.points[i]
            second = self.points[i + 1]

            if LineSegment(first=first, second=second).does_intersect(line_segment):
                intersections_counter += 1

        last = self.points[-1]
        first = self.points[0]
        if LineSegment(first=last, second=first).does_intersect(line_segment):
            intersections_counter += 1

        return intersections_counter

    def make_simple(self) -> None:
        """

        Args:
            input_points:

        Returns:

        """

        left_point = sorted(self.points, key=operator.attrgetter('x'))[0]
        self.points = sorted(self.points, key=left_point.get_tan)

    def make_convex_hull(self) -> None:

        def min_key(point: Point) -> tuple:
            return point.x, point.y

        def sort_key(point: Point) -> tuple:
            return point.slope(start), -point.y, point.x

        start = min(self.points, key=min_key)
        self.points.pop(self.points.index(start))

        self.points.sort(key=sort_key)

        convex_hull = [start]
        for point in self.points:
            convex_hull.append(point)
            while len(convex_hull) > 2 and Triangle(convex_hull[-3], convex_hull[-2], convex_hull[-1]).orientation() < 0:
                convex_hull.pop(-2)

        self.points = convex_hull

    def does_contain(self, point: Point) -> bool:
        """

        Args:
            point:

        Returns:

        """
        ray = LineSegment(first=point, second=Point(1000000, point.y))
        num_of_int = self.number_of_intersections(ray)
        return num_of_int % 2 != 0

    def does_intersect(self, line_segment: LineSegment) -> bool:
        """

        Args:
            line_segment:

        Returns:

        """
        return self.number_of_intersections(line_segment) > 0

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


