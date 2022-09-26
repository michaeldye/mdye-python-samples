# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_dec = is_inc = False

        for ix in range(len(nums) - 1):
            curr = nums[ix]
            next = nums[ix + 1]

            if next > curr:
                is_inc = True
            elif next < curr:
                is_dec = True

            # bail early if we see illegal condition
            if is_inc and is_dec:
                return False

        return True


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
