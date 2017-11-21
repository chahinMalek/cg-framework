"""
    Representation of 2D polygon - with helper methods
"""

from typing import List

from structures.line_segment import LineSegment
from structures.triangle import Triangle
from structures.point import Point
from util import sign

# TODO write docs
class Polygon:

    def __init__(self, points: List[Point]) -> None:
        self.points = points

    def draw(self, canvas):
        first = self.points[0]

        for i in range(0, len(self.points) - 1):
            LineSegment(self.points[i], self.points[i + 1]).draw(canvas)

        LineSegment(self.points[-1], first).draw(canvas)

    def orientation(self) -> int:
        """
        Returns:
            Orientation of polygon (self)
        """
        sum = 0
        for i in range(0, len(self.points)-1):
            current = self.points[i]
            next = self.points[i + 1]
            sum += (next.x - current.x) * (next.y - current.y)
        return sign(sum)

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
        For a given polygon (self), transforms it to simple polygon.
        """

        def get_tan(point: 'Point') -> tuple:

            distance = left_point.euclidean_dist_squared(point)

            tan = left_point.slope(point)

            if left_point.y == point.y:
                distance *= -1

            return tan, distance


        left_point = sorted(self.points, key= lambda point: (point.x, -point.y))[0]
        self.points = sorted(self.points, key= lambda point: left_point.get_tan(point))

    def make_convex_hull(self) -> None:
        """
        For a given polygon (self), transforms it to convex hull of itself. Implements Graham scan.
        Starts from left most bottom most point. Sorts other points in CCW order.
        """
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
        Determines if point "lies" in polygon (self)
        Args:
            point: Point object to be tested
        Returns:
            True if point is in polygon, False otherwise
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
        For a list of points determines if any of them "lie" in polygon (self)
        Args:
            points: List od Point objects to be tested
        Returns:
            True if no points are inside the polygon, False otherwise
        """
        for point in points:
            if self.does_contain(point):
                return False
        return True

    def is_convex(self) -> bool:
        """
        Determines if polygon (self) is convex
        Returns:
            True if polygon is convex, False otherwise
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

    def __str__(self):
        result = "Polygon: "

        for point in self.points:
            result += str(point) + ", "

        return result
