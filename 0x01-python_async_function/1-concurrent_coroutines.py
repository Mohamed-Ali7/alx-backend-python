#!/usr/bin/env python3
"""This module contains wait_random() function (Coroutine)"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> list:
    """
    Will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    """
    tasks: list = [wait_random(max_delay) for _ in range(n)]
    delays: list = []

    delays = [await delay for delay in asyncio.as_completed(tasks)]
    return delays
