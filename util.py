"""
    Collection of utility functions and constants
"""
from structures.point import Point


def sign(number) -> int:
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def determinant(first: Point, second: Point, third: Point) -> float:
    """
    Calculates the determinant of 3 points (cross product of 2 vector sides)

    Returns:
        Determinant of 3 points.
    """
    return (second.x - first.x) * (third.y - second.y) - \
           (third.x - second.x) * (second.y - first.y)


def orientation(first: Point, second: Point, third: Point) -> int:
    """
    Determines orientation of 3 points (self)

    Returns:
        -1 for CW, 1 for CCW and 0 for collinear
    """
    return sign(determinant(first, second, third))