# -*- coding: utf-8 -*-
import pytest

from mdye_leetcode.solution_191 import Solution


@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_191_basic(sol: Solution):
    assert 4 == sol.hammingWeight(39)
    assert 3 == sol.hammingWeight(11)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
