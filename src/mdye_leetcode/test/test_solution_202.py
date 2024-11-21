import pytest

from mdye_leetcode.solution_202 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_202_basic(sol: Solution):
    assert sol.is_happy(19)
    assert not sol.is_happy(2)
    assert sol.is_happy(7)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
