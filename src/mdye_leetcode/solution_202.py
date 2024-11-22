"""."""

from collections import deque
from typing import Any


def to_digits(n: int) -> deque[Any]:
    """."""
    digits = deque()

    # a deque is a data structure with O(1) prepend
    while n > 0:
        digit = n % 10
        digits.appendleft(digit)

        n = n // 10

    return digits


class Solution:
    def is_happy(self, n: int) -> bool:
        """."""

        def happy0(n: int, tail: set[int]) -> bool:
            if n == 1:
                return True

            if n in tail:
                return False

            tail.add(n)

            return happy0(sum(x**2 for x in to_digits(n)), tail)

        # in python, a set is a hashtable with some optimizations
        return happy0(n, set())


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
