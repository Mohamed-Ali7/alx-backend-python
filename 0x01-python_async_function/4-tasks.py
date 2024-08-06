#!/usr/bin/env python3
"""This module contains task_wait_n() function (Coroutine)"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await delay for delay in asyncio.as_completed(tasks)]
    return delays
