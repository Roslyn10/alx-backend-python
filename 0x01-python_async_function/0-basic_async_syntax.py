#!/usr/bin/env python3
""" An async function that returns a random float after a random time delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes random integers between 0 and the max_delay and returns random floats

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        Random floats
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
