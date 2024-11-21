from mdye_euler.solution_3_largest_prime_factor import lpf


def test_lpf_small():
    assert lpf(13195) == 29


def test_solution():
    assert lpf(600851475143) == 6857


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
