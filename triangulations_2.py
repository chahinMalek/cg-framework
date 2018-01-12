from typing import List

from structures.line_segment import LineSegment
from structures.point import Point
from structures.polygon import Polygon
from structures.triangle import Triangle
from tree import Node, Tree
from util import orientation
import sys

sys.setrecursionlimit(100000)

def polygon_remainders(triangle: Triangle, polygon: Polygon) -> List[Polygon]:
    diags = []
    for segment in triangle.get_segments():
        if polygon.has_diagonal(segment):
            diags.append(segment)

    if len(diags) == 1:
        diag = diags[0]
        remainder_points = list(polygon.points)
        if not diag.does_contain(triangle.first):
            remainder_points.remove(triangle.first)
        if not diag.does_contain(triangle.second):
            remainder_points.remove(triangle.second)
        if not diag.does_contain(triangle.third):
            remainder_points.remove(triangle.third)
        return [Polygon(remainder_points)]
    else:
        if diags[1].does_contain(diags[0].first):
            common_point = diags[0].first
        else:
            common_point = diags[0].second

        common_point_index = polygon.points.index(common_point)
        return [Polygon(polygon.points[1:common_point_index+1]), Polygon(
            [polygon.points[0]] + polygon.points[common_point_index:])]


def extend_triangulation(parent: Node, new_triangle: Triangle) -> List[Triangle]:
    triangles_so_far = list(parent.data)
    triangles_so_far.append(new_triangle)
    return triangles_so_far

def merge_triangs(first: Node, second: Node):
    first_leaf_nodes = Tree(first).get_leaf_nodes()
    second_leaf_nodes = Tree(second).get_leaf_nodes()
    for node_1 in first_leaf_nodes:
        for node_2 in second_leaf_nodes:
            node_1.add_child(Node(node_1.data + node_2.data))


def generate_triangulations(polygon: Polygon, parent: Node):
    print(polygon)
    if len(polygon.points) <= 3:

        new_triangs = extend_triangulation(parent, Triangle(polygon.points[0],
                                                            polygon.points[1],
                                                            polygon.points[2]))
        child = Node(new_triangs)
        parent.add_child(child)
        return child

    segment = [polygon.points[0], polygon.points[1]]

    for point in polygon.points[2:]:

        first_triangle = Triangle(segment[0], segment[1], point)

        remainders = polygon_remainders(first_triangle, polygon)
        sub_root = generate_triangulations(Polygon([segment[0], segment[1],
                                                    point]), parent)

        generate_triangulations(remainders[0], sub_root)
        if len(remainders) == 2:
            second_part_root = Node([])
            generate_triangulations(remainders[1], second_part_root)
            merge_triangs(sub_root, second_part_root)


pentagon = Polygon([Point(1, 0), Point(2, 0),
                    Point(3, 1), Point(1.5, 2), Point(0, 1)])

hexagon = Polygon([Point(0, 0), Point(1, -1), Point(2, 0),
                     Point(2, 1), Point(1, 2), Point(0, 1)])

septagon = Polygon([Point(1, 0), Point(2, 0), Point(3, 1), Point(3, 2),
                     Point(1.5, 3), Point(0, 2), Point(0, 1)])

septagon.make_simple()
print(pentagon)

tree = Tree(Node([]))
generate_triangulations(septagon, tree.root)
for node in tree.get_leaf_nodes():
    print(node)