#!/usr/bin/env python3 
"""An async function that takes 2 arguments and returns floats in specfic time delays"""


import asyncio
from typing import Type, List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes random integers between n and  max_delay and returns a list of Floats

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.
        n (int): Number of arguments passed and printed on the screen

    Returns:
        A list of floats, randomly generated
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
