# Northstar Retail — Automatic Retry & Exponential Backoff

This repository implements the easiest of the four Northstar team tasks:
**Automatic Retry & Exponential Backoff**.

## Goal
Retry a failed network request up to 3 times with increasing delays:
- 1st retry: 1 second
- 2nd retry: 2 seconds
- 3rd retry: 4 seconds

The implementation is deliberately simple and uses Python's standard library.

## Run

```bash
python -m unittest discover -s tests -v
```

## Example

```python
from src.retry import retry_with_backoff

result = retry_with_backoff(my_function, max_attempts=3)
```

## Definition of Done
- Retries temporary failures.
- Uses exponential backoff.
- Stops after the configured number of attempts.
- Returns the successful result.
- Raises the final error if all attempts fail.
- Includes automated tests.
