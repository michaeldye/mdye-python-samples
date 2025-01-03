import pytest

from mdye_leetcode.solution_1060 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1060_basic(sol: Solution):
    assert sol.missing_element([4, 7, 9, 10], 1) == 5
    assert sol.missing_element([4, 7, 9, 10], 3) == 8
    assert sol.missing_element([1, 2, 4], 3) == 6


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
