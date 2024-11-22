import pytest

from mdye_leetcode.solution_28 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_28_basic(sol: Solution):
    assert sol.str_str("mississippi", "issip") == 4
    assert sol.str_str("foogzon", "zon") == 4
    assert sol.str_str("sadbutsad", "sad") == 0
    assert sol.str_str("leetcode", "leeto") == -1


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
