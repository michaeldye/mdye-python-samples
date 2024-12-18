"""."""

# need a structure that allows low cost prepending; deque is good, so is linked list
from collections import deque
from typing import Deque, List


class Solution:
    def length_of_lis(self, nums: List[int]) -> int:
        """."""
        return len(self.patience_sort(nums))

    def patience_sort(self, nums: List[int]) -> List[Deque[int]]:
        """."""
        piles: List[Deque[int]] = []

        for n in nums:
            written = False

            # optimize by using binary search on head elements in all piles instead of iterating over them
            for p in piles:
                if len(p) > 0 and p[0] >= n:
                    written = True
                    p.appendleft(n)  # prepend
                    break  # only write number to one pile

            if not written:
                piles.append(deque([n]))

        return piles


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
