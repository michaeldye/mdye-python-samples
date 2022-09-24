# -*- coding: utf-8 -*-

from mdye_misc.sliding_window import avg_of_subarray_naive, avg_of_subarray_reuse_sum


def test_avg_of_subarray_naive():
    assert avg_of_subarray_naive(4, [9, 12, 52, 5, -2, 5, 1]) == [
        19.5,
        16.75,
        15.0,
        2.25,
    ]


def test_avg_of_subarray_reuse_sum():
    assert avg_of_subarray_reuse_sum(4, [9, 12, 52, 5, -2, 5, 1]) == [
        19.5,
        16.75,
        15.0,
        2.25,
    ]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
