"""."""

from typing import List


class Solution:
    def can_make_arithmetic_progression(self, arr: List[int]) -> bool:
        """."""
        # sorting first is O(n log n) and later our traversal will be O(n) which is worse so we're fine a sort
        arr.sort()

        expected_diff = arr[1] - arr[0]

        return all(arr[ix] - arr[ix - 1] == expected_diff for ix in range(2, len(arr)))


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
