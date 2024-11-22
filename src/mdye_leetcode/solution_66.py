"""."""

from collections import deque
from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        """."""
        v = 0
        for d in digits:
            v *= 10
            v += d

        v += 1

        o = deque()
        while v > 0:
            o.appendleft(v % 10)
            v //= 10

        return list(o)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
