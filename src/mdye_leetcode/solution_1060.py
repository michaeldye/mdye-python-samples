from typing import List

class Solution:
    def missingElement(self, arr: List[int], k: int) -> int:
        def distance(index: int) -> int:
            # doesn't work for index > len(arr)

            if index == 0:
                return 0
            else:
                return arr[index] - arr[index - 1] - 1

        missing_ct = 0
        ix = 0

        while True:
            missing_ct += distance(ix)

            # determines if we need to process the next value in arr to get to our desired k
            if ix + 1 == len(arr) or missing_ct + (distance(ix + 1)) >= k:
                break
            ix += 1

        return arr[ix] + (k - missing_ct)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
