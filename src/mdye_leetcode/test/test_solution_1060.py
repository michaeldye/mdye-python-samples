import pytest

from mdye_leetcode.solution_1060 import Solution

# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_5_basic(sol: Solution):
    assert 5 == sol.missingElement([4, 7, 9, 10], 1)
    assert 8 == sol.missingElement([4, 7, 9, 10], 3)
    assert 6 == sol.missingElement([1, 2, 4], 3)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
