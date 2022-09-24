# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:

        neg_ct = 0
        for n in nums:

            if n == 0:
                return 0
            if n * -1 > 0:
                # n is negative
                neg_ct += 1

        if neg_ct % 2 == 0:
            # return 1 if positive
            return 1

        # return -1 if negative
        return -1


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
