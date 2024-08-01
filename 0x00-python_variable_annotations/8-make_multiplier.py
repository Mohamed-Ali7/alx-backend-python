#!/usr/bin/env python3
"""This module contains make_multiplier() function"""
from typing import List, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier."""
    def multiply(a: float) -> float:
        return a * multiplier
    return multiply
