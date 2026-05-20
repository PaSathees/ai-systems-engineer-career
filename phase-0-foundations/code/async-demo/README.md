# Async API Demo

A small fully-typed asynchronous Python script built to refresh Python concepts.

This script fetches data concurrently from multiple weather APIs to demonstrate modern asynchronous I/O and strict type safety.

## Features
- **Concurrent I/O:** Uses `asyncio.gather` and `httpx.AsyncClient` to process network requests simultaneously without blocking the event loop.
- **Strict Typing:** Configured with `mypy --strict` and modern Python 3.12+ type hints (e.g., `ParamSpec`, `TypeVar`, generics).
- **Code Quality:** Enforces `flake8-annotations` (ANN) using `ruff` to ensure 100% type-hint coverage.
- **Modern Tooling:** Managed via `uv` for lightning-fast dependency and environment resolution.

## How to Run

1. Ensure you have [uv](https://github.com/astral-sh/uv) installed.
2. Run the script (uv will automatically sync the environment and install dependencies):
```bash
uv run main.py
```

## Checks
To run the linter and type-checker:
```bash
uv run ruff check .
uv run mypy .
```