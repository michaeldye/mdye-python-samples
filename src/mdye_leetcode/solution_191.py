# -*- coding: utf-8 -*-

class Solution:
    def hammingWeight(self, n: int) -> int:
        ct = 0

        while n > 0:
            if n & 1 == 1:
                ct += 1
            n = n >> 1

        return ct

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
