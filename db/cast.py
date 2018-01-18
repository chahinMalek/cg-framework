from typing import List

from structures.point import Point
from structures.triangle import Triangle
from structures.polygon import Polygon

from db.entities import Point as DBPoint
from db.entities import Triangle as DBTriangle
from db.entities import Triangulation as DBTriangulation
from db.entities import Polygon as DBPolygon


def cast_point(point: Point) -> DBPoint:
    db_point = DBPoint()

    db_point.x = point.x
    db_point.y = point.y

    return db_point


def cast_triangle(triangle: Triangle) -> DBTriangle:
    db_triangle = DBTriangle()

    db_triangle.points.append(cast_point(triangle.first))
    db_triangle.points.append(cast_point(triangle.second))
    db_triangle.points.append(cast_point(triangle.third))

    return db_triangle


def cast_triangulation(triangulation: List[Triangle]) -> DBTriangulation:
    db_triangulation = DBTriangulation()

    for triangle in triangulation:
        db_triangulation.triangles.append(cast_triangle(triangle))

    return db_triangulation


def cast_polygon(polygon: Polygon) -> DBPolygon:
    db_polygon = DBPolygon()

    for point in polygon.points:
        db_polygon.points.append(cast_point(point))

    return db_polygon
