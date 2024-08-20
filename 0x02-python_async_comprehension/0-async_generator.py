#!/usr/bin/env python3
"""An Async function that generates a random float between 1 and 10"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generates an random number between 1 and 10
    after waiting 1 second

    Args:
        Takes no arguments

    Returns:
            Random float between 1 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
