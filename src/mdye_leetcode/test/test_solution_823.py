import pytest

from mdye_leetcode.solution_823 import Solution

# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_823_basic(sol: Solution):
    assert 3 == sol.numFactoredBinaryTrees([2, 4])
    assert 7 == sol.numFactoredBinaryTrees([2, 4, 5, 10])


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
