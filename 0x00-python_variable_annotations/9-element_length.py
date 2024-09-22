#!/usr/bin/env python3
"""
Complex types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element.
    """
    return [(i, len(i)) for i in lst]
