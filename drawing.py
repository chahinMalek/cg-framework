from conf import CENTER
from structures.line_segment import LineSegment
from structures.point import Point
from structures.polygon import Polygon


def draw_point(canvas, point: Point) -> None:
    x = point.x + CENTER
    y = -(point.y - CENTER)
    canvas.create_line(x - 1, y - 1, x + 1, y + 1, width=3, fill="red")


def draw_line_segment(canvas, line_segment: LineSegment) -> None:

    first_x = line_segment.first.x + CENTER
    first_y = -(line_segment.first.y - CENTER)
    second_x = line_segment.second.x + CENTER
    second_y = -(line_segment.second.y - CENTER)

    canvas.create_line(first_x, first_y, second_x, second_y, width=1, fill="blue")


def draw_polygon(canvas, polygon: Polygon):
    first = polygon.points[0]

    for i in range(0, len(polygon.points) -1):
        draw_line_segment(canvas, LineSegment(polygon.points[i], polygon.points[i+1]))

    draw_line_segment(canvas, LineSegment(polygon.points[-1], first))