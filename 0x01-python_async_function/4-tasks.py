#!/usr/bin/env python3
"""An async function that takes an integer and returns asyncio.Task"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes an integer max_delay and returns a list of Floats

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.
        n (int): The number of arguments passed and printed on the screen

    Returns:
        A list of floats, randomly generated
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
