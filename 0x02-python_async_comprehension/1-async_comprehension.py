#!/usr/bin/env python3
"""This module contains async_comprehension() functions"""

from typing import List
import random
import asyncio


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    This coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """

    return [x async for x in async_generator()]
