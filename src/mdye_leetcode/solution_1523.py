# -*- coding: utf-8 -*-


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return self.countOddsMathy(low, high)

    def countOddsMathy(self, low: int, high: int) -> int:
        range_qty = (high - low) // 2  # b/c high is inclusive we don't subtract 1

        if low % 2 == 1 or high % 2 == 1:
            range_qty += 1

        return range_qty

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
