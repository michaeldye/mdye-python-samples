"""."""

from functools import reduce
from typing import List


class Solution:
    def extract_digits(self, n: int) -> List[int]:
        """."""
        digits = []

        while n > 0:
            value = n % 10
            digits.append(value)
            n = n // 10

        return digits

    def subtract_product_and_sum(self, n: int) -> int:
        """."""
        digits = self.extract_digits(n)

        return reduce(lambda acc, it: acc * it, digits) - sum(digits)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
