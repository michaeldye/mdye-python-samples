# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_dec = is_inc = False

        for ix in range(len(nums) - 1):
            curr_e = nums[ix]
            next_e = nums[ix + 1]

            if next_e > curr_e:
                is_inc = True
            elif next_e < curr_e:
                is_dec = True

            # bail early if we see illegal condition
            if is_inc and is_dec:
                return False

        return True


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
