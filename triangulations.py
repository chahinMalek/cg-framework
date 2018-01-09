from typing import List

from structures.line_segment import LineSegment
from structures.point import Point
from structures.polygon import Polygon
from structures.triangle import Triangle
from anytree import Node, RenderTree, Walker
from util import orientation


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



class Temp:

    def __init__(self):
        self.triangles = None

    def generate_triangulations(self, polygon: Polygon, parent: Node):

        if len(polygon.points) == 3:
            return Triangle(polygon.points[0], polygon.points[1], polygon.points[2])

        segment = LineSegment(polygon.points[0], polygon.points[1])

        for i in range(2, len(polygon.points)):

            triang = Triangle(segment.first, segment.second, polygon.points[i])

            temp = Node(triang, parent=parent)
            remainders = polygon_remainders(triang, polygon)
            for remaider in remainders:
                triangs = self.generate_triangulations(remaider, temp)
                if triangs:
                    Node(triangs, parent=temp)
            #parent.root.add_child(temp)


polygon_1 = Polygon([Point(1, 0), Point(2, 0), Point(3, 1),
                     Point(1.5,2),Point(0, 1)])
polygon_1.make_simple()

t = Temp()
t.triangles = Node(polygon_1)
t.generate_triangulations(polygon_1, t.triangles)
res = []
for pre, fill, node in Tree(t.triangles):
    if node.is_leaf:
        w = Walker()
        res.append(w.walk(node, t.triangles.root)[0])

print(res)