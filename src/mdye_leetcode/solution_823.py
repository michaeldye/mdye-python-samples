from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()

        # make dict for dynamic prog with 1 as default value (count) for all nodes, x;
        # this value makes sense b/c each single node is counted as its own tree
        dp = {x: 1 for x in arr}

        for ix, a in enumerate(arr):
            for b in arr[0:ix]:  # sliding window from 0 up to ix

                # (a, b) is a candidate pair of factors

                if a % b == 0:
                    # b divides a evenly so we count it; the key into our dp map is int(a / b)
                    key = a // b
                    if key in dp:
                        # we found a factor that is a node in our dp map, multiply the recorded ct for that node by the recorded ct for the divisor, b. Why ???
                        dp[a] += dp[b] * dp[key]
        from pprint import pprint

        pprint(dp)

        # sum of all counts recorded in dp map mod the special num they gave us in the instructions
        return sum(dp.values()) % (10**9 + 7)
