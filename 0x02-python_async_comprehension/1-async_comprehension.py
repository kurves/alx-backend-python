#!/usr/bin/env python3
"""
Module async_comprehension
This module contains a coroutine that collects 10 random numbers using an async comprehension.
"""

import asyncio
from typing import List
from async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    """
    return [num async for num in async_generator()]

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
