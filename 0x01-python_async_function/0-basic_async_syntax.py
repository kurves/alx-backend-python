import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive)
    and then returns the delay.

    Parameters:
    max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
    float: The amount of time waited in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
