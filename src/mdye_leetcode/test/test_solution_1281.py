import pytest

from mdye_leetcode.solution_1281 import Solution


@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1281_basic(sol: Solution):
    assert sol.subtract_product_and_sum(234) == 15
    assert sol.subtract_product_and_sum(4421) == 21


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
