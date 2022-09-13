#!/bin/env python3

import sys
import math

_range_lim_excl = 1000


def solve() -> int:
    v = math.fsum([n for n in range(_range_lim_excl) if n % 3 == 0 or n % 5 == 0])
    return int(v)


if __name__ == "__main__":
    print(solve())
    sys.exit(0)
