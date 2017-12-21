"""
    Representation of 2D point
"""

from collections import namedtuple
from tkinter import Canvas
from conf import CENTER

class Point(namedtuple('Point', ['x', 'y'])):
    # Fali komentar. Pogledati note u structures.line glede komentarisanja
    # klasa.

    def draw(self, canvas: Canvas):
        x = self.x + CENTER
        y = -(self.y - CENTER)
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, width=0, fill="red")

    def euclidean_dist_squared(self, other: 'Point') -> float:
        """
        Calculates euclidean distance between two points (self and other)
        Args:
            other: Point object
        Returns:
            Squared value of euclidean distance
        """
        return (self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y)

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

    def slope(self, other: 'Point') -> float:
        """
        Calculates slope between two points (self and other)
        Args:
            other: Point object
        Returns:
            slope between two points
        """
        if self.x != other.x:
            return 1.0 * (self.y - other.y) / (self.x - other.x)
        else:
            return float('inf')

    def __str__(self):  # Fali return type: str
        # Fali komentar.
        return "(" + str(self.x) + ", " + str(self.y) + ")"
