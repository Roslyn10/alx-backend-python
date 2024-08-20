#!/usr/bin/env python3
"""An async function that calculates the total runtime of another function"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Calculates the total runtime it takes for
    the async_comprehension function to run

    Args:
        No arguments

    Returns:
        The total runtime
    """

    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
