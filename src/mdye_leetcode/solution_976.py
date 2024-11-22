"""."""

from typing import List


class Solution:
    def largest_perimeter(self, nums: List[int]) -> int:
        """."""
        # sort nums since we want to evaluate bigger lengths first b/c those will have larger perimeters
        nums.sort()

        ax = len(nums) - 1

        while ax >= 0:
            z = nums[ax]
            y = nums[ax - 1]
            x = nums[ax - 2]

            # If x + y > z is not true, there is no value for x and y in this
            # list that is true and so we needn't search the list further. This
            # simple fact prevents us from needing an O(n^3) algorithm that
            # enumerates all three-tuples

            if x + y > z and z + y > x and z + x > y:
                # conditions above amount to requirements of Triangle Inequality Theorem
                return x + y + z

            ax -= 1

        return 0


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
