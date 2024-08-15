#!/usr/bin/env python3
"""A function that takes a float and returns a function that multiplies it by another float."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float by the specified multiplier.
    """
    def multiplier_func(x: float) -> float:
        """Returns the result of multiplying the given float by the multiplier."""
        return multiplier * x

    return multiplier_func
