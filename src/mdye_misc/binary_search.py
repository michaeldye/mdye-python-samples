"""."""

from typing import List, Optional


def contains(data: list[int], n: int) -> bool:
    """."""

    def _s(arr: List[int], n: int) -> Optional[int]:
        if len(arr) == 0:
            return None

        # possibly found the value we were looking for
        if len(arr) == 1:
            if arr[0] == n:
                return n
            return None

        # recur, looking at the left half of the list and then the right
        halfway = len(arr) // 2
        if n < arr[halfway]:
            return _s(arr[0:halfway], n)

        return _s(arr[halfway:], n)

    return _s(data, n) is not None


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
