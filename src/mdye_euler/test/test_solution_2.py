import pytest

from mdye_euler.solution_2_fib_evens import solve


def test_solution():
    assert 4613732 == solve(4e6)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
