import unittest
from unittest.mock import patch

from src.retry import retry_with_backoff


class TestRetryWithBackoff(unittest.TestCase):

    @patch("src.retry.time.sleep")
    def test_retries_then_succeeds(self, mock_sleep):
        calls = []

        def operation():
            calls.append(1)
            if len(calls) < 3:
                raise ConnectionError("temporary failure")
            return "success"

        result = retry_with_backoff(operation, max_attempts=3, base_delay=1)

        self.assertEqual(result, "success")
        self.assertEqual(len(calls), 3)
        mock_sleep.assert_any_call(1)
        mock_sleep.assert_any_call(2)

    @patch("src.retry.time.sleep")
    def test_raises_after_final_failure(self, mock_sleep):
        def operation():
            raise ConnectionError("warehouse unavailable")

        with self.assertRaises(ConnectionError):
            retry_with_backoff(operation, max_attempts=3, base_delay=1)

        self.assertEqual(mock_sleep.call_count, 2)
        mock_sleep.assert_any_call(1)
        mock_sleep.assert_any_call(2)

    def test_invalid_attempts(self):
        with self.assertRaises(ValueError):
            retry_with_backoff(lambda: "ok", max_attempts=0)


if __name__ == "__main__":
    unittest.main()
