#!/usr/bin/env python3
"""Using type annotations for the function"""

from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Returns the value from a dictionary using a specified key,
    or a default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
