# -*- coding: utf-8 -*-
import pytest

from mdye_leetcode.solution_1281 import Solution


@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1281_basic(sol: Solution):
    assert 15 == sol.subtractProductAndSum(234)
    assert 21 == sol.subtractProductAndSum(4421)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
