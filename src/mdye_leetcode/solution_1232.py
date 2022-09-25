# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def cslope(self, p1: List[int], p2: List[int]) -> Optional[float]:
        denom = p2[0] - p1[0]
        if denom == 0:
            return (
                None  # this means undefined for us; a vertical line has undefined slope
            )

        return (p2[1] - p1[1]) / denom

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        last = coordinates[1]

        # needs to remain constant among all points
        slope = self.cslope(coordinates[0], last)

        for point in coordinates[2:]:
            if self.cslope(last, point) != slope:
                return False
            last = point

        return True


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
