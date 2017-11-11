"""
    Collection of utility functions
"""


def sign(number) -> int:
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
