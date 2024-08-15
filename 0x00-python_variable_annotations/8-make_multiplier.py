#!/usr/bin/env python3
"""A function that takes a float and returns the multipiles of it"""
from typing import Callable


def make_multiplier(multipiler: float) -> Callable[[float], float]:
    """
    Returns the multiplication of the floats
    """
    def multipiler_func(x: float) -> float:
        return x * multipiler

    return multipiler_func
