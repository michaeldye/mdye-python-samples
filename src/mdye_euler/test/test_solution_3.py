import pytest

from mdye_euler.solution_3_largest_prime_factor import lpf


def test_lpf_small():
    assert 29 == lpf(13195)


def test_solution():
    assert 6857 == lpf(600851475143)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
