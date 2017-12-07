"""
    Representation of 2D polygon - with helper methods
"""

from typing import List, Tuple

from structures.line_segment import LineSegment
from structures.triangle import Triangle
from structures.point import Point
from util import sign
from conf import PSEUDO_INF

class Polygon:

    def __init__(self, points: List[Point]) -> None:
        if len(points) > 2:
            self.points = points
        else:
            raise ValueError("points length less than 3")

    def __eq__(self, other: 'Polygon'):
        return self.points == other.points

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
        orientation_sum = 0
        for i in range(0, len(self.points)-1):
            current_point = self.points[i]
            next_point = self.points[i + 1]
            orientation_sum += (next_point.x - current_point.x) * (next_point.y - current_point.y)
        return sign(orientation_sum)

    def number_of_intersections(self, line_segment: LineSegment) -> Tuple[int, bool]:
        """
        HELPER: Determines number of times that LineSegment object intersects with polygon (self)
        Args:
            line_segment: LineSegment object
        Returns:
            tuple consisting of int and bool. int is number of intersections, bool is True if point "lies"
            on one of the edges of the polygon
        """
        intersections_counter = 0
        on_edge = False
        points_count = len(self.points)

        for i in range(0, points_count):

            first = self.points[i % points_count]
            second = self.points[(i + 1) % points_count]

            current_line_segment = LineSegment(first=first, second=second)

            if current_line_segment.does_contain(line_segment.first):
                on_edge = True

            if current_line_segment.does_intersect(line_segment):
                intersections_counter += 1

        return intersections_counter, on_edge

    def make_simple(self) -> None:
        """
        For a given polygon (self), transforms it to simple polygon.
        Starts from left most top most point.
        """

        def get_tan(point: 'Point') -> tuple:

            distance = left_point.euclidean_dist_squared(point)

            tan = left_point.slope(point)

            if left_point.y == point.y:
                distance *= -1

            return tan, distance

        left_point = sorted(self.points, key=lambda point: (point.x, -point.y))[0]
        self.points = sorted(self.points, key=lambda point: get_tan(point))

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
        # NOTE: PSEUDO_INF used instead of float("inf") of numpy.inf because usage of these
        # methods gave incorrect results. Float comparison error?
        ray = LineSegment(first=point, second=Point(PSEUDO_INF, point.y))
        num_of_int, on_edge = self.number_of_intersections(ray)
        return num_of_int % 2 != 0 or on_edge

    def does_intersect(self, line_segment: LineSegment) -> bool:
        """
            Determines if line segment and polygon (line_segment, self) intersect
        Args:
            line_segment: LineSegment object.
        Returns:
            True if line_segment and self intersect. False otherwise
        """
        return self.number_of_intersections(line_segment)[0] > 0

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
        Determines if polygon (self) is convex. Loops over polygon points.
        For every three consecutive point checks if their orientation matches start_triangle_orientation
        Returns:
            True if polygon is convex, False otherwise
        """
        start_triangle_orientation = Triangle(self.points[0], self.points[1], self.points[2]).orientation()
        points_count = len(self.points)

        for i in range(0, points_count):

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
