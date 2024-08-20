#!/usr/bin/env python3
"""An async function that takes an async function
and generates 10 random floats"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generates a random List offloat between 1 and 10

    Args:
        Takes no arguments

    Returns:
        No returns
    """

    res = [i async for i in async_generator()]
    return res
