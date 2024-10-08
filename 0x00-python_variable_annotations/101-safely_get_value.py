#!/usr/bin/env python3
"""
type annotatns
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely retrieves a value from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
