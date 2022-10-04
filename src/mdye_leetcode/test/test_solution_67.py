# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_67 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_67_basic(sol: Solution):
    assert sol.addBinary("11", "1") == "100"
    assert sol.addBinary("1010", "1011") == "10101"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
