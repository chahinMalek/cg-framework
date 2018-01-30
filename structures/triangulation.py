from typing import List

from structures.line_segment import LineSegment
from structures.triangle import Triangle


class Triangulation:

    def __init__(self, triangles: List[Triangle]) -> None:
        self.triangles = triangles

    def get_edges(self) -> List[LineSegment]:
        edges = []
        for triangle in self.triangles:
            for edge in triangle.get_sides():
                if edge in edges:
                    edge.frontier = False
                else:
                    edges.append(edge)

        return edges

    def add(self, triangle: Triangle) -> None:
        self.triangles.append(triangle)

    def remove(self, triangle: Triangle) -> None:
        self.triangles.remove(triangle)