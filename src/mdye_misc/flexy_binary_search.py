# -*- coding: utf-8 -*-
from typing import List, Optional


def indices(n: int, arr: List[int]) -> List[int]:
    def ind0(arr: List[int], end: bool = False) -> Optional[int]:
        # returns index of first n in arr or None if not found

        if not arr:
            return None

        mid = len(arr) // 2

        if arr[mid] == n:
            if end:
                if arr[mid + 1] > n:
                    return mid
            # was 'elif' in error
            else:
                if arr[mid - 1] < n:
                    return mid

        if n < arr[mid]:
            return ind0(arr[0:mid])

        # fucked up the returned index (into original arr); fix by adding mid here …
        return ind0(arr[mid:])

    return [ind0(arr), ind0(arr, True)]


if __name__ == "__main__":
    assert indices(5, [2, 2, 5, 5, 5, 5, 7, 8, 9]) == [2, 5]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
