#!/usr/bin/env python3
"""A function that takes a string, float or int and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple from the str, int and float"""
    return k, v ** 2
