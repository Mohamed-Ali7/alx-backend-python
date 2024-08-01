#!/usr/bin/env python3
"""This module contains sum_list() function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of float list elements as a float."""

    result: float = 0
    for ele in input_list:
        result += ele

    return result
