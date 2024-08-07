#!/usr/bin/env python3
"""This module contains async_generator() functions"""

from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """

    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
