#!/usr/bin/env python3
"""This module contains sum_mixed_list() function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of mixed list elements as a float."""

    result: float = 0
    for ele in mxd_lst:
        result += ele

    return result
