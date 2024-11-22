#!/usr/bin/env python3
"""."""

import sys
from typing import List, Optional

from common.timing import TimingRecord, timed


# compute to the nth fibonacci number by calculating up from first
def calc_fib_dp(n: int) -> int:
    """."""
    dp = [0, 1]

    if n >= len(dp):
        for i in range(len(dp), n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


# limited by recursion depth
_max_n_for_fib_memo = 995


def calc_fib_memo(n: int) -> int:
    """."""

    def _calc(n: int, memo: List[int]) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        if memo[n] > 0:
            return memo[n]

        # value hasn't been computed yet, recur
        value = _calc(n - 1, memo) + _calc(n - 2, memo)
        memo[n] = value

        return value

    memo = [0] * (n + 1)
    return _calc(n, memo)


_max_n_for_fib_naive = 40


def calc_fib_naive(n: int) -> int:
    """."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)


def main(n: int) -> None:
    """."""
    if n < 0:
        raise ValueError("Given n must be >= 0")

    algs = [calc_fib_dp]

    if n <= _max_n_for_fib_memo:
        algs.append(calc_fib_memo)

    if n <= _max_n_for_fib_naive:
        algs.append(calc_fib_naive)

    last_answer: Optional[int] = None

    for fib_fn in algs:
        timer = TimingRecord(fib_fn.__name__)

        # let exceptions fly
        answer = timed(fib_fn, timer)(n)

        # make sure each answer is the same as the previous; if we wanted to
        # be more careful about this, we'd store "right" answers and check
        # against those
        if last_answer:
            assert last_answer == answer
        last_answer = answer
        print(f"{timer.report()}")

    print(f"{last_answer}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise RuntimeError("Missing required arg, n")

    main(int(sys.argv[1]))
    sys.exit(0)
