"""
    Representation of 2D polygon - with helper methods
"""

from typing import List, Tuple

from structures.line_segment import LineSegment
from structures.point import Point
from util import sign, orientation, neighbors
from conf import PSEUDO_INF


class Polygon:

    def __init__(self, points: List[Point]) -> None:
        if len(points) > 2:
            self.points = points
        else:
            raise ValueError("Points length less than 3")

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

            current = self.points[i]
            next = self.points[i + 1]
            orientation_sum += (next.x - current.x) * (next.y - current.y)

        return sign(orientation_sum)

    def intersection_count(self, line_segment: LineSegment) -> Tuple[int, bool]:
        """
        HELPER: Determines number of times that LineSegment object intersects
        with polygon (self)

        Args:
            line_segment: LineSegment object

        Returns:
            tuple consisting of int and bool. int is number of intersections,
            bool is True if point "lies" on one of the edges of the polygon
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

            distance = left_p.euclidean_dist_squared(point)

            tan = left_p.slope(point)

            if left_p.y == point.y:
                distance *= -1

            return tan, distance

        left_p = sorted(self.points, key=lambda point: (point.x, -point.y))[0]
        self.points = sorted(self.points, key=lambda point: get_tan(point))

    def make_convex_hull(self) -> None:
        """
        For a given polygon (self), transforms it to convex hull of itself.
        Implements Graham scan. Starts from left most bottom most point. Sorts
        other points in CCW order.
        """

        def _sort_key(point: Point) -> Tuple[float, float, float]:
            """
            HELPER. Defines sorting order of points.

            Args:
                point: Point object.

            Returns:
                Tuple consisting of comparison oreder priority (slope, -y, x)
            """
            return point.slope(start), -point.y, point.x

        start = min(self.points, key=lambda point: (point.x, point.y))
        self.points.pop(self.points.index(start))

        self.points.sort(key=_sort_key)

        convex_hull = [start]

        for point in self.points:

            convex_hull.append(point)

            while len(convex_hull) > 2 and orientation(convex_hull[-3],
                                                       convex_hull[-2],
                                                       convex_hull[-1]) < 0:
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
        # NOTE: PSEUDO_INF used instead of float("inf") of numpy.inf because
        # usage of these methods gave incorrect results. Float comparison error?
        ray = LineSegment(first=point, second=Point(PSEUDO_INF, point.y))
        num_of_int, on_edge = self.intersection_count(ray)
        return num_of_int % 2 != 0 or on_edge

    def does_intersect(self, line_segment: LineSegment) -> bool:
        """
            Determines if line segment and polygon (line_segment, self)
            intersect

        Args:
            line_segment: LineSegment object.

        Returns:
            True if line_segment and self intersect. False otherwise
        """
        return self.intersection_count(line_segment)[0] > 0

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
        For every three consecutive point checks if their orientation matches
        start_triangle_orientation

        Returns:
            True if polygon is convex, False otherwise
        """
        start_triangle_orientation = orientation(self.points[0],
                                                 self.points[1],
                                                 self.points[2])

        points_count = len(self.points)

        for i in range(0, points_count):

            first = self.points[i % points_count]
            second = self.points[(i + 1) % points_count]
            third = self.points[(i + 2) % points_count]

            if orientation(first, second, third) != start_triangle_orientation:
                return False

        return True

    def diagonals_from_point(self, start_point: Point) -> List[LineSegment]:
        """

        Args:
            start_point:

        Returns:

        """
        self.make_simple()
        diagonals = []

        for index, point in enumerate(self.points):

            if not neighbors(start_point, point, self.points):
                diagonals.append(LineSegment(start_point, point))

        return diagonals

    def has_diagonal(self, diagonal: LineSegment) -> bool:
        return not neighbors(diagonal.first, diagonal.second, self.points)

    def __str__(self) -> str:
        """
        Returns: String of polygon points as ordered pairs.
        """
        result = "Polygon: "

        for point in self.points:
            result = "{}{}".format(result, point)

        return result
