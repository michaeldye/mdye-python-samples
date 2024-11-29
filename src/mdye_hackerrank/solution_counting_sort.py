"""."""

import os
import sys


def counting_sort(arr: list[int]) -> list[int]:
    """."""
    # return a frequency array; for this exercise, it always has length == 100

    ret = [0] * 100

    for n in arr:
        ret[n] += 1

    return ret


if __name__ == "__main__":
    # N.B. the ignored lint items are given by hackerrank

    fptr = open(os.environ["OUTPUT_PATH"], "w")  # noqa: SIM115
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = counting_sort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
