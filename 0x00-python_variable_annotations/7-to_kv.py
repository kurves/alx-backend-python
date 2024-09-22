#!/usr/bin/env python3
""""
complex types
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string `k`
    """
    return (k, float(v ** 2))
