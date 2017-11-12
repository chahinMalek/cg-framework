from typing import List
from structures.point import Point
from numpy import inf
import operator


def simple_closed_path(input_points: List[Point]) -> List[Point]:
    """

    Args:
        input_points:

    Returns:

    """
    def get_tan(point: Point) -> tuple:
        """

        Args:
            point:

        Returns:

        """
        distance = point.euclidan_dist_squared(left_point)

        if point.x == left_point.x:
            tan = -inf
        else:
            tan = (point.y - left_point.y) / (point.x - left_point.x)

        if point.y == left_point.y:
            distance *= -1

        return tan, distance

    left_point = sorted(input_points, key=operator.attrgetter('x'))[0]
    return sorted(input_points, key=get_tan)


# testing

points = [Point(1, 10), Point(2, 5), Point(3, 2), Point(6, 1), Point(7, 8), Point(8, 5), Point(5, 7), Point(3, 8)]

print(simple_closed_path(points))
