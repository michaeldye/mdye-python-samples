import pytest

from mdye_leetcode.solution_5 import Solution


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_5_evens(sol: Solution):
    assert sol.longest_palindrome("aa") == "aa"
    assert sol.longest_palindrome("bbbb") == "bbbb"
    assert sol.longest_palindrome("cbbd") == "bb"


def test_solution_5_odds(sol: Solution):
    assert sol.longest_palindrome("a") == "a"
    assert sol.longest_palindrome("babad") == "bab"
    assert sol.longest_palindrome("bababa") == "babab"
    assert sol.longest_palindrome("babazpzzpz") == "zpzzpz"
    assert sol.longest_palindrome("aacabdkacaa") == "aca"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
