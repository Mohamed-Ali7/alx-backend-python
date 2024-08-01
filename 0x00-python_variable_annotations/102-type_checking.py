#!/usr/bin/env python3
"""This module contains zoom_array() function"""
from typing import List, Any, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


tup = (12, 72, 91)

zoom_2x = zoom_array(tup)

zoom_3x = zoom_array(tup, 3)
