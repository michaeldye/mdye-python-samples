import pytest

from mdye_leetcode.solution_1779 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1779_basic(sol: Solution):
    assert sol.nearest_valid_point(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]) == 2


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
