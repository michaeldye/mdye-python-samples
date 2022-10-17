# -*- coding: utf-8 -*-

from typing import List


def avg_of_subarray_naive(size: int, arr: List[int]) -> List[float]:
    windows = []

    for ix in range(len(arr) - size + 1):
        # ix will be every start

        avg = sum(arr[ix : ix + size])
        windows.append(avg / size)

    return windows


def avg_of_subarray_reuse_sum(size: int, arr: List[int]) -> List[float]:
    # a window-sized sum, for every number that is just added to the window we
    # subtract the outgoing value at the head of the window from the sum;
    # this strategy is from Arslan Ahmad

    windows = []

    window_sum, window_last = 0.0, 0

    for window_first in range(len(arr)):
        # window_first will be every window end

        window_sum += arr[window_first]

        if window_first >= size - 1:
            windows.append(window_sum / size)
            window_sum -= arr[window_last]
            window_last += 1

    return windows


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
