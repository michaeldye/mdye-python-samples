from typing import Generator

import pytest

from mdye_leetcode.solution_1822 import Solution


@pytest.fixture(scope="module")
def sol() -> Generator[Solution, None, None]:
    yield Solution()


def test_solution_1822_basic(sol: Solution):
    assert sol.array_sign([-1, -2, -3, -4, 3, 2, 1]) == 1
    assert sol.array_sign([1, 5, 0, 2, -3]) == 0
    assert sol.array_sign([-1, 1, -1, 1, -1]) == -1


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
