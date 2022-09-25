# -*- coding: utf-8 -*-

from typing import List


def add_up(nums: List[int], k: int) -> bool:
    # note: didn't come up with the best solution in time, my solution adds all nums to set
    comp = set()
    for n in nums:
        val = k - n

        if val in comp:
            return True

        # note: missed the method name here
        comp.add(n)

    return False


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
