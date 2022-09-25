# -*- coding: utf-8 -*-

from typing import List, Callable
import pytest

from mdye_leetcode.solution_496 import SolutionSlow, SolutionNotAsSlow, Solution

# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sols():
    yield [SolutionSlow(), SolutionNotAsSlow(), Solution()]


def test_solution_496_basic(sols: List[Callable[[List[int], List[int]], List[int]]]):
    for sol_fn in sols:
        assert sol_fn.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
        assert sol_fn.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
