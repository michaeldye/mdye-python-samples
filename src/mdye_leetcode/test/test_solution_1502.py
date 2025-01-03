import pytest

from mdye_leetcode.solution_1502 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1502_basic(sol: Solution):
    assert sol.can_make_arithmetic_progression([3, 5, 1])
    assert not sol.can_make_arithmetic_progression([1, 2, 4])


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
