import time
from typing import Callable, Any


def retry_with_backoff(
    operation: Callable[[], Any],
    max_attempts: int = 3,
    base_delay: float = 1.0,
) -> Any:
    """Run an operation and retry failures using exponential backoff.

    Delays follow: base_delay, base_delay*2, base_delay*4, ...
    """
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    if base_delay < 0:
        raise ValueError("base_delay cannot be negative")

    last_error = None

    for attempt in range(max_attempts):
        try:
            return operation()
        except Exception as error:
            last_error = error

            # No delay after the final failed attempt.
            if attempt == max_attempts - 1:
                break

            delay = base_delay * (2 ** attempt)
            time.sleep(delay)

    raise last_error
