import pytest

from mdye_leetcode.solution_1491 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1491_basic(sol: Solution):
    assert sol.average([4000, 3000, 1000, 2000]) == 2500
    assert sol.average([1000, 2000, 3000]) == 2000


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
