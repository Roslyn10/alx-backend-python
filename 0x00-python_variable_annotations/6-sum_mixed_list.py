#!/usr/bin/env python3
"""
A function that takes a list of ints and floats and
returns the sum(float)
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of floats and ints
    """
    return sum(mxd_lst)
