#!/usr/bin/env python3
"""An function that """

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Takes an integer n and max_delay, measures execution time for wait_n,
    and returns average time per task

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.
        n (int): Number of concurrent coroutines to run in wait_n.
    Returns:
        float: Average time per coroutine
    """
    start_time = time.time()
    delays = asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
