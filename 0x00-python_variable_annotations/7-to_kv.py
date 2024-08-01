#!/usr/bin/env python3
"""This module contains to_kv() function"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple with first element is the string k,
    and The second element is the square of the int/float v
    """

    return (k, float(v * v))
