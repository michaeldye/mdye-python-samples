# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_150 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_150_basic(sol: Solution):
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        sol.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    )


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
