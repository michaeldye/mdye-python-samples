# -*- coding: latin-1 -*-
""" """
from typing import Optional, List


class Solution:

    def find_lims(self, salary: List[int]) -> (int, int):
        low: Optional[int] = None
        high: Optional[int] = None

        for sval in salary:
            if high is None or sval > high:
                high = sval
            if low is None or sval < low:
                low = sval

        if None in [low, high]:
            raise ValueError("Failed to initialize low and high, bogus input")

        return low, high

    def average(self, salary: List[int]) -> float:

        # sort is slower than iterating through the whole list to find the min and max values
        low, high = self.find_lims(salary)

        # turns out running avgs. are kinda involved so we do the elementary school way instead
        total = 0
        count = 0
        for sval in salary:
            if sval != low and sval != high:
                count += 1
                total += sval

        return total / count

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
