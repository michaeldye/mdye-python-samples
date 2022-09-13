from typing import List, Callable, Any, Mapping

from time import time
from functools import wraps


class TimingRecord:
    def __init__(self, fn_name: str):
        self.fn_name = fn_name

        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.elapsed_time: Optional[float] = None

    def start(self) -> "TimingRecord":
        self.bail_if_finished()

        self.start_time = time()

    def finish(self) -> "TimingRecord":
        self.bail_if_finished()

        self.end_time = time()
        self.elapsed_time = self.end_time - self.start_time

    def report(self) -> Mapping[str, str]:
        return {"fn_name": self.fn_name, "time_s": "{:2.6}".format(self.elapsed_time)}

    def bail_if_finished(self):
        if self.elapsed_time is not None:
            raise RuntimeError("Attempt to modify after finished")


def timed(fn: Callable[[Any], Any], record: TimingRecord) -> Callable[[Any], Any]:
    @wraps(fn)
    def wrapped(*args, **kwargs):
        record.start()

        try:
            result = fn(*args, **kwargs)
        finally:
            record.finish()

        return result

    return wrapped
