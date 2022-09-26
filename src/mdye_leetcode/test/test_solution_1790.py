# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_1790 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1790_basic(sol: Solution):
    assert sol.areAlmostEqual("bank", "kanb")
    assert not sol.areAlmostEqual("attack", "defend")
    assert sol.areAlmostEqual("kelb", "kelb")


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
