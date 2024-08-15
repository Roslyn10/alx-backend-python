#!/usr/bin/env python3
"""A function that takes a float and returns the multipiles of it"""
from typing import Callable


def make_multiplier(multipiler: float) -> Callable[[float], float]:
    """
    Multiplies a float by a float
    """

    def multipiler_func(number: float) -> float:
        """
        Returns the multiplicaiton of the floats
        """
        return multipiler * number


    return multipiler_func
