import pytest

from mdye_leetcode.solution_300 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_300_basic(sol: Solution):
    assert (
        sol.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    )  # 2, 3, 7, 101 is longest increasing


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
