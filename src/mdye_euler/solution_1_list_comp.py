"""."""

import math

_range_lim_excl = 1000


def solve() -> int:
    """."""
    v = math.fsum([n for n in range(_range_lim_excl) if n % 3 == 0 or n % 5 == 0])
    return int(v)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
