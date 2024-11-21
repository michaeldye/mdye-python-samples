"""."""

from typing import List


class Solution:
    def num_factored_binary_trees(self, arr: List[int]) -> int:
        """."""
        arr.sort()

        # make dict for dynamic prog with 1 as default value (count) for all nodes, x;
        # this value makes sense b/c each single node is counted as its own tree
        dp = {x: 1 for x in arr}

        for ix, a in enumerate(arr):
            for b in arr[0:ix]:
                # (a, b) is a candidate pair of factors; for input (after sorting) [2,4,5,10], the first pair to get here will be a=4,b=2 , then a=5,b=2 , then a=5,b=4 ...

                if a % b == 0:
                    # b divides a evenly so next we need to see if the other factor ("c", where c * b == a)
                    # is in our list of nodes. If both "c" and "b" are in our list of nodes we can make a
                    # binary tree where "a" is the parent and "c" and "b" are children, just as the problem
                    # requires.
                    #
                    # The best way to see if c is in the list of nodes is to use the dict we built earlier.

                    c = a // b
                    if c in dp:
                        # We've found a tree of "a" (and its mirror will be picked up when we get to the
                        # other factor in our iteration). But if we were to only increment dp[a] by 1 here,
                        # we would fail to count all of the subtrees in that tree and those are valid too
                        # (so not just 18 with children 6 and 3, and its mirror, but also 18 with children
                        # 6 and 3, where 6 has children 2 and 3, and then all variations of those). The
                        # way to get all variations of the subtrees is to multiply the counts we have
                        # so far
                        #
                        dp[a] += dp[b] * dp[c]

        # sum of all counts recorded in dp map mod the special num they gave us in the instructions
        return sum(dp.values()) % (10**9 + 7)
