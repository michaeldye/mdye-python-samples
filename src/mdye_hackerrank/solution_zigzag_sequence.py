"""."""

import sys

# N.B. This was a debugging exercise and came with canned content. Lines adjusted are marked # fixed


def findZigZagSequence(a: list[int], n: int) -> None:  # noqa: D103, N802
    a.sort()
    mid = n // 2  # fixed
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2  # fixed
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1  # fixed

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        findZigZagSequence(a, n)

    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
