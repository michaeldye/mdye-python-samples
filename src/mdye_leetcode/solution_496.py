# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_stack = []
        nums2_lookup = {}

        for n in nums2:
            while len(nums2_stack) > 0 and n > (j := nums2_stack[-1]):
                nums2_lookup[nums2_stack.pop()] = n
            nums2_stack.append(n)

        # nums2_lookup has all valid results for lookups in num1; if no value
        # is present, we use the value -1 in that num1 index position
        return [nums2_lookup.get(n, -1) for n in nums1]


class SolutionNotAsSlow:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # make nums1 hashmap for lookup as we iterate over nums2, eliminating the
        # quadratic time complexity

        nums1_lookup = {}
        for ix, n in enumerate(nums1):
            nums1_lookup[n] = ix

        ans = [-1] * len(nums1)

        # this looks O(n**2) on first glance (b/c of nested loops) but the
        # range (ix .. end) diminishes on each iteration and we don't have to
        # look at all elements in nums2 except in the worst case

        for ix, n2 in enumerate(nums2):
            nx1 = nums1_lookup.get(n2, None)
            if nx1 is not None:
                # the value n2 is in nums1

                size = len(nums2)
                jx = ix + 1
                while size > jx and nums2[jx] < n2:
                    jx += 1

                if size != jx:
                    ans[nx1] = nums2[jx]

        return ans


class SolutionSlow:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for n in nums1:
            size = len(nums2)

            for j in range(size):
                if n == nums2[j]:
                    jx = j + 1
                    while size > jx and nums2[jx] < n:
                        jx += 1

                    if size == jx:
                        ans.append(-1)
                    else:
                        ans.append(nums2[jx])

        return ans


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
