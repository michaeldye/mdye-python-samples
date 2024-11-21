import pytest

from mdye_leetcode.solution_1523 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1491_basic(sol: Solution):
    assert sol.count_odds(3, 7) == 3
    assert sol.count_odds(8, 10) == 1


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
