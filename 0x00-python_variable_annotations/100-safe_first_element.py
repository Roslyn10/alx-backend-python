#!/usr/bin/env python3
"""Correcting the code to duck-typed annotations"""


import typing

def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """
    Returns the first element of a list or nonee if empty
    """

    if lst:
        return lst[0]
    else:
        return None
