""".

problem: https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem
"""

import sys

if __name__ == "__main__":
    ints = list(map(int, input().split()))
    assert len(ints) == 5

    ordered = sorted(ints)
    minsum = sum(ordered[0:4])
    maxsum = sum(ordered[-4:])
    print(f"{minsum} {maxsum}")

    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
