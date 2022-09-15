#!/usr/bin/env python3
# -*- coding: latin-1 -*-
""" """

from typing import List, Optional
import sys

data = [2, 4, 5, 6, 8, 9, 10, 11, 12, 42, 52, 99]


def contains(n: int) -> bool:
    def _s(arr: List[int], n: int) -> Optional[int]:
        if len(arr) == 0:
            return None

        # possibly found the value we were looking for
        if len(arr) == 1:
            if arr[0] == n:
                return n
            else:
                return None

        # recur, looking at the left half of the list and then the right
        halfway = len(arr) // 2
        if n < arr[halfway]:
            return _s(arr[0:halfway], n)

        return _s(arr[halfway:], n)

    if _s(data, n) is None:
        return False
    else:
        return True


if __name__ == "__main__":
    assert contains(99)
    assert not contains(15)
    assert contains(2)
    assert contains(8)
    sys.exit(0)

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
