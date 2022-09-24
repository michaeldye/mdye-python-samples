# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_1502 import Solution

# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1502_basic(sol: Solution):
    assert sol.canMakeArithmeticProgression([3, 5, 1])
    assert not sol.canMakeArithmeticProgression([1, 2, 4])


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
