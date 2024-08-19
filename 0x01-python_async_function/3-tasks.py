#!/usr/bin/env python3
"""An async function that takes an integer and returns asyncio.Task"""
import asyncio


wait_random = __import__('0-basic_async-syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns the asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
