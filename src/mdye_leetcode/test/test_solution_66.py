import pytest

from mdye_leetcode.solution_66 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_66_basic(sol: Solution):
    assert sol.plus_one([1, 2, 3]) == [1, 2, 4]
    assert sol.plus_one([9]) == [1, 0]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
