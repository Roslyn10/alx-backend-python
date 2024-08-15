#!/usr/bin/env python3
"""A function that returns the values of different types """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns the values of the types
    """
    return [(i, len(i)) for i in lst]
