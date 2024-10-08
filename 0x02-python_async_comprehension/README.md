## 0x02. Python - Async Comprehension

# Async Generator

This project contains a coroutine called `async_generator` that generates random numbers asynchronously.

## async_generator

- Loops 10 times
- Each iteration asynchronously waits for 1 second
- Yields a random number between 0 and 10

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS

## Usage

To use the `async_generator`, import it and run it within an asyncio event loop.

Example:

```python
import asyncio
from async_generator import async_generator

async def main():
    async for number in async_generator():
        print(number)

asyncio.run(main())

## measure_runtime

- Imports `async_comprehension` from `async_comprehension.py`
- Executes `async_comprehension` four times in parallel using `asyncio.gather`
- Measures and returns the total runtime

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS

## Usage

To use the `measure_runtime`, import it and run it within an asyncio event loop.

Example:

```python
import asyncio
from measure_runtime import measure_runtime

async def main():
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime:.2f} seconds")

asyncio.run(main())
