import pytest

from mdye_leetcode.solution_896 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_896_basic(sol: Solution):
    assert sol.is_monotonic([1, 2, 2, 3])
    assert sol.is_monotonic([6, 5, 4, 4])
    assert not sol.is_monotonic([1, 3, 2])


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
