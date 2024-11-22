"""."""

from functools import wraps
from time import time
from typing import Any, Callable, Mapping, Optional


class TimingRecord:
    def __init__(self, fn_name: str):
        """."""
        self.fn_name = fn_name

        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.elapsed_time: Optional[float] = None

    def start(self) -> "TimingRecord":
        """."""
        self.bail_if_finished()

        self.start_time = time()

        return self

    def finish(self) -> "TimingRecord":
        """."""
        self.bail_if_finished()

        self.end_time = time()

        if self.start_time is None:
            raise RuntimeError("Timer not started")

        self.elapsed_time = self.end_time - self.start_time

        return self

    def report(self) -> Mapping[str, str]:
        """."""
        return {"fn_name": self.fn_name, "time_s": f"{self.elapsed_time:2.6}"}

    def bail_if_finished(self) -> None:
        """."""
        if self.elapsed_time is not None:
            raise RuntimeError("Attempt to modify after finished")


def timed(fn: Callable[[Any], Any], record: TimingRecord) -> Callable[[Any], Any]:
    """."""

    @wraps(fn)
    def wrapped(*args: Any, **kwargs: Any):
        record.start()

        try:
            result = fn(*args, **kwargs)
        finally:
            record.finish()

        return result

    return wrapped
