#!/usr/bin/env python3
"""An async function that takes an integer and returns asyncio.Task"""
import asyncio
from typing import Type


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task
    that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task[float]: An asyncio.Task that will complete with
                             the result of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
