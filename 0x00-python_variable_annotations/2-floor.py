#!/usr/bin/env python3
"""
Module for a simple type-annotated function that returns the floor of a float.
"""

import math

def floor(n: float) -> int:
    """
    Returns the floor of a float.
    Returns:
    int: The floor value of the float as an integer.
    """
    return math.floor(n)
