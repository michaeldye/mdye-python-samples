import pytest

from mdye_leetcode.solution_459 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_459_basic(sol: Solution):
    assert sol.repeated_substring_pattern("abab")
    assert not sol.repeated_substring_pattern("aba")
    assert sol.repeated_substring_pattern("abcabcabcabc")


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
