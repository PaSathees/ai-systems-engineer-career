import asyncio
from dataclasses import dataclass
from functools import wraps
import time
import httpx
from collections.abc import Callable, Coroutine
from typing import Any, ParamSpec, TypeVar

# Generic shape
P = ParamSpec("P") # Capture unknown arguments
R = TypeVar("R") # Capture unknown return type

@dataclass
class Reading:
    city: str
    temperature_c: float

def timed_async(func: Callable[P, Coroutine[Any, Any, R]]) -> Callable[P, Coroutine[Any, Any, R]]:
    # Coroutine[Any, Any, R]: is an async function that yields a value of type R

    @wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start_time = time.perf_counter()

        result = await func(*args, **kwargs)

        end_time = time.perf_counter()
        print(f"{func.__name__} took {(end_time - start_time) * 1000:.0f}ms")
        return result

    return wrapper

async def fetch_temp(client: httpx.AsyncClient, city: str, url: str) -> Reading:
    """Fetches the temperature for a single city asynchronously."""
    response = await client.get(url, timeout=10.0)
    response.raise_for_status()

    # Parse the JSON response
    temp = response.json()["current"]["temperature_2m"]
    return Reading(city=city, temperature_c=temp)

@timed_async
async def main() -> None:
    # Open-Meteo weather API
    cities = {
        "Colombo": "https://api.open-meteo.com/v1/forecast?latitude=6.93&longitude=79.86&current=temperature_2m",
        "Berlin": "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m",
        "Paris": "https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&current=temperature_2m",
    }

    async with httpx.AsyncClient() as client:
        tasks = [fetch_temp(client, city, url) for city, url in cities.items()]
        results = await asyncio.gather(*tasks)

    for reading in results:
        print(f"{reading.city}: {reading.temperature_c}\N{DEGREE SIGN}C")

if __name__ == "__main__":
    asyncio.run(main())