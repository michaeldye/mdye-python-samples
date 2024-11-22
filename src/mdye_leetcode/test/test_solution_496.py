from typing import List

import pytest

from mdye_leetcode.solution_496 import (
    Solution,
    SolutionInterface,
    SolutionNotAsSlow,
    SolutionSlow,
)


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sols():
    yield [SolutionSlow(), SolutionNotAsSlow(), Solution()]


def test_solution_496_basic(sols: List[SolutionInterface]):
    for obj in sols:
        assert obj.next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
        assert obj.next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
