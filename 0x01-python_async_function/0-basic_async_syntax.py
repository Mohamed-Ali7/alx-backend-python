#!/usr/bin/env python3
"""This module contains wait_random() function (Coroutine)"""

import random
import asyncio


async def wait_random(max_delay:int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay,
    seconds and eventually returns it.
    """
    delay: float = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
