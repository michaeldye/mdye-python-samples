# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_1822 import Solution


@pytest.fixture(scope="module")
def sol() -> Solution:
    yield Solution()


def test_solution_1822_basic(sol: Solution):
    assert sol.arraySign([-1,-2,-3,-4,3,2,1]) == 1
    assert sol.arraySign([1,5,0,2,-3]) == 0
    assert sol.arraySign([-1,1,-1,1,-1]) == -1


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
