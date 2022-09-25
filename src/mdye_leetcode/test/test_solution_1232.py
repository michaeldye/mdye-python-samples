# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_1232 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1232_basic(sol: Solution):
    assert sol.checkStraightLine(
        [[0, -5], [0, 1], [0, 5], [0, 12]]
    )  # has undefined slope, but it's straight
    assert sol.checkStraightLine([[1, 0], [5, 0], [12, 0]])  # has slope 0
    assert sol.checkStraightLine([[2, 1], [4, 2], [6, 3]])
    assert sol.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    assert not sol.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
