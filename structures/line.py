"""
    Representation of 2D line - with helper methods
"""

from collections import namedtuple


class Line(namedtuple('Line', ['k', 'n'])):

    def __eq__(self, other: 'Line') -> bool:
        """
            Determines if self is same as other.
        Args:
            other: Another line object

        Returns:
            bool: True if lines are the same, False otherwise
        """
        return self.k == other.k and self.n == other.n

    def does_intersect(self, other: 'Line') -> bool:
        """
        Determines if self intersects with other
        Args:
            other: another line
        Returns:
            bool: True if lines intersect, False otherwise
        """
        return self.k != other.k or self == other

    def __str__(self):
        return "Line: y = " + self.k + " * x + " + self.n