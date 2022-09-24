# -*- coding: utf-8 -*-

from typing import List
import math


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        smallest_distance = math.inf
        index = -1

        for ix, c in enumerate(points):
            cx = c[0]
            cy = c[1]

            if x == cx or y == cy:
                di = abs(x - cx) + abs(y - cy)
                if di < smallest_distance:
                    smallest_distance = di
                    index = ix

        return index


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
