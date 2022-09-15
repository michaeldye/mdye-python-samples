# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_823 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_823_basic(sol: Solution):
    # these are all mini trees (where each is just a parent and two children)
    assert 3 == sol.numFactoredBinaryTrees([2, 4])
    assert 7 == sol.numFactoredBinaryTrees([2, 4, 5, 10])


def test_solution_823_deep(sol: Solution):
    # these are bigger trees than the minis and the solution needs to count all of the subtrees, including mirrors
    assert 12 == sol.numFactoredBinaryTrees([18, 3, 6, 2])


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
