"""
    Unit tests of LineSegment class methods
"""
from structures.point import Point
from structures.line_segment import LineSegment


def test_contains_point() -> None:
    """
        Tests if contains_point determines relationship between line_segment and point correctly.
        Tests both common and edge cases.
    """
    point_1 = Point(x=1, y=2)
    point_2 = Point(x=-2, y=-4)
    point_3 = Point(x=3, y=3)
    point_4 = Point(x=0, y=0)

    line_segment = LineSegment(first=point_1, second=point_2)

    assert line_segment.contains_point(point_1)
    assert line_segment.contains_point(point_2)
    assert not line_segment.contains_point(point_3)
    assert line_segment.contains_point(point_4)


def test_does_intersect() -> None:
    """
        Tests if does_intersect works correctly.
        Tests both common and edge cases.
    """

    line_segment_1 = LineSegment(first=Point(x=1, y=1), second=Point(x=4, y=4))
    line_segment_1_reverse = LineSegment(first=Point(x=4, y=4), second=Point(x=1, y=1))
    line_segment_2 = LineSegment(first=Point(x=1, y=1), second=Point(x=-2, y=-4))
    line_segment_3 = LineSegment(first=Point(x=3, y=3), second=Point(x=5, y=5))
    line_segment_4 = LineSegment(first=Point(x=1, y=0), second=Point(x=5, y=-5))

    assert line_segment_1.does_intersect(line_segment_1_reverse)
    assert line_segment_1.does_intersect(line_segment_2)
    assert line_segment_1.does_intersect(line_segment_3)
    assert not line_segment_1.does_intersect(line_segment_4)
