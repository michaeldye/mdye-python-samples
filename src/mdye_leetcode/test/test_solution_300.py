# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_300 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_300_basic(sol: Solution):
    assert 4 == sol.lengthOfLIS(
        [10, 9, 2, 5, 3, 7, 101, 18]
    )  # 2, 3, 7, 101 is longest increasing


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
