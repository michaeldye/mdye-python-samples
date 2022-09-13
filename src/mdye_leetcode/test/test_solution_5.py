
import pytest

from mdye_leetcode.solution_5 import Solution

# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()

def test_solution_5_evens(sol: Solution):
    assert ("aa" == sol.longestPalindrome("aa"))
    assert ("bbbb" == sol.longestPalindrome("bbbb"))
    assert ("bb" == sol.longestPalindrome("cbbd"))

def test_solution_5_odds(sol: Solution):
    assert ("a" == sol.longestPalindrome("a"))
    assert ("bab" == sol.longestPalindrome("babad"))
    assert ("babab" == sol.longestPalindrome("bababa"))
    assert ("zpzzpz" == sol.longestPalindrome("babazpzzpz"))
    assert ("aca" == sol.longestPalindrome("aacabdkacaa"))

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
