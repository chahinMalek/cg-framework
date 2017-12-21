"""
    Representation of 2D line - with helper methods
"""

from collections import namedtuple


class Line(namedtuple('Line', ['k', 'n'])):
    # Kako se komentarisu sve metode, tako je potrebno komentarisati i klase.
    # Primjer komentara za klasu:
    """ Class representing line in a plane """

    def __eq__(self, other: 'Line') -> bool:
        """
        Determines if two lines (self and other) are the same.
        Args:
            other: Another line object
        Returns:
            bool: True if lines are the same, False otherwise
        """
        return self.k == other.k and self.n == other.n

    def does_intersect(self, other: 'Line') -> bool:
        """
        Determines if two lines (self and other) intersect
        Args:
            other: Another line object
        Returns:
            bool: True if lines intersect, False otherwise
        """
        return self.k != other.k or self == other

    def __str__(self):  # Fali return type. U ovom slucaju: -> str
        # Fali komentar.
        return "Line: y = " + str(self.k) + " * x + " + str(self.n)
# Fali prazna linija na kraju file-a
