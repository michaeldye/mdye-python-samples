# -*- coding: utf-8 -*-

from mdye_misc import pair_can_sum


def test_pair_can_sum_basic():
    assert pair_can_sum.add_up([10, 15, 3, 7], 17)
    assert not pair_can_sum.add_up([3, 2], 3)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
