#!/usr/bin/env python3
"""
Module measure_runtime
This module contains a coroutine to measure the total runtime
"""

import asyncio
import time
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
