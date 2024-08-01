#!/usr/bin/env python3
"""This module contains safely_get_value() function"""
from typing import Union, TypeVar, Mapping, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns a dict or the default value"""
    if key in dct:
        return dct[key]
    else:
        return default
