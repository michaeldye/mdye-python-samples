import pytest

from mdye_leetcode.solution_191 import Solution


@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_191_basic(sol: Solution):
    assert sol.hamming_weight(39) == 4
    assert sol.hamming_weight(11) == 3


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
