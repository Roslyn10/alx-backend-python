#!/usr/bin/env python3
"""A function that takes a string, float or int and returns a tuple"""


from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    Returns a tuple where:
    k: str,
    v: [int, float]
    """
    return k, v ** 2
