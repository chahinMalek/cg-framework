"""
    Unit tests of Triangle class methods
"""

from structures.triangle import Triangle
from structures.point import Point


def test_eq() -> None:
    """
        Tests if overridden method __eq__ works correctly
    """
    point_1 = Point(x=1, y=2)
    point_2 = Point(x=2, y=-4)
    point_3 = Point(x=3, y=6)

    triangle_1 = Triangle(first=point_1, second=point_2, third=point_3)
    triangle_2 = Triangle(first=point_1, second=point_2, third=point_3)
    triangle_3 = Triangle(first=point_3, second=point_1, third=point_2)

    assert triangle_1 == triangle_2
    assert not triangle_1 == triangle_3


def test_determinant() -> None:
    """
        Tests if Triangle class method determinant works correctly
    """
    point_1 = Point(x=1, y=2)
    point_2 = Point(x=2, y=-4)
    point_3 = Point(x=3, y=6)
    point_4 = Point(x=6, y=10)

    triangle_1 = Triangle(first=point_1, second=point_2, third=point_3)
    triangle_2 = Triangle(first=point_1, second=point_2, third=point_2)
    triangle_3 = Triangle(first=point_2, second=point_1, third=point_3)
    triangle_4 = Triangle(first=point_3, second=point_1, third=point_4)

    assert triangle_1.determinant() == 16
    assert triangle_2.determinant() == 0
    assert triangle_3.determinant() == -16
    assert triangle_4.determinant() == 4


def test_orientation() -> None:
    """
        Tests if Triangle class method determinant works correctly
    """
    point_1 = Point(x=1, y=2)
    point_2 = Point(x=2, y=-4)
    point_3 = Point(x=3, y=6)

    triangle_1 = Triangle(first=point_1, second=point_2, third=point_3)
    triangle_2 = Triangle(first=point_2, second=point_1, third=point_3)
    triangle_3 = Triangle(first=point_3, second=point_3, third=point_3)

    assert triangle_1.orientation() == 1
    assert triangle_2.orientation() == -1
    assert triangle_3.orientation() == 0


def test_area() -> None:
    """
        Tests if area method works correctly. One common and one edge case
    """
    point_1 = Point(x=3, y=4)
    point_2 = Point(x=3, y=0)
    point_3 = Point(x=0, y=0)

    assert Triangle(first=point_1, second=point_1, third=point_1).area() == 0
    assert Triangle(first=point_1, second=point_2, third=point_3).area() == 6


def test_does_contain() -> None:
    """

    """
    pass


def test_is_empty() -> None:
    """

    """
    point_1 = Point(x=1, y=2)
    point_2 = Point(x=2, y=-4)
    point_3 = Point(x=3, y=6)

    triangle = Triangle(first=point_1, second=point_2, third=point_3)
    points_out = [Point(x=0, y=0), Point(x=2, y=5), Point(x=7, y=9), Point(x=3, y=8), Point(x=4, y=4), Point(x=0, y=5)]
    points_in = [Point(x=2, y=2), Point(x=2, y=4), Point(x=0, y=0), Point(x=2, y=7), Point(x=6, y=3), Point(x=-5, y=5)]

    assert triangle.is_empty(points_out)
    assert not triangle.is_empty(points_in)
