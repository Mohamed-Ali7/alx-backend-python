#!/usr/bin/env python3
"""This module contains safe_first_element() function"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns a list of elements"""
    if lst:
        return lst[0]
    else:
        return None
